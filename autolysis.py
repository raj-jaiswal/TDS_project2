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
    sns.scatterplot(data=data, x=col1, y=col2)
    plt.title(f"Scatter Plot: {col1} vs {col2}")
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.savefig(output_file)
    plt.close()

# Entry point of the script
if __name__ == "__main__":
    # Obtain input and output filenames from command-line arguments
    inputFile = sys.argv[1]  # First argument: Input CSV file
    outputFile = (sys.argv[2] + '/') if len(sys.argv) > 2 else ""  # Second argument: Output directory

    # Initialize a variable to store data from the CSV file
    data = ''

    # Read the CSV file. Try different encodings to handle potential issues with file encoding.
    try:
        data = pd.read_csv(inputFile, encoding="utf8")
    except:
        try:
            data = pd.read_csv(inputFile, encoding="cp1252")
        except:
            data = pd.read_csv(inputFile)  # Default fallback if encoding fails

    # Perform statistical analysis on the dataset 
    key_stats = data.describe().loc[['mean', 'std', 'min', 'max']].to_string() # Generate a detailed description of numerical columns
    corr_matrix = data.select_dtypes(include='number').corr()  # Generate the correlation matrix
    significant_corr = corr_matrix[(corr_matrix.abs() > 0.5) & (corr_matrix < 1)].stack().to_string() # Filter the essential elements of the correlation matrix

    # Select numeric columns for outlier detection
    numeric_columns = data.select_dtypes(include=np.number).columns
    outliers_zscore = detect_outliers_zscore(data, numeric_columns).head(10).to_string()  # Detect and list top 15 outliers

    # Get the pair of columns for scatter plot
    col1, col2 = get_scatter_plot_columns(corr_matrix)

    # Plot and save the scatter plot
    plot_scatter(data, col1, col2, output_file=(outputFile + "scatter_plot.png"))

    # Open the output file for writing
    file = open(outputFile + "README.md", "w")

    # Define a prompt for GPT-4o-mini to generate a markdown summary of the dataset
    prompt = f"""give me a detailed summary of the data having filename {inputFile} and columns as {data.columns}. The first few rows of data are {data.iloc[0:4, :].values}. then add a detailed statistical analysis in form of paragraphs from the following info: {key_stats} and correlation matrix
 {significant_corr} 
 The outliers detected using z-score in the data are 
 {outliers_zscore} 
Format it as a markdown file with appropriate title and subheadings. A scatter plot is plotted between {col1} and {col2} named "scatter_plot.png" include it in the file with suitable description. Add some description of your interpretation of data. Add any other elements as needed. Write in friendly tone. Sequence the sections as Title, Overview, Data Structure, Statistical Analysis, Correlation Analysis, Outliers, Interpretation, Key Findings, Conclusion."""

    # Get the response from the model
    content = get_gpt4_mini_response(prompt)

    # Write the generated content to the output file
    file.write(content)
    file.close()