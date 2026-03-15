#!/usr/bin/env python
"""
Interactive setup wizard for Claude API
Guides users through getting their API key and configuring the app
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

def check_anthropic():
    """Check if anthropic is installed"""
    try:
        import anthropic
        return True
    except ImportError:
        return False

def test_api_key(api_key):
    """Test if API key is valid"""
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        # Try to complete a simple message
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=100,
            messages=[{"role": "user", "content": "Hi"}]
        )
        return True, "✅ API key is valid!"
    except Exception as e:
        return False, f"❌ Error: {str(e)}"

def main():
    print_header("💙 Emotional Support Website - Claude AI Setup Wizard")
    
    # Check if already set up
    current_key = os.getenv("CLAUDE_API_KEY")
    if current_key:
        print(f"\n✅ CLAUDE_API_KEY is already set!")
        test_valid, msg = test_api_key(current_key)
        print(f"   {msg}")
        if test_valid:
            proceed = input("\n   Do you want to set a new key? (y/n): ").lower()
            if proceed != 'y':
                print("\n✅ Setup is complete! Run: streamlit run app.py")
                return 0
    
    # Step 1: Check dependencies
    print_step(1, "Checking dependencies...")
    if not check_anthropic():
        print("   ❌ anthropic package not found")
        print("   Installing dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    else:
        print("   ✅ All packages installed")
    
    # Step 2: Get API key
    print_step(2, "Get Your Claude API Key")
    print("""
   To use the intelligent AI assistant, you need a Claude API key:
   
   1. Go to: https://console.anthropic.com/
   2. Click "Sign Up" or "Sign In"
   3. Navigate to "API Keys"
   4. Click "Create Key"
   5. Copy the key (looks like: sk-ant-xxxxxxxxxxxx)
   
   💰 Pricing: Free tier (100K tokens/month) or pay-as-you-go (~$0.003 per message)
    """)
    
    api_key = input("\n   Paste your API key here: ").strip()
    
    if not api_key:
        print("\n   ❌ No API key provided. Setup cancelled.")
        return 1
    
    if not api_key.startswith("sk-ant-"):
        print("\n   ⚠️  Warning: API key should start with 'sk-ant-'")
        confirm = input("   Continue anyway? (y/n): ").lower()
        if confirm != 'y':
            return 1
    
    # Step 3: Test API key
    print_step(3, "Testing API key...")
    print("   Connecting to Claude API...")
    valid, msg = test_api_key(api_key)
    print(f"   {msg}")
    
    if not valid:
        print("\n   ❌ API key test failed. Please check your key and try again.")
        return 1
    
    # Step 4: Set environment variable
    print_step(4, "Saving API key...")
    
    platform = sys.platform
    if platform == "win32":
        # Windows
        os.system(f'setx CLAUDE_API_KEY "{api_key}"')
        print("   ✅ API key saved to Windows environment variables")
        print("   ℹ️  Note: You may need to restart your terminal for changes to take effect")
    else:
        # Mac/Linux
        print(f"\n   Add this line to your shell profile (~/.bashrc or ~/.zshrc):")
        print(f"   export CLAUDE_API_KEY='{api_key}'")
    
    # Also create .env file as backup
    env_file = Path(".env")
    env_file.write_text(f"CLAUDE_API_KEY={api_key}\n")
    print("   ✅ API key also saved to .env file")
    
    # Step 5: Verify setup
    print_step(5, "Verifying setup...")
    
    # Create a small test script
    test_code = """
import os
from ai_assistant_claude import RealEmotionalAIAssistant

assistant = RealEmotionalAIAssistant()
if assistant.mode == 'claude':
    print('✅ SUCCESS! Claude AI is ready!')
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
      "🤖 AI Mode: Real Intelligence (Claude)" ✅
   
   If you still see fallback mode:
   - Restart your terminal and try again
   - Check that CLAUDE_API_KEY is set: echo $CLAUDE_API_KEY
   - Verify .env file exists with your key
   
   🚀 You now have a real AI assistant for your students!
   
   📚 For more info, see: CLAUDE_AI_GUIDE.md
   💙 Good luck helping your students!
    """)
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    if exit_code == 0:
        input("\nPress Enter to close...")
    sys.exit(exit_code)
