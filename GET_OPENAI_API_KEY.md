# 🔑 Getting Your OpenAI API Key (ChatGPT)

Perfect for Hong Kong, Taiwan, and most Asian regions! 🇭🇰 🇹🇼

## Step 1: Create OpenAI Account
1. Go to https://platform.openai.com/signup
2. Sign up with email or Google/Microsoft account
3. Verify your email
4. Add your phone number (for verification)

## Step 2: Get API Key
1. Log in to https://platform.openai.com/
2. Click your profile in top right corner
3. Select "API Keys" from dropdown
4. Click "+ Create new secret key"
5. Copy the key (starts with `sk-proj-...`)
6. **Keep it safe!** 🔐 (You won't see it again)

## Step 3: Add Billing (Important!)
1. Go to https://platform.openai.com/account/billing/overview
2. Click "Set up paid account"
3. Add a payment method (Visa/Mastercard/etc)
4. Set a monthly spending limit (e.g., $100) for safety

**Hong Kong Note:** Credit cards work fine. No special restrictions.

## Step 4: Set Environment Variable

### Windows (Batch)
```batch
setx OPENAI_API_KEY "sk-proj-yourkeyhere"
```

### Windows (PowerShell)
```powershell
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sk-proj-yourkeyhere", "User")
```

### Mac/Linux
```bash
export OPENAI_API_KEY="sk-proj-yourkeyhere"
```

## Step 5: Add to .env File (Optional Backup)
Create `.env` file in the project folder:
```
OPENAI_API_KEY=sk-proj-yourkeyhere
```

## Step 6: Restart Terminal
Close and reopen your terminal for changes to take effect.

## Pricing

### Very Affordable!
- **GPT-4o mini** (what we use): ~$0.002-0.003 per message
- **Much cheaper than Claude**
- **Free tier available** ($5 free credits for first 3 months)

### Cost Examples
| Students | Messages/Day | Cost/Day | Cost/Month |
|----------|-------------|----------|-----------|
| 10 | 5 | $0.05 | $1.50 |
| 50 | 5 | $0.25 | $7.50 |
| 100 | 10 | $0.50 | $15 |
| 500 | 10 | $2.50 | $75 |
| 1000 | 10 | $5 | $150 |

**Hong Kong schools:** Typically $20-50/month

## Verify Setup
After setting the key, run:
```bash
python -c "
from openai import OpenAI
client = OpenAI()
print('✅ OpenAI API is working!')
"
```

## Restart the App
Close the current app and restart:
```bash
streamlit run app.py
```

You should see a green checkmark: **🤖 AI Mode: ChatGPT (OpenAI)** ✅

## Available Models

We use **GPT-4o mini** for:
- ✅ Fast responses (~1-2 seconds)
- ✅ Excellent quality
- ✅ Very affordable
- ✅ Perfect for emotional support

Alternative models available:
- `gpt-4o` - More powerful, higher cost
- `gpt-4-turbo` - Advanced, more expensive
- `gpt-3.5-turbo` - Cheaper, simpler

## Troubleshooting

### Error: "API key not found"
- Check you set the environment variable correctly
- Check `.env` file exists with your key
- Restart terminal and try again

### Error: "Invalid API key format"
- Make sure key starts with `sk-proj-`
- Check there are no extra spaces or quotes
- Generate a new key if unsure

### Error: "Insufficient quota"
- Check https://platform.openai.com/account/billing/overview
- May need to add/update payment method
- Set higher spending limit

### No response from API
- Check internet connection
- Check OpenAI status: https://status.openai.com/
- Try again in 1 minute

## More Help

- **OpenAI Documentation:** https://platform.openai.com/docs
- **API Reference:** https://platform.openai.com/docs/api-reference
- **Pricing Details:** https://openai.com/pricing

## Next Steps

1. Get your API key (5 min)
2. Set environment variable (1 min)
3. Run the app: `streamlit run app.py`
4. See it work instantly!

🎉 **You're ready! The AI will provide intelligent emotional support for your students.** 💙
