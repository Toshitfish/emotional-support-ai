# 部署指南 | Deployment Guide

## 本地部署 | Local Deployment

### Windows 用戶
1. 下載項目
2. 雙擊 `start.bat`
3. 等待瀏覽器自動打開

### Mac/Linux 用戶
```bash
chmod +x start.sh
./start.sh
```

---

## 遠程部署 | Remote Deployment

### 1. Streamlit Cloud (最簡單) ⭐⭐⭐⭐⭐

**優點：**
- 完全免費
- 自動更新
- 無需管理服務器
- 一鍵部署

**步驟：**
```bash
# 1. 將代碼推送到 GitHub
git add .
git commit -m "Initial commit"
git push origin main

# 2. 訪問 https://streamlit.io
# 3. 登錄 GitHub 帳號
# 4. 點擊 "New app"
# 5. 選擇 Repository 和 app.py
# 6. 部署！
```

---

### 2. Docker + Heroku

**先決條件：**
- Heroku 帳號
- Docker 已安裝
- Heroku CLI 已安裝

```bash
# 1. 登錄 Heroku
heroku login

# 2. 創建應用
heroku create your-emotional-support-app

# 3. 設置容器
heroku container:push web

# 4. 發布
heroku container:release web

# 5. 打開應用
heroku open
```

---

### 3. AWS EC2

**步驟：**
```bash
# 1. 啟動 EC2 實例（Ubuntu）
# 2. SSH 進去
ssh -i your-key.pem ubuntu@ec2-instance

# 3. 安裝 Python 和 pip
sudo apt update
sudo apt install python3-pip

# 4. 克隆倉庫
git clone your-repo-url
cd emotional_support_website

# 5. 安裝依賴
pip install -r requirements.txt

# 6. 在後台運行
nohup streamlit run app.py &
```

---

### 4. Docker Compose（推薦用於學校 IT）

```bash
# 構建
docker-compose build

# 運行
docker-compose up -d

# 停止
docker-compose down
```

---

## 安全建議 | Security Recommendations

### 1. 隱私保護
- [ ] 不保存用戶信息
- [ ] 使用 HTTPS
- [ ] 定期刪除日誌

### 2. 備份
```bash
# 自動備份重要資源
# 在 cron job 中運行
0 2 * * * tar -czf backup_$(date +\%Y\%m\%d).tar.gz /app
```

### 3. 監控
- 設置錯誤日誌監控
- 定期檢查應用狀態
- 設置告警機制

---

## 性能優化 | Performance

### 1. 緩存設置
```python
@st.cache_resource
def load_model():
    return EmotionalSupportAssistant()
```

### 2. 數據庫優化
- 使用 SQLite 或 PostgreSQL 存儲日誌
- 定期清理舊數據
- 建立索引

### 3. CDN
- 將靜態資源放在 CDN 上
- 使用圖片優化

---

## 監控和日誌 | Monitoring & Logging

### Streamlit 日誌
```bash
streamlit run app.py --logger.level=debug
```

### 將日誌寫入文件
```python
import logging
logging.basicConfig(filename='app.log', level=logging.INFO)
```

---

## 自動化 CI/CD | CI/CD Pipeline

### GitHub Actions (推薦)

創建 `.github/workflows/deploy.yml`:
```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Streamlit Cloud
        run: |
          # 配置 Streamlit Cloud 部署
```

---

## 定價對比 | Pricing Comparison

| 平台 | 成本 | 推薦度 |
|------|------|--------|
| Streamlit Cloud | 免費 | ⭐⭐⭐⭐⭐ |
| Heroku | 7-50 USD/月 | ⭐⭐⭐⭐ |
| AWS | 按使用付費 | ⭐⭐⭐ |
| Google Cloud | 按使用付費 | ⭐⭐⭐ |
| 自建服務器 | 50-200 USD/月 | ⭐⭐ |

---

## 故障排除 | Troubleshooting

### 應用崩潰
1. 檢查日誌
2. 驗證依賴版本
3. 計算資源

### 緩慢响應
1. 優化代碼
2. 增加服務器資源
3. 使用緩存

### 連接問題
1. 檢查網絡
2. 驗證防火牆
3. 確認 DNS

---

## 維護清單 | Maintenance Checklist

- [ ] 每週檢查應用日誌
- [ ] 每月更新資源
- [ ] 每季度進行安全審計
- [ ] 定期備份數據
- [ ] 監控服務器性能
- [ ] 更新依賴包
- [ ] 測試新功能

---

## 聯絡支持 | Support

遇到部署問題？
1. 檢查 README.md
2. 查看常見問題
3. 提交 GitHub Issue

💙 **祝部署順利！**
