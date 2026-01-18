# ETF Flow Agent

Agent phân tích dòng tiền ETF BTC & ETH hằng ngày cho Warden Protocol.

## Endpoint
POST /inference

## Response format
Compatible with Warden Studio UI.

## Run local
```bash
pip install -r requirements.txt
uvicorn main:app --reload
