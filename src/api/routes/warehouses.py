from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.warehouse import Warehouse
from src.core.database import get_db

router = APIRouter()

@router.get("/warehouses")
async def get_warehouses(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Warehouse))
    warehouses = result.scalars().all()
    return warehouses
