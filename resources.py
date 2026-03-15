# Crisis Resources Configuration
# 危機資源配置

CRISIS_RESOURCES = {
    "Hong Kong": {
        "name": "香港",
        "resources": [
            {
                "name": "撒瑪利亞防止撥款會",
                "phone": "2389 2222",
                "hours": "24小時 | 24/7",
                "website": "https://www.samaritans.org.hk",
                "email": "lifelinecentre@samaritans.org.hk",
                "whatsapp": "+852 5162 0000"
            },
            {
                "name": "撒瑪利亞防止撥款會 - 生命熱線",
                "phone": "2389 2222",
                "hours": "24小時 | 24/7",
                "email": "lifelinecentre@samaritans.org.hk"
            }
        ]
    },
    "Taiwan": {
        "name": "台灣",
        "resources": [
            {
                "name": "安心專線",
                "phone": "1925",
                "hours": "24小時 | 24/7",
                "app": "安心講 APP (可進行文字諮詢)"
            },
            {
                "name": "全國自殺防治中心",
                "phone": "1925",
                "hours": "24小時 | 24/7"
            }
        ]
    },
    "Mainland China": {
        "name": "中國大陸",
        "resources": [
            {
                "name": "全國心理援助熱線",
                "phone": "400-161-9995",
                "hours": "24小時 | 24/7"
            }
        ]
    },
    "Singapore": {
        "name": "新加坡",
        "resources": [
            {
                "name": "生命急救熱線",
                "phone": "1800 221 4444",
                "hours": "24小時 | 24/7",
                "website": "https://www.tsos.org.sg"
            }
        ]
    },
    "Malaysia": {
        "name": "馬來西亞",
        "resources": [
            {
                "name": "警察部隊失踪人口辦公室",
                "phone": "03-2149 0000",
                "hours": "24小時 | 24/7"
            }
        ]
    }
}

# Support tip translations
SUPPORT_TIPS = [
    {
        "zh": "在這裡你可以匿名分享你的感受",
        "en": "You can share your feelings anonymously here"
    },
    {
        "zh": "我們的AI助手會提供支持和建議",
        "en": "Our AI assistant will provide support and suggestions"
    },
    {
        "zh": "如果感到危險，請立即聯絡緊急服務",
        "en": "If you feel in danger, please contact emergency services immediately"
    },
    {
        "zh": "我們建議尋求專業心理健康幫助",
        "en": "We recommend seeking professional mental health support"
    }
]

# Keywords for different languages (for better detection)
CRISIS_KEYWORDS = {
    "Chinese": [
        "自殺", "自杀", "死", "死亡", "結束", "结束", "想死", "想不活",
        "沒有意義", "没有意义", "絕望", "绝望", "活著沒意義", "活着没意义",
        "傷害自己", "伤害自己", "割腕", "吞藥", "吞药", "尋死", "寻死",
        "害死自己", "不活了", "撞牆", "撞墙"
    ],
    "English": [
        "suicide", "kill myself", "self harm", "kill myself", "hopeless",
        "worthless", "don't want to live", "harm myself", "cut myself",
        "end my life", "no point", "pointless"
    ]
}

# Emergency numbers by category
EMERGENCY_NUMBERS = {
    "General Emergency": {
        "Hong Kong": "999",
        "Taiwan": "112",
        "Singapore": "999",
        "Malaysia": "999",
        "US": "911",
        "UK": "999"
    }
}
