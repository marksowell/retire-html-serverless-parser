# Retire HTML Serverless Parser
The Retire HTML Serverless Parser consists of a client-side script and a serverless cloud function. The tool is designed to parse HTML output from [Retire.js](https://github.com/RetireJS/retire.js). Utilizing the client-side script to send the HTML file to the serverless function, serverless component fetches vulnerability data for the identified JavaScript libraries. The consolidated results are then presented to the user in a clear and comprehensive format through the client-side script.

## Requirements
- Python 3.6 or higher
- `requests` library in Python

If the `requests` library is not installed, install with pip:
```bash
pip install requests
```

## Setting Up Your Client Script
Before you can utilize the Retire HTML Serverless Parser client script, you need to configure it to communicate with your deployed serverless cloud function. Here's how you do it:

1. Open the client script using your preferred text editor.
1. Insert the Cloud Function URL. Search for the line:

    ```python
    url = "<CLOUD_FUNCTION_URL>"
    ```
    Replace `<CLOUD_FUNCTION_URL>` with your actual serverless cloud function URL.
1. Insert the API key. The cloud function is protected with an API key. When making a request to the cloud function the API key is sent in the headers. Replace `<YOUR_API_KEY>` with your actual API key.
    ```python
    headers = {'X-API-KEY': '<YOUR_API_KEY>'}
    ```
4. Save and Close:
After making the necessary modifications, save the file and exit the editor.

## Usage
The client script takes a single command-line argument, which is the path to the HTML file containing the Retire.js scan results. It will then display the parsed information about the vulnerable JavaScript libraries with details obtained from the serverless function.

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory where you saved the script.
3. Save the report:
![Save report](images/save_report.png)
4. Run the script using the following command:

    ```bash
    python retire_html_serverless_parser.py <path-to-html-file>
    ```
    Replace `<path-to-html-file>` with the path to your HTML file.

The script will print vulnerability information for each library found in the HTML file. For each library, it will print:

- The library name and version
- The locations where the library was found
- The number of known vulnerabilities
- The highest severity level of the vulnerabilities
- A link to a the vulnerability details

## Error Handling
If there is an error while making the request to the cloud function, the script will print the HTTP status code and the response body. The response body might contain additional information about the error.

## Security
The cloud function is protected with an API key. Do not share your API key with others. If you believe your API key has been compromised, contact the administrator to have it changed.

## Data Privacy and Handling
The Retire HTML Serverless Parser application is designed with a strong emphasis on data privacy and security. Here's a brief outline of how third-party data is handled:

**Input**: Users submit an HTML file as input. This file is expected to contain information about JavaScript libraries used by the third-party application, including their versions and the locations (i.e., file paths or script URLs) where they are found. This is the only third-party data processed by the application.

**Processing**: The application parses the HTML file, specifically looking for vulnerable JavaScript libraries and their versions. It then checks online databases for vulnerability details associated with these libraries.

**Data Storage**: To optimize performance, the application uses Google Firestore to cache the results of the online vulnerability check. However, it is important to note that the Firestore database is used to store vulnerability information about JavaScript libraries (library name, version, and associated vulnerabilities), and does not retain any data specific to third-party applications, such as library locations or other unique identifiers. This means that no third-party application specific data is stored in the application at any point.

**Output**: The application outputs the consolidated results, which includes the library name, version, location, and vulnerability details. While the third-party applications library location is in the output, it doesn't find its way into any storage, logging, or caching mechanisms.

In summary, the third-party application-specific data (i.e., the library locations found in the HTML file) is used only during the processing stage, and is not stored, logged, or cached at any point. The application's storage and caching mechanisms are used solely to improve performance and do not contain any third-party application-specific data. This design ensures that the privacy and security of third-party application-specific data is maintained at all times.
