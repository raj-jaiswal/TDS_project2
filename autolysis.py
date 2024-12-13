# /// script
# dependencies = [
#   "pandas",
#   "requests",
# ]
# ///

import sys
import os
import pandas as pd
import requests
import json

token = os.environ["AIPROXY_TOKEN"]

def get_gpt4_mini_response(prompt):
    api_url = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    api_key = token

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ],
    }

    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    inputFile = sys.argv[1]
    outputFile = (sys.argv[2] + '/README.md') if len(sys.argv) > 2 else "README.md"
    data = ''
    try:
        data = pd.read_csv(inputFile, encoding="utf8")
    except:
        try:
            data = pd.read_csv(inputFile, encoding = "cp1252")
        except:
            data = pd.read_csv(inputFile)


    file = open(outputFile, "w")
    prompt = f"give me a 3 paragraph summary of the data having filename {inputFile} nd columns as {data.columns}. The first few rows of data are {data.iloc[0:4, :].values}. then add a detailed statistical analysis in 4 more paragraphs from the following info: {data.describe().to_string()} \nFormat it as a markdown file with appropriate title. Write in friendly tone."
    content = get_gpt4_mini_response(prompt)
    file.write(content)
    file.close()
