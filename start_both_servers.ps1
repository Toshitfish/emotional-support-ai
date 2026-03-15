# PowerShell script to start Next.js + Flask servers
# Run: .\start_both_servers.ps1

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  💙 Emotional Support Website" -ForegroundColor Cyan
Write-Host "  Next.js + Flask Servers" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Function to start server in new window
function Start-InNewWindow {
    param(
        [string]$Title,
        [string]$Command,
        [string]$WorkingDir
    )
    
    $scriptblock = {
        param($cmd, $wd)
        if ($wd) { Set-Location $wd }
        Invoke-Expression $cmd
    }
    
    Start-Process powershell -ArgumentList @(
        "-NoExit",
        "-Command",
        "Set-Location '$WorkingDir'; & { $Command }"
    ) -WindowTitle $Title
}

# Check Python
Write-Host "Checking Python..." -ForegroundColor Yellow
try {
    python --version | Out-Null
    Write-Host "✓ Python found" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found. Install from https://python.org" -ForegroundColor Red
    exit 1
}

# Check Node.js
Write-Host "Checking Node.js..." -ForegroundColor Yellow
try {
    node --version | Out-Null
    Write-Host "✓ Node.js found" -ForegroundColor Green
} catch {
    Write-Host "✗ Node.js not found. Install from https://nodejs.org" -ForegroundColor Red
    exit 1
}

# Install dependencies if needed
$nextjsPath = "nextjs-app"
if (-not (Test-Path "$nextjsPath/node_modules")) {
    Write-Host ""
    Write-Host "Installing Next.js dependencies..." -ForegroundColor Yellow
    Set-Location $nextjsPath
    npm install
    Set-Location ..
    Write-Host "✓ Dependencies installed" -ForegroundColor Green
}

# Create .env.local if not exists
if (-not (Test-Path "$nextjsPath/.env.local")) {
    Write-Host ""
    Write-Host "Creating .env.local..." -ForegroundColor Yellow
    @"
PYTHON_BACKEND_URL=http://localhost:5000
NEXT_PUBLIC_API_URL=http://localhost:3000
"@ | Out-File -FilePath "$nextjsPath/.env.local" -Encoding UTF8
    Write-Host "✓ Created .env.local" -ForegroundColor Green
}

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "🚀 STARTING SERVERS" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Frontend:  http://localhost:3000" -ForegroundColor Green
Write-Host "Backend:   http://localhost:5000" -ForegroundColor Green
Write-Host ""
Write-Host "Opening new terminal windows..." -ForegroundColor Yellow
Write-Host ""

# Start Flask backend in new window
Start-InNewWindow -Title "Flask Backend - http://localhost:5000" -Command "python flask_api.py" -WorkingDir (Get-Location).Path

# Wait a bit for Flask to start
Start-Sleep -Seconds 2

# Start Next.js frontend in new window
Start-InNewWindow -Title "Next.js Frontend - http://localhost:3000" -Command "npm run dev" -WorkingDir "$((Get-Location).Path)\nextjs-app"

Write-Host "✅ Servers starting in new windows..." -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Wait for both servers to be ready"
Write-Host "2. Open browser to http://localhost:3000"
Write-Host "3. Test the chat interface"
Write-Host ""
Write-Host "To stop servers: Close the terminal windows or press Ctrl+C"
