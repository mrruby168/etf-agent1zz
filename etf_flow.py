import requests
from datetime import datetime

def fetch_etf_flow():
    """
    Mock dữ liệu ETF Flow.
    Có thể thay bằng API CoinGlass / CryptoQuant sau.
    """
    return {
        "btc": 120_000_000,   # +120M USD
        "eth": -15_000_000   # -15M USD
    }

def analyze_trend(flow):
    score = 0
    if flow["btc"] > 0:
        score += 1
    if flow["eth"] > 0:
        score += 1

    if score == 2:
        trend = "Strong Bullish"
        confidence = 0.85
    elif score == 1:
        trend = "Bullish"
        confidence = 0.7
    else:
        trend = "Bearish"
        confidence = 0.6

    return {
        "trend": trend,
        "confidence": confidence,
        "updated_at": datetime.utcnow().strftime("%Y-%m-%d")
    }
