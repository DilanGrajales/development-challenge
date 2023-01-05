from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Sale
from app.schemas import SaleCreate
from app.services import create, get_all_sales, get_sales_by_product


router = APIRouter(
    prefix='/sale',
    tags=['Sale']
)

model = Sale
schema = SaleCreate
msg = 'Sale'


@router.post('/')
async def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    if not sale.quantity:
        sale.quantity = 1
    return await create(data=sale, model=model, db=db, msg=msg)


@router.get('/products/')
async def get_sales_of_each_product(db: Session = Depends(get_db)):
    return await get_sales_by_product(db=db)


@router.get('/all')
async def get_sales(db: Session = Depends(get_db)):
    return await get_all_sales(db=db)
