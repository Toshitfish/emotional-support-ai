import os
import random
from datetime import datetime

class EmotionalSupportAssistant:
    """
    AI assistant for providing emotional support and crisis intervention
    """
    
    def __init__(self):
        self.crisis_keywords = [
            "自殺", "自杀", "死", "死亡", "結束", "结束", "想死", "想不活",
            "沒有意義", "没有意义", "絕望", "绝望", "活著沒意義", "活着没意义",
            "傷害自己", "伤害自己", "割腕", "吞藥", "吞药", "尋死", "寻死",
            "害死自己", "suicide", "kill myself", "self harm"
        ]
        
        self.supportive_responses = {
            "greeting": [
                "你好！歡迎來到情緒支持平臺。我很高興見到你。你今天怎麼樣？",
                "Hi there! 👋 I'm here to listen and support you. How are you feeling today?",
                "你好！感謝你信任我們。告訴我現在的感受吧。"
            ],
            "sadness": [
                "我很遺憾聽到你感到難過。那一定很困難。你想談談是什麼讓你感到這樣嗎？",
                "It sounds like you're going through a tough time. That's completely valid. I'm here to listen.",
                "感到悲傷是正常的。你現在願意分享一下發生了什麼嗎？"
            ],
            "stress": [
                "壓力很大時，我們的身心都會受到影響。你已經很勇敢地表達出來了。",
                "Stress can be overwhelming, but you're not alone. What's been making you feel this way?",
                "學習壓力大是很多學生都經歷過的。你是否嘗試過一些紓壓方法？"
            ],
            "hopelessness": [
                "我明白你現在可能感到絕望，但這些感受是會改變的。你願意與我分享更多嗎？",
                "When things feel hopeless, it can be really hard to see a way forward. But reaching out shows strength.",
                "有時候生活會讓我們感到希望渺茫，但請記住，這只是暫時的感受。"
            ],
            "not_alone": [
                "請記住，你並不孤獨。有很多人關心你，包括我們。",
                "You're not alone in feeling this way. Many people experience similar emotions.",
                "你很勇敢能夠表達你的感受。有支持網絡可以幫助你。"
            ],
            "encourage_help": [
                "我建議你考慮與信任的人談論這個問題——朋友、家人或專業心理健康人士。他們可以提供真正幫助。",
                "Have you considered talking to a school counselor or mental health professional? They have tools and training to help.",
                "尋求專業幫助是一個勇敢的決定。學校的輔導員很樂意幫助你。"
            ]
        }
    
    def detect_crisis(self, text):
        """Detect if user mentions crisis/suicide indicators"""
        text_lower = text.lower()
        for keyword in self.crisis_keywords:
            if keyword in text_lower:
                return True
        return False
    
    def get_crisis_response(self):
        """Generate immediate crisis intervention response"""
        return """
        💙 **我很關心你的安全**  
        **I'm concerned about your safety**

        ---
        
        **如果你正在經歷危機，請立即尋求幫助：**
        
        🆘 **香港** - 撒瑪利亞防止撥款會: **2389 2222** (24小時)
        📱 WhatsApp: +852 5162 0000
        
        🆘 **台灣** - 安心專線: **1925** (24小時)
        
        🆘 **其他地區** - 請聯絡當地應急服務
        
        ---
        
        **Please reach out to a crisis service immediately:**
        
        - **Hong Kong**: Samaritans 2389 2222 (24/7)
        - **Taiwan**: 1925 (24/7)
        - **Other regions**: Contact local emergency services
        
        ---
        
        你的生命很重要。❤️ 請不要獨自承受這些。
        **Your life matters. Please don't face this alone.**
        """
    
    def analyze_sentiment(self, text):
        """Simple sentiment analysis"""
        sadness_words = ["難過", "难过", "悲傷", "悲伤", "傷心", "伤心", "痛苦", "sad", "hurt", "pain"]
        stress_words = ["壓力", "压力", "焦慮", "焦虑", "緊張", "紧张", "stress", "anxiety", "worried"]
        hopelessness_words = ["絕望", "绝望", "沒希望", "没希望", "hopeless", "worthless", "失敗", "失败"]
        
        text_lower = text.lower()
        
        if any(word in text_lower for word in hopelessness_words):
            return "hopelessness"
        elif any(word in text_lower for word in sadness_words):
            return "sadness"
        elif any(word in text_lower for word in stress_words):
            return "stress"
        return "neutral"
    
    def get_base_response(self, sentiment):
        """Get response based on detected sentiment"""
        if sentiment == "sadness":
            responses = self.supportive_responses["sadness"]
        elif sentiment == "stress":
            responses = self.supportive_responses["stress"]
        elif sentiment == "hopelessness":
            responses = self.supportive_responses["hopelessness"]
        else:
            responses = self.supportive_responses["greeting"]
        
        return random.choice(responses)
    
    def get_response(self, user_message):
        """Main method to get response from assistant"""
        
        # Check for crisis indicators first
        if self.detect_crisis(user_message):
            return self.get_crisis_response()
        
        # Analyze sentiment
        sentiment = self.analyze_sentiment(user_message)
        
        # Get base response
        base_response = self.get_base_response(sentiment)
        
        # Add supportive follow-up
        if sentiment in ["sadness", "hopelessness", "stress"]:
            follow_up = random.choice([
                self.supportive_responses["not_alone"],
                self.supportive_responses["encourage_help"]
            ])
            return base_response + "\n\n" + follow_up[0]
        
        return base_response + "\n\n" + random.choice(self.supportive_responses["not_alone"])
    
    def log_conversation(self, user_msg, assistant_response, filename="conversations.log"):
        """Log conversations for analysis (anonymized)"""
        try:
            with open(filename, "a", encoding="utf-8") as f:
                f.write(f"\n[{datetime.now()}]\n")
                f.write(f"User: {user_msg}\n")
                f.write(f"Assistant: {assistant_response}\n")
                f.write("-" * 50 + "\n")
        except Exception as e:
            print(f"Error logging conversation: {e}")
