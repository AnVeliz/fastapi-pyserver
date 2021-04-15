from fastapi import APIRouter

app_public = APIRouter()

@app_public.get("/health")
async def health_check():
    return { "Status": "I'm alive." }