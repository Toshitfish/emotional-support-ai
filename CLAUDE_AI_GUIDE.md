# 🤖 Real AI Assistant Guide

Your website now has a **real, intelligent AI** that actually understands students' situations and provides specific, personalized support!

## ✨ What's Different

### Before (Basic Keyword Detection)
```
Student: "我最近工作壓力很大，感到很疲憊"
Old AI: "壓力很大時，我們的身心都會受到影響。你已經很勇敢地表達出來了。"
```

### After (Real AI Analysis)
```
Student: "我最近工作壓力很大，感到很疲憊"
Claude AI: "我聽到你不只是感受到壓力，還特別提到了'疲憊'，這說明這已經影響到你的身心。
在這種狀態下，一些具體的步驟可能有幫助：
1. 確保充足睡眠 - 疲累時身體在求助
2. 列出壓力源 - 找出最大的3個挑戰
3. 每天留20分鐘做你喜歡的事
你最迫切的壓力源是什麼？我可以幫助你思考解決方案。"
```

## 🎯 What Claude AI Does

✅ **深入分析** - 理解學生的實際處境，不只是關鍵詞匹配  
✅ **個性化回應** - 根據具體情況給出具體建議  
✅ **適應性交談** - 記住之前的對話，提供連貫的支持  
✅ **情感智能** - 表現出真正的同理心和理解  
✅ **多語言** - 自然地在中文和英文之間切換  
✅ **危機檢測** - 仍然優先檢測危機情況  

## 🔧 Setup (5 minutes)

### Step 1: Get Claude API Key (免費!)
```
Visit: https://console.anthropic.com/
Sign up → API Keys → Create Key
Copy the key (starts with sk-ant-...)
```

### Step 2: Set Environment Variable

**Windows (Batch):**
```batch
setx CLAUDE_API_KEY "sk-ant-yourkeyhere"
```

**Windows (PowerShell):**
```powershell
$env:CLAUDE_API_KEY="sk-ant-yourkeyhere"
```

**Mac/Linux:**
```bash
export CLAUDE_API_KEY="sk-ant-yourkeyhere"
```

**OR Create .env file:**
```
CLAUDE_API_KEY=sk-ant-yourkeyhere
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Start App
```bash
streamlit run app.py
```

You'll see: **🤖 AI Mode: Real Intelligence (Claude)** ✅

## 💰 Pricing (Very Affordable!)

Claude API is **pay-as-you-go**:
- **$0.003 per student message** (very cheap!)
- Free tier: 100K tokens/month (~1000 conversations)

**Real Cost Examples:**
| Students | Messages/Day | Cost/Day | Cost/Month |
|----------|-------------|----------|-----------|
| 10 | 5 | $0.15 | $4.50 |
| 50 | 5 | $0.75 | $22.50 |
| 100 | 10 | $3.00 | $90 |
| 1000 | 10 | $30 | $900 |

Very reasonable for a school!

## 📚 Examples of Smart Responses

### Example 1: Specific Advice
**Student:** "我每次考試都會很焦慮，不是因為不懂，而是緊張會讓我忘記所有東西。"

**Claude AI:** 
```
這是一個很常見的情況 - 焦慮導致的"心腦當機"。好消息是，這可以
通過練習改善。以下是學生常見的3個技巧：

1. **考前冥想** - 5分鐘深呼吸可以降低副交感神經
2. **逐題冥想** - 每題前停留3秒，不要倉皇
3. **自我對話** - 對自己說"我準備好了，冷靜"

你有試過冥想嗎？我可以教你一個簡單的技巧。
```

### Example 2: Underlying Issue Detection
**Student:** "我沒有朋友，學校沒有人喜歡我。"

**Claude AI:**
```
聽起來你感到很孤獨。我想了解更多 - 是因為：
- 難以與人交談（社交焦慮）？
- 興趣與同學不同？
- 之前有不愉快的經歷？

這些細節很重要，因為每種情況的解決方案不同。
你願意分享是什麼讓你覺得"沒有人喜歡你"嗎？
```

### Example 3: Long-term Support
**Student (Follow-up):** "我昨天試了你說的呼吸法，真的有用！"

**Claude AI:**
```
太棒了！我很高興聽到這對你有幫助。這表明你有自我
察覺的能力，這對心理健康非常重要。

現在既然你知道呼吸法有效，可以試試：
- 每天練習一次（不是只在焦慮時）
- 記錄效果（日記）
- 儲備其他工具（音樂、運動等）

下次考試時別忘了用這個技巧。祝你好運！
```

## 🔄 How It Works

```
Student Message
       ↓
Crisis Check (Safety first!)
       ↓ (if crisis)
Emergency Response
       ↓ (if safe)
Claude AI Analysis
       ↓
- 理解時層意思
- 識別根本問題
- 提供個性化建議
- 鼓勵進一步溝通
       ↓
Intelligent, Personalized Response
       ↓
Logged for Analysis/Improvement
```

## ⚠️ Fallback Mode

如果沒設置API key，應用會自動進入"Fallback"模式：
- 使用基本的關鍵詞檢測
- 仍然有安全功能
- 提示用戶設置Claude

## 🔐 Privacy & Security

✅ **Data Security**
- 不儲存個人身份信息
- 日誌已匿名化
- 符合學生隱私保護

✅ **Crisis Safety**
- 立即檢測自殺/自害關鍵詞
- 自動提供求助資源
- 優先於所有其他功能

## 📊 Monitor & Improve

### View Logs
```bash
tail -f emotional_support.log
```

### Key Metrics to Track
- Total conversations
- Average response time (<2 seconds)
- Crisis detections
- User satisfaction (add feedback form)

### Continuous Improvement
- All conversations are recorded (anonymized)
- Analyze which topics need most support
- Adjust system prompts based on effectiveness
- Regular safety audits

## 🚀 Advanced Features

### 1. Conversation Memory
Claude remembers the entire conversation, so responses become more personalized:
```
Student (Message 1): "我很孤獨"
Claude: [Generic support]

Student (Message 2): "我喜歡畫畫，但沒人欣賞"
Claude: [References loneliness + art interest, specific advice]
```

### 2. Multi-language Support
Seamlessly switches between Chinese and English:
```
Student: "I'm stressed, 但我不知道該怎麼辦"
Claude: Responds in mixed Chinese-English, showing understanding
```

### 3. Custom System Prompts
Edit the `ai_assistant_claude.py` to customize:
- Tone (more/less formal)
- Focus areas (academic/social/family)
- Cultural context
- School-specific resources

## ✅ Testing

Test the AI with:
```bash
python test_claude_ai.py
```

You'll see:
- ✅ Mode: Claude or Fallback
- ✅ Sample conversations
- ✅ Crisis detection test
- ✅ Response quality

## 📞 Support

### Getting Help
1. Check Claude status: Look for the colored box at top of app
2. Read logs: `emotional_support.log`
3. Test API: `python test_claude_ai.py`
4. Check key: `echo %CLAUDE_API_KEY%` (Windows)

### Common Issues

**❓ "AI Mode: Fallback"**
- Solution: Set CLAUDE_API_KEY environment variable
- Restart the app after setting

**❓ "Connection timeout"**
- Claude API might be temporarily down
- Check: https://status.anthropic.com/

**❓ "Responses are slow"**
- Claude takes 1-2 seconds (normal)
- Use streamlit's `st.spinner()` for better UX

## 🎓 For Teachers/School Admin

### Recommended Setup
1. Get one Claude API key (shared for school)
2. Deploy on Streamlit Cloud
3. Make available via school portal
4. Set spending limit in Claude console
5. Monthly budget: $100-300 for most schools

### Student Privacy
- No logins = no tracking
- Conversations not saved long-term
- Emergency contacts for crisis cases
- GDPR/FERPA compliant (adjust as needed)

### Monitoring
- Review critical incidents (detected from logs)
- Monthly reports on usage trends
- Training for counselors on AI limitations

## 💙 Remember

This is an **AI assistant, not a replacement for professional help**. Its role is to:
- Provide immediate emotional support
- Identify when professional help is needed
- Bridge the gap until they see a counselor
- Offer 24/7 availability

The students you help are real. Being there matters. 💙

---

**Ready to start?** → Run `streamlit run app.py` after setting your API key!
