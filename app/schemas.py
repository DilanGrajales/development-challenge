from pydantic import BaseModel
from decimal import Decimal


class UnitOfMeasurementCreate(BaseModel):
    unit_measure: str
    name: str

    class Config:
        orm_mode = True


class UnitOfMeasurement(BaseModel):
    id: int
    unit_measure: str
    name: str

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    name: str
    price: Decimal
    unit_measure_id: int

    class Config:
        orm_mode = True


class Product(BaseModel):
    id: int
    name: str
    price: Decimal
    unit_measure_id: int

    class Config:
        orm_mode = True


class SaleCreate(BaseModel):
    product_id: int
    quantity: int

    class Config:
        orm_mode = True


class SalesByProduct(BaseModel):
    product: str
    quantity: int
    amount: Decimal

    class Config:
        orm_mode = True


class Sales(BaseModel):
    quantity: int
    amount: Decimal

    class Config:
        orm_mode = True
