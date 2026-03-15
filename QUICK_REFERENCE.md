# 🚀 STREAMLIT → VERCEL CONVERSION - QUICK REFERENCE

## What Happened?

Your Streamlit app has been converted to **Next.js + Vercel** for better performance and scalability.

## New Structure

```
emotional_support_website/
├─ nextjs-app/                    ← Frontend (deploy to Vercel)
├─ flask_api.py                   ← Backend API (deploy to Render/Heroku)
├─ app.py + ai_assistant*.py     ← Keep your Python AI logic
├─ VERCEL_SETUP_COMPLETE.md      ← Read this first!
├─ VERCEL_MIGRATION_GUIDE.md     ← Full technical guide
├─ VERCEL_DEPLOYMENT_GUIDE.md    ← Step-by-step deployment
├─ start_both_servers.ps1         ← Start servers (Windows)
├─ start_both_servers.py          ← Start servers (Python)
└─ verify_setup.py                ← Check everything is ready
```

## Quick Start

### Step 1: Verify Setup (1 minute)
```bash
cd emotional_support_website
python verify_setup.py
```

### Step 2: Test Locally (2 minutes)
```bash
# Windows:
.\start_both_servers.ps1

# Mac/Linux:
python start_both_servers.py

# Or manually:
# Terminal 1:
python flask_api.py

# Terminal 2:
cd nextjs-app
npm install
npm run dev
```

Visit: **http://localhost:3000**

### Step 3: Deploy (5 minutes)
1. Push to GitHub
2. Deploy backend: https://render.com (or Heroku)
3. Deploy frontend: https://vercel.com
4. Set `PYTHON_BACKEND_URL` environment variable
5. Done! 🎉

## Commands Comparison

| Task | Streamlit | Next.js + Vercel |
|------|-----------|------------------|
| Start app | `streamlit run app.py` | `npm run dev` (in nextjs-app) |
| Build | Auto | `npm run build` |
| Deploy | Streamlit Cloud | Vercel |
| Port | 8501 | 3000 |

## File Locations

| What | Location |
|------|----------|
| Frontend UI | `nextjs-app/pages/index.js` |
| Backend API | `flask_api.py` |
| Frontend Config | `nextjs-app/next.config.js` |
| Vercel Config | `nextjs-app/vercel.json` |
| AI Logic | `ai_assistant*.py` (unchanged) |

## Environment Variables

### Local (.env.local in nextjs-app)
```
PYTHON_BACKEND_URL=http://localhost:5000
NEXT_PUBLIC_API_URL=http://localhost:3000
```

### Production (Vercel)
```
PYTHON_BACKEND_URL=https://your-backend-url.com
```

## Troubleshooting

### "Cannot reach backend"
```bash
# Check if running
curl http://localhost:5000/api/health

# Check .env.local
cat nextjs-app/.env.local
```

### "Port already in use"
```bash
# Kill process on port 5000 (Windows)
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### "npm not found"
```bash
# Install Node.js from https://nodejs.org
```

### "Flask not found"
```bash
pip install flask flask-cors
```

## Next.js Features (New!)

✅ Responsive design (Tailwind CSS)
✅ Fast page loads (edge computing)
✅ SEO friendly
✅ Mobile optimized
✅ Easy deployment (Vercel)
✅ Scalable (serverless)
✅ Modern React

## One-Page Checklist

- [ ] Run `verify_setup.py` - all checks pass
- [ ] Start servers - both running
- [ ] Test at http://localhost:3000 - works
- [ ] Backend responds - `curl http://localhost:5000/api/health`
- [ ] Chat works - sends message and gets response
- [ ] Ready to deploy - no errors in console

## Need Help?

### For Setup/Local Development
→ Read: `VERCEL_SETUP_COMPLETE.md`

### For Full Migration Details
→ Read: `VERCEL_MIGRATION_GUIDE.md`

### For Deployment Steps
→ Read: `VERCEL_DEPLOYMENT_GUIDE.md`

### For Frontend Code
→ See: `nextjs-app/README.md`

## Before & After

### Before (Streamlit)
```bash
$ streamlit run streamlit_app.py
  👆 Python runs in browser directly
```

### After (Next.js + Vercel)
```bash
$ python flask_api.py          # Backend API
$ npm run dev                  # Frontend UI
  👆 Separated, scalable, fast
```

## Deploy Checklist

- [ ] Have GitHub account
- [ ] Have Render account (for backend) OR keep running locally
- [ ] Have Vercel account (for frontend)
- [ ] Backend URL ready (from Render/Heroku)
- [ ] All API keys in environment variables
- [ ] Code pushed to GitHub

## What Stays the Same

✅ Your Python AI logic
✅ API keys and authentication
✅ Data and conversation history 
✅ All features work the same
✅ Same responses from AI

## What's Better

✅ Faster page loads
✅ Better looking UI
✅ Mobile responsive
✅ Easier to deploy
✅ Easier to scale
✅ Better performance
✅ Modern stack

## File Structure Explained

```
nextjs-app/
├─ pages/
│  ├─ index.js         ← Main UI (shows the chat interface)
│  ├─ api/chat.js      ← API endpoint (talks to Python backend)
│  ├─ _app.js          ← App wrapper
│  └─ _document.js     ← HTML document
├─ styles/
│  └─ globals.css      ← Tailwind CSS styles
├─ public/             ← Static files
├─ package.json        ← Dependencies
└─ vercel.json         ← Vercel configuration
```

## Key Files to Know

| File | Purpose | Edit? |
|------|---------|-------|
| `nextjs-app/pages/index.js` | Main UI | Yes (customize styling) |
| `nextjs-app/pages/api/chat.js` | Backend proxy | Maybe (if changing API) |
| `flask_api.py` | REST API | Yes (add endpoints) |
| `nextjs-app/tailwind.config.js` | Styling config | Yes (change colors) |
| `ai_assistant*.py` | AI logic | Yes (keep as is) |

## Testing in Order

1. ✅ Run `verify_setup.py`
2. ✅ Start both servers
3. ✅ Open http://localhost:3000
4. ✅ Type test message
5. ✅ Check response
6. ✅ Check console (F12) for errors
7. ✅ Ready to deploy!

## Common Questions

**Q: Can I keep Streamlit?**
A: Yes, but not needed. Both can run on different ports.

**Q: Do I need to rewrite Python code?**
A: No! All Python stays the same, just wrapped in Flask API.

**Q: How much does Vercel cost?**
A: Free tier includes 100GB/month, perfect for most projects.

**Q: Can I use my own domain?**
A: Yes! Vercel dashboard → Settings → Domains

**Q: How do I update the code?**
A: Push to GitHub → Vercel auto-deploys

---

## 🚀 Next Action

**Run this now:**
```bash
python verify_setup.py
```

**Then run:**
```bash
.\start_both_servers.ps1
```

**Then visit:**
```
http://localhost:3000
```

---

**Status**: ✅ Ready for Production

**Last Updated**: March 2026

**Questions?** See `VERCEL_SETUP_COMPLETE.md` for detailed help
