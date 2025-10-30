from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from models import Product, Sale, SaleItem, Client, Pet
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Regras de negócio
LOW_STOCK_THRESHOLD = 10
LOW_ACTIVITY_DAYS = 30   # produtos sem venda no período
BEST_SELLER_DAYS = 30
CONSUMPTION_DAYS = 180

@router.get("/low-stock")
def low_stock_products(db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.stock <= LOW_STOCK_THRESHOLD).all()
    return products

@router.get("/low-activity")
def low_activity_products(db: Session = Depends(get_db)):
    date_limit = datetime.now() - timedelta(days=LOW_ACTIVITY_DAYS)

    # Produtos vendidos no período
    active_products = db.query(SaleItem.product_id).join(Sale).filter(
        Sale.date >= date_limit
    ).distinct()

    # Produtos que NÃO aparecem no período
    inactive = db.query(Product).filter(
        Product.id.not_in(active_products)
    ).all()

    return inactive

from sqlalchemy import func

@router.get("/best-sellers")
def best_sellers(db: Session = Depends(get_db)):
    date_limit = datetime.now() - timedelta(days=BEST_SELLER_DAYS)

    results = db.query(
        Product.name,
        func.sum(SaleItem.quantity).label("total_sold")
    ).join(Sale).join(Product).filter(
        Sale.date >= date_limit
    ).group_by(Product.id).order_by(func.sum(SaleItem.quantity).desc()).limit(10).all()

    return results

@router.get("/consumption-patterns")
def consumption_patterns(db: Session = Depends(get_db)):
    date_limit = datetime.now() - timedelta(days=CONSUMPTION_DAYS)

    results = db.query(
        Client.name.label("client"),
        Pet.name.label("pet"),
        Product.name.label("product"),
        func.sum(SaleItem.quantity).label("qty")
    ).join(Sale, Sale.client_id == Client.id)\
     .join(SaleItem, SaleItem.sale_id == Sale.id)\
     .join(Product, Product.id == SaleItem.product_id)\
     .join(Pet, Pet.owner_id == Client.id)\
     .filter(Sale.date >= date_limit)\
     .group_by(Client.id, Pet.id, Product.id)\
     .order_by(func.sum(SaleItem.quantity).desc())\
     .all()

    return results