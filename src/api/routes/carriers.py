from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.carrier import Carrier
from src.core.database import get_db

router = APIRouter()

@router.get("/carriers")
async def get_carriers(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Carrier))
    carriers = result.scalars().all()
    return carriers
