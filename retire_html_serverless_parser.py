import requests
import sys

def main():
    # Replace this with the path to your file
    file_path = sys.argv[1]

    url = "<CLOUD_FUNCTION_URL>"

    with open(file_path, 'r') as file:
        headers = {'X-API-KEY': '<YOUR_API_KEY>'}
        files = {'file': file}
        response = requests.post(url, files=files, headers=headers)

    if response.status_code != 200:
        print(f'Error: {response.status_code} - {response.text}')
        return

    data = response.json()
    results = data.get('results', [])

    for result in results:
        print(f'Library Version: {result["library"]}@{result["version"]}')
        print(result["location"])
        print(f'Vulnerability Count: {result["vulnerability_count"]}')
        print(f'Highest Severity: {result["highest_severity"]}')
        print(f'Vulnerability Details: {result["snyk_link"]}\n')

if __name__ == "__main__":
    main()
