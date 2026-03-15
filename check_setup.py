#!/usr/bin/env python
"""Setup verification script"""

import os
import sys
from pathlib import Path

def check_environment():
    """Check if the environment is properly set up"""
    
    print("=" * 60)
    print("🔍 Emotional Support Website - Setup Verification")
    print("=" * 60)
    
    checks_passed = 0
    checks_total = 0
    
    # Check Python version
    checks_total += 1
    print(f"\n✓ Python version: {sys.version.split()[0]}")
    if sys.version_info >= (3, 8):
        print("  ✅ Python version OK")
        checks_passed += 1
    else:
        print("  ❌ Python 3.8+ required")
    
    # Check required files
    required_files = [
        'app.py',
        'ai_assistant.py',
        'ai_assistant_advanced.py',
        'requirements.txt',
        'README.md',
        'QUICK_START.md'
    ]
    
    print("\n📋 Checking required files:")
    for file in required_files:
        checks_total += 1
        if os.path.exists(file):
            print(f"  ✅ {file}")
            checks_passed += 1
        else:
            print(f"  ❌ {file} - MISSING")
    
    # Check Python packages
    print("\n📦 Checking Python packages:")
    try:
        import streamlit
        checks_total += 1
        print(f"  ✅ streamlit ({streamlit.__version__})")
        checks_passed += 1
    except ImportError:
        checks_total += 1
        print("  ⚠️  streamlit not installed - run: pip install -r requirements.txt")
    
    # Check if modules can be imported
    print("\n🔧 Checking module imports:")
    try:
        checks_total += 1
        from ai_assistant import EmotionalSupportAssistant
        print("  ✅ ai_assistant module")
        checks_passed += 1
    except Exception as e:
        checks_total += 1
        print(f"  ❌ ai_assistant module: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    print(f"✅ Passed: {checks_passed}/{checks_total}")
    
    if checks_passed == checks_total:
        print("\n🎉 All checks passed! You're ready to go!")
        print("\n🚀 To start the app, run:")
        print("   streamlit run app.py")
        return 0
    else:
        print("\n⚠️  Some checks failed. Please install missing dependencies:")
        print("   pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    exit_code = check_environment()
    sys.exit(exit_code)
