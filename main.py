from fastapi import FastAPI, Request

app = FastAPI(
    title="ETF Flow Intelligence Agent",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "status": "ok",
        "agent": "ETF Flow Intelligence Agent"
    }

@app.post("/inference")
async def inference(request: Request):
    return {
        "status": "success",
        "signal": {
            "title": "Daily ETF Flow Report",
            "summary": "BTC ETF inflow, ETH outflow, market bias bullish",
            "confidence": 0.7,
            "bias": "Bullish",
            "metrics": {
                "btc_etf_flow": "120M USD",
                "eth_etf_flow": "-15M USD"
            }
        }
    }
