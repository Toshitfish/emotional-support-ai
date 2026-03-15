# 🌟 START HERE - Emotional Support Website with Google Gemini

Welcome! Your emotional support website is now powered by **Google Gemini AI** and ready to use.

---

## ⚡ 3-Step Quick Start

### Step 1: Get Your Free API Key (30 seconds)
Go to: **https://aistudio.google.com/app/apikey**
- Sign in with your Google account (Gmail, etc.)
- Click "Create API Key"
- Copy your key

### Step 2: Configure Your App
```bash
python setup_gemini.py
```
This interactive wizard will:
- Ask for your API key
- Verify it works
- Save it safely to `.env`

### Step 3: Launch the App
```bash
streamlit run app.py
```
Your app will open at: `http://localhost:8501`

---

## 📚 Full Documentation

| Document | Purpose |
|----------|---------|
| [GET_GOOGLE_API_KEY.md](GET_GOOGLE_API_KEY.md) | How to get your free Gemini API key |
| [GEMINI_READY.md](GEMINI_READY.md) | What's new with Gemini integration |
| [README.md](README.md) | Complete project documentation |
| [HONG_KONG_SETUP.md](HONG_KONG_SETUP.md) | Hong Kong-specific setup guide |

---

## 🎯 What This Website Does

✅ **Emotional Support Chat**
- AI listens and responds with empathy
- Helps students process emotions
- Available 24/7
- Works in English and Chinese (繁體中文)

✅ **Crisis Detection**
- Automatically detects crisis keywords
- Provides emergency hotlines
- Hong Kong numbers included
- Always prioritizes safety

✅ **Context-Aware**
- Remembers conversation history
- Provides personalized support
- Learns student preferences
- Improves over time

---

## 🔄 Why Google Gemini?

**Before:** OpenAI and Claude were blocked in Hong Kong ❌

**Now:** Using Google Gemini instead! ✅
- **Works everywhere** in Hong Kong
- **100% FREE** (generous free tier)
- **Fast & Smart** responses
- **No regional restrictions**

---

## 🛠️ Troubleshooting

### "I can't access OpenAI website"
Don't worry! You'll use Google Gemini instead. It's:
- Free
- Works in Hong Kong
- Even better for emotional support
- Recommended for your region

### "Python not found"
Make sure you're using the correct terminal. From the project folder:
```bash
pip install -r requirements.txt
python setup_gemini.py
```

### "API key invalid"
1. Go to https://aistudio.google.com/app/apikey
2. Create a NEW API key
3. Copy it carefully (no extra spaces)
4. Run `python setup_gemini.py` again

### "Still having issues?"
Check [GET_GOOGLE_API_KEY.md](GET_GOOGLE_API_KEY.md) for detailed help.

---

## 📋 File Structure

```
emotional_support_website/
├── app.py                         ← Main Streamlit app
├── ai_assistant_gemini.py        ← Gemini AI integration (NEW)
├── setup_gemini.py               ← Setup wizard (NEW)
├── requirements.txt              ← Python dependencies
├── .env.example                  ← Config template
├── .env                          ← Your settings (create this)
├── START_HERE.md                 ← This file
├── GEMINI_READY.md              ← What's new
├── GET_GOOGLE_API_KEY.md        ← How to get API key
├── HONG_KONG_SETUP.md           ← Hong Kong specific steps
├── README.md                      ← Full documentation
└── .streamlit/config.toml        ← Web UI settings
```

---

## 🆘 Emergency Resources

If you or someone you know is in crisis:

**Hong Kong:**
- 📞 Samaritans: **2389 2222** (24/7)
- 💬 WhatsApp: **+852 5162 0000**
- 🌐 Website: https://www.samaritans.org.hk/

**Other Regions:**
- 🇺🇸 USA: National Suicide Prevention Lifeline 988
- 🇬🇧 UK: Samaritans 116 123
- 🌍 International: https://findahelpline.com

---

## 📱 How to Use

1. **Start chatting** with your emotions/concerns
2. **AI responds** with understanding and support
3. **Share what's on your mind** - the more you share, the better the support
4. **Get resources** if you're in crisis
5. **Feel heard** - this is a safe space

### Example Conversations:

**Student:** "I feel so stressed about exams..."
**AI:** [Responds with empathy, offers coping strategies, asks clarifying questions]

**Student:** "I don't want to live anymore"
**AI:** [Detects crisis, provides Hong Kong hotlines, encourages help-seeking]

---

## ✅ Verification Checklist

Before you start, make sure you have:

- [ ] Python installed (check with `python --version`)
- [ ] Downloaded and extracted the project
- [ ] Created `.env` file (or run `setup_gemini.py`)
- [ ] API key from https://aistudio.google.com/app/apikey
- [ ] Installed dependencies with `pip install -r requirements.txt`
- [ ] Successfully run `python setup_gemini.py`

---

## 🚀 Go Live!

Ready to help students with emotional support?

```bash
# Run this ONE command:
streamlit run app.py
```

Your emotional support website is now live! 🌟

---

## 💡 Pro Tips

**Tip 1:** Share the app link with students who need support
```
Your friends can access it at your local address
```

**Tip 2:** The app remembers conversation history in the same session
- Each session starts fresh (privacy by design)
- Users won't see previous conversations

**Tip 3:** Crisis detection works automatically
- You don't need to configure anything
- Just chat normally
- AI will detect if help is needed

**Tip 4:** Use both languages freely
- "I feel sad" ← works
- "我感到很傷心" ← also works
- Mix them: "I feel very sad about 考試" ← works

---

## 🎓 For Teachers/Counselors

If deploying in your school:

1. **Setup** (run once):
   ```bash
   python setup_gemini.py
   streamlit run app.py
   ```

2. **Access** (give students):
   - Local network: `http://[your-ip]:8501`
   - Or deploy to cloud (Streamlit Cloud, Heroku, etc.)

3. **Monitor** (optional):
   - Check conversation logs for crisis keywords
   - Generate reports for your administration
   - Integrate with existing systems

4. **Support**:
   - Train students on using the app
   - Have human support available
   - Use as complement to counseling, not replacement

---

## 📞 Need Help?

1. **Setup issues?** → See [GET_GOOGLE_API_KEY.md](GET_GOOGLE_API_KEY.md)
2. **Feature questions?** → Check [README.md](README.md)
3. **Hong Kong specific?** → Read [HONG_KONG_SETUP.md](HONG_KONG_SETUP.md)
4. **Technical problems?** → Run `python setup_gemini.py` again

---

## 🌟 You're All Set!

Your emotional support website with Google Gemini is ready.

Start with this command:
```bash
streamlit run app.py
```

Then open your browser and start supporting students! 💚

---

**Remember:** This tool helps provide emotional support, but it's not a replacement for professional mental health treatment. Always encourage users to seek help from qualified professionals when needed.

**In Hong Kong Crisis?** Call Samaritans: **2389 2222**

---

**Setup Date:** January 2025  
**AI Provider:** Google Gemini  
**Status:** Ready to Use  
**Version:** 1.0
