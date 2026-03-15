# 🔑 Getting Your Claude API Key

## Step 1: Create Anthropic Account
1. Go to https://console.anthropic.com/
2. Click "Sign Up" (use your email)
3. Verify your email

## Step 2: Get API Key
1. Click your profile/avatar in top right
2. Select "API Keys" 
3. Click "Create Key"
4. Copy the key (starts with `sk-ant-...`)
5. **Keep it secret!** 🔐

## Step 3: Set Environment Variable

### Windows (Batch)
```batch
setx CLAUDE_API_KEY "sk-ant-yourkeyhere"
```

### Windows (PowerShell)
```powershell
[Environment]::SetEnvironmentVariable("CLAUDE_API_KEY", "sk-ant-yourkeyhere", "User")
```

### Mac/Linux
```bash
export CLAUDE_API_KEY="sk-ant-yourkeyhere"
```

## Step 4: Add to .env File (Optional)
Create `.env` file in the project folder:
```
CLAUDE_API_KEY=sk-ant-yourkeyhere
```

## Pricing
- **Very affordable:** ~$0.003 per student message
- Free tier: 100K tokens/month (that's ~1000 conversations!)
- Pay as you go after that

**Example costs:**
- 100 students × 10 messages/day = $0.30/day
- 1000 students × 10 messages/day = $3/day

## Restart the App
After setting the key, restart the application:
```bash
streamlit run app.py
```

The app will automatically use Claude for intelligent responses! 💙
