from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from server.utils.access_guard import AccessGuard

app_public = APIRouter()
access_guard = AccessGuard()

@app_public.get("/health")
async def health_check():
    return { "Status": "I'm alive." }

@app_public.post("/token")
async def login(passwordRequestForm: OAuth2PasswordRequestForm = Depends()):
    userInfo = {"username": passwordRequestForm.username, "password": passwordRequestForm.password}
    # check if use is valid
    token = access_guard.createToken(userInfo)
    return {"access_token": token}
