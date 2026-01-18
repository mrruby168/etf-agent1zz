from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.api_route("/", methods=["GET", "HEAD"])
def root():
    return {"status": "ok", "message": "ETF Agent is running"}

@app.api_route("/inference", methods=["GET", "HEAD"])
def inference_get():
    return {
        "status": "ok",
        "message": "Use POST with JSON body {}"
    }

@app.api_route("/inference", methods=["OPTIONS"])
def inference_options():
    return JSONResponse(
        content={"status": "ok"},
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS, HEAD",
            "Access-Control-Allow-Headers": "*",
        },
    )

@app.api_route("/inference", methods=["POST"])
def inference_post():
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
