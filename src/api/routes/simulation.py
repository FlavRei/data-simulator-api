from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.services.generator import generate_carriers, generate_vehicles, generate_warehouses, generate_deliveries

router = APIRouter(prefix="/simulate", tags=["Simulation"])

@router.post("/")
async def simulate_all(db: AsyncSession = Depends(get_db), carriers: int = 5, vehicles: int = 15, warehouses: int = 10, deliveries: int = 50):
    # Génération des données liées
    carriers_list = generate_carriers(carriers)
    vehicles_list = generate_vehicles(carriers_list, vehicles)
    warehouses_list = generate_warehouses(warehouses)
    deliveries_list = generate_deliveries(vehicles_list, warehouses_list, deliveries)

    db.add_all(carriers_list + vehicles_list + warehouses_list + deliveries_list)
    await db.commit()

    return {
        "carriers": len(carriers_list),
        "vehicles": len(vehicles_list),
        "warehouses": len(warehouses_list),
        "deliveries": len(deliveries_list)
    }
