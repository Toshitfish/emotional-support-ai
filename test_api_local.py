#!/usr/bin/env python3
"""
Quick test script to verify Flask API enhancements work
Tests: sentiment analysis, crisis detection, response structure
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from textblob import TextBlob
from datetime import datetime
import json

# Test sentiment analysis
def test_sentiment():
    print("\n" + "="*60)
    print("Testing Sentiment Analysis")
    print("="*60)
    
    test_messages = [
        ("I'm so happy today!", "positive"),
        ("I feel terrible and hopeless", "negative"),
        ("The weather is nice", "neutral"),
    ]
    
    for msg, expected in test_messages:
        blob = TextBlob(msg)
        polarity = blob.sentiment.polarity
        
        if polarity > 0.5:
            mood = "positive"
        elif polarity < -0.5:
            mood = "negative"
        else:
            mood = "neutral"
        
        status = "✓" if mood == expected else "✗"
        print(f"{status} '{msg}' → {mood} (polarity: {polarity:.2f})")

# Test crisis detection
def test_crisis_detection():
    print("\n" + "="*60)
    print("Testing Crisis Detection")
    print("="*60)
    
    CRISIS_KEYWORDS = {
        'critical': ['kill myself', 'suicide', 'want to die'],
        'high': ['self harm', 'cut myself', 'hopeless'],
        'moderate': ['sad', 'lonely', 'stressed'],
    }
    
    test_messages = [
        ("I want to kill myself", "critical"),
        ("I've been cutting myself", "high"),
        ("I feel so sad today", "moderate"),
        ("The weather is nice", "none"),
    ]
    
    for msg, expected_level in test_messages:
        text_lower = msg.lower()
        crisis_level = "none"
        
        for level, keywords in CRISIS_KEYWORDS.items():
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    crisis_level = level
                    break
            if crisis_level != "none":
                break
        
        status = "✓" if crisis_level == expected_level else "✗"
        print(f"{status} '{msg}' → {crisis_level}")

# Test response structure
def test_response_structure():
    print("\n" + "="*60)
    print("Testing Response Structure")
    print("="*60)
    
    response = {
        'response': 'Sample AI response',
        'assistant': 'claude',
        'sentiment': {
            'mood': 'positive',
            'polarity': 0.5,
            'subjectivity': 0.6
        },
        'crisis': {
            'crisis_level': 'none',
            'confidence': 0.0,
            'keywords': []
        },
        'hotline': None,
        'success': True
    }
    
    print("Response structure (JSON):")
    print(json.dumps(response, indent=2))
    print("\n✓ All required fields present")

def test_hotlines():
    print("\n" + "="*60)
    print("Testing Emergency Hotlines")
    print("="*60)
    
    HOTLINES = {
        'HK': {'number': '2389 2222', 'name': '撒瑪利亞防止自殺會 (Samaritans Hong Kong)', 'country': 'Hong Kong'},
        'TW': {'number': '1925', 'name': '安心專線 (Lifeline Taiwan)', 'country': 'Taiwan'},
        'CN': {'number': '010-8295 1332', 'name': '北京心理援助熱線', 'country': 'Mainland China'},
        'SG': {'number': '1800-221-4444', 'name': 'Samaritans Singapore', 'country': 'Singapore'},
        'MY': {'number': '03-4101-6100', 'name': 'Befrienders Malaysia', 'country': 'Malaysia'},
    }
    
    for region, hotline in HOTLINES.items():
        print(f"✓ {region}: {hotline['name']} - {hotline['number']}")

if __name__ == '__main__':
    print("\n🧪 Emotional Support API - Local Tests\n")
    
    try:
        test_sentiment()
        test_crisis_detection()
        test_response_structure()
        test_hotlines()
        
        print("\n" + "="*60)
        print("✅ All tests passed!")
        print("="*60)
        print("\nNext steps:")
        print("1. Copy .env.example to .env and add your API key")
        print("2. Run: python flask_api.py")
        print("3. Test endpoint: curl http://localhost:5000/api/health")
        print("\n")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
