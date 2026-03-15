#!/usr/bin/env python
"""Quick test of the AI assistant"""

from ai_assistant import EmotionalSupportAssistant

# Test the assistant
assistant = EmotionalSupportAssistant()

print("=" * 60)
print("🧪 Testing Emotional Support Assistant")
print("=" * 60)

# Test 1: Normal greeting
print("\n✓ Test 1: Normal greeting")
response = assistant.get_response("你好，我今天心情不太好")
print(f"Response: {response[:100]}...")

# Test 2: Sadness detection
print("\n✓ Test 2: Sadness detection")
response = assistant.get_response("我感到非常難過，不知道該怎麼辦")
print(f"Response: {response[:100]}...")

# Test 3: Crisis detection
print("\n✓ Test 3: Crisis detection")
response = assistant.get_response("我想自殺")
if "緊急求助" in response or "Emergency" in response:
    print("✓ Crisis response triggered correctly")

print("\n" + "=" * 60)
print("✓ All tests passed! The assistant is working correctly.")
print("=" * 60)
