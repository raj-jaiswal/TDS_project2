# Data Summary and Statistical Analysis Script

This project is a Python script that automates the generation of a summarized report and statistical analysis of a CSV dataset. The output is formatted as a Markdown file and can be used to quickly understand the dataset's structure and characteristics. The script utilizes `pandas` for data manipulation and `requests` to interact with an AI API for text generation.

## Features

- **Data Loading**: Automatically detects encoding issues and loads CSV files using `pandas`.
- **AI-Powered Summary**: Generates a concise summary and detailed statistical analysis of the dataset using GPT-4 Mini API.
- **Markdown Output**: Creates a `README.md` file containing the summary and analysis for easy sharing and documentation.
- **Customizable Output**: Specify the output directory or use the default (`README.md` in the current directory).

## Dependencies

The script requires the following Python packages:

- `pandas`
- `requests`

Install these dependencies via pip:
```bash
pip install pandas requests
```

## Usage

### Prerequisites
1. Set the environment variable `AIPROXY_TOKEN` with your API key for the GPT-4 Mini proxy service.
2. Ensure the required Python dependencies are installed.

### Running the Script

Use the following command to run the script:
```bash
python script.py <input_csv_file> [output_directory]
```

- `<input_csv_file>`: Path to the CSV file to analyze.
- `[output_directory]`: (Optional) Directory where the output `README.md` will be saved. If not specified, the file will be created in the current directory.

### Example
```bash
python script.py data.csv ./output
```
This command processes `data.csv` and generates the `README.md` file in the `./output` directory.

## Output Format

The output `README.md` includes:
- **Summary**: A three-paragraph overview of the dataset's structure and contents.
- **Statistical Analysis**: Four paragraphs detailing descriptive statistics, including measures like mean, median, standard deviation, and more.

## API Integration

The script interacts with the GPT-4 Mini API proxy to generate textual summaries. The API endpoint is:
```
http://aiproxy.sanand.workers.dev/openai/v1/chat/completions
```
Ensure your API key is valid and stored in the `AIPROXY_TOKEN` environment variable.

## Error Handling

The script includes robust error handling for:
- File encoding issues.
- API request failures.

In case of errors, the script provides descriptive messages for debugging.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.
