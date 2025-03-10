# Web Vulnerability Scanner

A comprehensive web application vulnerability scanner capable of detecting common security issues such as SQL Injection, Cross-Site Scripting (XSS), and missing security headers. The tool is available both as a command-line utility and a web application.

## Features

- **SQL Injection Detection**: Identifies potential SQL injection vulnerabilities in web forms and parameters
- **Cross-Site Scripting (XSS) Detection**: Discovers XSS vulnerabilities that could allow code injection
- **Security Header Analysis**: Checks for missing security headers in HTTP responses
- **Web Crawling**: Automatically discovers pages within the target website
- **Detailed Reporting**: Generates comprehensive reports categorized by severity
- **Web Interface**: User-friendly interface for running scans and viewing results
- **API Access**: Programmatic access for integration with other tools

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository or download the source code:
`
git clone https://github.com/yourusername/WebVulnScanner.git
cd WebVulnScanner
`

2. Install the required dependencies:
`
pip install -r requirements.txt
`

## Usage

### Command Line Interface

Run a basic scan:
`
python src/main.py --url https://example.com
`

Run a scan with verbose output:
`
python src/main.py --url https://example.com --verbose
`

Display help:
`
python src/main.py --help
`

### Web Interface

1. Start the web server:
`
# On Windows
.\run_web.ps1

# On Linux/Mac
python src/web_api.py
`

2. Open your browser and navigate to http://localhost:5000
3. Enter the target URL and click "Start Scan"
4. Review the results and download the report if needed

### API

You can also interact with the scanner programmatically:

`python
import requests
import json

# Scan a website
response = requests.post('http://localhost:5000/api/scan', 
    json={'url': 'https://example.com', 'verbose': True})

# Print the results
print(json.dumps(response.json(), indent=2))
`

## Project Structure

`
WebVulnScanner/
├── results/                  # Scan result files
├── run_web.ps1               # Windows PowerShell web launcher
├── requirements.txt          # Python dependencies
└── src/
    ├── main.py               # Core scanner functionality
    ├── web_api.py            # Flask web interface
    ├── static/               # Static web assets
    │   └── css/
    │       └── style.css     # CSS styling
    └── templates/            # HTML templates
        ├── index.html        # Home page
        └── results.html      # Results page
`

## Extending the Scanner

To add a new vulnerability check:
1. Create a new scanner class in main.py
2. Implement the detection logic
3. Add it to the main Scanner class scanning process
4. Update the report generation to include the new vulnerability type

## Security Considerations

This tool is designed for legitimate security testing with permission from the system owner. Usage against systems without explicit permission may be illegal and is not recommended.

## License

MIT License - See LICENSE file for details.
