from app.db.database import Base
from sqlalchemy import *


class UnitMeasure(Base):
    __tablename__ = "unit_measures"

    id = Column(Integer, Identity(start=1, cycle=True), primary_key=True)
    unit_measure = Column(String(10), nullable=False)
    name = Column(String(30), nullable=False)
    
    
class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, Identity(start=1, cycle=True), primary_key=True)
    name = Column(String(30), nullable=False)
    price = Column(DECIMAL, nullable=False)
    unit_measure_id = Column(Integer, ForeignKey("unit_measures.id"), nullable=False)
    
    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, unit_measure_id={self.unit_measure_id})"


class Sale(Base):
    __tablename__ = "sales"
    
    id = Column(Integer, Identity(start=1, cycle=True), primary_key=True)
    date = Column(DateTime, nullable=False, server_default=func.now())
    quantity = Column(Integer, nullable=False, default=1)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)