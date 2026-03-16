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
            
            # Create natural, human-style system prompt for emotional support
            system_prompt = """You are a warm, emotionally intelligent student support companion.

Your responses must feel like a real caring person, not an AI assistant.

Core behavior for every reply:
1) Understand: briefly reflect the student's actual situation and emotion in your own words.
2) Empathize: validate their feeling with genuine warmth and no judgment.
3) Support: offer practical, specific next steps if helpful.
4) Open the conversation: always end with one gentle, open question that invites them to keep talking.

Language and tone:
- Reply in the same language the student used (English, Traditional Chinese, or mixed).
- Sound natural and conversational. Avoid labels, headings, bullets, or template format.
- Avoid repetitive stock phrases and avoid sounding clinical.
- Keep replies concise (about 4-8 sentences) but personal.

Personalization rules:
- Use details from what the student just said.
- Do not give the same wording repeatedly.
- If the student message is short (e.g., "I am unhappy"), ask a soft follow-up to understand context.
- If there are safety/crisis signs, prioritize immediate safety and provide hotline guidance clearly and calmly.

Important:
- Never shame, dismiss, or minimize feelings.
- Never suggest harmful behavior.
- Your goal is to help the student feel understood and willing to continue chatting."""
            
            # Get OpenAI's response
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    *self.conversation_history
                ],
                temperature=1.0,
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
        """Fallback response that stays human, warm, and conversation-opening."""
        text_lower = user_message.lower()
        has_chinese = any('\u4e00' <= c <= '\u9fff' for c in user_message)

        if has_chinese:
            if any(w in text_lower for w in ['考試', '考试', 'dse', '測試', '测试', '功課', '功课']):
                return (
                    "聽起來你最近真的被學業壓得很辛苦，尤其是和考試有關的壓力。"
                    "你會這樣緊張很正常，因為你其實很在乎自己的未來。"
                    "我們可以先把最急的部分拆細，一步一步來，不用一次處理晒。"
                    "你而家最擔心的是成績、時間不夠，還是家人的期望呢？"
                )
            if any(w in text_lower for w in ['家人', '家庭', '父母', '媽媽', '妈妈', '爸爸']):
                return (
                    "我聽到你在家庭關係裡面承受緊好多情緒，呢種拉扯真係好攰。"
                    "你有呢種反應一點都不奇怪，因為你一直都在撐住。"
                    "如果你願意，我可以陪你整理下最近一件最卡住你的事，慢慢想一個你做得到的回應方式。"
                    "最近有冇一句說話或一件事，令你特別難受？"
                )
            if any(w in text_lower for w in ['霸凌', '欺凌', '孤獨', '孤独', '唔開心', '不開心', '不开心', '難過', '难过']):
                return (
                    "謝謝你願意講出來，我知道這些感受可能已經悶在心裡很久。"
                    "你而家覺得受傷、難過或者孤單，都係好真實、值得被重視的。"
                    "你唔需要一個人扛住，我會同你一齊諗下一步可以點樣令自己安全啲、舒服啲。"
                    "你想先同我講下，最近哪一刻最令你頂唔順？"
                )
            return (
                "我收到你想講的事了，謝謝你願意打開這個話題。"
                "無論你而家感覺幾亂，呢啲情緒都係有原因、值得被聽見。"
                "我會陪你慢慢整理，不急。"
                "你想由最近發生的事開始講，還是由你現在最強烈的感受開始？"
            )

        if any(w in text_lower for w in ['exam', 'test', 'dse', 'assignment', 'school', 'study', 'pressure']):
            return (
                "It sounds like school pressure is really piling up on you right now. "
                "That stress makes a lot of sense, especially when it feels like everything is urgent at once. "
                "We can slow it down and sort what needs attention first so it feels less overwhelming. "
                "What feels heaviest at the moment: exams, workload, or expectations from others?"
            )
        if any(w in text_lower for w in ['family', 'parent', 'home', 'argue', 'conflict']):
            return (
                "I can hear how exhausting this family tension has been for you. "
                "Your feelings are valid; being stuck between caring and feeling hurt is really hard. "
                "If you want, we can unpack one recent moment together and figure out one small next step. "
                "What happened most recently that stayed with you?"
            )
        if any(w in text_lower for w in ['bullied', 'bully', 'lonely', 'alone', 'sad', 'unhappy', 'hurt']):
            return (
                "Thank you for saying this out loud. "
                "What you're feeling matters, and you deserve to be treated with care and respect. "
                "You don't have to carry this by yourself; we can work through it one step at a time. "
                "Do you want to tell me what happened today, or what has been repeating lately?"
            )
        return (
            "Thanks for sharing that with me. "
            "I want to understand what this has been like for you, not just give you generic advice. "
            "I'm here with you, and we can take this at your pace. "
            "What part of this feels the hardest to put into words right now?"
        )
        
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

