# /// script
# dependencies = [
#   "pandas",
#   "requests",
#   "numpy",
#   "seaborn",
#   "matplotlib",
# ]
# ///
# Script to add the required dependencies using uv

# Importing required dependencies
import sys
import os
import pandas as pd
import numpy as np
import requests
import json
import seaborn as sns
import matplotlib.pyplot as plt

# Token to be used for AI Proxy. The token is expected to be set as an environment variable.
token = os.environ["AIPROXY_TOKEN"]

def detect_outliers_zscore(df, columns, threshold=3):
    """
    Detects outliers in the given DataFrame using the Z-score method.

    Parameters:
    df (DataFrame): The input DataFrame.
    columns (list): List of column names to check for outliers.
    threshold (float): The Z-score threshold to identify outliers. Default is 3.

    Returns:
    DataFrame: A DataFrame containing rows identified as outliers.
    """
    outliers = pd.DataFrame()
    
    for col in columns:
        if pd.api.types.is_numeric_dtype(df[col]):  # Check if the column is numeric
            # Calculate Z-scores for the column
            z_scores = (df[col] - df[col].mean()) / df[col].std()
            # Identify rows where Z-score exceeds the threshold
            outliers_in_col = df[(z_scores.abs() > threshold)]
            # Concatenate outliers from the current column
            outliers = pd.concat([outliers, outliers_in_col])
    
    return outliers.drop_duplicates()  # Remove duplicate rows (in case a row is an outlier in multiple columns)

# Function to send a POST request to the specified API endpoint
def get_response(api_url, headers, payload):
    """
    Sends a POST request to the specified API endpoint and returns the response.

    Parameters:
    api_url (str): The API URL.
    headers (dict): Headers to include in the request.
    payload (dict): The payload to send in the request body.

    Returns:
    str: The response content or an error message in case of failure.
    """
    try:
        # Send the POST request
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an error for HTTP status codes 4xx/5xx
        result = response.json()
        # Extract and return the content of the response
        # print('Monthly Cost:', result['monthlyCost'])
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        # Handle request errors gracefully
        return f"An error occurred: {e}"

# Main function to interact with the GPT-4 model
def get_gpt4_mini_response(prompt):
    """
    Sends a prompt to the GPT-4o-mini model and returns the generated response.

    Parameters:
    prompt (str): The prompt to send to the model.

    Returns:
    str: The response content from the model.
    """
    # Define the API URL for the GPT-4o-mini model
    api_url = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    api_key = token  # Use the token from environment variables

    # Define headers for the POST request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Define the payload for the model, including the prompt
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ],
    }

    # Send the POST request and return the response
    return get_response(api_url, headers, payload)

def get_scatter_plot_columns(correlation_matrix):
    """
    Asks GPT to recommend a pair of columns for a scatter plot based on the correlation matrix.

    Parameters:
    correlation_matrix (str): The string representation of the correlation matrix.

    Returns:
    tuple: A pair of column names recommended for the scatter plot.
    """
    prompt = f"Based on the following correlation matrix:\n{correlation_matrix}\nWhich pair of columns would you recommend for creating a scatter plot? Provide only the column names as a comma-separated pair."
    response = get_gpt4_mini_response(prompt)
    columns = response.split(",")
    return columns[0].strip(), columns[1].strip()

def plot_scatter(data, col1, col2, output_file="scatter_plot.png"):
    """
    Plots a scatter plot for the given columns and saves it as a PNG file.

    Parameters:
    data (DataFrame): The dataset containing the columns.
    col1 (str): The name of the first column.
    col2 (str): The name of the second column.
    output_file (str): The file path to save the scatter plot. Default is 'scatter_plot.png'.
    """
    plt.figure(figsize=(5.12, 5.12))  # Set figure size to 512x512 pixels
    
    # Create the scatter plot with enhanced visual elements
    scatter_plot = sns.scatterplot(
        data=data, x=col1, y=col2, hue=col1, size=col2, palette="viridis", legend="brief", alpha=0.8
    )

    # Add a title and axis labels
    plt.title(f"Scatter Plot: {col1} vs {col2}", fontsize=14, weight='bold')
    plt.xlabel(col1, fontsize=12)
    plt.ylabel(col2, fontsize=12)

    # Customize the legend
    plt.legend(title="Legend", title_fontsize=10, fontsize=9, loc='best')

    # Add annotations for the first few points
    for i in range(min(10, len(data))):  # Annotate up to 10 points
        plt.annotate(
            text=f"({data[col1].iloc[i]:.2f}, {data[col2].iloc[i]:.2f})",
            xy=(data[col1].iloc[i], data[col2].iloc[i]),
            xytext=(5, 5),  # Offset for annotation text
            textcoords='offset points',
            fontsize=8,
            color="black",
            arrowprops=dict(arrowstyle="->", color="gray", lw=0.5)
        )

    # Apply grid for better readability
    plt.grid(True, linestyle='--', alpha=0.6)

    # Save the plot as a PNG file
    plt.savefig(output_file, dpi=300, bbox_inches="tight")  # High-quality image
    plt.close()

def read_csv_file(input_file):
    """
    Reads a CSV file and returns the DataFrame. Handles different encodings.

    Parameters:
    input_file (str): Path to the input CSV file.

    Returns:
    DataFrame: Loaded data from the CSV file.
    """
    try:
        return pd.read_csv(input_file, encoding="utf8")
    except:
        try:
            return pd.read_csv(input_file, encoding="cp1252")
        except:
            return pd.read_csv(input_file)

def perform_statistical_analysis(data):
    """
    Performs statistical analysis on the dataset.

    Parameters:
    data (DataFrame): The dataset.

    Returns:
    tuple: Key statistics and significant correlations.
    """
    key_stats = data.describe().loc[['mean', 'std', 'min', 'max']].to_string()
    corr_matrix = data.select_dtypes(include='number').corr()
    significant_corr = corr_matrix[(corr_matrix.abs() > 0.5) & (corr_matrix < 1)].stack().to_string()
    return key_stats, corr_matrix, significant_corr

def detect_outliers(data):
    """
    Detects outliers in the dataset using Z-score.

    Parameters:
    data (DataFrame): The dataset.

    Returns:
    str: Top 10 outliers as a string.
    """
    numeric_columns = data.select_dtypes(include=np.number).columns
    return detect_outliers_zscore(data, numeric_columns).head(10).to_string()

def generate_markdown_summary(input_file, data, key_stats, significant_corr, outliers, col1, col2):
    """
    Generates a markdown summary of the dataset using GPT.

    Parameters:
    input_file (str): Path to the input CSV file.
    data (DataFrame): The dataset.
    key_stats (str): Key statistics of the dataset.
    significant_corr (str): Significant correlations.
    outliers (str): Detected outliers.
    col1 (str): First column for scatter plot.
    col2 (str): Second column for scatter plot.

    Returns:
    str: Generated markdown content.
    """
    prompt = f"""give me a detailed summary of the data having filename {input_file} and columns as {data.columns}. The first few rows of data are {data.iloc[0:4, :].values}. then add a detailed statistical analysis in form of paragraphs from the following info: {key_stats} and correlation matrix
 {significant_corr} 
 The outliers detected using z-score in the data are 
 {outliers} 
Format it as a markdown file with appropriate title and subheadings. A scatter plot is plotted between {col1} and {col2} named "scatter_plot.png" include it in the file with suitable description. Add some description of your interpretation of data. Add any other elements as needed. Write in friendly tone. Sequence the sections as Title, Overview, Data Structure, Statistical Analysis, Correlation Analysis, Outliers, Interpretation, Key Findings, Conclusion. Output only the markdown file without ```."""
    return get_gpt4_mini_response(prompt)

def write_to_file(file_path, content):
    """
    Writes content to a specified file.

    Parameters:
    file_path (str): Path to the output file.
    content (str): Content to write.
    """
    with open(file_path, "w") as file:
        file.write(content)

def main():
    """
    Main function to execute the script.
    """
    # Obtain input and output filenames from command-line arguments
    input_file = sys.argv[1]  # First argument: Input CSV file
    output_dir = (sys.argv[2] + '/') if len(sys.argv) > 2 else ""  # Second argument: Output directory

    # Read the CSV file
    data = read_csv_file(input_file)

    # Perform statistical analysis
    key_stats, corr_matrix, significant_corr = perform_statistical_analysis(data)

    # Detect outliers
    outliers = detect_outliers(data)

    # Get the pair of columns for scatter plot
    col1, col2 = get_scatter_plot_columns(corr_matrix)

    # Plot and save the scatter plot
    plot_scatter(data, col1, col2, output_file=(output_dir + "scatter_plot.png"))

    # Generate markdown summary
    content = generate_markdown_summary(input_file, data, key_stats, significant_corr, outliers, col1, col2)

    # Write the generated content to the output README file
    write_to_file(output_dir + "README.md", content.replace("```", ""))

# Entry point of the script
if __name__ == "__main__":
    main()
