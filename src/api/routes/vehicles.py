from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from src.api.deps import get_db_dep, get_api_key_dep
from src.models.vehicle import Vehicle

router = APIRouter(prefix="/vehicles", tags=["Vehicles"], dependencies=[Depends(get_api_key_dep())])

@router.get("/", response_model=List[dict])
async def list_vehicles(limit: int = Query(100, le=1000), db: AsyncSession = Depends(get_db_dep)):
    stmt = select(Vehicle).limit(limit)
    result = await db.execute(stmt)
    rows = result.scalars().all()
    return rows
