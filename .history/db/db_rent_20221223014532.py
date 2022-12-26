from fastapi import HTTPException, status
from router.schemas import RentRequestSchema
from sqlalchemy import func
from sqlalchemy.orm.session import Session
from .rents_feed import rents
import time
from db.models import DbRent


def db_feed(db: Session):
    new_rent_list = [DbRent(
        rentname=rent["rentname"],
        rentcategory=rent["rentcategory"],
        rentprice=rent["rentprice"],
        rentimg_url=rent["rentpicone_url"],
        rentpicone_url=rent["rentpicone_url"],
        rentpictwo_url=rent["rentpictwo_url"],
        rentpicthree_url=rent["rentpicthree_url"],
        rentintro=rent["rentintrot"],
        teachintro=rent["teachintro"],
        area=rent["area"],
        owner_id=rent["owner_id"]
    ) for rent in rents]
    db.query(DbRent).delete()
    db.commit()
    db.add_all(new_rent_list)
    db.commit()
    return db.query(DbRent).all()


def create(db: Session, request: RentRequestSchema) -> DbRent:
    new_rent = DbRent(
        rentname=request.rentname,
        rentcategory=request.rentcategory,
        rentprice=request.rentprice,
        rentimg_url=request.rentimg_url,
        rentpicone_url=request.rentpicone_url,
        rentpictwo_url=request.rentpictwo_url,
        rentpicthree_url=request.rentpicthree_url,
        rentintro=request.rentintro,
        teachintro=request. teachintro,
        owner_id=request.owner_id
    )
    db.add(new_rent)
    db.commit()
    db.refresh(new_rent)
    return new_rent


def get_all(db: Session) -> list[DbRent]:
    # time.sleep(10)
    return db.query(DbRent).all()


def get_rent_by_id(rent_id: int, db: Session) -> DbRent:
    # time.sleep(10)
    rent = db.query(DbRent).filter(DbRent.id == rent_id).first()
    if not rent:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Rent with id = {rent_id} not found')
    return rent

#類別
def get_rent_by_category(category: str, db: Session) -> list[DbRent]:
    # time.sleep(2)
    rent = db.query(DbRent).filter(func.upper(DbRent.category) == category.upper()).all()
    if not rent:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'rent with category = {category} not found')
    return rent
