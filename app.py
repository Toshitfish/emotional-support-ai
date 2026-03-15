import streamlit as st
import os
from datetime import datetime

# Try to import based on available API keys
if os.getenv("GOOGLE_API_KEY"):
    from ai_assistant_gemini import RealEmotionalAIAssistant
    ai_provider = "Gemini"
elif os.getenv("OPENAI_API_KEY"):
    from ai_assistant_openai import RealEmotionalAIAssistant
    ai_provider = "OpenAI"
elif os.getenv("CLAUDE_API_KEY"):
    from ai_assistant_claude import RealEmotionalAIAssistant
    ai_provider = "Claude"
else:
    from ai_assistant_gemini import RealEmotionalAIAssistant
    ai_provider = "Gemini"

# Page configuration
st.set_page_config(
    page_title="情緒支持 - Emotional Support",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 20px;
    }
    .stChatMessage {
        font-size: 16px;
    }
    .support-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 30px;
    }
    .crisis-alert {
        background-color: #ff6b6b;
        color: white;
        padding: 15px;
        border-radius: 8px;
        margin: 20px 0;
        font-weight: bold;
    }
    .resources-box {
        background-color: #e7f3ff;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #1f77b4;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "assistant" not in st.session_state:
    st.session_state.assistant = RealEmotionalAIAssistant()

# Header
st.markdown("""
    <div class="support-header">
        <h1>💙 情緒支持平臺 - Emotional Support Hub</h1>
        <p>我們在這裡傾聽和支持你 | We're here to listen and support you</p>
    </div>
    """, unsafe_allow_html=True)

# Show AI mode status
assistant = st.session_state.assistant
if assistant.mode == "gemini":
    st.success(f"🤖 **AI Mode: Google Gemini** - Advanced emotional intelligence (Works perfectly in Hong Kong!)", icon="✅")
elif assistant.mode == "openai":
    st.success(f"🤖 **AI Mode: ChatGPT (OpenAI)** - Advanced emotional intelligence powered by GPT-4o", icon="✅")
elif assistant.mode == "claude":
    st.success("🤖 **AI Mode: Real Intelligence (Claude)** - Your responses are powered by advanced AI analysis", icon="✅")
else:
    st.warning("⚠️ **AI Mode: Fallback** - Set GOOGLE_API_KEY to enable intelligent responses. See setup guide.", icon="ℹ️")

# Sidebar - Crisis Resources
with st.sidebar:
    st.markdown("## 🆘 緊急求助 | Crisis Resources")
    
    st.markdown("""
    **如果你有自殺傾向，請立即聯絡：**
    """)
    
    st.markdown("""
    <div class="resources-box">
    <strong>🇭🇰 香港撒瑪利亞防止撥款會</strong><br>
    24小時熱線: 2389 2222<br>
    <a href="https://www.samaritans.org.hk" target="_blank">www.samaritans.org.hk</a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="resources-box">
    <strong>🇭🇰 撒瑪利亞防止撥款會 - 生命熱線</strong><br>
    24小時: 2389 2222<br>
    文字求助: 2389 2222
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="resources-box">
    <strong>🇭🇰 撒瑪利亞防止撥款會</strong><br>
    郵件: lifelinecentre@samaritans.org.hk<br>
    Whatsapp: +852 5162 0000
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="resources-box">
    <strong>🇹🇼 台灣安心專線</strong><br>
    24小時: 1925<br>
    安心講 APP
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="resources-box">
    <strong>🇨🇳 全國心理援助熱線</strong><br>
    24小時: 400-161-9995
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("### 📋 使用提示 | Tips")
    st.markdown("""
    - 在這裡你可以匿名分享你的感受
    - 我們的AI助手會提供支持和建議
    - 如果感到危險，請立即聯絡緊急服務
    - 如有需要，我們建議尋求專業心理健康幫助
    """)

# Main chat interface
st.markdown("### 💬 和我們聊天 | Chat with us")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input(
    placeholder="分享你的感受... / Share your feelings...",
    key="user_input"
)

if user_input:
    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get assistant response
    with st.spinner("💭 正在思考... Thinking..."):
        response = st.session_state.assistant.get_response(user_input)
    
    # Add assistant message to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
    
    # Display assistant message
    with st.chat_message("assistant"):
        st.markdown(response)

# Bottom section with important information
st.divider()
st.markdown("""
### ⚠️ 重要提示 | Important Notice

**此平台的AI助手旨在提供情感支持，不能替代專業心理健康治療。**

**This AI assistant is designed to provide emotional support and cannot replace professional mental health treatment.**

- 如果你有即時危險的想法，請立即聯絡當地緊急服務或撥打上面提供的求助電話
- If you are in immediate danger, please contact local emergency services or call the crisis hotlines above
- 我們建議定期與合格的心理健康專業人士進行諮詢
- We recommend regular consultation with qualified mental health professionals
""")
