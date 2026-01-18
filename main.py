from fastapi import FastAPI
from etf_flow import fetch_etf_flow, analyze_trend

app = FastAPI(
    title="ETF Flow Agent",
    version="1.0.0"
)

@app.post("/inference")
def run_agent():
    flow = fetch_etf_flow()
    analysis = analyze_trend(flow)

    return {
        "status": "success",
        "data": {
            "title": "Daily ETF Flow Report",
            "summary": (
                f"BTC ETF Flow: {flow['btc'] / 1e6:.0f}M USD | "
                f"ETH ETF Flow: {flow['eth'] / 1e6:.0f}M USD | "
                f"Market Trend: {analysis['trend']}"
            ),
            "metrics": {
                "btc_etf_flow": f"{flow['btc'] / 1e6:.0f}M USD",
                "eth_etf_flow": f"{flow['eth'] / 1e6:.0f}M USD",
                "trend": analysis["trend"]
            },
            "confidence": analysis["confidence"],
            "updated_at": analysis["updated_at"]
        }
    }
