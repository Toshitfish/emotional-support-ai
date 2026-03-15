# 💙 情緒支持平臺 - Emotional Support Website

一個為學生提供情緒支持和防止自殺干預的網站，**使用真實 AI！**  
A website providing emotional support and suicide prevention intervention for students, **powered by real AI!**

## 🚀 Now with Real AI (Claude)

✨ **智能分析** - 不再是簡單的關鍵詞匹配，真正理解學生的處境  
✨ **個性化支持** - 根據具體情況給出針對性的建議  
✨ **自然對話** - 像與真人諮詢師交談一樣  
✨ **記憶對話** - AI 記住對話歷史，提供連貫的支持  

[詳細了解 → 查看 CLAUDE_AI_GUIDE.md](CLAUDE_AI_GUIDE.md)

## 功能 | Features

✅ **AI 聊天助手** - 24/7 情緒支持  
✅ **Crisis 資源** - 立即求助按鈕和熱線號碼  
✅ **匿名聊天** - 安全私密的環境  
✅ **多語言支持** - 中文和英文  
✅ **即時危機檢測** - 自動識別危機情況並提供幫助  

## 快速開始 | Quick Start

### 安裝依賴 | Install Dependencies

```bash
pip install -r requirements.txt
```

### 運行應用 | Run the Application

```bash
streamlit run app.py
```

應用將在 `http://localhost:8501` 開啟

## 項目結構 | Project Structure

```
emotional_support_website/
├── app.py                 # 主應用 | Main Streamlit app
├── ai_assistant.py       # AI助手邏輯 | AI assistant logic
├── requirements.txt      # 依賴 | Dependencies
└── README.md            # 本文件 | This file
```

## 特性詳解 | Feature Details

### 1. AI 助手 (ai_assistant.py)

- **情感分析** - 檢測用戶的情緒狀態
- **危機檢測** - 識別可能的自殺傾向或自害行為
- **個性化回應** - 根據檢測到的情感提供支持
- **資源推薦** - 建議專業幫助

### 2. 網頁介面 (app.py)

- **聊天界面** - 簡單直觀的對話框
- **側邊欄資源** - 香港、台灣等地的求助熱線
- **聊天歷史** - 保存對話記錄用於支持
- **安全警告** - 重要的免責聲明和安全提示

### 3. 危機干預

當檢測到以下關鍵詞時，系統會立即提供緊急幫助：
- 自殺相關詞彙
- 自害相關詞彙
- 絕望相關詞彙

## 求助資源 | Crisis Resources

### 香港 | Hong Kong
- **撒瑪利亞防止撥款會**: 2389 2222 (24小時)
- **生命熱線**: lifelinecentre@samaritans.org.hk
- **WhatsApp**: +852 5162 0000

### 台灣 | Taiwan
- **安心專線**: 1925 (24小時)
- **安心講 APP**: 用於文字諮詢

### 中國大陸 | Mainland China
- **全國心理援助熱線**: 400-161-9995

## 未來改進 | Future Enhancements

🔄 **計畫中的功能**:
- [ ] 更先進的NLP模型集成
- [ ] 用戶反饋系統
- [ ] 心理健康資源庫
- [ ] 匿名用戶群體支持功能
- [ ] 專業心理治療師推薦系統
- [ ] 多語言支持擴展
- [ ] 情感追蹤數據分析（用於改進）

## 重要提示 | Important Notes

⚠️ **此平台不是專業醫療服務的替代品**
- This platform is NOT a replacement for professional medical services
- 如有嚴重心理健康問題，請立即尋求專業幫助
- 所有敏感信息應被視為匿名
- 請定期與心理健康專業人士進行諮詢

## 部署 | Deployment

### 本地運行 | Local Deployment
```bash
streamlit run app.py
```

### Streamlit Cloud 部署 | Deploy on Streamlit Cloud
1. 將代碼推送到 GitHub
2. 登錄 streamlit.io
3. 創建新應用，選擇您的 GitHub 倉庫
4. 設置 app.py 作為主文件

### Docker 部署 | Docker Deployment
```bash
docker build -t emotional-support .
docker run -p 8501:8501 emotional-support
```

## 貢獻 | Contributing

我們歡迎貢獻！請通過以下方式參與：
- 報告 Bug
- 提建議改進
- 添加新的求助資源
- 改進AI響應邏輯

## 許可 | License

MIT License - 自由使用和修改

## 聯絡方式 | Contact

如有任何問題或建議，請聯絡項目維護者。

---

**記住：你並不孤獨。💙**  
**Remember: You are not alone. 💙**
