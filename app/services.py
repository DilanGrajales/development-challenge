from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.models import Product, Sale
from app.schemas import Sales, SalesByProduct


# ***************** CRUD Services ***********************
async def get_all(model, schema, db: Session):
    objs = db.query(model).all()
    return list(map(schema.from_orm, objs))


async def get_by_id(id: int, model, schema, db: Session, msg: str):
    obj = db.query(model).filter(model.id == id).first()

    if not obj:
        return {'error': f'{msg} not found'}

    return schema.from_orm(obj)


async def create(data, model, db: Session, msg: str):
    try:
        obj = model(**data.dict())
        db.add(obj)
        db.commit()
        db.refresh(obj)

        return obj
    except Exception as e:
        print(e)
        return {'error': f'{msg} not created'}


async def update(id: int, data, model, db: Session, msg: str):
    obj = db.query(model).filter(model.id == id).one()

    if not obj:
        return {'error': f'{msg} not found'}

    try:
        obj_data = data.dict(exclude_unset=True)

        for key, value in obj_data.items():
            setattr(obj, key, value)

        db.add(obj)

        db.commit()
        db.refresh(obj)

        return obj_data
    except Exception as e:
        print(e)
        return {'error': f'{msg} not updated'}


async def delete(id: int, model, db: Session, msg):
    obj = db.query(model).filter(model.id == id).first()

    if not obj:
        return {'error': f'{msg} not found'}

    try:
        db.delete(obj)
        db.commit()

        return {'message': f'{msg} deleted successfully'}
    except Exception as e:
        print(e)
        return {'error': f'{msg} can not be deleted'}


# ***************** Sales Services ***********************
async def get_sales_by_product(db: Session):
    sales = db.query(
        Product.name.label('product'),
        func.sum(Sale.quantity).label('quantity'),
        func.sum(Product.price * Sale.quantity).label('amount')
    ).join(Product).group_by(Product.id).all()

    if not sales:
        return {'error': 'There are no sales yet'}

    return list(map(SalesByProduct.from_orm, sales))


async def get_all_sales(db: Session):
    sales = db.query(
        func.sum(Sale.quantity).label('quantity'),
        func.sum(Product.price * Sale.quantity).label('amount')
    ).join(Product).group_by().all()

    if not sales:
        return {'error': 'There are no sales yet'}

    return list(map(Sales.from_orm, sales))
