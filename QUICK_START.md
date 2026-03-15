# 🚀 快速開始指南 | Quick Start Guide

## 一分鐘快速啟動 | Start in 1 minute

### 選項 1：直接運行 | Option 1: Direct Run
```bash
# 1. 進入項目目錄 | Go to project directory
cd emotional_support_website

# 2. 安裝依賴 (只需一次) | Install dependencies (one time)
pip install -r requirements.txt

# 3. 啟動應用 | Start the app
streamlit run app.py
```

✅ **應用將在 http://localhost:8501 開啟**

---

### 選項 2：使用快速啟動批次文件 | Option 2: Batch File
雙擊 `start.bat` 文件即可自動完成所有設置並啟動應用程序。

---

### 選項 3：使用 Docker | Option 3: Docker
```bash
docker-compose up
```
然後訪問 http://localhost:8501

---

## 功能簡介 | Features at a Glance

| 功能 | 描述 |
|------|------|
| 💬 AI 聊天 | 24/7 情感支持 |
| 🆘 Crisis Resources | 即時求助熱線 |
| 🛡️ 危機檢測 | 自動識別風險 |
| 🌐 雙語支持 | 中文/英文 |

---

## 部署到網絡 | Deploy Online

### 使用 Streamlit Cloud (推薦)
1. 登錄 https://streamlit.io
2. 連接 GitHub 倉庫
3. 選擇此應用並部署
4. 分享 URL 給學生

### 使用 Heroku
```bash
# 需要 Procfile 和 setup.sh
```

### 使用 AWS/Azure
參考 README.md 中的詳細說明

---

## 文件說明 | File Structure

```
emotional_support_website/
├── app.py                  ← 主應用程序
├── ai_assistant.py         ← AI 邏輯
├── ai_assistant_advanced.py ← 進階功能
├── resources.py            ← 資源配置
├── requirements.txt        ← 依賴列表
├── start.bat              ← Windows 快速啟動
├── Dockerfile             ← Docker 配置
├── docker-compose.yml     ← Docker Compose
└── README.md              ← 完整文檔
```

---

## 自定義 | Customization

### 添加新的求助資源
編輯 `resources.py` 並在 `CRISIS_RESOURCES` 中添加：

```python
"Your Country": {
    "name": "Country Name",
    "resources": [
        {
            "name": "Hotline Name",
            "phone": "XXX-XXX-XXXX",
            "hours": "Available Hours"
        }
    ]
}
```

### 修改 AI 回應
編輯 `ai_assistant.py` 中的 `supportive_responses` 字典。

### 更改動機和顏色
編輯 `app.py` 中的 CSS 部分（在 markdown 標籤中）。

---

## 故障排除 | Troubleshooting

### 問題：模塊未找到
```bash
pip install -r requirements.txt
```

### 問題：端口已被占用
```bash
streamlit run app.py --server.port 8502
```

### 問題：中文顯示亂碼
確保你使用 UTF-8 編碼的編輯器

---

## 聯絡與支持 | Contact & Support

- 📧 有問題或建議？提交 Issue
- 🤝 想要貢獻？發送 Pull Request
- 💙 記住：你的支持可以拯救生命

---

**祝你好運！Keep supporting students! 💙**
