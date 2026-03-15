# Migration Guide: Streamlit → Next.js + Vercel

## Overview

This guide explains how to migrate from Streamlit to a modern Next.js frontend with Python backend API hosted on Vercel.

## Why Migrate?

| Aspect | Streamlit | Next.js + Vercel |
|--------|-----------|------------------|
| **Deployment** | Streamlit Cloud | Vercel (fast, free tier) |
| **Customization** | Limited | Full control |
| **Performance** | Slower builds | Fast edge computing |
| **Scalability** | Limited | Enterprise-grade |
| **Mobile Support** | Limited | Full responsive design |
| **SEO** | Not great | Excellent |
| **User Limits** | Restrictions | Unlimited |

## Architecture

### Before (Streamlit)
```
┌─────────────────┐
│  Browser        │
│  ↓              │
│  streamlit run  │
│  app.py         │
│  ↓              │
│  Python App     │
│  (direct calls) │
└─────────────────┘
```

### After (Next.js + Flask API)
```
┌──────────────────────────────────────────┐
│ Browser                                   │
│ ↓                                         │
│ ┌─────────────────────────────────────┤ │
│ │ Vercel (Next.js Frontend)           │ │
│ │ - pages/index.js (UI)               │ │
│ │ - pages/api/chat.js (API proxy)     │ │
│ │ - Tailwind CSS Styling              │ │
│ └─────────────────────────────────────┤ │
│ ↓                                         │
│ ┌─────────────────────────────────────┤ │
│ │ Your Server (Flask API)             │ │
│ │ - flask_api.py (REST endpoints)     │ │
│ │ - ai_assistant_*.py (AI logic)      │ │
│ │ - Python backend (local or cloud)   │ │
│ └─────────────────────────────────────┤ │
└──────────────────────────────────────────┘
```

## Step-by-Step Migration

### Phase 1: Setup (Current)
✅ Next.js project created (`nextjs-app/`)
✅ Flask API created (`flask_api.py`)
✅ Environment configured

### Phase 2: Testing Locally

#### Terminal 1: Start Python Backend
```bash
cd emotional_support_website
pip install flask flask-cors

# Copy and modify if needed
python flask_api.py
# Should show: Starting on http://localhost:5000
```

#### Terminal 2: Start Next.js Frontend
```bash
cd emotional_support_website/nextjs-app
npm install
npm run dev
# Should show: Ready on http://localhost:3000
```

#### Terminal 3: Test
```bash
# Visit http://localhost:3000 and test the chat
```

### Phase 3: Prepare for Deployment

#### 1. Remove Old Streamlit Files (Optional)
```bash
# Keep for backup, but no longer needed:
# - streamlit_app.py
# - start_dashboard.py
# - start.bat
# - start.ps1
```

#### 2. Update Dependencies
```bash
cd emotional_support_website

# Ensure all Python packages are in requirements.txt
pip install flask flask-cors

# Add to requirements.txt:
# flask>=2.3.0
# flask-cors>=4.0.0
```

#### 3. Deploy Backend
Choose one:

**Option A: Deploy Python to Render (Recommended)**
```
1. Go to render.com
2. Create new "Web Service"
3. Connect your GitHub repo
4. Set build command: pip install -r requirements.txt
5. Set start command: python flask_api.py
6. Get URL: https://your-api.onrender.com
7. Copy this URL for Vercel config
```

**Option B: Keep Backend Local (for testing)**
- Python backend runs on your machine
- Next.js calls http://localhost:5000
- Only frontend is on Vercel

**Option C: Deploy to Heroku**
```bash
heroku create your-api-name
git push heroku main
```

#### 4. Deploy Frontend to Vercel

**Method 1: Using Vercel CLI**
```bash
npm install -g vercel

cd emotional_support_website/nextjs-app

vercel --env PYTHON_BACKEND_URL=https://your-api.onrender.com
# Follow prompts, set environment variables
```

**Method 2: GitHub Integration (Recommended)**
1. Push to GitHub:
```bash
git add .
git commit -m "Add Next.js frontend + Flask API"
git push origin main
```

2. Go to [vercel.com](https://vercel.com/dashboard)
3. Click "New Project"
4. Select your GitHub repository
5. Choose `nextjs-app` folder as root
6. Add Environment Variables:
   - `PYTHON_BACKEND_URL`: Your Flask API URL
7. Click "Deploy"

## File Changes Summary

### Removed
- ❌ `streamlit_app.py` (replaced by `nextjs-app/pages/index.js`)
- ❌ `start_dashboard.py` (replaced by `npm run dev`)
- ❌ `start.bat`, `start.ps1` (use npm instead)
- ❌ `STREAMLIT_DASHBOARD_GUIDE.md` (outdated)

### Added
- ✅ `nextjs-app/` (Full Next.js application)
- ✅ `flask_api.py` (REST API backend)
- ✅ `VERCEL_MIGRATION_GUIDE.md` (this file)

### Modified
- 📝 `requirements.txt` (add Flask dependencies)
- 📝 `README.md` (update instructions)

## Configuration Files

### `.env.local` (Next.js)
```
PYTHON_BACKEND_URL=https://your-api.onrender.com
NEXT_PUBLIC_API_URL=http://localhost:3000
```

### `vercel.json` (Vercel Deployment)
Already configured. Key settings:
- Framework: nextjs
- Build command: `npm run build`
- Deploy directory: `.next`

## Common Issues & Solutions

### Issue: "Cannot reach backend"
**Solution:**
```bash
# Check backend is running
curl http://localhost:5000/api/health

# Check PYTHON_BACKEND_URL in .env.local
cat .env.local
```

### Issue: CORS errors
**Solution:** Flask API has CORS enabled. If still failing:
```python
# In flask_api.py, CORS is already set to allow all
from flask_cors import CORS
CORS(app)
```

### Issue: Vercel deployment fails
**Solution:**
```bash
# Check locally first
npm run build
npm start

# Ensure all dependencies in package.json
npm list

# Push to GitHub and check Vercel logs
```

### Issue: API timeout
**Solution:**
- Increase timeout in `nextjs-app/pages/api/chat.js`
- Check backend is responding: `curl http://BACKEND_URL/api/health`

## Performance Tips

1. **Frontend (Vercel)**
   - Uses CDN for fast delivery
   - Automatic image optimization
   - Edge functions for low latency

2. **Backend (Flask)**
   - Use async calls for long tasks
   - Add caching with redis
   - Deploy to region closest to users

3. **Database** (if adding later)
   - Use serverless database (Supabase, PlanetScale)
   - Connect from Flask API
   - Cache results in Next.js

## Next Steps After Migration

- [ ] Add user authentication (NextAuth.js)
- [ ] Add database (Supabase, MongoDB)
- [ ] Add conversation history
- [ ] Add user settings page
- [ ] Add dark mode
- [ ] Add mobile app
- [ ] Add analytics
- [ ] Add rate limiting
- [ ] Add logging & monitoring

## Rollback Plan

If issues occur:
1. Keep Streamlit files as backup
2. Don't delete `streamlit_app.py` and old files yet
3. Can run both in parallel during transition
4. Switch DNS/URLs after testing

## FAQ

**Q: Can I keep Streamlit running?**
A: Yes! You can run both in parallel. Just use different ports.

**Q: Do I need to rewrite my Python code?**
A: No! Your AI logic stays the same in flask_api.py

**Q: How much does Vercel cost?**
A: Free tier includes 100GB bandwidth/month, plenty for small projects.

**Q: Can I use a database now?**
A: Yes! Flask API can now connect to databases (currently it's stateless).

**Q: What about the old Streamlit deployment?**
A: You can deprecate it once Next.js is stable. Keep credentials safe!

## Support

- [Next.js Docs](https://nextjs.org/docs)
- [Vercel Docs](https://vercel.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com)
- This project's README.md

---

**Last Updated**: March 2026
**Migration Status**: Ready for Production
