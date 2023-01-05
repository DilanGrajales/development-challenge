from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import UnitMeasure
from app.schemas import UnitOfMeasurement, UnitOfMeasurementCreate
from app.services import (
    get_all,
    get_by_id,
    create,
    update,
    delete
)


router = APIRouter(
    prefix="/unit-measure",
    tags=["Unit Measure"]
)

model = UnitMeasure
schema = UnitOfMeasurement
msg = 'Product'


@router.get('/')
async def get_all_unit_measures(db: Session = Depends(get_db)):
    return await get_all(model=model, schema=schema, db=db)


@router.get('/{id}')
async def get_unit_measure_by_id(id: int, db: Session = Depends(get_db)):
    return await get_by_id(id=id, model=model, schema=schema, db=db, msg=msg)


@router.post('/')
async def create_unit_measure(unit_measure: UnitOfMeasurementCreate, db: Session = Depends(get_db)):
    return await create(data=unit_measure, model=model, db=db, msg=msg)


@router.put('/{id}')
async def update_unit_measure(id: int, unit_measure: UnitOfMeasurementCreate, db: Session = Depends(get_db)):
    return await update(id=id, data=unit_measure, model=model, db=db, msg=msg)


@router.delete('/{id}')
async def delete_unit_measure(id: int, db: Session = Depends(get_db)):
    return await delete(id=id, model=model, db=db, msg=msg)
