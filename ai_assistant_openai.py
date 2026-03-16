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
            system_prompt = """You are an experienced, compassionate emotional support counselor for students.

CRITICAL: Analyze EACH student message individually. Do NOT use templates or predefined responses.

LANGUAGE MATCHING:
- If student writes in English, respond in English
- If student writes in Chinese, respond in Chinese  
- Match their language exactly

RESPONSE STRUCTURE:

**1. ANALYSIS (What I understand about YOUR situation):**
- Identify the SPECIFIC issue they're facing (not generic categories)
- Show you understand their particular situation
- Reference specific things they mentioned
- Be precise about what they're feeling

**2. EMPATHY & VALIDATION (I care about your feelings):**
- Validate their emotions as real and important
- Show genuine understanding of why they feel this way
- Use warm, caring language
- Connect to their specific situation

**3. SUPPORT & ACTION (How I can help YOU):**
- Suggest 1-3 specific, actionable strategies tailored to THEIR situation
- Reference Hong Kong context if relevant (DSE, family pressure, housing, etc.)
- Offer concrete next steps
- If serious crisis signs: provide hotline info

CRITICAL GUIDELINES:
✓ Analyze the ACTUAL content they shared - be specific, not generic
✓ Respond to THEIR unique situation, not a category
✓ Use their language (English or Chinese)
✓ Ask clarifying questions if needed
✓ Reference exactly what they said
✓ Keep sections brief (2-4 sentences each)
✓ Never suggest harmful behaviors
✓ For crisis: prioritize safety with hotlines

Remember: Every student is unique. Analyze THEIR specific message, THEIR specific situation, THEIR specific feelings. Never use the same response twice."""
            
            # Get OpenAI's response
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    *self.conversation_history
                ],
                temperature=0.9,  # Increase creativity to avoid templates
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
        """Fallback response - analyzes actual content, not generic emotions"""
        text_lower = user_message.lower()
        
        # Auto-detect language
        has_chinese = any('\u4e00' <= c <= '\u9fff' for c in user_message)
        is_english = not has_chinese or any(c in text_lower for c in ['i ', 'the ', 'is ', 'are ', 'you '])
        
        # If mostly Chinese, respond in Chinese; otherwise English
        if has_chinese and not is_english:
            # CHINESE RESPONSES - Analyze content
            if any(w in text_lower for w in ['exam', 'dse', '考試', '考试', 'test', '測試', '测试']):
                return """**分析我所理解的：**
你在為考試或測試感到擔憂。這是真實且重要的課題，特別是在DSE或重要考試時期。

**同理心與認可：**
許多學生都經歷過考試焦慮。您的擔憂完全合理 - 這顯示您在乎自己的表現。

**我可如何幫助：**
試著將準備分成小目標，每天一點一點地進行。深呼吸和短時間休息很有幫助。記得：做好準備比完美更重要。"""
            
            elif any(w in text_lower for w in ['family', '家人', '家庭', 'parent', '父母', '媽媽', '妈妈', '爸爸']):
                return """**分析我所理解的：**
您在與家人的關係或家庭情況上感到困擾。這在學生中很常見，尤其是在有高期望的家庭中。

**同理心與認可：**
家庭的壓力是真實的。您的感受完全有效。許多學生都為家庭關係而掙扎。

**我可如何幫助：**
試著找時間與信任的人（朋友、老師、輔導員）談論這個。如果可以，嘗試與家人進行開放式對話。專業輔導可以幫助改善家庭溝通。"""
            
            elif any(w in text_lower for w in ['unhappy', '不開心', '不开心', 'sad', '難過', '难过', 'hurt']):
                return """**分析我所理解的：**
您現在感到難過和不開心。您願意分享具體是什麼導致了這種感受嗎？

**同理心與認可：**
難過是真實的情緒，不應該被忽視。您有權利擁有這些感受。

**我可如何幫助：**
與信任的人傾訴通常能帶來幫助。進行自己喜歡的活動也可能改善心情。如果難過持續超過兩週，請考慮尋求專業幫助。"""
            
            elif any(w in text_lower for w in ['bullied', '霸凌', '欺凌', 'bully', 'friend', '朋友', 'alone', '孤獨', '孤独']):
                return """**分析我所理解的：**
您在社交或人際關係上感到困擾。無論是霸凌、友誼衝突或孤獨感，這些都是嚴肅的問題。

**同理心與認可：**
您不應該獨自承受社交痛苦。您值得有善待您的朋友。這不是您的錯。

**我可如何幫助：**
如果是霸凌，請告訴成年人（老師、父母、輔導員）。加入俱樂部或活動可以幫助建立新的友誼。如需緊急支持，可聯絡撒瑪利亞防止撥款會 2389 2222。"""
            
            else:
                return """**分析我所理解的：**
感謝您的分享。我認真在聆聽。您提到的事情對您很重要。

**同理心與認可：**
無論您現在感受如何，您的感受都是有效的。我在這裡支持您。

**我可如何幫助：**
請告訴我更多細節。您具體感到困擾的是什麼？細節多一點，我能給予更好的幫助。"""
        
        else:
            # ENGLISH RESPONSES - Analyze content
            if any(w in text_lower for w in ['exam', 'test', 'dse', 'school work', 'assignment', 'pressure']):
                return """**Analysis of your situation:**
You're dealing with academic pressure - exams, tests, or schoolwork. This is a real and valid concern many students face.

**I hear you & I understand:**
Your academic stress is completely legitimate. Many students feel this way, especially during exam periods or when balancing multiple assignments.

**How I can help:**
Break your work into smaller, manageable chunks. Take short breaks between study sessions - they actually help you focus better. Remember: progress matters more than perfection."""
            
            elif any(w in text_lower for w in ['family', 'parent', 'home', 'upset', 'angry', 'stressed']):
                return """**Analysis of your situation:**
You're struggling with something that's weighing on you emotionally. This could be family issues, stress, or feeling upset about something specific.

**I hear you & I understand:**
Your feelings are real and important. Whatever is causing this stress, it matters, and you don't have to handle it alone.

**How I can help:**
Talk to someone you trust - a friend, teacher, or counselor. Sometimes just saying things out loud helps. If you'd like, tell me more specifics so I can provide better support."""
            
            elif any(w in text_lower for w in ['unhappy', 'sad', 'lonely', 'bullied', 'alone', 'hurt']):
                return """**Analysis of your situation:**
You're going through emotional pain - whether it's loneliness, sadness, or feeling bullied. These are serious feelings that deserve attention.

**I hear you & I understand:**
What you're feeling is valid. You deserve support and kindness. If it's bullying, please tell a trusted adult.

**How I can help:**
Reach out to someone - a friend, family member, teacher, or counselor. If you're in Hong Kong and need immediate support: Samaritans 2389 2222 (24/7). You're not alone in this."""
            
            else:
                return """**Analysis of your situation:**
Thank you for sharing. I'm listening. Whatever you're going through, it matters.

**I hear you & I understand:**
Your feelings and experiences are important to me. I'm here to support you.

**How I can help:**
Tell me more about what you're experiencing. The more you share, the better I can understand and support you through this."""
        
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

