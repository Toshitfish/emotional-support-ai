# Emotional Support Website - Vercel Deployment Guide

## 🚀 Quick Deploy to Vercel

Complete these steps to deploy your Next.js frontend to Vercel.

## Prerequisites

- GitHub account (optional, but recommended)
- Node.js 16+ installed locally
- Python backend URL (or set it up first)

## Option 1: Deploy via GitHub (Recommended)

### Step 1: Prepare Your GitHub Repository

```bash
# If not already a git repo
cd emotional_support_website
git init

# Add all files
git add .
git commit -m "Initial commit with Vercel setup"

# Create repo on github.com and push
git remote add origin https://github.com/your-username/your-repo.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy to Vercel

1. Go to https://vercel.com/dashboard
2. Click **"New Project"**
3. Select your GitHub repository
4. Configure Project Settings:
   - **Framework Preset**: Next.js
   - **Root Directory**: `emotional_support_website/nextjs-app`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`

5. Add Environment Variables:
   - Click **"Environment Variables"**
   - Add: `PYTHON_BACKEND_URL` = `https://your-backend-url.com`

6. Click **"Deploy"**
7. Wait for build to complete
8. Your site is live! 🎉

## Option 2: Deploy via Vercel CLI

### Step 1: Install Vercel CLI

```bash
npm install -g vercel
```

### Step 2: Login to Vercel

```bash
vercel login
# Follow the browser prompt
```

### Step 3: Deploy

```bash
cd emotional_support_website/nextjs-app

vercel \
  --env PYTHON_BACKEND_URL=https://your-backend-url.com \
  --project emotional-support-website
```

### Step 4: Configure Production URL

```bash
vercel env add PYTHON_BACKEND_URL --environment production
# Enter: https://your-backend-url.com
```

## Option 3: Deploy Backend to Render

### Step 1: Push to GitHub

```bash
cd emotional_support_website
git add .
git commit -m "Add Flask API for Vercel"
git push
```

### Step 2: Create Render Service

1. Go to https://render.com
2. Click **"New +"** → **"Web Service"**
3. Select your GitHub repository
4. Configure:
   - **Name**: `emotional-support-api`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python flask_api.py`
   - **Plan**: Free (or paid for better uptime)

5. Add Environment Variables:
   - `OPENAI_API_KEY` (if using OpenAI)
   - `ANTHROPIC_API_KEY` (if using Claude)
   - `GOOGLE_API_KEY` (if using Gemini)

6. Click **"Create Web Service"**
7. Get your URL: `https://your-service-name.onrender.com`

### Step 3: Update Vercel with Backend URL

1. Go to Vercel project settings
2. Update `PYTHON_BACKEND_URL` = `https://your-service-name.onrender.com`
3. Redeploy from Vercel dashboard

## Testing After Deployment

### 1. Check Health Endpoint

```bash
# Replace with your actual backend URL
curl https://your-backend-url.com/api/health

# Should return:
# {"status":"ok","environment":"production","message":"Emotional Support API is running"}
```

### 2. Check Vercel Frontend

Visit your Vercel URL in browser. Should see:
- ✅ Purple card with 💙 Emotional Support heading
- ✅ Dropdown to select AI assistant
- ✅ Text input for message
- ✅ "Get Support" button

### 3. Test Chat

1. Type a message
2. Click "Get Support"
3. Should get AI response within 30 seconds
4. Check browser console (F12) for errors if it fails

## Environment Variables Reference

### For Vercel (Frontend)

| Variable | Purpose | Example |
|----------|---------|---------|
| `PYTHON_BACKEND_URL` | Flask API endpoint | `https://api.example.com` |
| `NEXT_PUBLIC_API_URL` | Client-side API URL | `https://your-site.vercel.app` |

### For Render or Your Backend

| Variable | Purpose | Required |
|----------|---------|----------|
| `OPENAI_API_KEY` | GPT API key | If using OpenAI |
| `ANTHROPIC_API_KEY` | Claude API key | If using Claude |
| `GOOGLE_API_KEY` | Gemini API key | If using Gemini |
| `FLASK_ENV` | Environment | `production` |

## Monitoring & Logs

### Vercel Logs

```bash
# View deployment logs
vercel logs

# Watch real-time logs
vercel logs --follow
```

### Render Logs

1. Go to Render dashboard
2. Select your service
3. Click **"Logs"** tab
4. View real-time logs

## Optimization Tips

### 1. Vercel Edge Middleware

```javascript
// middleware.js (Vercel edge)
export function middleware(request) {
  return new Response('Hello from Edge!');
}
```

### 2. Image Optimization

```javascript
// Use Next.js Image component
import Image from 'next/image'

<Image 
  src="/logo.png" 
  alt="Logo"
  width={100}
  height={100}
/>
```

### 3. API Response Caching

```javascript
// pages/api/chat.js
response.setHeader(
  'Cache-Control',
  'public, max-age=60, s-maxage=120'
);
```

## Troubleshooting

### Error: "Cannot reach backend"

**Cause**: Backend URL not configured or server down

**Fix**:
```bash
# Test backend directly
curl https://your-backend-url.com/api/health

# Update Vercel env variable
vercel env add PYTHON_BACKEND_URL --environment production
```

### Error: "500 Internal Server Error"

**Cause**: Python backend error

**Fix**:
```bash
# Check Render logs for errors
# Ensure all API keys are set
# Test locally: python flask_api.py
```

### Error: "Build failed on Vercel"

**Cause**: Dependency or build issue

**Fix**:
```bash
# Delete node_modules and rebuild
rm -rf node_modules package-lock.json
npm install

# Build locally first
npm run build

# Commit and push
git add .
git commit -m "Fix build"
git push
```

### Error: "429 Too Many Requests"

**Cause**: Rate limit exceeded

**Fix**:
```python
# In flask_api.py, add rate limiting
from flask_limiter import Limiter

limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/api/chat')
@limiter.limit("10 per hour")
def chat():
    ...
```

## Security Checklist

- [ ] API keys are in environment variables (NOT in code)
- [ ] CORS is properly configured
- [ ] Vercel hosting is under HTTPS
- [ ] Backend is also under HTTPS
- [ ] API keys are not logged
- [ ] Rate limiting is configured
- [ ] Input validation is in place

## Performance Metrics

After deployment, check:

1. **Vercel Analytics**: https://vercel.com/dashboard/your-project/analytics
2. **Render Metrics**: Render dashboard → Metrics
3. **User Experience**: [Web Vitals](https://web.dev/vitals/)

Target metrics:
- LCP (Largest Contentful Paint): < 2.5s
- FID (First Input Delay): < 100ms
- CLS (Cumulative Layout Shift): < 0.1

## Next Steps

- [ ] Set up custom domain (Vercel → Settings → Domains)
- [ ] Enable automatic deploys on push
- [ ] Set up monitoring alerts
- [ ] Add database (Supabase, MongoDB)
- [ ] Add authentication (NextAuth.js)
- [ ] Set up CI/CD pipeline

## Support & Resources

- **Vercel Docs**: https://vercel.com/docs
- **Next.js Docs**: https://nextjs.org/docs
- **Render Docs**: https://render.com/docs
- **Community**: https://github.com/vercel/next.js/discussions

---

**Deployed Successfully?** 🎉

Share your site! Get feedback from users and iterate.

**Need Help?** Check the main README.md or VERCEL_MIGRATION_GUIDE.md
