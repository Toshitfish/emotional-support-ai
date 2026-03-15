# Emotional Support Website - Next.js Frontend

Modern frontend for the Emotional Support Website, built with Next.js and deployed on Vercel.

## 🚀 Quick Start

### Prerequisites
- Node.js 16+ 
- npm or yarn
- Python backend running (Flask API)

### Installation

```bash
# Navigate to the nextjs-app folder
cd nextjs-app

# Install dependencies
npm install

# Create .env.local with your backend URL
cp .env.example .env.local

# Edit .env.local if needed
# PYTHON_BACKEND_URL=http://localhost:5000
```

### Development

```bash
# Start development server
npm run dev

# Open http://localhost:3000 in your browser
```

### Build for Production

```bash
npm run build
npm run start
```

## 📡 Python Backend Integration

This Next.js app expects a Python Flask backend running on port 5000 (or custom URL in `.env.local`).

The backend should provide an endpoint:
```
POST /api/chat
{
  "message": "user message",
  "assistant_type": "openai" | "claude" | "gemini"
}

Response:
{
  "response": "AI response text"
}
```

### Starting the Python Backend

From the parent directory:
```bash
python app.py
# or
python START_HERE.py
```

## 🔗 Deploy to Vercel

### Option 1: Using Vercel CLI

```bash
npm install -g vercel

# Deploy
vercel

# Set environment variables when prompted
# PYTHON_BACKEND_URL=https://your-backend-url.com
```

### Option 2: GitHub Integration (Recommended)

1. Push this folder to GitHub
2. Go to [Vercel Dashboard](https://vercel.com/dashboard)
3. Click "New Project"
4. Select your GitHub repository
5. Set environment variables:
   - `PYTHON_BACKEND_URL`: Your Python backend URL (Flask, Render, Heroku, etc.)
6. Deploy!

### Option 3: Using Vercel UI

1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Choose "Other" and upload the nextjs-app folder
4. Configure environment variables
5. Deploy

## 🔐 Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| PYTHON_BACKEND_URL | URL to your Python Flask backend | `http://localhost:5000` or `https://api.example.com` |
| NEXT_PUBLIC_API_URL | Public API URL (for client-side calls) | `http://localhost:3000` |

## 📁 Project Structure

```
nextjs-app/
├── pages/
│   ├── _app.js           # App wrapper
│   ├── _document.js      # HTML document
│   ├── index.js          # Home page
│   └── api/
│       └── chat.js       # API proxy to Python backend
├── styles/
│   └── globals.css       # Global Tailwind styles
├── components/           # React components
├── public/               # Static assets
├── package.json
├── next.config.js
├── tailwind.config.js
├── vercel.json          # Vercel deployment config
└── .env.example         # Environment variables template
```

## 🎨 Styling

This project uses **Tailwind CSS** for styling. Modify styles in:
- `styles/globals.css` - Global styles
- `pages/index.js` - Component styles

## 🐛 Troubleshooting

### Backend connection error
- Make sure Python backend is running: `python app.py`
- Check `PYTHON_BACKEND_URL` in `.env.local`
- Ensure CORS is enabled in Python backend

### Build fails on Vercel
- Delete `node_modules` and `package-lock.json`
- Run `npm install` locally
- Commit and push changes

### Page not loading
- Check browser console for errors (F12)
- Verify environment variables are set in Vercel dashboard
- Check Vercel deployment logs

## 📝 Next Steps

1. ✅ Deploy to Vercel
2. 📊 Add more pages (dashboard, settings, help)
3. 💾 Add database for storing conversations
4. 🔐 Add user authentication
5. 📱 Mobile app version

## 📚 Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [Vercel Documentation](https://vercel.com/docs)
- [Tailwind CSS](https://tailwindcss.com)
- [Deployment Guide](./DEPLOYMENT.md)

## 📄 License

Same as parent project
