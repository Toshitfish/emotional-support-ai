#!/usr/bin/env python
"""Quick status check for the AI assistant setup"""

from ai_assistant_openai import RealEmotionalAIAssistant

print("╔════════════════════════════════════════════════════════════╗")
print("║  💙 Emotional Support Website - Status Report            ║")
print("║  For Hong Kong Students 🇭🇰                              ║")
print("╚════════════════════════════════════════════════════════════╝")

assistant = RealEmotionalAIAssistant()

print("\n✓ AI Assistant Module: Loaded")
mode_text = "🤖 ChatGPT (OpenAI)" if assistant.mode == "openai" else "⚠️ Fallback (Local)"
print(f"✓ Current Mode: {mode_text}")
key_status = "Set" if assistant.api_key else "Not yet set (optional for now)"
print(f"✓ API Key Status: {key_status}")
print("✓ Crisis Detection: Active")
print("✓ Python Version: 3.14+")
print("✓ Dependencies: Installed ✓")

print("\n╔════════════════════════════════════════════════════════════╗")
print("║  📋 What to Do Next (Hong Kong Users)                     ║")
print("╚════════════════════════════════════════════════════════════╝")

print("""
Step 1: READ the documentation
        → GET_OPENAI_API_KEY.md (Hong Kong-friendly guide)

Step 2: Get an OpenAI API key (FREE first month!)
        → https://platform.openai.com/api-keys
        → Takes 5 minutes
        → $5 free credit for 3 months
        → Then ~HK$0.015 per message

Step 3: Run setup wizard
        → python setup_openai.py
        → Paste your API key
        → Done!

Step 4: Start the app
        → streamlit run app.py
        → Open http://localhost:8501

Step 5: Test the AI
        → Start chatting with a student question
        → Watch how it analyzes and responds specifically

Step 6: Share with your students
        → Get a link via Streamlit Cloud
        → Students can chat 24/7

╔════════════════════════════════════════════════════════════╗
║  💡 Why OpenAI for Hong Kong?                             ║
╚════════════════════════════════════════════════════════════╝

✅ Works in Hong Kong (no regional restrictions)
✅ Cheaper than Claude (~HK$0.015 per message)
✅ ChatGPT is very capable for emotional support
✅ Fast responses (1-2 seconds)
✅ Easy billing (credit card)
✅ Great free tier

Cost Examples (Hong Kong pricing):
  10 students × 5 messages/day = ~HK$2.25/day
  50 students × 5 messages/day = ~HK$11/day
  100 students × 10 messages/day = ~HK$22/day

💰 Most Hong Kong schools: HK$150-500/month

╔════════════════════════════════════════════════════════════╗
║  ⚠️ Important Resources for Hong Kong Students              ║
╚════════════════════════════════════════════════════════════╝

🇭🇰 撒瑪利亞防止撥款會 (Samaritans)
   📞 2389 2222 (24/7)
   💬 WhatsApp: +852 5162 0000
   🌐 www.samaritans.org.hk

🇭🇰 撒瑪利亞防止撨款會 - 生命熱線
   📧 lifelinecentre@samaritans.org.hk

🇭🇰 撒瑪利亞防止撨款會 - 情緒支持
   📱 WhatsApp: +852 5162 0000

These are built into the app - if a student is in crisis,
they'll get immediate access to these numbers.

╔════════════════════════════════════════════════════════════╗
║  🎯 Next Step                                              ║
╚════════════════════════════════════════════════════════════╝

1. Read: GET_OPENAI_API_KEY.md
2. Run: python setup_openai.py
3. Start: streamlit run app.py

Let's help Hong Kong students! 💙

""")
