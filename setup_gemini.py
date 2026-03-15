#!/usr/bin/env python3
"""
Google Gemini Setup Wizard for Emotional Support Website
Helps users get their Google API key and set up Gemini AI
"""

import os
import sys
from pathlib import Path

def print_header():
    """Print welcome banner"""
    print("\n" + "="*70)
    print("🤖 Google Gemini Setup Wizard".center(70))
    print("🌏 Perfect for Hong Kong & all regions".center(70))
    print("="*70 + "\n")

def print_step(num, title):
    """Print a numbered step"""
    print(f"\n{'='*70}")
    print(f"STEP {num}: {title}")
    print("="*70)

def get_api_key():
    """Get API key from user"""
    print_step(1, "Get Your Google API Key")
    print("""
Google Gemini is FREE and accessible from Hong Kong, China, and everywhere!

📍 Steps to get your API key:
1. Go to: https://aistudio.google.com/app/apikey
2. Click "Create API Key"
3. Select or create a project
4. Copy the generated key
5. Paste it below when prompted

⏱️  Takes about 30 seconds!
""")
    
    api_key = input("🔑 Enter your Google API Key: ").strip()
    
    if not api_key:
        print("❌ No API key provided. Exiting.")
        return None
    
    if len(api_key) < 10:
        print("❌ API key seems too short. Please try again.")
        return None
    
    return api_key

def verify_api_key(api_key):
    """Test the API key"""
    print_step(2, "Verify API Key")
    print("Testing your API key...")
    
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Simple test message
        response = model.generate_content("Hello! Say 'API key verified' if you can read this.")
        
        if response.text:
            print(f"✅ API key verified successfully!")
            print(f"   Response: {response.text[:50]}...")
            return True
    except Exception as e:
        print(f"❌ API key verification failed:")
        print(f"   Error: {str(e)}")
        return False
    
    return False

def save_to_env(api_key):
    """Save API key to .env file"""
    print_step(3, "Save to .env File")
    
    env_file = Path(".env")
    
    # Check if .env exists
    if env_file.exists():
        print("Found existing .env file")
        backup = input("Create backup? (y/n): ").strip().lower()
        if backup == 'y':
            backup_file = Path(".env.backup")
            with open(env_file, 'r') as f:
                backup_content = f.read()
            with open(backup_file, 'w') as f:
                f.write(backup_content)
            print(f"✅ Backup saved to .env.backup")
        
        # Check if GOOGLE_API_KEY already exists
        with open(env_file, 'r') as f:
            content = f.read()
        
        if "GOOGLE_API_KEY=" in content:
            print("⚠️  GOOGLE_API_KEY already exists in .env")
            overwrite = input("Overwrite? (y/n): ").strip().lower()
            if overwrite != 'y':
                return False
            # Remove old GOOGLE_API_KEY line
            lines = [line for line in content.split('\n') 
                    if not line.startswith('GOOGLE_API_KEY=')]
            content = '\n'.join(lines)
        
        # Add new key
        if not content.endswith('\n'):
            content += '\n'
        content += f"GOOGLE_API_KEY={api_key}\n"
        
        with open(env_file, 'w') as f:
            f.write(content)
        print(f"✅ API key saved to .env")
    else:
        # Create new .env file
        env_content = f"""# Google Gemini Configuration
GOOGLE_API_KEY={api_key}

# For more options, see .env.example
"""
        with open(env_file, 'w') as f:
            f.write(env_content)
        print(f"✅ Created .env file with API key")
    
    return True

def print_next_steps():
    """Print what to do next"""
    print_step(4, "You're All Set!")
    print("""
🎉 Congratulations! Google Gemini is now configured.

🚀 Next steps:
1. Start the app:
   streamlit run app.py

2. Open the app in your browser (usually http://localhost:8501)

3. Start chatting with your emotional support AI!

💡 Features:
   ✓ Chat in English or Chinese
   ✓ Crisis detection with Hong Kong hotlines
   ✓ Context-aware emotional support
   ✓ Works 100% in Hong Kong
   ✓ FREE to use

🆘 In a crisis?
   Call Samaritans: 2389 2222 (Hong Kong)
   Or WhatsApp: +852 5162 0000

❓ Need help?
   See GET_GOOGLE_API_KEY.md for more info
   Or check the README.md file

Thank you for using the Emotional Support Website! 💚
""")

def main():
    """Main setup flow"""
    print_header()
    
    # Step 1: Get API key
    api_key = get_api_key()
    if not api_key:
        return False
    
    # Step 2: Verify API key (optional but recommended)
    print("\n" + "-"*70)
    verify = input("Verify API key before saving? (Recommended) (y/n): ").strip().lower()
    if verify == 'y':
        if not verify_api_key(api_key):
            print("\n⚠️  Continuing anyway...")
    
    # Step 3: Save to .env
    if not save_to_env(api_key):
        print("Setup cancelled.")
        return False
    
    # Step 4: Print next steps
    print_next_steps()
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed with error: {e}")
        sys.exit(1)
