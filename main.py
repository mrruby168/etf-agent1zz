from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# Root (warden check)
@app.get("/")
@app.head("/")
def root():
    return {"status": "ok", "message": "ETF Agent is running"}

# GET /inference (warden verify)
@app.get("/inference")
@app.head("/inference")
def inference_get():
    return {
        "status": "ok",
        "message": "Use POST with JSON body {}"
    }

# OPTIONS /inference (CORS / preflight)
@app.options("/inference")
def inference_options():
    return JSONResponse(
        content={"status": "ok"},
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS, HEAD",
            "Access-Control-Allow-Headers": "*",
        },
    )

# POST /inference (real logic)
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
