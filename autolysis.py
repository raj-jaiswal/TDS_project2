# /// script
# dependencies = [
#   "pandas",
#   "requests",
#   "numpy",
# ]
# ///
# Script to add the required dependencies using uv

#importing dependenciess
import sys
import os
import pandas as pd
import numpy as np
import requests
import json

#token to be used for AI Proxy
token = os.environ["AIPROXY_TOKEN"]

def detect_outliers_zscore(df, columns, threshold=3):
    """
    Detects outliers in the given DataFrame using the Z-score method.
    """
    outliers = pd.DataFrame()
    
    for col in columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            # Calculate Z-scores
            z_scores = (df[col] - df[col].mean()) / df[col].std()
            outliers_in_col = df[(z_scores.abs() > threshold)]
            outliers = pd.concat([outliers, outliers_in_col])
    
    return outliers.drop_duplicates()  # Remove duplicate rows (if a row is outlier in multiple columns)

#function for post resquest
def get_response(api_url, headers, payload):
    try:
        #post request
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        result = response.json()
        #result is formatted as {'choices': [{'message': {'content': " "}}]}
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        #in case of error
        return f"An error occurred: {e}"

#main function to get response from model
def get_gpt4_mini_response(prompt):
    api_url = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    api_key = token

    #defining header for request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    #defining appropriate payload to be sent to the model; model used - gpt-4o-mini
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ],
    }

    #post request call with headers and payload
    return get_response(api_url, headers, payload)


#Initial Code
if __name__ == "__main__":
    #obtaining input and output filenames
    inputFile = sys.argv[1]
    outputFile = (sys.argv[2] + '/README.md') if len(sys.argv) > 2 else "README.md"
    data = ''

    #obtainign data from csv file using read_csv
    #data may be in different encodings so try except is used to account for different encodings
    try:
        data = pd.read_csv(inputFile, encoding="utf8")
    except:
        try:
            data = pd.read_csv(inputFile, encoding = "cp1252")
        except:
            data = pd.read_csv(inputFile)

    #Statistical Analysis
    stat_desc = data.describe().to_string()
    #correlation matrix
    corr_matrix = data.select_dtypes(include='number').corr().to_string()

    numeric_columns = data.select_dtypes(include=np.number).columns  # Select only numeric columns
    # Outliers using Z-score method
    outliers_zscore = detect_outliers_zscore(data, numeric_columns).head(15).to_string()
    
    #defining file to write
    file = open(outputFile, "w")
    #defining prompt
    prompt = f"give me a detailed summary of the data having filename {inputFile} and columns as {data.columns}. The first few rows of data are {data.iloc[0:4, :].values}. then add a detailed statistical analysis in form of paragraphs from the following info: {stat_desc} and correlation matrix\n {corr_matrix} \n The outliers detected using z-score in the data are \n {outliers_zscore} \nFormat it as a markdown file with appropriate title and subheadings. Add some description of your interpretation of data. Add any other elements as needed. Write in friendly tone. Sequence the sections as Title, Overview, Data Structure, Statistical Analysis, Correlation Analysis, Outliers, Interpretation, Key Findings, Conclusion."
    content = get_gpt4_mini_response(prompt)
    #writing results to file
    file.write(content)
    file.close()
