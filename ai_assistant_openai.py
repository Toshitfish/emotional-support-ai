"""
Real AI Assistant using OpenAI API (ChatGPT)
For users in regions where Claude is unavailable (e.g., Hong Kong, China)
"""

import os
import json
from datetime import datetime
from typing import Tuple, Dict, Any

# Try to import OpenAI
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

class RealEmotionalAIAssistant:
    """
    Real AI assistant using OpenAI API (ChatGPT)
    Analyzes student messages deeply and provides specific, personalized support
    """
    
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = None
        self.conversation_history = []
        self.model = "gpt-4o-mini"  # Fast and cost-effective
        
        # Initialize OpenAI if API key is available
        if OPENAI_AVAILABLE and self.api_key:
            try:
                self.client = OpenAI(api_key=self.api_key)
                self.mode = "openai"
                print("✅ OpenAI API connected - Using ChatGPT intelligence")
            except Exception as e:
                print(f"⚠️  OpenAI connection failed: {e}")
                self.mode = "fallback"
        else:
            self.mode = "fallback"
            if not OPENAI_AVAILABLE:
                print("⚠️  Install openai: pip install openai")
            if not self.api_key:
                print("⚠️  Set OPENAI_API_KEY environment variable")
        
        # Crisis keywords
        self.crisis_keywords = [
            "自殺", "自杀", "想死", "死亡", "結束", "结束",
            "傷害自己", "伤害自己", "割腕", "吞藥", "吞药",
            "尋死", "寻死", "溺水", "跳樓", "跳楼",
            "自害", "suicide", "kill myself", "self harm",
            "hurt myself", "end my life", "noose", "poison"
        ]
    
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

🇭🇰 **Hong Kong | 香港撒瑪利亞防止撥款會**
   📞 24/7 Hotline: **2389 2222**
   💬 WhatsApp: +852 5162 0000
   🌐 Website: www.samaritans.org.hk

🇭🇰 **生命熱線 | Life Line**
   📧 Email: lifelinecentre@samaritans.org.hk

---

**If you are in immediate danger:**
- Call 999 (Hong Kong Emergency)
- Go to the nearest hospital
- Tell someone you trust RIGHT NOW

---

**Your life matters. Please reach out to someone NOW.** ❤️

You don't have to face this alone. Help is available. 💙
        """
    
    def analyze_with_openai(self, user_message: str) -> str:
        """Use OpenAI to analyze and respond"""
        try:
            # Add to history
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            # Create structured system prompt for emotional support
            system_prompt = """You are an experienced, compassionate emotional support counselor for students in Hong Kong.

RESPONSE STRUCTURE - Always follow this format:

**ANALYSIS (What I understand):**
- Identify the core issue/emotion the student is expressing
- Show that you've understood their specific situation
- Be specific, not generic

**EMPATHY & VALIDATION (How I feel with you):**
- Validate their feelings as real and important
- Show genuine understanding and care
- Use their language (Chinese/English as they used)
- Be warm and non-judgmental

**SUPPORT & ACTION (How I can help):**
- Provide 1-3 specific, actionable suggestions or coping strategies
- Tailor advice to their specific situation
- Encourage professional help if appropriate
- End with hope and reassurance

IMPORTANT GUIDELINES:
- Respond in the language they used
- Be genuine and avoid generic phrases
- Ask clarifying questions if needed
- Reference specific things they mentioned
- Keep each section brief (2-4 sentences max)
- Never suggest harmful behaviors
- For crisis signs: prioritize safety and hotlines
- Consider Hong Kong context (DSE exams, family pressure, academic stress, housing issues, etc.)

Remember: You're a caring mentor helping them find their way forward."""
            
            # Get OpenAI's response
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    *self.conversation_history
                ],
                temperature=0.8,
                max_tokens=1024
            )
            
            assistant_message = response.choices[0].message.content
            
            # Add to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            print(f"OpenAI API error: {e}")
            return self.get_fallback_response(user_message)
    
    def get_fallback_response(self, user_message: str) -> str:
        """Fallback response if OpenAI API fails - structured format"""
        emotion = self._detect_emotion(user_message)
        
        # Structured responses for fallback
        responses = {
            "stressed": """**ANALYSIS (What I understand):**
你感到很大的壓力。這種感受在學生中很常見，尤其是在考試季節或有重要截止日期時。

**EMPATHY & VALIDATION (How I feel with you):**
你的壓力是真實的，完全可以理解。許多優秀的學生都經歷過這種感受。你願意分享具體是什麼讓你感到這樣嗎？

**SUPPORT & ACTION (How I can help):**
試試將壓力分解成更小的、可管理的部分。如果可以，每天騰出15分鐘進行深呼吸或散步。記住：你不需要一次性解決所有問題。""",
            
            "sad": """**ANALYSIS (What I understand):**
你現在感到難過。這可能與特定的事件有關，或者只是一種籠罩著你的情緒。

**EMPATHY & VALIDATION (How I feel with you):**
感到難過是完全正常的。你有權利擁有這些感受。很多時候，難過會隨著時間改變。

**SUPPORT & ACTION (How I can help):**
考慮與信任的人分享你的感受。有時候傾訴能帶來極大幫助。如果感受持續，專業輔導員可以提供更深層的支持。""",
            
            "hopeless": """**ANALYSIS (What I understand):**
你現在可能感到絕望，仿佛沒有辦法改變現狀。

**EMPATHY & VALIDATION (How I feel with you):**
我聽到你的痛苦。這些感受雖然很真實，但絕望往往是暫時的。許多人在最黑暗的時刻找到了出路。

**SUPPORT & ACTION (How I can help):**
請不要獨自承受。如果你有自殺念頭，請立即聯絡：撒瑪利亞防止撥款會 2389 2222 (24/7)。與我分享更多細節，或者找一個信任的人傾訴。""",
            
            "anxious": """**ANALYSIS (What I understand):**
你感到焦慮和緊張。這可能與某個特定情況有關，或者只是一種持續的擔心感。

**EMPATHY & VALIDATION (How I feel with you):**
焦慮在現代生活中很常見。你的擔憂是真實的，許多聰明人都經歷過這種感受。

**SUPPORT & ACTION (How I can help):**
嘗試一些放鬆技巧：深呼吸（4秒吸氣，4秒呼氣）、散步或運動。限制社交媒體的使用時間也有幫助。如果焦慮影響日常生活，考慮尋求專業幫助。""",
            
            "neutral": """**ANALYSIS (What I understand):**
感謝你的分享。我正在認真傾聽你的情況。

**EMPATHY & VALIDATION (How I feel with you):**
無論你現在的感受如何，我都在這裡支持你。

**SUPPORT & ACTION (How I can help):**
請告訴我更多細節。我想更好地理解你的處境，這樣我才能提供更有針對性的幫助。"""
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
        
        # Use OpenAI if available, otherwise fallback
        if self.mode == "openai" and self.client:
            return self.analyze_with_openai(user_message)
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
_openai_assistant = RealEmotionalAIAssistant()

def get_openai_response(message: str) -> str:
    """Get response from OpenAI assistant (for Flask API)"""
    return _openai_assistant.get_response(message)

