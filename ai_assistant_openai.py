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
        # Provider selection: OpenRouter first, then native OpenAI.
        self.provider = "openrouter" if os.getenv("OPENROUTER_API_KEY") else "openai"
        self.api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
        self.base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1") if self.provider == "openrouter" else None
        self.client = None
        self.conversation_history = []
        self.model = os.getenv("OPENAI_MODEL") or ("openai/gpt-4o-mini" if self.provider == "openrouter" else "gpt-4o-mini")
        self.last_followup = None
        self.last_style = None
        self.init_error = None
        
        # Initialize OpenAI if API key is available
        if OPENAI_AVAILABLE and self.api_key:
            try:
                if self.provider == "openrouter":
                    self.client = OpenAI(
                        api_key=self.api_key,
                        base_url=self.base_url,
                        default_headers={
                            "HTTP-Referer": os.getenv("APP_URL", "https://emotional-support-ai.onrender.com"),
                            "X-Title": os.getenv("APP_NAME", "Students SoulCare")
                        },
                    )
                    print("✅ OpenRouter connected via OpenAI-compatible API")
                else:
                    self.client = OpenAI(api_key=self.api_key)
                    print("✅ OpenAI API connected - Using ChatGPT intelligence")
                self.mode = "openai"
            except Exception as e:
                print(f"⚠️  {self.provider} connection failed: {e}")
                self.mode = "fallback"
                self.init_error = str(e)
        else:
            self.mode = "fallback"
            if not OPENAI_AVAILABLE:
                print("⚠️  Install openai: pip install openai")
                self.init_error = "openai package not available"
            if not self.api_key:
                print("⚠️  Set OPENROUTER_API_KEY or OPENAI_API_KEY environment variable")
                self.init_error = "OPENROUTER_API_KEY / OPENAI_API_KEY is missing"
        
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
            has_chinese = analysis['language'] in ['chinese', 'mixed']
            internal = self._build_internal_assessment(user_message, analysis)
            songs = self._suggest_songs(has_chinese, analysis['primary_emotion'], analysis['primary_topic'])
            
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
- Your goal is to help the student feel understood and willing to continue chatting.

Internal reasoning requirement (do this silently, never expose as headings):
1) infer what the student is facing,
2) infer how they feel,
3) estimate safety risk (low/moderate/high/critical).

Then reply naturally like a real supportive person, without showing your internal analysis process.
End with one open question to continue the conversation.
If student is stressed/sad, you may suggest 1-2 calming songs naturally (no links)."""
            
            # Pass explicit student context so replies are specific and non-generic.
            context_prompt = (
                "Student context extracted from latest message:\n"
                f"- language: {analysis['language']}\n"
                f"- primary_emotion: {analysis['primary_emotion']}\n"
                f"- topics: {', '.join(analysis['topics']) if analysis['topics'] else 'general'}\n"
                f"- urgency: {analysis['urgency']}\n"
                f"- key_phrases: {', '.join(analysis['key_phrases']) if analysis['key_phrases'] else 'none'}\n"
                f"- situation_summary: {internal['situation_summary']}\n"
                f"- feeling_summary: {internal['feeling_summary']}\n"
                f"- suicide_risk: {internal['suicide_risk']}\n"
                f"- risk_reasons: {', '.join(internal['risk_reasons']) if internal['risk_reasons'] else 'none'}\n"
                f"- optional_song_ideas: {', '.join(songs) if songs else 'none'}\n"
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
            raise RuntimeError(f"OpenAI API error: {e}")

    def get_fallback_response(self, user_message: str) -> str:
        """Fallback response: hidden analysis, natural empathetic output."""
        analysis = self._analyze_student_message(user_message)
        has_chinese = analysis['language'] in ['chinese', 'mixed']
        internal = self._build_internal_assessment(user_message, analysis)

        topic = analysis['primary_topic']
        if topic == 'general':
            topic = self._topic_from_recent_history() or 'general'

        key_phrase = analysis['key_phrases'][0] if analysis['key_phrases'] else None
        key_hint = ""
        if key_phrase and not self._is_noisy_phrase(key_phrase):
            key_hint = f"「{key_phrase}」" if has_chinese else f'"{key_phrase}"'

        songs = self._suggest_songs(has_chinese, analysis['primary_emotion'], topic)
        followup = self._next_followup(has_chinese=has_chinese, topic=topic, key_phrase=key_phrase)

        if has_chinese:
            insight = internal['situation_summary']
            empathy = internal['feeling_summary']
            support_map = {
                'academic': "如果你願意，我們先把今天最急的一件事拆成兩步，先完成第一步就好。",
                'family': "你可以先寫下一句你最想被理解的話，之後再決定怎樣說出口。",
                'social': "先保護自己，暫時遠離會讓你受傷的場景，再找一個可信任的人做支援。",
                'emotion': "先做一分鐘慢呼吸，讓身體降下來，再一起處理你最卡的地方。",
                'general': "我們先從最近最困擾你的一件事開始，慢慢拆開就會清楚很多。",
            }
            support_text = support_map.get(topic, support_map['general'])
            song_line = ""
            if songs:
                song_line = f" 如果想先穩定心情，你可以聽聽：{songs[0]}、{songs[1]}。"
            return f"我聽到你在面對{insight}。{empathy} {support_text}{song_line} {followup}"

        support_map = {
            'academic': "If you want, let us split your most urgent task into two tiny steps and finish step one first.",
            'family': "You could write one sentence you wish they understood before deciding how to say it.",
            'social': "Protect your space first, then reach out to one trusted person for support.",
            'emotion': "Start with one minute of slow breathing to settle your body, then we can unpack the hardest part.",
            'general': "Let us start with one specific moment that felt hardest and break it down together.",
        }
        support_text = support_map.get(topic, support_map['general'])
        song_line = ""
        if songs:
            song_line = f" If it helps, try {songs[0]} or {songs[1]} to calm your mind first."
        return f"From what you shared, you seem to be dealing with {internal['situation_summary']}. {internal['feeling_summary']} {support_text}{song_line} {followup}"

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
        normalized = re.sub(r'[^\w\u4e00-\u9fff\s]', ' ', text)
        raw_phrases = re.findall(r'\b[a-zA-Z]{4,}\b|[\u4e00-\u9fff]{2,8}', normalized)
        key_phrases = []
        for p in raw_phrases:
            p_clean = p.strip().lower()
            if p_clean in self.noise_tokens:
                continue
            if len(p_clean) <= 3:
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

    def _build_internal_assessment(self, user_message: str, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Internal-only assessment used for safer, more personalized replies."""
        text_lower = user_message.lower()

        topic_map = {
            'academic': 'academic pressure and performance anxiety',
            'family': 'family conflict or pressure at home',
            'social': 'social hurt, exclusion, or bullying stress',
            'emotion': 'ongoing emotional overload',
            'general': 'a difficult personal situation that feels heavy',
        }
        situation_summary = topic_map.get(analysis.get('primary_topic', 'general'), topic_map['general'])

        emotion_map = {
            'anxiety': 'It sounds like they are tense, worried, and mentally exhausted.',
            'sadness': 'It sounds like they are feeling low, hurt, and emotionally drained.',
            'hopeless': 'It sounds like they may feel trapped and losing hope.',
            'despair': 'It sounds like they may be in severe emotional pain and possible danger.',
            'mixed': 'It sounds like they are carrying mixed emotions and need emotional safety first.',
        }
        feeling_summary = emotion_map.get(analysis.get('primary_emotion', 'mixed'), emotion_map['mixed'])

        risk_reasons = []
        suicide_risk = 'low'
        if any(w in text_lower for w in ['suicide', 'kill myself', 'want to die', 'end my life', '自殺', '自杀', '想死']):
            suicide_risk = 'critical'
            risk_reasons.append('explicit self-harm/suicide language present')
        elif any(w in text_lower for w in ['hopeless', 'worthless', "can't go on", '絕望', '绝望', '無望', '无望']):
            suicide_risk = 'high'
            risk_reasons.append('strong hopelessness indicators')
        elif any(w in text_lower for w in ['panic', 'anxious', 'anxiety', 'nervous', '焦慮', '焦虑', '壓力', '压力']):
            suicide_risk = 'moderate'
            risk_reasons.append('high distress/anxiety indicators')

        if analysis.get('urgency') == 'critical' and suicide_risk != 'critical':
            suicide_risk = 'high'
            risk_reasons.append('model urgency detected as critical')

        return {
            'situation_summary': situation_summary,
            'feeling_summary': feeling_summary,
            'suicide_risk': suicide_risk,
            'risk_reasons': risk_reasons,
        }

    def _pick_response_style(self, has_chinese: bool) -> Dict[str, str]:
        """Rotate section labels to keep responses less repetitive."""
        zh_styles = [
            {'analysis': '1) 我聽到的重點', 'empathy': '2) 我理解你的感受', 'support': '3) 我們可以這樣做'},
            {'analysis': '1) 先整理你的情況', 'empathy': '2) 你這樣感受很合理', 'support': '3) 下一步支持建議'},
            {'analysis': '1) 你的話在說什麼', 'empathy': '2) 我想先抱住你的情緒', 'support': '3) 實際可做的小步驟'},
        ]
        en_styles = [
            {'analysis': '1) What I Heard In Your Words', 'empathy': '2) Why Your Feelings Make Sense', 'support': '3) Support Plan You Can Try'},
            {'analysis': '1) Quick Read Of Your Situation', 'empathy': '2) I Want You To Feel Understood', 'support': '3) Practical Support Steps'},
            {'analysis': '1) What Stands Out To Me', 'empathy': '2) You Are Not Overreacting', 'support': '3) One-Step-At-A-Time Support'},
        ]

        pool = zh_styles if has_chinese else en_styles
        options = [s for s in pool if s != self.last_style]
        selected = choice(options if options else pool)
        self.last_style = selected
        return selected

    def _suggest_songs(self, has_chinese: bool, emotion: str, topic: str) -> list:
        """Return optional calming/encouraging songs based on mood."""
        if topic not in ['academic', 'emotion'] and emotion not in ['anxiety', 'sadness', 'hopeless']:
            return []

        if has_chinese:
            pools = [
                ['G.E.M. 鄧紫棋 - 光年之外', '陳奕迅 - 陀飛輪'],
                ['岑寧兒 - 追光者', '盧冠廷 - 一生所愛'],
                ['Serrini - 樹木真美', '林家謙 - 一人之境'],
            ]
            return choice(pools)

        pools = [
            ['Coldplay - Fix You', 'AURORA - Runaway'],
            ['Billie Eilish - everything i wanted', 'Lewis Capaldi - Someone You Loved'],
            ['Ed Sheeran - Photograph', 'OneRepublic - I Lived'],
        ]
        return choice(pools)

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
        
        # Use OpenAI only for normal chat responses
        if self.mode == "openai" and self.client:
            return self.analyze_with_openai(user_message)
        else:
            raise RuntimeError("LLM provider is not available. Please check OPENROUTER_API_KEY or OPENAI_API_KEY and deployment configuration.")
    
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


def get_openai_status() -> Dict[str, Any]:
    """Return runtime status for OpenAI integration (no secrets)."""
    return {
        "package_available": OPENAI_AVAILABLE,
        "key_set": bool(_openai_assistant.api_key),
        "provider": _openai_assistant.provider,
        "base_url": _openai_assistant.base_url,
        "model": _openai_assistant.model,
        "mode": _openai_assistant.mode,
        "client_initialized": _openai_assistant.client is not None,
        "ready": (_openai_assistant.mode == "openai" and _openai_assistant.client is not None),
        "init_error": _openai_assistant.init_error,
    }

