from fastapi import HTTPException, status
#from router.schemas import ActivityRequestSchema
from sqlalchemy import func
from sqlalchemy.orm.session import Session
#from .activities_feed import activities
import time
from db.models import DbActivity


def db_feed(db: Session):
    new_activity_list = [DbActivity(
        eventname=activity["eventname"],
        category=activity["category"],
        eventbigimg_url=activity["eventbigimg_url"],
        eventpicone_url=activity["eventpicone_url"],
        eventpictwo_url=activity["eventpictwo_url"],
        eventpicthree_url=activity["eventpicthree_url"],
        eventpicfour_url=activity["eventpicfour_url"],
        eventpicfive_url=activity["eventpicfive_url"],
        eventintro_first=activity["eventintro_first"],
        eventintro_second=activity["eventintro_second"],
        #owner_id=activity["owner_id"]
    ) for activity in activities]
    db.query(DbActivity).delete()
    db.commit()
    db.add_all(new_activity_list)
    db.commit()
    return db.query(DbActivity).all()


def create(db: Session, request: ActivityRequestSchema) -> DbActivity:
    new_activity = DbActivity(
        eventname=request.eventname,
        category=request.category,
        eventbigimg_url=request.eventbigimg_url,
        eventpicone_url=request.eventpicone_url,
        eventpictwo_url=request.eventpictwo_url,
        eventpicthree_url=request.eventpicthree_url,
        eventpicfour_url=request.eventpicfour_url,
        eventpicfive_url=request.eventpicfive_url,
        eventintro_first=request.eventintro_first,
        eventintro_second=request. eventintro_second,
        #owner_id=request.owner_id
    )
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)
    return new_activity


def get_all(db: Session) -> list[DbActivity]:
    # time.sleep(10)
    return db.query(DbActivity).all()


def get_activity_by_id(activity_id: int, db: Session) -> DbActivity:
    # time.sleep(10)
    activity = db.query(DbActivity).filter(DbActivity.id == activity_id).first()
    if not activity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Activity with id = {activity_id} not found')
    return activity

#類別
def get_activity_by_category(category: str, db: Session) -> list[DbActivity]:
    # time.sleep(2)
    activity = db.query(DbActivity).filter(func.upper(DbActivity.category) == category.upper()).all()
    if not activity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'activity with category = {category} not found')
    return activity
