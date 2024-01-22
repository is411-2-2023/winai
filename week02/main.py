from fastapi import FastAPI
from pydantic import BaseModel

class Tour(BaseModel):
    name: str
    destination: str
    price: float
    banner: str

app = FastAPI()

@app.post("/tour/")
async def create_tour(tour: Tour) -> Tour:
    print(tour)
    tour.price -= 10
    return tour

@app.get("/tours/")
async def read_all_tour() -> list[Tour]:
    return [
        Tour(name="Big buddha", destination="North", price=112.22, banner="Buddha.jpg"),
        Tour(name="Big monster", destination="South", price=1112.22, banner="Monster.jpg"),
    ]

@app.get("/tour/{tourId}")
async def read_tour(tourId: str):
    return {"tourId": tourId}