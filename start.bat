@echo off
REM Run the Emotional Support Website
REM This script starts the Streamlit application

echo ======================================
echo   情緒支持平臺 Starter
echo   Emotional Support Website
echo ======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo 錯誤：Python 未安裝或不在 PATH 中
    pause
    exit /b 1
)

REM Check if streamlit is installed
python -m pip show streamlit >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    echo 安裝依賴...
    python -m pip install -r requirements.txt
)

REM Run the app
echo.
echo Starting the website at http://localhost:8501
echo 網站啟動於 http://localhost:8501
echo.
streamlit run app.py

pause
