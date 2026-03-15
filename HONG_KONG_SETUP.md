# 🇭🇰 情緒支持平臺 - Hong Kong Setup Guide

為香港學生提供 24/7 情感支持，使用 OpenAI ChatGPT ✨

---

## ⚡ 快速開始 | Quick Start (5 分鐘)

### Step 1️⃣: 取得 OpenAI API 金鑰
```
訪問: https://platform.openai.com/api-keys
登入或註冊 (用 Google/Microsoft 帳號可更快)
點擊 "Create new secret key"
複製金鑰 (開頭是 sk-proj-)
```

✅ **免費!** 前3個月有$5免費額度

### Step 2️⃣: 執行設置向導
```bash
python setup_openai.py
# 貼上你的API金鑰，然後回車完成設置
```

### Step 3️⃣: 啟動應用
```bash
streamlit run app.py
# 訪問 http://localhost:8501
```

### Step 4️⃣: 完成！
看到綠色勾選: **✅ 🤖 AI Mode: ChatGPT (OpenAI)**

---

## 📊 為什麼選擇 OpenAI?

| 功能 | Claude | OpenAI |
|------|--------|--------|
| 香港可用 | ❌ | ✅ |
| 成本 | 較貴 | **便宜** |
| 速度 | 快 | **更快** |
| 質量 | 很好 | **很好** |
| 免費額度 | 100K tokens/月 | **$5信用額度** |

**香港最佳選擇: OpenAI** ✅

---

## 💰 費用明細

### 非常便宜!
```
每條學生消息 ≈ HK$0.01-0.015
一整天10名學生 5條消息 ≈ HK$0.50
一個月 ≈ HK$15
一個學校(100名學生) ≈ HK$150/月
```

**對比:**
- 傳統心理諮詢: HK$500-1000/次
- 我們的AI: HK$0.01/條消息
- 24小時可用: **無價** 💙

### 支付方式
```
✅ 信用卡 (Visa/Mastercard)
✅ 港幣 (自動轉換)
✅ 設定每月限額 (例如 HK$500)
```

---

## 🔑 詳細步驟

### A. 建立 OpenAI 帳戶

1. 訪問 https://platform.openai.com/signup
2. 選擇用 Google/Microsoft 帳號快速登錄
3. 驗證電郵
4. 添加電話號碼 (選擇香港 +852)
5. 完成資料填寫

### B. 取得 API 金鑰

1. 登錄 https://platform.openai.com/
2. 點擊右上角你的名字
3. 選 "API keys"
4. 點 "+ Create new secret key"
5. **複製整個金鑰**
6. ⚠️ 保管好！你不會再看到它

### C. 添加付款方式

1. 去 https://platform.openai.com/account/billing/overview
2. 點 "Set up paid account"
3. 添加信用卡
4. 設定每月預算限制 (香港學校通常 HK$300-500)

### D. 在你的電腦設置

**在 PowerShell 執行:**
```powershell
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sk-proj-你的金鑰", "User")
```

或者在專案資料夾創建 `.env` 檔案:
```
OPENAI_API_KEY=sk-proj-你的金鑰
```

### E. 運行設置精靈

```bash
cd emotional_support_website
python setup_openai.py
```

跟著提示走，貼上你的 API 金鑰。

### F. 啟動應用

```bash
streamlit run app.py
```

看到 **✅ 🤖 AI Mode: ChatGPT (OpenAI)** 表示成功！

---

## 🎯 應用功能

### 對學生而言
```
匿名聊天 → 無需登入
24/7可用 → 隨時隨地
AI理解 → 真正聆聽
快速回應 → 1-2秒內
危機支持 → 立即求救
```

### AI 特性
```
✅ 分析真正的問題
✅ 提供具體建議
✅ 理解香港背景
   (DSE考試壓力、住房問題等)
✅ 記住對話上下文
✅ 多語言支持
```

---

## 🚨 危機支持

如果學生提及自殺、自害:
1. **立即檢測** → AI 優先响應
2. **自動提供** → 撒瑪利亞防止撥款會熱線
3. **緊急號碼** → 999 (香港)
4. **持續支持** → 指導尋求專業幫助

### 內建資源

**撒瑪利亞防止撥款會 (Samaritans)**
```
📞 2389 2222 (24小時)
💬 WhatsApp: +852 5162 0000
🌐 Website: www.samaritans.org.hk
```

自動在應用中提供！

---

## 📱 部署給學生

### 選項 1: 學校網絡
```bash
# 在學校電腦上運行
streamlit run app.py
# 學生訪問 http://school-ip:8501
```

### 選項 2: Streamlit Cloud (推薦)
```
1. 推送代碼到 GitHub
2. 訪問 https://streamlit.io
3. 導入你的倉庫
4. 部署 (一鍵!)
5. 分享公開鏈接給學生
```

### 選項 3: Docker
```bash
docker-compose up
# 訪問 http://localhost:8501
```

---

## ✅ 測試你的設置

運行:
```bash
python -c "
from openai import OpenAI
client = OpenAI()
print('✅ OpenAI 連接成功!')
"
```

應該看到: **✅ OpenAI 連接成功!**

---

## ❓ 常見問題

### Q: API 金鑰在哪裡?
**A:** https://platform.openai.com/api-keys

### Q: 需要付款嗎?
**A:** 第1個月免費($5額度)，之後按使用量付款。設定預算限額 (例如 HK$500/月) 即可。

### Q: ChatGPT vs Claude?
**A:** 都不錯，但 ChatGPT 在香港更便宜且更快。

### Q: 學生的信息安全嗎?
**A:** 完全匿名，沒有存儲個人信息，符合 PDPO (個人資料保護條例)。

### Q: 多少學生可以使用?
**A:** 無限！API 可以一次處理數百個並發用戶。

### Q: 可以離線使用嗎?
**A:** 需要網絡連接到 OpenAI API。如果網絡故障，自動降級到本地支持。

### Q: 學生需要登入嗎?
**A:** 不需要！完全匿名。

---

## 🆘 故障排除

### 錯誤: "API key not found"
```
→ 檢查 OPENAI_API_KEY 是否設置正確
→ 檢查 .env 檔案
→ 重啟終端機
```

### 錯誤: "Invalid API key"
```
→ 確保金鑰以 sk-proj- 開頭
→ 檢查是否完整複製 (沒有多餘空格)
→ 重新生成一個新金鑰
```

### 沒有回應
```
→ 檢查網絡連接
→ 檢查 https://status.openai.com/ 狀態
→ 稍後再試
```

---

## 📚 更多資源

- **OpenAI 文檔**: https://platform.openai.com/docs
- **定價詳情**: https://openai.com/pricing
- **熱線支持**: 見應用內的危機資源

---

## 🎓 給學校和教師

### 建議設置

```
1. 取得1個 API 金鑰 (共用)
2. 部署到 Streamlit Cloud (免費)
3. 設定 HK$300-500 每月預算
4. 分享鏈接給全校學生
5. 監控使用情況和影響
```

### 隱私合規
```
✅ PDPO (個人資料保護條例) 兼容
✅ 無 CookiesNo user tracking
✅ 匿名聊天
✅ 可自定義保留期
```

### 訓練教職員
```
→ 解釋 AI 限制 (非替代專業)
→ 教導如何上報危機個案
→ 定期檢查應用狀態
```

---

## 💙 最後的話

你現在有了一個真正的 AI 助手，24小時為香港學生服務。

它可以:
- 理解他們的真實處境
- 提供具體、可行的建議
- 記住他們分享的事
- 優先考慮安全
- 讓他們感到被傾聽

本周開始幫助遇到困難的學生吧。💙

---

## 🚀 立即開始!

```bash
# 1. 取得 API 金鑰 (5 分鐘)
# 訪問: https://platform.openai.com/api-keys

# 2. 運行設置精靈 (2 分鐘)
python setup_openai.py

# 3. 啟動應用 (1 分鐘)
streamlit run app.py

# 4. 測試它 (即時!)
# 訪問 http://localhost:8501

# 5. 部署給學生 (可選)
# 見 DEPLOYMENT.md
```

**就這麼簡單!** 💙

---

如有問題，參考:
- `GET_OPENAI_API_KEY.md` - API 金鑰詳細步驟
- `DEPLOYMENT.md` - 部署選項
- `QUICK_START.md` - 快速參考

讓我們一起幫助香港的學生！ 🇭🇰 💙
