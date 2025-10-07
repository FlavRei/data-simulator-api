from fastapi import FastAPI
from src.data_generator import generate_deliveries

app = FastAPI(
    title="Logistics Data Simulator API",
    description="API simulant des données de livraison (camions, distances, retards, etc.)",
    version="1.0.0",
)

@app.get("/deliveries")
def get_deliveries(count: int = 10):
    """
    Retourne une liste simulée de livraisons.
    """
    data = generate_deliveries(count)
    return {"deliveries": data, "count": len(data)}

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API de simulation de données logistiques !"}
