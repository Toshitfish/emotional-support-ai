# PowerShell startup script for Emotional Support Website
# Run: .\start.ps1

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  情緒支持平臺 - Emotional Support" -ForegroundColor Cyan
Write-Host "  Website Starter" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found! Please install Python 3.8+" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if streamlit is installed
Write-Host ""
Write-Host "Checking for dependencies..." -ForegroundColor Yellow
$streamlitCheck = python -c "import streamlit; print('OK')" 2>&1

if ($streamlitCheck -eq "OK") {
    Write-Host "✓ Dependencies already installed" -ForegroundColor Green
} else {
    Write-Host "Installing dependencies..." -ForegroundColor Yellow
    pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "✗ Failed to install dependencies" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

# Run the app
Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "🚀 Starting the website..." -ForegroundColor Green
Write-Host "📱 Open your browser: http://localhost:8501" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

streamlit run app.py

Read-Host "Press Enter to close this window"
