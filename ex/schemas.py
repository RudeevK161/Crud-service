import datetime
from typing import Optional

from pydantic import BaseModel, Field   # импортировали нужные библиотеки


class UserGet(BaseModel):
    id: int
    first_name: str = ""
    last_name: str = ""
    address: str = ""
    email: str = ""

    class Config:
        orm_mode = True

class ProductGet(BaseModel):
    id: int
    name: str = ""
    description: str = ""
    price: int

    class Config:
        orm_mode = True

class OrderGet(BaseModel):
    id: int
    user_idr: UserGet
    product_ordered: ProductGet
    total_paid: int

    class Config:
        orm_mode = True
