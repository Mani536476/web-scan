# Web Vulnerability Scanner - Command Line Scan Launcher
param (
    [Parameter(Mandatory=$true, Position=0, HelpMessage="Target URL to scan")]
    [string]$Url,
    
    [Parameter(Mandatory=$false)]
    [switch]$Verbose,
    
    [Parameter(Mandatory=$false)]
    [switch]$SaveReport,
    
    [Parameter(Mandatory=$false)]
    [string]$OutputPath = "results"
)

Write-Host "Web Vulnerability Scanner" -ForegroundColor Cyan
Write-Host "------------------------" -ForegroundColor Cyan
Write-Host "Target URL: $Url" -ForegroundColor Yellow

# Make sure we're in the right directory
Set-Location $PSScriptRoot

# Create results directory if it doesn't exist
if ($SaveReport -and -not (Test-Path $OutputPath)) {
    New-Item -Path $OutputPath -ItemType Directory | Out-Null
    Write-Host "Created output directory: $OutputPath" -ForegroundColor Green
}

# Build the command arguments
$arguments = "src/main.py --url "$Url""
if ($Verbose) {
    $arguments += " --verbose"
}
if ($SaveReport) {
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $reportPath = Join-Path $OutputPath "scan_report_$timestamp.json"
    $arguments += " --output "$reportPath""
}

Write-Host "Starting scan..." -ForegroundColor Green

# Run the scan
python $arguments

# Report completion
Write-Host "Scan completed." -ForegroundColor Green
if ($SaveReport) {
    Write-Host "Report saved to: $reportPath" -ForegroundColor Cyan
}

# Keep console open if run directly
if ($Host.Name -eq 'ConsoleHost') {
    Write-Host "Press any key to exit..." -ForegroundColor Yellow
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}
