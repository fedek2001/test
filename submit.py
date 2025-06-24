from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.post("/api/submit")
async def proxy(request: Request):
    body = await request.json()
    r = requests.post(
        "https://mhxnojvd97.execute-api.us-east-1.amazonaws.com/prod/submit",
        json=body
    )
    return r.json()
