from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.delivery import Delivery
from src.core.database import get_db

router = APIRouter()

@router.get("/deliveries")
async def get_deliveries(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Delivery))
    deliveries = result.scalars().all()
    return deliveries
