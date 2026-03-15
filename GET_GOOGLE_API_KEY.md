# 🤖 Get Your Free Google Gemini API Key

## ⚡ Quick Start (2 minutes)

### 1️⃣ Go to Google AI Studio
👉 **https://aistudio.google.com/app/apikey**

### 2️⃣ Click "Create API Key"
- If you're not signed in, sign in with your Google account (Gmail, etc.)
- Click the blue "Create API Key" button

### 3️⃣ Copy Your Key
- Select your project (or create a new one)
- Copy the generated key

### 4️⃣ Save It
**Option A (Automatic - Recommended):**
```bash
python setup_gemini.py
```
This will guide you through saving the key automatically.

**Option B (Manual):**
1. Open `.env` file in the project folder
2. Add: `GOOGLE_API_KEY=your-key-here`
3. Replace `your-key-here` with your actual key
4. Save the file

---

## ❓ FAQ

### Q: Is it FREE?
**A: YES!** Google Gemini has a generous free tier:
- ✅ 60 requests per minute
- ✅ Up to 2 million tokens per month
- ✅ Completely free, no credit card needed

### Q: Will it work in Hong Kong?
**A: YES!** Google services work perfectly in Hong Kong:
- ✅ No regional restrictions
- ✅ Same speed as everywhere else
- ✅ No VPN needed

### Q: What if I lose my API key?
**A: You can create a new one anytime!** Just go back to https://aistudio.google.com/app/apikey and click "Create API Key" again. Old keys can be deleted.

### Q: Can I modify the limit?
**A: Yes!** If you need higher limits:
1. Go to https://console.cloud.google.com/
2. Upgrade to "Google Cloud" (you can still use free tier, just with higher limits)
3. Review the [pricing page](https://ai.google.dev/pricing)

---

## 🔒 Security Tips

✅ **DO:**
- Keep your API key private
- Don't share it in emails or chat
- Regenerate if you think it's exposed
- Use `.env` file (don't commit to Git)

❌ **DON'T:**
- Paste your key in public forums
- Upload to GitHub without `.gitignore`
- Share screenshots with key visible
- Use same key across multiple projects

---

## 🆘 If It Doesn't Work

### Problem: "API key invalid"
**Solution:** Copy the key again carefully, make sure there are no extra spaces.

### Problem: "Quota exceeded"
**Solution:** You've hit the free tier limit. Wait 60 seconds or upgrade your plan.

### Problem: "Can't access the website"
**Try:**
- Use a VPN (though usually not needed from Hong Kong)
- Try from a different network
- Clear browser cache: `Ctrl+Shift+Delete`
- Use incognito mode

### Problem: Still stuck?
1. Check the [official setup guide](https://ai.google.dev/tutorials/setup)
2. Visit the [Gemini API troubleshooting](https://ai.google.dev/tutorials/rest_quickstart)
3. Create an issue on the project repository

---

## 🚀 Next Steps

Once you have your API key:

### Option 1: Interactive Setup (Recommended)
```bash
python setup_gemini.py
```
This wizard will:
- Verify your API key works
- Save it to `.env` safely
- Test the connection

### Option 2: Manual Setup
1. Copy this file: `.env.example`
2. Rename to: `.env`
3. Edit and add your key
4. Save

### Option 3: System Environment Variable
Set `GOOGLE_API_KEY` in your system environment (advanced).

---

## 📚 Resources

- **Official Gemini API Docs:** https://ai.google.dev/
- **Python Library:** https://ai.google.dev/tutorials/python_quickstart
- **Model Info:** https://ai.google.dev/models/gemini
- **Pricing Calculator:** https://ai.google.dev/pricing

---

## ✨ What You Get

With your Gemini API key, the emotional support website will:

✅ **Real AI Intelligence**
- Understands emotions and context
- Gives personalized, thoughtful responses
- Learns conversation history

✅ **Crisis Support** 
- Detects crisis keywords automatically
- Provides Hong Kong hotline numbers
- Handles urgent situations appropriately

✅ **Multilingual**
- Works in English
- Works in Traditional Chinese (繁體中文)
- Supports code-switching

✅ **Always Available**
- Works from Hong Kong perfectly
- No regional restrictions
- Fast response times

---

## 🎉 Ready?

After setting up your API key:

```bash
streamlit run app.py
```

Your emotional support website will be live! 🌟

---

**Last Updated:** 2025-01-18  
**Version:** Gemini Integration v1.0  
**Status:** ✅ Tested & Working
