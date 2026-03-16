"""
Real AI Assistant using OpenAI API (ChatGPT)
For users in regions where Claude is unavailable (e.g., Hong Kong, China)
"""

import os
import json
from datetime import datetime
from typing import Tuple, Dict, Any
from random import choice
import re

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
        self.last_followup = None
        
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

        # Common filler words/phrases that should not be mirrored as key phrases.
        self.noise_tokens = {
            'the', 'this', 'that', 'with', 'from', 'have', 'just', 'really', 'will', 'would',
            'could', 'should', 'been', 'very', 'more', 'some', 'later', 'minute', 'minutes',
            'today', 'yesterday', 'tomorrow', 'hello', 'hi', 'hey', 'haloo', 'okay', 'ok'
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

            analysis = self._analyze_student_message(user_message)
            
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
- Keep replies concise (about 3-6 sentences) but personal.
- Read like real chat, not an essay.

Personalization rules:
- Use details from what the student just said.
- Do not give the same wording repeatedly.
- If the student message is short (e.g., "I am unhappy"), ask a soft follow-up to understand context.
- If they are vague, ask one simple question to help them open up.
- If they share something specific, respond specifically before giving suggestions.
- If there are safety/crisis signs, prioritize immediate safety and provide hotline guidance clearly and calmly.

Important:
- Never shame, dismiss, or minimize feelings.
- Never suggest harmful behavior.
- Your goal is to help the student feel understood and willing to continue chatting."""
            
            # Pass explicit student context so replies are specific and non-generic.
            context_prompt = (
                "Student context extracted from latest message:\n"
                f"- language: {analysis['language']}\n"
                f"- primary_emotion: {analysis['primary_emotion']}\n"
                f"- topics: {', '.join(analysis['topics']) if analysis['topics'] else 'general'}\n"
                f"- urgency: {analysis['urgency']}\n"
                f"- key_phrases: {', '.join(analysis['key_phrases']) if analysis['key_phrases'] else 'none'}\n"
                "Use this context naturally. Do not mention this list explicitly."
            )

            # Get OpenAI's response
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "system", "content": context_prompt},
                    *self.conversation_history
                ],
                temperature=1.05,
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
        """Fallback response that remains conversational and personalized."""
        text_lower = user_message.lower()
        analysis = self._analyze_student_message(user_message)
        has_chinese = analysis['language'] in ['chinese', 'mixed']

        # Keep continuity: if latest input is vague, carry the last meaningful topic.
        topic = analysis['primary_topic']
        if topic == 'general':
            topic = self._topic_from_recent_history() or 'general'

        # Handle greeting/check-in naturally instead of generic support block.
        if self._is_greeting_or_checkin(text_lower):
            if has_chinese:
                greeting_openers = [
                    "哈囉，我在這裡。",
                    "嗨，見到你真好。",
                    "你好呀，我有在聽。",
                ]
                if topic == 'academic':
                    return (
                        f"{choice(greeting_openers)}"
                        "你剛剛提到學業／考試壓力，我記得。"
                        "如果你願意，我們可以先聊最令你緊張的那一部分。"
                        "你想先講讀不完、怕失手，還是家人期望？"
                    )
                return (
                    f"{choice(greeting_openers)}"
                    "你可以慢慢講，我不會催你。"
                    "你現在比較想聊今天發生的事，還是你這陣子的心情？"
                )
            greeting_openers = [
                "Hey, I’m here with you.",
                "Hi, good to hear from you.",
                "Hello, I’m listening.",
            ]
            if topic == 'academic':
                return (
                    f"{choice(greeting_openers)} "
                    "I remember you mentioned exam pressure. "
                    "If you want, we can focus on the most stressful part first and make it manageable. "
                    "Is it more fear of results, not enough time, or panic before studying?"
                )
            return (
                f"{choice(greeting_openers)} "
                "Take your time, we can go at your pace. "
                "Do you want to talk about what happened today, or how you’ve been feeling lately?"
            )

        zh_openers = [
            "謝謝你願意跟我講，",
            "我有聽到你，",
            "你願意說出來已經好重要，",
        ]
        en_openers = [
            "Thanks for sharing this with me, ",
            "I hear you, ",
            "I'm really glad you said this out loud, ",
        ]

        key_phrase = analysis['key_phrases'][0] if analysis['key_phrases'] else None

        if has_chinese:
            opener = choice(zh_openers)
            if topic == 'academic':
                return (
                    f"{opener}聽起來學業壓力真的壓住你了，尤其是你可能一直都在逼自己撐住。"
                    "你有這種焦慮很合理，因為你很在乎自己的表現。"
                    "如果你願意，我們可以先把最急的一件事拆細，先搞掂第一步。"
                    f"{self._next_followup(has_chinese=True, topic='academic', key_phrase=key_phrase)}"
                )
            if topic == 'family':
                return (
                    f"{opener}你在家裡承受的拉扯感我感受得到，真的會令人很累。"
                    "你有這些情緒不是你太敏感，而是你一直在努力撐住關係。"
                    "我們可以先從一件最近最刺痛你的事講起，再想一個你做得到的小回應。"
                    f"{self._next_followup(has_chinese=True, topic='family', key_phrase=key_phrase)}"
                )
            if topic == 'social':
                return (
                    f"{opener}人際上的傷很真，也真的很痛。"
                    "無論是被排擠、被欺負，還是覺得孤單，你的感受都值得被重視。"
                    "你不需要自己扛，我可以陪你慢慢整理，先把你最難受的時刻講出來就好。"
                    f"{self._next_followup(has_chinese=True, topic='social', key_phrase=key_phrase)}"
                )
            if topic == 'emotion':
                return (
                    f"{opener}我聽得出你現在真的不好受。"
                    "你有這些感受完全可以理解，不需要硬撐成『沒事』。"
                    "如果你想，我可以先陪你把情緒講清楚，再一起想一個今晚能做到的小方法。"
                    f"{self._next_followup(has_chinese=True, topic='emotion', key_phrase=key_phrase)}"
                )
            return (
                f"{opener}你現在的狀態對你來說一定不容易。"
                "我不會急著下判斷，你可以慢慢說。"
                "我會在這裡陪你，把事情一層一層理清。"
                f"{self._next_followup(has_chinese=True, topic='general', key_phrase=key_phrase)}"
            )

        opener = choice(en_openers)
        if topic == 'academic':
            return (
                f"{opener}it sounds like school pressure has been building up for a while. "
                "That pressure is real, especially when you care a lot and keep pushing yourself. "
                "If you want, we can break it down and choose one small step for today so it feels less heavy. "
                f"{self._next_followup(has_chinese=False, topic='academic', key_phrase=key_phrase)}"
            )
        if topic == 'family':
            return (
                f"{opener}family tension can feel exhausting, especially when you are trying to keep everything together. "
                "Your feelings make sense, and you are not overreacting. "
                "We can start with one recent moment and work out a response that protects your peace. "
                f"{self._next_followup(has_chinese=False, topic='family', key_phrase=key_phrase)}"
            )
        if topic == 'social':
            return (
                f"{opener}social pain can hit really hard, and you should not have to carry it alone. "
                "Whether it is bullying, exclusion, or loneliness, your experience matters. "
                "I can stay with you through this and help you think through safe next steps. "
                f"{self._next_followup(has_chinese=False, topic='social', key_phrase=key_phrase)}"
            )
        if topic == 'emotion':
            return (
                f"{opener}I can feel that things are heavy for you right now. "
                "What you are feeling is valid, and you do not have to pretend to be okay here. "
                "If you want, we can name what is hurting most first, then decide one small thing that might help tonight. "
                f"{self._next_followup(has_chinese=False, topic='emotion', key_phrase=key_phrase)}"
            )
        return (
            f"{opener}I want to understand your situation, not just give you generic advice. "
            "You can take your time and say it however it comes out. "
            "I am here with you, and we can figure this out step by step. "
            f"{self._next_followup(has_chinese=False, topic='general', key_phrase=key_phrase)}"
        )

    def _analyze_student_message(self, user_message: str) -> Dict[str, Any]:
        """Extract lightweight context so responses can mirror the student's message."""
        text = user_message.strip()
        text_lower = text.lower()

        has_chinese = any('\u4e00' <= c <= '\u9fff' for c in text)
        has_english = bool(re.search(r'[a-zA-Z]', text))

        if has_chinese and has_english:
            language = 'mixed'
        elif has_chinese:
            language = 'chinese'
        else:
            language = 'english'

        topics = []
        if any(w in text_lower for w in ['exam', 'test', 'dse', 'assignment', 'study', 'school', '功課', '功课', '考試', '考试']):
            topics.append('academic')
        if any(w in text_lower for w in ['family', 'parent', 'home', '家人', '家庭', '父母', '媽媽', '妈妈', '爸爸']):
            topics.append('family')
        if any(w in text_lower for w in ['bully', 'bullied', 'friend', 'lonely', 'alone', '霸凌', '欺凌', '朋友', '孤獨', '孤独']):
            topics.append('social')
        if any(w in text_lower for w in [
            'sad', 'unhappy', 'hurt', 'anxious', 'anxiety', 'nervous', 'nervoue', 'stressed', 'stress',
            'hopeless', '難過', '难过', '不開心', '不开心', '焦慮', '焦虑', '壓力', '压力'
        ]):
            topics.append('emotion')

        if not topics:
            topics = ['general']

        if any(w in text_lower for w in ['suicide', 'kill myself', 'want to die', 'end my life', '自殺', '自杀', '想死']):
            urgency = 'critical'
            primary_emotion = 'despair'
        elif any(w in text_lower for w in ['hopeless', 'worthless', 'can\'t go on', '絕望', '绝望']):
            urgency = 'high'
            primary_emotion = 'hopeless'
        elif any(w in text_lower for w in ['panic', 'anxious', 'anxiety', 'nervous', 'nervoue', 'stressed', 'stress', '焦慮', '焦虑', '壓力', '压力']):
            urgency = 'moderate'
            primary_emotion = 'anxiety'
        elif any(w in text_lower for w in ['sad', 'unhappy', 'hurt', '難過', '难过', '不開心', '不开心']):
            urgency = 'moderate'
            primary_emotion = 'sadness'
        else:
            urgency = 'low'
            primary_emotion = 'mixed'

        # Keep short phrase snippets to ground response in student wording.
        raw_phrases = re.findall(r'\b[a-zA-Z]{4,}\b|[\u4e00-\u9fff]{2,6}', text)
        key_phrases = []
        for p in raw_phrases:
            p_clean = p.strip().lower()
            if p_clean in ['that', 'this', 'with', 'from', 'have', 'just', 'really']:
                continue
            if p not in key_phrases:
                key_phrases.append(p)
            if len(key_phrases) >= 4:
                break

        return {
            'language': language,
            'topics': topics,
            'primary_topic': topics[0],
            'urgency': urgency,
            'primary_emotion': primary_emotion,
            'key_phrases': key_phrases,
        }

    def _next_followup(self, has_chinese: bool, topic: str, key_phrase: str = None) -> str:
        """Choose a fresh open-ended question to keep the conversation going."""
        zh_pool = {
            'academic': [
                "你現在最卡住的是哪一科，還是時間根本不夠用？",
                "如果只選一件事先處理，你會想先處理哪一個功課或考試？",
                "最近哪個時段壓力最大，早上、下午還是晚上？",
            ],
            'family': [
                "最近是哪句話或哪件事最影響你？",
                "你最希望家人先明白你哪一點？",
                "如果要描述你在家裡的感受，你會用哪三個字？",
            ],
            'social': [
                "你想由今天發生的事開始講，還是最近一直重複的情況？",
                "那一刻你最受傷的是對方說了什麼，還是沒有人站在你這邊？",
                "你身邊有沒有一個你比較信任、可以先聊一下的人？",
            ],
            'emotion': [
                "此刻最強烈的是難過、焦慮，還是委屈？",
                "你覺得這種感受是突然出現，還是累積了很久？",
                "現在你最需要的是有人聽你說，還是一起想具體做法？",
            ],
            'general': [
                "你想先講最近發生了什麼，還是先講你現在的感受？",
                "如果從0到10分，你現在的壓力大概是幾分？",
                "今天有沒有一個瞬間讓你特別想放棄或特別難受？",
            ],
        }

        en_pool = {
            'academic': [
                "What feels most overwhelming right now: exams, deadlines, or expectations?",
                "If we pick just one task to start with, which one would help you breathe easier?",
                "When does the stress hit hardest for you, morning, afternoon, or late night?",
            ],
            'family': [
                "What happened recently that hurt the most?",
                "What do you wish your family understood about you right now?",
                "If you had to name your feeling at home in three words, what would they be?",
            ],
            'social': [
                "Do you want to start with what happened today, or what keeps repeating?",
                "What hurt more in that moment, what was said, or feeling alone in it?",
                "Is there one person you trust enough to talk to first?",
            ],
            'emotion': [
                "Is it more sadness, anxiety, anger, or feeling numb right now?",
                "Does this feeling come in waves, or has it been constant lately?",
                "Would it help more if I just listen first, or if we plan one small next step?",
            ],
            'general': [
                "What feels hardest to carry at this moment?",
                "Do you want to start with what happened, or how it made you feel?",
                "If your day had one hardest moment, what was it?",
            ],
        }

        pool = zh_pool if has_chinese else en_pool
        options = pool.get(topic, pool['general'])

        # Avoid asking the same follow-up twice in a row when possible.
        candidates = [q for q in options if q != self.last_followup]
        selected = choice(candidates if candidates else options)

        if key_phrase and not self._is_noisy_phrase(key_phrase):
            if has_chinese:
                selected = f"你剛剛提到「{key_phrase}」，{selected}"
            else:
                selected = f"You mentioned \"{key_phrase}\" - {selected}"

        self.last_followup = selected
        return selected

    def _topic_from_recent_history(self) -> str:
        """Infer topic from recent user turns for continuity in fallback mode."""
        recent_users = [m.get('content', '') for m in self.conversation_history if m.get('role') == 'user'][-3:]
        for msg in reversed(recent_users):
            a = self._analyze_student_message(msg)
            if a['primary_topic'] != 'general':
                return a['primary_topic']
        return 'general'

    def _is_greeting_or_checkin(self, text_lower: str) -> bool:
        """Detect short greetings/status check-ins that should be handled conversationally."""
        trimmed = text_lower.strip()
        if trimmed in {'hi', 'hello', 'hey', 'halo', 'haloo', 'yo', 'sup', '你好', '哈囉', '嗨'}:
            return True
        if any(p in trimmed for p in ['minutes later', 'min later', 'i am back', 'im back', 'back now', '回來了', '返嚟', '返來']):
            return True
        # Very short non-emotional message should be treated as check-in.
        return len(trimmed.split()) <= 2 and not any(
            w in trimmed for w in ['sad', 'unhappy', 'anxious', 'stress', '壓力', '難過', '不開心']
        )

    def _is_noisy_phrase(self, phrase: str) -> bool:
        """Avoid echoing meaningless words in follow-up prompts."""
        p = phrase.strip().lower()
        if p in self.noise_tokens:
            return True
        if len(p) <= 3:
            return True
        if p.isdigit():
            return True
        return False
        
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
            # Preserve memory even in fallback mode for continuity.
            self.conversation_history.append({"role": "user", "content": user_message})
            reply = self.get_fallback_response(user_message)
            self.conversation_history.append({"role": "assistant", "content": reply})
            return reply
    
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

