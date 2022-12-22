from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from router.schemas import ActivityRequestSchema, ActivityResponseSchema
from db.database import get_db
from db import db_activity
from typing import List

router = APIRouter(
    prefix='/api/v1/products',
    tags=['products']
)


@router.post('', response_model=ActivityResponseSchema)
def create_activity(request: ActivityRequestSchema, db: Session = Depends(get_db)):
    return db_activity.create(db=db, request=request)


@router.get('/feed', response_model=List[ActivityResponseSchema])
def feed_initial_products(db: Session = Depends(get_db)):
    return db_activity.db_feed(db)


@router.get('/all', response_model=List[ActivityResponseSchema])
def get_all_activities(db: Session = Depends(get_db)):
    return db_activity.get_all(db)

@router.get("/{category}", response_model=List[ActivityResponseSchema])
def get_activity_by_category(category: str, db: Session = Depends(get_db)):
    return db_activity.get_activity_by_category(category=category, db=db)
