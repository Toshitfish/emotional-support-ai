#!/usr/bin/env python3
"""
Verification script to check if everything is set up correctly
Run this before and after deployment
"""

import subprocess
import sys
import os
from pathlib import Path

def check_python():
    """Check Python and Flask"""
    print("\n📍 Checking Python Setup...")
    try:
        import flask
        print("  ✅ Flask is installed")
        return True
    except ImportError:
        print("  ❌ Flask not found. Run: pip install flask flask-cors")
        return False

def check_nodejs():
    """Check Node.js and npm"""
    print("\n📍 Checking Node.js Setup...")
    try:
        result = subprocess.run(['npm', '--version'], 
                              capture_output=True, text=True, check=True)
        print(f"  ✅ npm {result.stdout.strip()} found")
        return True
    except:
        print("  ❌ Node.js/npm not found. Install from https://nodejs.org")
        return False

def check_nextjs():
    """Check Next.js installation"""
    print("\n📍 Checking Next.js Setup...")
    nextjs_path = Path("nextjs-app")
    
    if not nextjs_path.exists():
        print("  ❌ nextjs-app folder not found!")
        return False
    
    if not (nextjs_path / "package.json").exists():
        print("  ❌ package.json not found in nextjs-app")
        return False
    
    print("  ✅ Next.js project folder found")
    
    if not (nextjs_path / "node_modules").exists():
        print("  ⚠️  node_modules not found. Run: cd nextjs-app && npm install")
        return False
    
    print("  ✅ Dependencies installed")
    return True

def check_flask_api():
    """Check Flask API file"""
    print("\n📍 Checking Flask API Setup...")
    
    if not Path("flask_api.py").exists():
        print("  ❌ flask_api.py not found!")
        return False
    
    print("  ✅ flask_api.py found")
    
    # Check if it has required endpoints
    with open("flask_api.py", 'r') as f:
        content = f.read()
        if '/api/chat' not in content:
            print("  ❌ /api/chat endpoint not found")
            return False
        if '/api/health' not in content:
            print("  ❌ /api/health endpoint not found")
            return False
    
    print("  ✅ API endpoints configured")
    return True

def check_env_files():
    """Check environment files"""
    print("\n📍 Checking Environment Files...")
    
    nextjs_env = Path("nextjs-app/.env.local")
    if not nextjs_env.exists():
        print("  ⚠️  nextjs-app/.env.local not found")
        print("     Create it with: PYTHON_BACKEND_URL=http://localhost:5000")
    else:
        print("  ✅ .env.local found in nextjs-app")
    
    return True

def check_files():
    """Check all required files"""
    print("\n📍 Checking Required Files...")
    
    required_files = [
        "nextjs-app/pages/index.js",
        "nextjs-app/pages/api/chat.js",
        "nextjs-app/pages/_app.js",
        "nextjs-app/pages/_document.js",
        "nextjs-app/styles/globals.css",
        "nextjs-app/next.config.js",
        "nextjs-app/tsconfig.json",
        "nextjs-app/tailwind.config.js",
        "nextjs-app/postcss.config.js",
        "nextjs-app/vercel.json",
        "flask_api.py",
        "VERCEL_SETUP_COMPLETE.md",
        "VERCEL_MIGRATION_GUIDE.md",
        "VERCEL_DEPLOYMENT_GUIDE.md",
    ]
    
    all_exist = True
    for file in required_files:
        path = Path(file)
        if path.exists():
            print(f"  ✅ {file}")
        else:
            print(f"  ❌ {file} MISSING")
            all_exist = False
    
    return all_exist

def check_ports():
    """Check if ports are available"""
    print("\n📍 Checking Ports...")
    
    ports_to_check = {
        3000: "Next.js Frontend",
        5000: "Flask Backend",
    }
    
    for port, service in ports_to_check.items():
        try:
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('127.0.0.1', port))
            sock.close()
            
            if result == 0:
                print(f"  ⚠️  Port {port} ({service}) is in use")
            else:
                print(f"  ✅ Port {port} ({service}) is available")
        except:
            print(f"  ⚠️  Could not check port {port}")
    
    return True

def main():
    print("="*60)
    print("🔍 Emotional Support Website - Setup Verification")
    print("="*60)
    
    checks = {
        "Python/Flask": check_python(),
        "Node.js/npm": check_nodejs(),
        "Next.js": check_nextjs(),
        "Flask API": check_flask_api(),
        "Environment Files": check_env_files(),
        "Required Files": check_files(),
        "Ports Available": check_ports(),
    }
    
    print("\n" + "="*60)
    print("📊 Verification Summary")
    print("="*60)
    
    passed = sum(1 for v in checks.values() if v)
    total = len(checks)
    
    for check_name, result in checks.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {check_name}")
    
    print("\n" + "="*60)
    if passed == total:
        print("✅ ALL CHECKS PASSED!")
        print("="*60)
        print("\nYou're ready to go! Run:")
        print("  • PowerShell: .\\start_both_servers.ps1")
        print("  • Python: python start_both_servers.py")
        print("  • Manual: python flask_api.py & npm run dev")
        return 0
    else:
        print(f"⚠️  {total - passed} check(s) failed")
        print("="*60)
        print("\nFix issues above and run again")
        return 1

if __name__ == '__main__':
    sys.exit(main())
