from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete
from src.core.database import get_db
from src.models.carrier import Carrier
from src.models.vehicle import Vehicle
from src.models.warehouse import Warehouse
from src.models.delivery import Delivery

router = APIRouter(prefix="/reset", tags=["Reset"])

@router.post("/")
async def reset_all_data(db: AsyncSession = Depends(get_db)):
    try:
        # Supprimer les données dans le bon ordre pour éviter les conflits FK
        await db.execute(delete(Delivery))
        await db.execute(delete(Vehicle))
        await db.execute(delete(Carrier))
        await db.execute(delete(Warehouse))
        await db.commit()
        return {"status": "success", "message": "All data has been deleted"}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
