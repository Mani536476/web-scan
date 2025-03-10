# Update web_api.py to add missing endpoints and functionality
import os
import json
import sys
import random
import uuid
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, send_file

# Import scanner components from main.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from main import Scanner, SQLInjectionScanner, XSSScanner, HeaderScanner

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Ensure the results directory exists
RESULTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../results')
os.makedirs(RESULTS_DIR, exist_ok=True)

@app.route('/')
def index():
    """Render the home page with URL input form."""
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    """Process the scan request and redirect to results page."""
    url = request.form.get('url', '')
    
    if not url:
        flash('Please enter a valid URL', 'error')
        return redirect(url_for('index'))
    
    try:
        # Create a unique ID for this scan
        scan_id = str(uuid.uuid4())
        
        # Start time for scan duration calculation
        start_time = datetime.now()
        
        # Initialize scanner
        scanner = Scanner(url, verbose=True)
        
        # Run the scan
        results = scanner.scan()
        
        # Calculate scan duration
        duration = (datetime.now() - start_time).total_seconds()
        
        # Process and categorize vulnerabilities
        vulnerabilities = []
        high_count = 0
        medium_count = 0
        low_count = 0
        
        # Add SQL injection vulnerabilities
        for vuln in results.get('sql_injection', []):
            severity = 'High'
            high_count += 1
            vulnerabilities.append({
                'name': 'SQL Injection',
                'severity': severity,
                'location': vuln.get('url', ''),
                'description': 'SQL injection vulnerability found that could allow attackers to manipulate your database.',
                'payload': vuln.get('payload', ''),
                'remediation': 'Use parameterized queries or prepared statements. Validate and sanitize all user inputs.'
            })
        
        # Add XSS vulnerabilities
        for vuln in results.get('xss', []):
            severity = 'Medium'
            medium_count += 1
            vulnerabilities.append({
                'name': 'Cross-Site Scripting (XSS)',
                'severity': severity,
                'location': vuln.get('url', ''),
                'description': 'XSS vulnerability allows attackers to inject client-side scripts into your web pages.',
                'payload': vuln.get('payload', ''),
                'remediation': 'Sanitize and encode user inputs. Use Content Security Policy (CSP) headers.'
            })
        
        # Add header security issues
        for vuln in results.get('headers', []):
            severity = 'Low'
            low_count += 1
            vulnerabilities.append({
                'name': 'Missing Security Header',
                'severity': severity,
                'location': url,
                'description': f"Missing security header: {vuln.get('header', '')}",
                'remediation': f"Add the {vuln.get('header', '')} header to your server responses."
            })
        
        # Create scan data object
        scan_data = {
            'id': scan_id,
            'url': url,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'duration': round(duration, 2),
            'vulnerabilities': vulnerabilities,
            'high_count': high_count,
            'medium_count': medium_count,
            'low_count': low_count
        }
        
        # Save scan results to file
        result_file = os.path.join(RESULTS_DIR, f"{scan_id}.json")
        with open(result_file, 'w') as f:
            json.dump(scan_data, f, indent=2)
        
        # Flash success message
        flash('Scan completed successfully', 'success')
        
        # Redirect to results page
        return redirect(url_for('scan_results', scan_id=scan_id))
        
    except Exception as e:
        flash(f'Error during scan: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/results/<scan_id>')
def scan_results(scan_id):
    """Display scan results."""
    try:
        # Load scan results from file
        result_file = os.path.join(RESULTS_DIR, f"{scan_id}.json")
        
        if not os.path.exists(result_file):
            flash('Scan results not found', 'error')
            return redirect(url_for('index'))
        
        with open(result_file, 'r') as f:
            scan_data = json.load(f)
        
        return render_template('results.html', scan_data=scan_data)
        
    except Exception as e:
        flash(f'Error loading results: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/download/<scan_id>')
def download_report(scan_id):
    """Download scan results as JSON file."""
    try:
        result_file = os.path.join(RESULTS_DIR, f"{scan_id}.json")
        
        if not os.path.exists(result_file):
            flash('Report not found', 'error')
            return redirect(url_for('index'))
        
        return send_file(
            result_file,
            mimetype='application/json',
            as_attachment=True,
            download_name=f"vulnerability_scan_{scan_id[:8]}_{datetime.now().strftime('%Y%m%d')}.json"
        )
        
    except Exception as e:
        flash(f'Error downloading report: {str(e)}', 'error')
        return redirect(url_for('scan_results', scan_id=scan_id))

@app.route('/api/scan', methods=['POST'])
def api_scan():
    """API endpoint for running scans programmatically."""
    data = request.json
    
    if not data or 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400
    
    url = data['url']
    verbose = data.get('verbose', False)
    
    try:
        # Create scanner and run scan
        scanner = Scanner(url, verbose=verbose)
        results = scanner.scan()
        
        # Generate a scan ID
        scan_id = str(uuid.uuid4())
        
        # Add metadata
        response = {
            'scan_id': scan_id,
            'url': url,
            'timestamp': datetime.now().isoformat(),
            'results': results
        }
        
        # Save results to file
        result_file = os.path.join(RESULTS_DIR, f"{scan_id}.json")
        with open(result_file, 'w') as f:
            json.dump(response, f, indent=2)
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
