# Web Vulnerability Scanner - Web Interface Launcher
Write-Host "Starting Web Vulnerability Scanner Web Interface..." -ForegroundColor Green

# Set Flask environment variables
$env:FLASK_APP = "src/web_api.py"
$env:FLASK_ENV = "development"

# Make sure we're in the right directory
Set-Location $PSScriptRoot

# Install dependencies if needed
if (-not (Get-Command flask -ErrorAction SilentlyContinue)) {
    Write-Host "Installing Flask..." -ForegroundColor Yellow
    pip install flask
}

# Check if other required packages are installed
if (-not (Get-Command pip -ErrorAction SilentlyContinue)) {
    Write-Host "Installing required packages..." -ForegroundColor Yellow
    pip install -r requirements.txt
}

# Create results directory if it doesn't exist
if (-not (Test-Path "results")) {
    New-Item -Path "results" -ItemType Directory | Out-Null
    Write-Host "Created results directory" -ForegroundColor Green
}

# Run Flask web server
Write-Host "Starting web server - access at http://localhost:5000" -ForegroundColor Cyan
flask run --host=0.0.0.0

# Wait for user input before closing
Write-Host "Server stopped. Press any key to exit..." -ForegroundColor Red
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
