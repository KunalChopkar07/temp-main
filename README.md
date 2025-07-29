# 📈 Jesse FastAPI Indicators API

This project is a FastAPI backend for exposing over **100+ trading indicators** (many from [Jesse](https://jesse.trade/)) via API endpoints. You can fetch real-time indicator values using Binance candle data for any symbol, interval, and lookback.

---

## 🚀 Features

✅ Real-time indicator calculation  
✅ Uses `Jesse` library for indicator logic  
✅ Async support with FastAPI  
✅ Easily extendable — add your own indicators  
✅ Compatible with TradingView-style indicators

---

## 🛠️ Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Your requirements.txt should include:
```bash
fastapi
uvicorn
jesse
numpy
requests
```
If using .env for secrets or proxies, also add:
```bash
python-dotenv
```
---
## 📁 Project Structure
```bash
temp-main/
│
├── indicators/                   # Contains all individual indicator .py files
│   ├── sma.py
│   ├── rsi.py
│   ├── volume24h.py
│   └── ...
│
├── models/
│   └── indicator_request.py      # Pydantic request models for each endpoint
│
├── services/
│   └── binance_service.py        # Candle fetching logic from Binance
│
├── main.py                       # FastAPI app with all indicator routes
└── README.md                     # ← This file
```
---
## ▶️ Running the API

### 1. Activate your virtual environment:
```bash
& "venv/Scripts/Activate.ps1"  # PowerShell (Windows)
```
Or (Linux/macOS):
```bash
source venv/bin/activate
```
### 2. Start the FastAPI server:
---
```bash
uvicorn main:app --reload
```
### 3. Open in browser:
---
```bash
http://127.0.0.1:8000/docs
```
##### ✅ Swagger UI will appear with all available endpoints.
---
## 📬 Example API Request

Endpoint:
```bash
POST /sma
```
Body:
```bash
{
  "symbol": "BTCUSDT",
  "interval": "1m",
  "limit": 100,
  "period": 14
}
```
---
## ➕ Adding New Indicators

1. Create a new Python file in indicators/ (e.g., my_indicator.py)

2. Implement calculate_my_indicator(candles) in that file

3. Add an endpoint in main.py:
```bash
@app.post("/my_indicator")
async def get_my_indicator(data: IndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = calculate_my_indicator(candles, data.period)
    return result
```

4. Add a Pydantic model in models/indicator_request.py if the endpoint requires custom parameters
---
## 📚 References
- Jesse Indicators

- FastAPI Documentation

- Binance Spot API
---
## 👨‍💻 Author
#### Made by Kunal Chopkar
---


