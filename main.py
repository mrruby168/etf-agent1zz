from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "ETF Agent is running"}

@app.get("/inference")
def inference_get():
    return {
        "info": "Use POST method with JSON body {} to run inference"
    }

@app.post("/inference")
def inference():
    return {
        "status": "success",
        "data": {
            "title": "Daily ETF Flow Report",
            "summary": "BTC ETF Flow: 120M USD | ETH ETF Flow: -15M USD | Market Trend: Bullish",
            "metrics": {
                "btc_etf_flow": "120M USD",
                "eth_etf_flow": "-15M USD",
                "trend": "Bullish"
            },
            "confidence": 0.7,
            "updated_at": "2026-01-18"
        }
    }
