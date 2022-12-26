from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from router.schemas import RentRequestSchema, RentResponseSchema #ProductResponseWithUserSchema
from db.database import get_db
from db import db_rent
from typing import List

router = APIRouter(
    prefix='/api/v1/rents',
    tags=['rents']
)


@router.post('', response_model=RentResponseSchema)
def create_rent(request: RentRequestSchema, db: Session = Depends(get_db)):
    return db_rent.create(db=db, request=request)


@router.get('/feed', response_model=List[RentResponseSchema])
def feed_initial_rents(db: Session = Depends(get_db)):
    return db_rent.db_feed(db)


@router.get('/all', response_model=List[RentResponseSchema])
def get_all_rents(db: Session = Depends(get_db)):
    return db_rent.get_all(db)


#@router.get('/id/{product_id}', response_model=RentResponseWithUserSchema)
#def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
#    return db_product.get_product_by_id(product_id=product_id, db=db)


@router.get("/{category}", response_model=List[RentResponseSchema])
def get_rent_by_category(category: str, db: Session = Depends(get_db)):
    return db_rent.get_product_by_category(category=category, db=db)
