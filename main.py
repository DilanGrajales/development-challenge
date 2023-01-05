from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.routers.unit_measure import unit_measure
from app.routers.product import product
from app.routers.sale import sale


Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    ".up.railway.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(unit_measure.router)
app.include_router(product.router)
app.include_router(sale.router)
