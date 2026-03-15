"""
Enhanced AI Assistant with advanced features
This module provides more sophisticated emotional support
"""

import os
import random
import json
from datetime import datetime
from typing import Tuple, List

class EnhancedEmotionalSupportAssistant:
    """
    Enhanced AI assistant with sentiment tracking and user context awareness
    """
    
    def __init__(self):
        self.conversation_history = []
        self.user_sentiment_history = []
        self.crisis_keywords = {
            "suicidal": ["自殺", "自杀", "死", "suicide", "kill myself"],
            "self_harm": ["傷害自己", "伤害自己", "割腕", "self harm", "cut"],
            "hopelessness": ["絕望", "绝望", "hopeless", "worthless", "no point"],
            "extreme_stress": ["極度", "极度", "承受不了", "极端", "extreme"]
        }
        
        self.coping_strategies = {
            "stress": [
                "💆 嘗試深呼吸練習 - 吸氣4秒，屏息4秒，呼氣4秒",
                "🚶 去散步或做運動 - 身體活動可以释放內啡肽",
                "📝 寫日記 - 把感受寫下來可以幫助處理情緒",
                "🎵 聽喜歡的音樂 - 音樂有治癒的力量",
                "☕ 給自己一些獨處時間 - 自我照顧很重要"
            ],
            "sadness": [
                "🤝 與朋友或家人聊天 - 分享可以減輕負擔",
                "🎨 做自己喜歡的活動 - 投入有興趣的事物",
                "📖 看勵志書籍或視頻 - 汲取正能量",
                "🌍 參與社區活動 - 與他人連結",
                "💪 設定小目標 - 分步完成可增加成就感"
            ],
            "hopelessness": [
                "🎯 與專業諮詢師談話 - 他們有具體工具幫助",
                "💙 提醒自己此刻的困難是暫時的 - 一切都會改變",
                "📞 聯絡信任的人 - 分享可以改變觀點",
                "🧠 嘗試認知療法 - 質疑負面思維",
                "🌟 回想過往克服的困難 - 你已經很堅強了"
            ]
        }
        
        self.support_resources = {
            "professional": [
                "🏥 學校輔導員 - 大多數學校都有免費諮詢服務",
                "👨‍⚕️ 心理治療師 - 專業的心理健康治療",
                "📞 心理援助熱線 - 24小時可得的支持",
                "💻 在線諮詢平台 - 便利的遠端服務"
            ],
            "daily": [
                "🧘 冥想應用 (如 Calm, Headspace)",
                "📱 情緒追蹤應用",
                "🤗 支持社群/論壇",
                "📚 自助書籍和資源"
            ]
        }
    
    def get_sentiment_severity(self, text: str) -> Tuple[str, int]:
        """
        Analyze text and return sentiment with severity score (0-10)
        """
        crisis_level = 0
        detected_keywords = []
        text_lower = text.lower()
        
        for category, keywords in self.crisis_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    crisis_level += 3
                    detected_keywords.append(category)
        
        # Additional severity indicators
        if "一直" in text or "always" in text:
            crisis_level += 1
        if "無法" in text or "can't" in text:
            crisis_level += 1
        if "只能" in text or "死" in text:
            crisis_level += 2
        
        severity = min(crisis_level, 10)
        
        if severity >= 8:
            return "critical", severity
        elif severity >= 5:
            return "high", severity
        elif severity >= 2:
            return "moderate", severity
        else:
            return "mild", severity
    
    def provide_coping_strategies(self, emotion_type: str) -> str:
        """Provide practical coping strategies"""
        if emotion_type in self.coping_strategies:
            strategies = self.coping_strategies[emotion_type]
            return "💡 **一些可能有幫助的方法：**\n\n" + "\n".join(random.sample(strategies, min(3, len(strategies))))
        return ""
    
    def provide_resources(self) -> str:
        """Provide additional resources"""
        resources = "📚 **可用資源：**\n\n"
        
        resources += "**專業幫助 | Professional Help:**\n"
        for resource in self.support_resources["professional"][:2]:
            resources += f"- {resource}\n"
        
        resources += "\n**日常工具 | Daily Tools:**\n"
        for resource in self.support_resources["daily"][:2]:
            resources += f"- {resource}\n"
        
        return resources
    
    def log_interaction(self, user_input: str, severity: str, response: str):
        """Log interaction for analysis"""
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "user_input_length": len(user_input),
            "severity": severity,
            "response_provided": bool(response)
        }
        self.conversation_history.append(interaction)
    
    def get_enhanced_response(self, user_message: str) -> str:
        """Generate enhanced response with coping strategies and resources"""
        sentiment, severity = self.get_sentiment_severity(user_message)
        
        # Determine emotion type for strategies
        emotion_type = "stress"  # default
        if any(word in user_message.lower() for word in ["難過", "sad", "hurt"]):
            emotion_type = "sadness"
        elif any(word in user_message.lower() for word in ["絕望", "hopeless"]):
            emotion_type = "hopelessness"
        
        base_response = f"我聽到你的聲音。你描述的情況聽起來確實很具挑戰性。\n\n"
        
        # Add severity-appropriate support
        if severity >= 8:
            base_response = "⚠️ **我很關心你的安全。** 根據你分享的內容，我想確保你得到專業幫助。"
        elif severity >= 5:
            base_response = "💙 我明白這對你來說很困難。你不必獨自承受這些。"
        
        # Add coping strategies
        coping = self.provide_coping_strategies(emotion_type)
        
        # Add resources
        resources = self.provide_resources()
        
        final_response = base_response + "\n\n" + coping + "\n\n" + resources
        
        # Log interaction
        self.log_interaction(user_message, sentiment, final_response)
        
        return final_response
