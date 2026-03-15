# Emotional Support AI - Deployment Guide (MVP)

## 🚀 Quick Deployment Steps (20 minutes total)

### Prerequisites
- GitHub account
- Vercel account (free: https://vercel.com)
- Render account (free: https://render.com)
- API key for at least one AI provider:
  - **Claude**: https://console.anthropic.com/
  - **OpenAI**: https://platform.openai.com/api-keys
  - **Gemini**: https://aistudio.google.com/app/apikey

---

## Phase 1: Prepare for Deployment

### Step 1A: Check GitHub Repository
The code needs to be in GitHub. If not already there:

```bash
cd emotional_support_website
git init
git add .gitignore flask_api.py requirements.txt nextjs-app/
git commit -m "Initial: Emotional Support AI MVP"
# Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/emotional-support-ai.git
git branch -M main
git push -u origin main
```

### Step 1B: Create `.env` file locally
```bash
cp .env.example .env
# Edit .env and add ONLY ONE API key:
# Option 1: CLAUDE_API_KEY=sk-ant-...
# Option 2: OPENAI_API_KEY=sk-proj-...
# Option 3: GOOGLE_API_KEY=...
```

### Step 1C: Test Flask API locally (optional)
```bash
cd emotional_support_website
python flask_api.py
# Should print: "Starting on http://localhost:5000"
# Test: curl http://localhost:5000/api/health
```

---

## Phase 2: Deploy Flask Backend to Render

### Step 2A: Create Render Web Service
1. Go to https://render.com
2. Click **"+ New"** → **"Web Service"**
3. Connect your GitHub repository
4. Select the repository with `flask_api.py`
5. Fill in:
   - **Name**: `emotional-support-api`
   - **Root Directory**: `.` (or `emotional_support_website/` if at root)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python flask_api.py`
6. Click **"Create Web Service"**

### Step 2B: Add Environment Variables in Render
1. After creation, go to **Settings** → **Environment**
2. Add these variables:
   - `FLASK_ENV`: `production`
   - `CLAUDE_API_KEY`: `sk-ant-...` (your actual key)
   - (OR `OPENAI_API_KEY` or `GOOGLE_API_KEY`)
   - `PORT`: `5000`
3. Click **"Save Changes"**
4. Render auto-redeploys (watch the **"Events"** tab)

### Step 2C: Get Your Backend URL
- Once deployed, Render shows: `https://emotional-support-api.onrender.com`
- **Test it**: `curl https://emotional-support-api.onrender.com/api/health`
- Should return: `{"status": "ok", "environment": "production"}`

---

## Phase 3: Deploy Next.js Frontend to Vercel

### Step 3A: Create Vercel Project
1. Go to https://vercel.com
2. Click **"Add New"** → **"Project"**
3. Import your GitHub repository
4. Select the project

### Step 3B: Configure Environment Variables

**CRITICAL**: Set up the backend URL in Vercel:

1. In Vercel dashboard, go to **Settings** → **Environment Variables**
2. Add:
   - **Name**: `PYTHON_BACKEND_URL`
   - **Value**: `https://emotional-support-api.onrender.com` (your Render URL)
   - **Environments**: Select `Production`, `Preview`, `Development`
3. Click **"Save"**

### Step 3C: Specify Build Settings
1. In Vercel, go to **Settings** → **Build & Development Settings**
2. Set:
   - **Framework Preset**: `Next.js`
   - **Build Command**: `next build` (auto-detected)
   - **Output Directory**: `.next` (auto-detected)
   - **Root Directory**: `nextjs-app` (if not at root)
3. Click **"Save"**

### Step 3D: Deploy
1. Click **"Deploy"**
2. Wait for build to complete (~2-3 minutes)
3. Get your URL: `https://your-project.vercel.app`

---

## Phase 4: Test End-to-End

### Test 1: Health Check
```bash
curl https://your-project.vercel.app/
# Should load the chat UI
```

### Test 2: Chat Message
Send a message from the chat UI:
- Type: "Hello, I'm feeling stressed"
- Expected: AI response + mood indicator (🤖)

### Test 3: Crisis Detection
Type: "I want to kill myself"
- Expected: Red crisis alert with hotline number (🆘)

### Test 4: Chat History  
- Send 3+ messages
- Refresh the page
- Expected: All previous messages still visible (persisted in memory)

---

## Phase 5: Optional - Post-Launch Refinements

### Add Firebase for Persistent Database
Currently, chat is stored in memory (resets when server restarts). For production:

1. Create Firebase project: https://firebase.google.com
2. Set `FIREBASE_DB_URL` in Render environment
3. The `flask_api.py` will auto-enable Firebase persistence

### Add User Authentication
- Implement OAuth (Google/GitHub) in Next.js
- Track user sessions instead of anonymous sessions

### Add Advanced Analytics
- Log all conversations to database
- Analyze sentiment trends over time
- Identify at-risk users for follow-up

### Enable CORS for Custom Domains
In `flask_api.py`, update CORS configuration:
```python
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://your-domain.com", "https://your-project.vercel.app"]
    }
})
```

---

## Troubleshooting

### "Failed to reach AI service"
- Check `CLAUDE_API_KEY` (or other key) is set in Render environment
- Verify the key is valid (test in CLI: `echo $CLAUDE_API_KEY`)

### "Backend error: No AI assistant available"
- At least one API key must be configured
- Check Render's **Logs** tab: `Settings → Logs`

### Chat not persisting after refresh
- Currently using in-memory storage (resets on server restart)
- Set up Firebase (see Phase 5) for real persistence

### Render "Free Tier Spinning Down"
- Free Render services sleep after 15 minutes of inactivity
- Users may experience 30-second delay on first message
- Upgrade to Render Pro for always-on ($10/month)

---

## Architecture

```
Next.js Frontend (Vercel)
    ↓ (HTTPS)
Vercel Proxy Route (/api/chat)
    ↓
Flask REST API (Render)
    ↓ (parallel)
    ├→ ChatGPT / Claude / Gemini
    ├→ TextBlob (Sentiment Analysis)
    ├→ Crisis Keyword Detector
    └→ In-Memory Chat Storage or Firebase DB
```

---

## Estimated Costs

| Service | Tier | Cost | Status |
|---------|------|------|--------|
| Vercel | Free | $0 | ✅ |
| Render | Free | $0 | ⚠️ Sleeps after 15 min |
| Claude API | Pay-as-you-go | $0.003/1K tokens | Depends on usage |
| **Total** | MVP | ~$0 | 🎉 Free for MVP |

Upgrade Render to Pro ($10/month) if you want 24/7 uptime.

---

## Quick Reference

| Environment | URL | Manage |
|-------------|-----|--------|
| Frontend | https://your-project.vercel.app | Vercel Dashboard |
| Backend | https://emotional-support-api.onrender.com | Render Dashboard |
| Repository | https://github.com/YOUR_USERNAME/... | GitHub |

---

## Support & Resources

- **Vercel Docs**: https://vercel.com/docs
- **Render Docs**: https://render.com/docs
- **Claude API**: https://console.anthropic.com/
- **Next.js**: https://nextjs.org/docs
- **Flask**: https://flask.palletsprojects.com/

---

**Status**: ✅ MVP Complete (Sentiment + Crisis Detection + Chat History)  
**Next Phase**: User Auth + Persistent Database + Advanced Analytics

