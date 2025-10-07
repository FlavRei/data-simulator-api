from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional
from src.api.deps import get_db_dep, get_api_key_dep
from src.models.delivery import Delivery
from src.schemas.delivery import DeliveryOut
from src.services.generator import generate_deliveries_batch

router = APIRouter(prefix="/deliveries", tags=["Deliveries"], dependencies=[Depends(get_api_key_dep())])

@router.post("/simulate", summary="Génère et insère des livraisons simulées")
async def simulate_deliveries(count: int = Query(10, ge=1, le=1000), db: AsyncSession = Depends(get_db_dep)):
    deliveries = generate_deliveries_batch(count)
    objs = [Delivery(**d) for d in deliveries]
    db.add_all(objs)
    await db.commit()
    return {"inserted": len(objs)}

@router.get("/", response_model=List[DeliveryOut], summary="Liste des livraisons (filtrable)")
async def list_deliveries(
    status: Optional[str] = Query(None),
    carrier: Optional[str] = Query(None),
    limit: int = Query(100, le=1000),
    db: AsyncSession = Depends(get_db_dep)
):
    stmt = select(Delivery)
    if status:
        stmt = stmt.where(Delivery.status == status)
    if carrier:
        stmt = stmt.where(Delivery.carrier == carrier)
    stmt = stmt.limit(limit)
    result = await db.execute(stmt)
    rows = result.scalars().all()
    return rows

@router.get("/{delivery_id}", response_model=DeliveryOut, summary="Récupérer une livraison par id")
async def get_delivery(delivery_id: str, db: AsyncSession = Depends(get_db_dep)):
    stmt = select(Delivery).where(Delivery.delivery_id == delivery_id)
    result = await db.execute(stmt)
    obj = result.scalar_one_or_none()
    if not obj:
        raise HTTPException(status_code=404, detail="Delivery not found")
    return obj
