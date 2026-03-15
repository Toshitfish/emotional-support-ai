"""
Real AI Assistant using Google Gemini API
For users in regions where OpenAI and Claude are unavailable (e.g., Hong Kong, China)
"""

import os
import json
from datetime import datetime
from typing import Tuple, Dict, Any

# Try to import Google Generative AI
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

class RealEmotionalAIAssistant:
    """
    Real AI assistant using Google Gemini API
    Analyzes student messages deeply and provides specific, personalized support
    """
    
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.model = None
        self.conversation_history = []
        
        # Initialize Gemini if API key is available
        if GEMINI_AVAILABLE and self.api_key:
            try:
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel('gemini-1.5-flash')
                self.mode = "gemini"
                print("✅ Google Gemini API connected - Using real AI intelligence")
            except Exception as e:
                print(f"⚠️  Gemini connection failed: {e}")
                self.mode = "fallback"
        else:
            self.mode = "fallback"
            if not GEMINI_AVAILABLE:
                print("⚠️  Install google-generativeai: pip install google-generativeai")
            if not self.api_key:
                print("⚠️  Set GOOGLE_API_KEY environment variable")
        
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

🇭🇰 **Hong Kong | 撒瑪利亞防止撥款會**
   📞 24/7 Hotline: **2389 2222**
   💬 WhatsApp: +852 5162 0000
   🌐 Website: www.samaritans.org.hk
   📧 Email: lifelinecentre@samaritans.org.hk

🇭🇰 **撒瑪利亞防止撨款會 - 生命熱線**
   📞 **2389 2222** (24小時)

---

**If you are in immediate danger:**
- Call 999 (Hong Kong Emergency)
- Go to the nearest hospital
- Tell someone you trust RIGHT NOW

---

**Your life matters. Please reach out to someone NOW.** ❤️

You don't have to face this alone. Help is available. 💙
        """
    
    def analyze_with_gemini(self, user_message: str) -> str:
        """Use Google Gemini to analyze and respond"""
        try:
            # Create system prompt for emotional support
            system_prompt = """You are an experienced, compassionate emotional support counselor for students in Hong Kong.

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
- Consider Hong Kong context (DSE exams, housing pressure, etc.)

Remember: You're here to listen, support, and guide them toward help. You're not a therapist, but a caring mentor."""
            
            # Build conversation history for context
            conversation_text = system_prompt + "\n\n"
            
            # Add previous messages for context
            for msg in self.conversation_history[-4:]:  # Keep last 4 messages for context
                if msg["role"] == "user":
                    conversation_text += f"Student: {msg['content']}\n\n"
                else:
                    conversation_text += f"Counselor: {msg['content']}\n\n"
            
            # Add current message
            conversation_text += f"Student: {user_message}\n\nCounselor:"
            
            # Get Gemini's response
            response = self.model.generate_content(
                conversation_text,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=1024,
                    temperature=0.7,
                )
            )
            
            assistant_message = response.text
            
            # Add to history
            self.conversation_history.append({"role": "user", "content": user_message})
            self.conversation_history.append({"role": "assistant", "content": assistant_message})
            
            return assistant_message
            
        except Exception as e:
            print(f"Gemini API error: {e}")
            return self.get_fallback_response(user_message)
    
    def get_fallback_response(self, user_message: str) -> str:
        """Fallback response if Gemini API fails"""
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
        
        # Use Gemini if available, otherwise fallback
        if self.mode == "gemini" and self.model:
            return self.analyze_with_gemini(user_message)
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
