"""
Test the new Claude-based AI assistant
"""

from ai_assistant_claude import RealEmotionalAIAssistant
import os

print("=" * 70)
print("🧪 Testing Real AI Assistant with Claude")
print("=" * 70)

assistant = RealEmotionalAIAssistant()

print(f"\n📊 Assistant Mode: {assistant.mode}")
print(f"🔑 API Key Set: {'✅ Yes' if assistant.api_key else '❌ No'}")
print(f"💫 Claude Client: {'✅ Connected' if assistant.client else '❌ Not connected'}")

if assistant.mode == "fallback":
    print("\n⚠️  Using fallback mode. To enable Claude AI:")
    print("   1. Get your API key from https://console.anthropic.com/")
    print("   2. Set: CLAUDE_API_KEY=your-key-here")
    print("   3. Restart the app")

print("\n" + "=" * 70)
print("🧪 Test Responses")
print("=" * 70)

# Test cases
test_cases = [
    {
        "name": "Academic Stress",
        "message": "考試臨近，我很擔心自己會失敗。最近每天都睡眠不足，而且對什麼都沒有興趣。"
    },
    {
        "name": "Social Pressure",
        "message": "我覺得自己不如同學聰明，他們都有很多朋友，但我很孤獨。Sometimes I think I don't belong here."
    },
    {
        "name": "Family Issues",
        "message": "我的父母總是互相爭執，我夾在中間。他們對我的期望很高，但我感到筋疲力盡。"
    },
    {
        "name": "Self-doubt",
        "message": "我不知道我的將來會怎樣。我失敗過很多次，有時候我想放棄。但我想改變。"
    }
]

for i, test in enumerate(test_cases, 1):
    print(f"\n{'=' * 70}")
    print(f"Test {i}: {test['name']}")
    print(f"{'=' * 70}")
    print(f"📝 Student Message:\n{test['message']}")
    print(f"\n🤖 AI Response:\n")
    
    response = assistant.get_response(test['message'])
    print(response)
    
    print(f"\n{'─' * 70}")

# Test crisis detection
print(f"\n{'=' * 70}")
print("🚨 Crisis Detection Test")
print(f"{'=' * 70}")

crisis_message = "I can't take this anymore. I want to kill myself."
print(f"Testing: '{crisis_message}'")
print(f"Crisis Detected: {'✅ YES' if assistant.detect_crisis(crisis_message) else '❌ NO'}")

response = assistant.get_response(crisis_message)
print(f"\n🚨 Crisis Response (First 300 chars):\n{response[:300]}...")

print("\n" + "=" * 70)
print("✅ Test Complete!")
print("=" * 70)

# Show conversation history length
summary = assistant.get_conversation_summary()
print(f"\n📊 Conversation Summary:")
print(f"   Messages: {summary['messages_count']}")
print(f"   Mode: {summary['mode']}")
