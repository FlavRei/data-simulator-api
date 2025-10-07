from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from src.api.deps import get_db_dep, get_api_key_dep
from src.models.carrier import Carrier

router = APIRouter(prefix="/carriers", tags=["Carriers"], dependencies=[Depends(get_api_key_dep())])

@router.get("/", response_model=List[dict])
async def list_carriers(db: AsyncSession = Depends(get_db_dep)):
    stmt = select(Carrier)
    result = await db.execute(stmt)
    rows = result.scalars().all()
    return rows
