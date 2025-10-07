from fastapi import Header, HTTPException, Depends
from src.core.config import settings

async def require_api_key(x_api_key: str = Header(None)):
    if not settings.REQUIRE_API_KEY:
        return True
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")
    return True
