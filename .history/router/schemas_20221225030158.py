from pydantic import BaseModel, Field, validator, EmailStr
from typing import List, Optional

class RentRequestSchema(BaseModel):
    rentname: str
    rentcategory: str
    rentprice: str
    rentimg_url: str
    rentpicone_url: str
    rentpictwo_url: str
    rentpicthree_url: str
    rentintro: str
    teachintro: str
    area: str
    owner_id: int

class RentResponseSchema(RentRequestSchema):
    id: int
    owner_id: int
    class Config:
        orm_mode = True
class ActivityRequestSchema(BaseModel):
    eventname: str
    category: str
    eventbigimg_url: str
    eventpicone_url: str
    eventpictwo_url: str
    eventpicthree_url: str
    eventpicfour_url: str
    eventpicfive_url: str
    eventintro_first: str
    eventintro_second: str

class ActivityResponseSchema(ActivityRequestSchema):
    id: int
    class Config:
        orm_mode = True
        
class ProductRequestSchema(BaseModel):
    category: str
    name: str
    sku: str
    price: int
    image: str
    description: str
    description_long: str
    currency: str
    countInStock: int
    owner_id: int


class ProductResponseSchema(ProductRequestSchema):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_admin = False


class SignInRequestSchema(BaseModel):
    email: EmailStr
    password: str


class UpdateProfileRequestSchema(BaseModel):
    user_id: int
    username: str
    password: Optional[str]
    address: Optional[str]
    tel: str


class UserRequestSchema(UserBase):
    password: str

    @classmethod
    @validator("password")
    def password_must_have_6_digits(cls, v):
        if len(v) < 6:
            raise ValueError("Password must have at least 6 digits")
        return v


# class UserRequestSchema(UserBase):
#     password1: str
#     password2: str
#
#     @classmethod
#     @validator('password2')
#     def passwords_match(cls, v, values, **kwargs):
#         if 'password1' in values and v != values['password1']:
#             raise ValueError('passwords do not match')
#         return v
#
#     @classmethod
#     @validator("password1")
#     def password_must_have_6_digits(cls, v):
#         if len(v) < 6:
#             raise ValueError("Password must have at least 6 digits")
#         return v


class UserResponseSchema(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserSignInResponseSchema(BaseModel):
    access_token: str
    token_type: str = 'bearer'
    user_id: int
    username: str
    #address: str
    #tel: str


class ProductResponseWithUserSchema(ProductRequestSchema):
    id: int
    owner_id: int
    owner: UserResponseSchema

    class Config:
        orm_mode = True


class UserDetailResponseSchema(BaseModel):
    id: int
    address: Optional[str]
    tel: str
    owner_id: int

    class Config:
        orm_mode = True


class UserResponseWithProductsSchema(UserBase):
    id: int
    user_detail: UserDetailResponseSchema = None
    created_products: List[ProductResponseSchema]

    class Config:
        orm_mode = True
