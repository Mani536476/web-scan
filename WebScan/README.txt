===================================================
WEB APPLICATION VULNERABILITY SCANNER
===================================================

OVERVIEW
---------------------------------------------------
The Web Vulnerability Scanner is a comprehensive tool designed to identify common 
security vulnerabilities in web applications. It can detect various types of 
vulnerabilities including SQL Injection, Cross-Site Scripting (XSS), and other 
common web security issues.

FEATURES
---------------------------------------------------
1. SQL Injection Detection
- Tests for common SQL injection patterns
- Identifies potential database exposure points
- Checks both GET and POST parameters

2. Cross-Site Scripting (XSS) Detection
- Tests for reflected XSS vulnerabilities
- Checks form inputs and URL parameters
- Analyzes responses for script execution

3. Miscellaneous Security Checks
- HTTP Headers analysis
- Form submission testing
- Basic crawling capabilities

4. User-friendly Reports
- Colored console output for better readability
- Detailed explanation of found vulnerabilities
- Severity classification

REQUIREMENTS
---------------------------------------------------
To run the Python script directly:
- Python 3.6 or higher
- Required libraries (specified in requirements.txt)

The desktop executable (.exe) version does not require Python to be installed.

INSTALLATION
---------------------------------------------------
Method 1: Using the Python Script

1. Clone or download the WebVulnScanner repository
2. Navigate to the WebVulnScanner directory
3. Install the required dependencies:
```
pip install -r requirements.txt
```

Method 2: Using the Desktop Executable

1. Clone or download the WebVulnScanner repository
2. Navigate to the WebVulnScanner directory
3. Run the build script to create the executable:
```
.\build.ps1
```
4. Find the generated .exe file in the dist directory

USAGE
---------------------------------------------------
Method 1: Running the Python Script

1. Open a command prompt or terminal
2. Navigate to the WebVulnScanner directory
3. Run the script with a target URL:
```
python src/main.py -u https://example.com
```

Method 2: Using the Desktop Executable

1. Double-click the WebVulnScanner.exe file in the dist directory
2. Enter the URL when prompted or use command-line arguments:
```
WebVulnScanner.exe -u https://example.com
```

COMMAND LINE ARGUMENTS
---------------------------------------------------
-u, --url       : Target URL to scan (required)
-a, --all       : Run all available scans (default)
-s, --sql       : Run only SQL injection tests
-x, --xss       : Run only XSS tests
-h, --headers   : Run only HTTP header tests
-v, --verbose   : Enable verbose output
--help          : Display help information

EXAMPLES
---------------------------------------------------
1. Scan a website for all vulnerabilities:
```
python src/main.py -u https://example.com -a
```

2. Scan only for SQL injection:
```
python src/main.py -u https://example.com -s
```

3. Scan for XSS with verbose output:
```
python src/main.py -u https://example.com -x -v
```

UNDERSTANDING SCAN RESULTS
---------------------------------------------------
The scanner outputs results with color-coded severity levels:

- RED: High severity issues that require immediate attention
- YELLOW: Medium severity issues that should be addressed
- BLUE: Informational findings
- GREEN: Secure/passed tests

Each finding includes:
- Vulnerability type
- Location (URL, parameter, etc.)
- Description of the issue
- Potential impact
- Suggested remediation steps

TROUBLESHOOTING
---------------------------------------------------
1. Connection Issues
- Verify the target URL is accessible
- Check your internet connection
- Ensure proper URL format (include http:// or https://)

2. False Positives
- Use the verbose mode for detailed scan information
- Manually verify reported vulnerabilities

3. Executable Won't Run
- Ensure you have the necessary permissions
- Try running as administrator
- Check Windows SmartScreen settings

DISCLAIMER
---------------------------------------------------
This tool is intended for educational purposes and legitimate security testing only.
Always obtain proper authorization before scanning any website. The developers are
not responsible for any misuse or damage caused by this tool.

===================================================
© 2023 Web Vulnerability Scanner
===================================================

