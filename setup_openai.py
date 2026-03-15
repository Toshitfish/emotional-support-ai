#!/usr/bin/env python
"""
Interactive setup wizard for OpenAI API
Guides users through getting their API key and configuring the app
For Hong Kong and regions where Claude is unavailable
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)

def print_step(number, text):
    """Print a step"""
    print(f"\n📍 Step {number}: {text}")

def check_openai():
    """Check if openai is installed"""
    try:
        import openai
        return True
    except ImportError:
        return False

def test_api_key(api_key):
    """Test if API key is valid"""
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        # Try to complete a simple message
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Hi"}],
            max_tokens=100
        )
        return True, "✅ API key is valid!"
    except Exception as e:
        return False, f"❌ Error: {str(e)}"

def main():
    print_header("💙 Emotional Support Website - OpenAI Setup Wizard")
    print("\n🇭🇰 Perfect for Hong Kong, Taiwan, and Asian regions!\n")
    
    # Check if already set up
    current_key = os.getenv("OPENAI_API_KEY")
    if current_key:
        print(f"\n✅ OPENAI_API_KEY is already set!")
        test_valid, msg = test_api_key(current_key)
        print(f"   {msg}")
        if test_valid:
            proceed = input("\n   Do you want to set a new key? (y/n): ").lower()
            if proceed != 'y':
                print("\n✅ Setup is complete! Run: streamlit run app.py")
                return 0
    
    # Step 1: Check dependencies
    print_step(1, "Checking dependencies...")
    if not check_openai():
        print("   ❌ openai package not found")
        print("   Installing dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "-q"])
    else:
        print("   ✅ All packages installed")
    
    # Step 2: Get API key
    print_step(2, "Get Your OpenAI API Key")
    print("""
   To use ChatGPT for emotional support:
   
   1. Go to: https://platform.openai.com/api-keys
   2. Sign up or log in with your account
   3. Click "Create new secret key"
   4. Copy the key (looks like: sk-proj-xxxxxxxxxxxx)
   5. Keep it safe! 🔐
   
   💰 Pricing: 
      - Free: $5 credits for first 3 months (great for testing!)
      - Then: ~HK$0.015 per message for emotional support
      - Hong Kong schools typically spend HK$150-500/month
    """)
    
    api_key = input("\n   Paste your API key here: ").strip()
    
    if not api_key:
        print("\n   ❌ No API key provided. Setup cancelled.")
        return 1
    
    if not api_key.startswith("sk-proj-"):
        print("\n   ⚠️  Warning: API key should start with 'sk-proj-'")
        print("      (Old format 'sk-' keys may not work)")
        confirm = input("   Continue anyway? (y/n): ").lower()
        if confirm != 'y':
            return 1
    
    # Step 3: Test API key
    print_step(3, "Testing API key...")
    print("   Connecting to OpenAI API...")
    valid, msg = test_api_key(api_key)
    print(f"   {msg}")
    
    if not valid:
        print("\n   ❌ API key test failed.")
        print("   Make sure:")
        print("      - You copied the full key")
        print("      - You added a payment method")
        print("      - Your account is active")
        return 1
    
    # Step 4: Set environment variable
    print_step(4, "Saving API key...")
    
    platform = sys.platform
    if platform == "win32":
        # Windows
        os.system(f'setx OPENAI_API_KEY "{api_key}"')
        print("   ✅ API key saved to Windows environment variables")
        print("   ℹ️  Note: You may need to restart your terminal for changes to take effect")
    else:
        # Mac/Linux
        print(f"\n   Add this line to your shell profile (~/.bashrc or ~/.zshrc):")
        print(f"   export OPENAI_API_KEY='{api_key}'")
    
    # Also create .env file as backup
    env_file = Path(".env")
    env_file.write_text(f"OPENAI_API_KEY={api_key}\n")
    print("   ✅ API key also saved to .env file")
    
    # Step 5: Verify setup
    print_step(5, "Verifying setup...")
    
    # Create a small test script
    test_code = """
import os
from ai_assistant_openai import RealEmotionalAIAssistant

assistant = RealEmotionalAIAssistant()
if assistant.mode == 'openai':
    print('✅ SUCCESS! ChatGPT AI is ready!')
else:
    print('❌ Still in fallback mode. Restart your app and try again.')
"""
    
    result = subprocess.run(
        [sys.executable, "-c", test_code],
        capture_output=True,
        text=True
    )
    
    print("   " + result.stdout.strip())
    if result.returncode != 0:
        print("   Error:", result.stderr)
    
    # Final instructions
    print_header("🎉 Setup Complete!")
    print("""
   You're all set! Here's what to do next:
   
   1. Close this terminal completely
   2. Open a new terminal/PowerShell
   3. Run: streamlit run app.py
   4. Check the app - you should see a green checkmark:
      "🤖 AI Mode: ChatGPT (OpenAI)" ✅
   
   If you still see fallback mode:
   - Restart your terminal and try again
   - Check that OPENAI_API_KEY is set
   - Verify .env file exists with your key
   
   🚀 You now have a real AI assistant using ChatGPT!
   
   📚 For more info, see: GET_OPENAI_API_KEY.md
   💙 Good luck helping your students in Hong Kong!
    """)
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    if exit_code == 0:
        input("\nPress Enter to close...")
    sys.exit(exit_code)
