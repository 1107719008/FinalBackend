from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey


class DbProduct(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    sku = Column(String(30))
    price = Column(Integer, nullable=False)
    image = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    description_long = Column(String(255), nullable=True)
    currency = Column(String(10))
    countInStock = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship('DbUser', back_populates='created_products')


class DbUserDetail(Base):
    __tablename__ = 'user_detail'
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String(255))
    tel = Column(String(30))
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner_info = relationship("DbUser", back_populates='user_detail')


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False, nullable=True)
    created_products = relationship('DbProduct', back_populates='owner')
    user_detail = relationship('DbUserDetail', back_populates="owner_info", uselist=False)

class DbActivity(Base):
    __tablename__ = 'activity'
    id = Column(Integer, primary_key=True, index=True)
    Limg_url = Column(String(255), nullable=False)
    sone_img_url = Column(String(255), nullable=False)
    stwo_img_url = Column(String(255), nullable=False)
    sthree_img_url = Column(String(255), nullable=False)
    sfour_img_url = Column(String(255), nullable=False)
    sfive_img_url = Column(String(255), nullable=False)
    intro_first = Column(String(255), nullable=False)
    intro_second = Column(String(255), nullable=False)
