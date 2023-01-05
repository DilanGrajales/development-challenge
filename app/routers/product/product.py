from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Product
from app.schemas import ProductCreate, Product as ProductSchema
from app.services import (
    get_all,
    get_by_id,
    create,
    update,
    delete
)


router = APIRouter(
    prefix='/product',
    tags=['Product']
)

model = Product
schema = ProductSchema
msg = 'Product'


@router.get('/')
async def get_all_products(db: Session = Depends(get_db)):
    return await get_all(model=model, schema=schema, db=db)


@router.get('/{id}')
async def get_product_by_id(id: int, db: Session = Depends(get_db)):
    return await get_by_id(id=id, model=model, schema=schema, db=db, msg=msg)


@router.post('/')
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return await create(data=product, model=model, db=db, msg=msg)


@router.put('/{id}')
async def update_product(id: int, product: ProductCreate, db: Session = Depends(get_db)):
    return await update(id=id, data=product, model=model, db=db, msg=msg)


@router.delete('/{id}')
async def delete_product(id: int, db: Session = Depends(get_db)):
    return await delete(id=id, model=model, db=db, msg=msg)
