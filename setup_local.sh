#!/bin/bash
# Quick Setup Script for Local Testing
# Run: bash setup_local.sh

echo "🚀 Emotional Support AI - Local Setup"
echo "======================================"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.10+"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "⚠️  Node.js not found. Frontend may not work without it."
    echo "   Install from: https://nodejs.org"
else
    echo "✅ Node.js found: $(node --version)"
fi

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo ""
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Edit .env and add your API key before running!"
    echo "   - CLAUDE_API_KEY or"
    echo "   - OPENAI_API_KEY or"
    echo "   - GOOGLE_API_KEY"
else
    echo "✅ .env file exists"
fi

# Install Python dependencies
echo ""
echo "Installing Python dependencies..."
pip install -r requirements.txt --quiet

if [ $? -eq 0 ]; then
    echo "✅ Python dependencies installed"
else
    echo "❌ Failed to install Python dependencies"
    exit 1
fi

# Install Node dependencies (if Node is available)
if command -v node &> /dev/null; then
    echo ""
    echo "Installing Node.js dependencies..."
    cd nextjs-app
    npm install --silent
    if [ $? -eq 0 ]; then
        echo "✅ Node.js dependencies installed"
        cd ..
    else
        echo "⚠️  Failed to install Node.js dependencies"
    fi
fi

echo ""
echo "======================================"
echo "✅ Setup complete!"
echo ""
echo "To test locally:"
echo ""
echo "1. Terminal 1 - Backend:"
echo "   python flask_api.py"
echo ""
echo "2. Terminal 2 - Frontend (if Node.js installed):"
echo "   cd nextjs-app"
echo "   PYTHON_BACKEND_URL=http://localhost:5000 npm run dev"
echo ""
echo "3. Visit: http://localhost:3000"
echo ""
echo "For deployment instructions, see: DEPLOYMENT_MVP_GUIDE.md"
echo "======================================"
