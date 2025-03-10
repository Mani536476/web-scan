# Web Vulnerability Scanner Build Script
# This script installs dependencies and builds the executable

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "Web Vulnerability Scanner Build Process" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

# Set the working directory to the script's location
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Create dist directory if it doesn't exist
if (-not (Test-Path ".\dist")) {
    New-Item -ItemType Directory -Path ".\dist" | Out-Null
    Write-Host "Created dist directory" -ForegroundColor Green
}

# Install dependencies
Write-Host "`nStep 1: Installing dependencies..." -ForegroundColor Yellow
try {
    pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to install dependencies"
    }
    Write-Host "Dependencies installed successfully" -ForegroundColor Green
}
catch {
    Write-Host "Error installing dependencies: $_" -ForegroundColor Red
    exit 1
}

# Build the executable
Write-Host "`nStep 2: Building executable with PyInstaller..." -ForegroundColor Yellow
try {
    pyinstaller --onefile --name "WebVulnScanner" --icon="NONE" --add-data "src;src" ".\src\main.py"
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to build executable"
    }
    Write-Host "Executable built successfully" -ForegroundColor Green
    
    # Copy executable to dist folder
    Move-Item -Path ".\dist\WebVulnScanner.exe" -Destination ".\WebVulnScanner.exe" -Force
    Write-Host "Executable moved to project root" -ForegroundColor Green
}
catch {
    Write-Host "Error building executable: $_" -ForegroundColor Red
    exit 1
}

# Cleanup build files
Write-Host "`nStep 3: Cleaning up build files..." -ForegroundColor Yellow
Remove-Item -Path ".\dist" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".\build" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".\*.spec" -Force -ErrorAction SilentlyContinue
Write-Host "Cleanup completed" -ForegroundColor Green

Write-Host "`n=========================================" -ForegroundColor Cyan
Write-Host "Build process completed successfully!" -ForegroundColor Cyan
Write-Host "Executable is available at: $scriptDir\WebVulnScanner.exe" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

