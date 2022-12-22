from fastapi import HTTPException, status
#from router.schemas import ProductRequestSchema
from sqlalchemy import func
from sqlalchemy.orm.session import Session
from .activities_feed import activitiess
import time
from db.models import DbActivity


def db_feed(db: Session):
    new_activity_list = [DbActivity(
        category=product["category"],
        name=product["name"],
        sku=product["sku"],
        price=product["price"],
        image=product["image"],
        description=product["description"],
        description_long=product["description_long"],
        currency=product["currency"],
        countInStock=product["countInStock"],
        owner_id=product["owner_id"]
    ) for product in products]
    db.query(DbActivity).delete()
    db.commit()
    db.add_all(new_activity_list)
    db.commit()
    return db.query(DbActivity).all()


def create(db: Session, request: ProductRequestSchema) -> DbActivity:
    new_product = DbActivity(
        category=request.category,
        name=request.name,
        sku=request.sku,
        price=request.price,
        image=request.image,
        description=request.description,
        description_long=request.description_long,
        currency=request.currency,
        countInStock=request.countInStock,
        owner_id=request.owner_id
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def get_all(db: Session) -> list[DbActivity]:
    # time.sleep(10)
    return db.query(DbActivity).all()


def get_product_by_id(activity_id: int, db: Session) -> DbActivity:
    # time.sleep(10)
    activity = db.query(DbActivity).filter(DbActivity.id == activity_id).first()
    if not activity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Activity with id = {activity_id} not found')
    return activity

#類別
def get_product_by_category(category: str, db: Session) -> list[DbActivity]:
    # time.sleep(2)
    activity = db.query(DbActivity).filter(func.upper(DbActivity.category) == category.upper()).all()
    if not activity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'activity with category = {category} not found')
    return activity
