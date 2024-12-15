# /// script
# dependencies = [
#   "pandas",
#   "requests",
#   "numpy",
#   "seaborn",
#   "matplotlib",
#   "scikit-learn",
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
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

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
        print('Monthly Cost:', result['monthlyCost'])
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

def get_linear_regression_column_pairs(correlation_matrix, column_info):
    """
    Ask GPT-4o-mini to suggest two pairs of columns for linear regression.

    Parameters:
    - correlation_matrix (DataFrame): The correlation matrix of the dataset.
    - column_info (list): List of column names in the dataset.

    Returns:
    - list of tuples: Two pairs of columns (e.g., [(col1, col2), (col3, col4)]).
    """
    corr_details = correlation_matrix.to_string()
    prompt = f"""Based on the correlation matrix below and column names, suggest two pairs of columns for linear regression. 
    Ensure that each pair has a moderate-to-strong correlation and represents a meaningful relationship:

    Correlation Matrix:
    {corr_details}

    Available columns:
    {column_info}

    Output only the two pairs of columns as a Python list of tuples, e.g., [('col1', 'col2'), ('col3', 'col4')].
    """
    response = get_gpt4_mini_response(prompt)
    try:
        return eval(response.strip())  # Convert the string output into a Python object
    except Exception as e:
        print(f"Error parsing GPT-4o-mini response: {e}")
        return []

def run_linear_regression(data, col1, col2):
    """
    Run linear regression on two columns, handling missing or NaN values, and print the results.

    Parameters:
    - data (DataFrame): The dataset containing the columns.
    - col1 (str): The predictor (independent variable).
    - col2 (str): The target (dependent variable).

    Returns:
    - dict: A dictionary containing regression results.
    """
    # Drop rows with NaN values in the specified columns
    filtered_data = data[[col1, col2]].dropna()

    if filtered_data.empty:
        print(f"No valid data available for regression between {col1} and {col2}.")
        return {
            "intercept": None,
            "coefficient": None,
            "mse": None,
            "r2_score": None,
        }

    X = filtered_data[[col1]].values  # Independent variable
    y = filtered_data[col2].values    # Dependent variable

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # Calculate metrics
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    results = {
        "intercept": model.intercept_,
        "coefficient": model.coef_[0],
        "mse": mse,
        "r2_score": r2,
    }

    return results

def get_linear_regression_summary(results, col1, col2):
    """
    Prints a summary of linear regression results.

    Parameters:
    - results (dict): A dictionary containing regression results (intercept, coefficient, mse, r2_score).
    - col1 (str): The predictor (independent variable).
    - col2 (str): The target (dependent variable).
    """
    reg_result = ''
    reg_result += (f"Linear Regression Summary for {col1} -> {col2}\n")
    reg_result += ("=" * 50)
    reg_result += (f"\nPredictor (Independent Variable): {col1}\n")
    reg_result += (f"Target (Dependent Variable): {col2}\n")
    reg_result += (f"Intercept: {results['intercept']:.4f}\n")
    reg_result += (f"Coefficient: {results['coefficient']:.4f}\n")
    reg_result += (f"Mean Squared Error (MSE): {results['mse']:.4f}\n")
    reg_result += (f"R² Score: {results['r2_score']:.4f}\n")
    reg_result += ("\nInterpretation:\n")
    
    if results["r2_score"] > 0.7:
        reg_result += ("  - The model fits the data well, explaining a significant proportion of the variance.\n")
    elif results["r2_score"] > 0.4:
        reg_result += ("  - The model has a moderate fit; additional predictors might improve the results.\n")
    else:
        reg_result += ("  - The model has a weak fit; consider reevaluating the predictors or data quality.\n")
    
    if results["coefficient"] > 0:
        reg_result += (f"  - There is a positive relationship between {col1} and {col2}. As {col1} increases, {col2} tends to increase.\n")
    else:
        reg_result += (f"  - There is a negative relationship between {col1} and {col2}. As {col1} increases, {col2} tends to decrease.\n")
    reg_result += ("=" * 50 + "\n")
    return reg_result

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

def generate_markdown_summary(input_file, data, key_stats, significant_corr, outliers, col1, col2, reg_result):
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
    prompt = f"""Generate a detailed and structured Markdown summary of the dataset with the following details:
- **Filename**: {input_file}
- **Columns**: {list(data.columns)}
- **First Few Rows of Data**: {data.iloc[0:4, :].values}

### Requirements:
1. Provide a **concise overview** of the dataset, highlighting its purpose and any relevant context.
2. Include a **statistical analysis** section with detailed insights based on:
    - Summary statistics: {key_stats}
    - Correlation matrix (only significant correlations): {significant_corr}
3. Discuss the **outliers** detected using the Z-score method:
    {outliers}
4. Describe the **scatter plot** visualized between {col1} and {col2}, stored as "scatter_plot.png". Explain the relationship between the variables and any key trends or anomalies visible in the plot. Also, include the image in the markdown file.
5. Include following regression result in the summary: 
    {reg_result}
6. Emphasize the **implications** of the data and the analysis, focusing on actionable insights, potential patterns, or areas for further investigation.
7. Present **key findings** in a bullet-point list for quick reference.
8. Conclude with a brief summary of the analysis and its significance.

### Formatting:
- Use friendly and engaging language suitable for a technical audience.
- Include appropriate titles and subheadings: Title, Overview, Data Structure, Statistical Analysis, Correlation Analysis, Outliers, Scatter Plot Description, Interpretation, Key Findings, and Conclusion.
- Reference the scatter plot as an integral part of the analysis.

Ensure the Markdown output is cohesive, well-structured, and insightful, helping readers easily grasp the dataset's characteristics and implications."""
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
    csv_data = read_csv_file(input_file)

    # Perform statistical analysis
    key_stats, corr_matrix, significant_corr = perform_statistical_analysis(csv_data)

    # Detect outliers
    outliers = detect_outliers(csv_data)

    # Get the pair of columns for scatter plot
    col1, col2 = get_scatter_plot_columns(corr_matrix)

    # Plot and save the scatter plot
    plot_scatter(csv_data, col1, col2, output_file=(output_dir + "scatter_plot.png"))

    # Run Linear Regression on significant columns based on correlation matrix
    reg_column_pairs = get_linear_regression_column_pairs(corr_matrix, list(csv_data.columns))
    
    if len(reg_column_pairs) < 2:
        reg_result = "Could not retrieve two valid column pairs for regression."
    else:
        for reg_col1, reg_col2 in reg_column_pairs:
            result = run_linear_regression(csv_data, reg_col1, reg_col2)
            reg_result = get_linear_regression_summary(result, reg_col1, reg_col2)

    # Generate markdown summary
    content = generate_markdown_summary(input_file, csv_data, key_stats, significant_corr, outliers, col1, col2, reg_result)

    # Write the generated content to the output README file
    write_to_file(output_dir + "README.md", content.replace("```", ""))


# Entry point of the script
if __name__ == "__main__":
    main()
