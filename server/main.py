from fastapi import FastAPI
from server.models import Account

app = FastAPI()

@app.get("/health")
async def health_check():
    return { "Status": "I'm alive." }

@app.post("/account")
async def post_user(account: Account):
    return account