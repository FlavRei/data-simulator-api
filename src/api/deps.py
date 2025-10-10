from typing import AsyncGenerator
from src.core.database import get_db
from src.core.security import require_api_key

async def get_db_dep() -> AsyncGenerator:
    async for session in get_db():
        yield session

def get_api_key_dep():
    return require_api_key
