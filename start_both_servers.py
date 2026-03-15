#!/usr/bin/env python3
"""
Quick start script for the new Next.js + Flask setup
This starts both the backend and frontend servers
"""

import subprocess
import time
import os
import sys
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle output"""
    print(f"\n{'='*60}")
    print(f"📌 {description}")
    print(f"{'='*60}")
    print(f"Running: {' '.join(cmd)}")
    
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    for line in process.stdout:
        print(line.rstrip())
    
    return process

def main():
    print("\n" + "="*60)
    print("💙 Emotional Support Website - Next.js + Flask")
    print("="*60)
    
    # Check Python
    print("\n✓ Checking Python...")
    try:
        import flask
        print("  ✓ Flask installed")
    except ImportError:
        print("  ✗ Flask not installed. Run: pip install -r requirements.txt")
        sys.exit(1)
    
    # Check Node.js
    print("✓ Checking Node.js...")
    try:
        subprocess.run(['node', '--version'], capture_output=True, check=True)
        print("  ✓ Node.js installed")
    except:
        print("  ✗ Node.js not installed. Visit https://nodejs.org")
        sys.exit(1)
    
    # Setup Next.js if needed
    nextjs_app = Path("nextjs-app")
    if not (nextjs_app / "node_modules").exists():
        print("\n✓ Installing Next.js dependencies...")
        subprocess.run(['npm', 'install'], cwd='nextjs-app', check=True)
    
    # Create env file for Next.js
    env_local = nextjs_app / ".env.local"
    if not env_local.exists():
        print("\n✓ Creating .env.local for Next.js...")
        with open(env_local, 'w') as f:
            f.write("PYTHON_BACKEND_URL=http://localhost:5000\n")
            f.write("NEXT_PUBLIC_API_URL=http://localhost:3000\n")
        print("  Created: nextjs-app/.env.local")
    
    print("\n" + "="*60)
    print("🚀 STARTING SERVERS")
    print("="*60)
    
    print("\nPress Ctrl+C to stop all servers\n")
    
    # Start Flask backend
    flask_process = run_command(
        ['python', 'flask_api.py'],
        "Starting Python Flask Backend (Port 5000)"
    )
    
    # Wait for Flask to start
    time.sleep(2)
    
    # Start Next.js frontend
    nextjs_process = run_command(
        ['npm', 'run', 'dev'],
        "Starting Next.js Frontend (Port 3000)"
    )
    
    print("\n" + "="*60)
    print("✅ SERVERS STARTED")
    print("="*60)
    print("\n📍 Frontend:  http://localhost:3000")
    print("📍 Backend:   http://localhost:5000")
    print("📍 API:       http://localhost:5000/api/chat")
    print("\n🌐 Open http://localhost:3000 in your browser")
    print("\n⏹️  Press Ctrl+C to stop all servers\n")
    
    # Wait for processes
    try:
        flask_process.wait()
        nextjs_process.wait()
    except KeyboardInterrupt:
        print("\n\n" + "="*60)
        print("⏹️  Shutting down servers...")
        print("="*60)
        flask_process.terminate()
        nextjs_process.terminate()
        time.sleep(1)
        flask_process.kill()
        nextjs_process.kill()
        print("✓ Servers stopped")

if __name__ == '__main__':
    main()
