from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.core.config import settings
from src.core.database import engine, Base
from src.api.routes import deliveries, vehicles, carriers, warehouses, simulation

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title=settings.APP_NAME, version="1.0.0", lifespan=lifespan)

app.include_router(deliveries.router)
app.include_router(vehicles.router)
app.include_router(carriers.router)
app.include_router(warehouses.router)
app.include_router(simulation.router)
