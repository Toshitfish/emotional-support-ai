"""
Enhanced AI Assistant with Claude API
Provides real, intelligent emotional support with deep analysis
"""

import os
import json
from datetime import datetime
from typing import Tuple, Dict, Any
import re

# Try to import Claude
try:
    import anthropic
    CLAUDE_AVAILABLE = True
except ImportError:
    CLAUDE_AVAILABLE = False

class RealEmotionalAIAssistant:
    """
    Real AI assistant using Claude API
    Analyzes student messages deeply and provides specific, personalized support
    """
    
    def __init__(self):
        self.api_key = os.getenv("CLAUDE_API_KEY")
        self.client = None
        self.conversation_history = []
        
        # Initialize Claude if API key is available
        if CLAUDE_AVAILABLE and self.api_key:
            try:
                self.client = anthropic.Anthropic(api_key=self.api_key)
                self.mode = "claude"
                print("✅ Claude API connected - Using AI intelligence")
            except Exception as e:
                print(f"⚠️  Claude connection failed: {e}")
                self.mode = "fallback"
        else:
            self.mode = "fallback"
            if not CLAUDE_AVAILABLE:
                print("⚠️  Install anthropic: pip install anthropic")
            if not self.api_key:
                print("⚠️  Set CLAUDE_API_KEY environment variable")
        
        # Crisis keywords
        self.crisis_keywords = [
            "自殺", "自杀", "想死", "死亡", "結束", "结束",
            "傷害自己", "伤害自己", "割腕", "吞藥", "吞药",
            "尋死", "寻死", "溺水", "跳樓", "跳楼",
            "自害", "suicide", "kill myself", "self harm",
            "hurt myself", "end my life", "noose", "poison"
        ]
        
        self.hotlines = {
            "Hong Kong": "撒瑪利亞防止撥款會: 2389 2222 (24/7)",
            "Taiwan": "安心專線: 1925 (24/7)",
            "Mainland": "全國心理援助熱線: 400-161-9995 (24/7)",
            "Singapore": "1800 221 4444",
            "Malaysia": "03-2149 0000"
        }
    
    def detect_crisis(self, text: str) -> bool:
        """Detect crisis indicators"""
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in self.crisis_keywords)
    
    def get_crisis_response(self) -> str:
        """Generate crisis response"""
        return """
🚨 **I'm very concerned about your safety**  
**我非常擔心你的安全**

---

**您正在經歷危機。請立即聯絡：**

🇭🇰 **Hong Kong**: Samaritans **2389 2222** (24/7)
   WhatsApp: +852 5162 0000

🇹🇼 **Taiwan**: 安心專線 **1925** (24/7)

🇨🇳 **Mainland**: 全國心理援助熱線 **400-161-9995** (24/7)

---

**Your life matters. Please reach out to someone NOW.** ❤️

If you're in immediate danger, please:
- Call emergency services (999/911/112)
- Go to the nearest hospital
- Tell someone you trust immediately

You don't have to face this alone. Help is available. 💙
        """
    
    def analyze_with_claude(self, user_message: str) -> str:
        """Use Claude to analyze and respond"""
        try:
            # Add to history
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            # Create system prompt for emotional support
            system_prompt = """You are an experienced, compassionate emotional support counselor for students. 

Your role:
1. LISTEN deeply to what the student is actually saying
2. ANALYZE their specific situation, emotions, and challenges
3. VALIDATE their feelings - show you understand
4. PROVIDE SPECIFIC, ACTIONABLE advice tailored to their situation
5. ENCOURAGE professional help when appropriate
6. STAY SAFE - never suggest harmful behaviors

Guidelines:
- Respond in the language they use (Chinese/English)
- Be warm, non-judgmental, and genuine
- Ask follow-up questions if their concern is unclear
- Offer concrete coping strategies or steps they can take
- Reference what they specifically shared (not generic advice)
- Be brief but meaningful (2-3 paragraphs)
- Show you understand their unique situation

Remember: You're here to listen, support, and guide them toward help. You're not a therapist, but a caring mentor."""
            
            # Get Claude's response
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                system=system_prompt,
                messages=self.conversation_history
            )
            
            assistant_message = response.content[0].text
            
            # Add to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            print(f"Claude API error: {e}")
            return self.get_fallback_response(user_message)
    
    def get_fallback_response(self, user_message: str) -> str:
        """Fallback response if Claude API fails"""
        # Analyze emotion from keywords
        emotion = self._detect_emotion(user_message)
        
        responses = {
            "stressed": "我聽到你感受到很大的壓力。這種感受是真實的，許多學生都經歷過。能告訴我具體是什麼讓你感到這樣嗎？有時候，將壓力分解為更小的部分會有幫助。",
            "sad": "我很遺憾聽到你感到難過。請記住，這些感受是暫時的，會改變的。你周圍有支援者嗎？有時候傾訴可以帶來很大的幫助。",
            "hopeless": "我明白你現在可能感到絕望。但請相信，這個時刻會過去。很多人在最黑暗的時刻找到了光明。你願意與我分享更多嗎？",
            "anxious": "焦慮是一種常見的感受，特別是在現代。深呼吸和運動有時候可以幫助。但最重要的是，你不需要獨自承受。",
            "neutral": "謝謝你的分享。我正在傾聽。請告訴我更多你的感受。"
        }
        
        return responses.get(emotion, responses["neutral"])
    
    def _detect_emotion(self, text: str) -> str:
        """Basic emotion detection"""
        text_lower = text.lower()
        
        if any(w in text_lower for w in ["壓力", "压力", "stress", "overwhelmed", "too much"]):
            return "stressed"
        elif any(w in text_lower for w in ["難過", "难过", "sad", "hurt", "痛苦"]):
            return "sad"
        elif any(w in text_lower for w in ["絕望", "绝望", "hopeless", "無望", "无望"]):
            return "hopeless"
        elif any(w in text_lower for w in ["焦慮", "焦虑", "anxiety", "nervous", "worried"]):
            return "anxious"
        
        return "neutral"
    
    def get_response(self, user_message: str) -> str:
        """Main method - get intelligent response"""
        
        # Check for crisis first (safety priority)
        if self.detect_crisis(user_message):
            return self.get_crisis_response()
        
        # Use Claude if available, otherwise fallback
        if self.mode == "claude" and self.client:
            return self.analyze_with_claude(user_message)
        else:
            return self.get_fallback_response(user_message)
    
    def get_conversation_summary(self) -> Dict[str, Any]:
        """Get summary of conversation for analysis"""
        return {
            "messages_count": len(self.conversation_history),
            "mode": self.mode,
            "timestamp": datetime.now().isoformat()
        }
    
    def log_interaction(self, user_input: str, response: str):
        """Log for safety monitoring"""
        try:
            with open("emotional_support.log", "a", encoding="utf-8") as f:
                f.write(f"\n[{datetime.now()}]\n")
                f.write(f"User: {user_input[:100]}...\n")
                f.write(f"Mode: {self.mode}\n")
                f.write(f"Crisis detected: {self.detect_crisis(user_input)}\n")
                f.write("-" * 50 + "\n")
        except Exception as e:
            print(f"Error logging: {e}")


# For backward compatibility
EmotionalSupportAssistant = RealEmotionalAIAssistant

# Create global instance for Flask API
_claude_assistant = RealEmotionalAIAssistant()

def get_claude_response(message: str) -> str:
    """Get response from Claude assistant (for Flask API)"""
    return _claude_assistant.get_response(message)

