from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class GoodsBase(BaseModel):
    name: str
    definition: Optional[str] = None
    price: float


class GoodsCreate(GoodsBase):
    pass


class GoodsResponse(GoodsBase):
    id: int
    
    class Config:
        model_config = {
            'from_attributes': True
        }


class OrdersBase(BaseModel):
    client_id: int
    goods_id: int
    order_date: datetime
    status: str


class OrdersCreate(OrdersBase):
    pass


class OrdersResponse(OrdersBase):
    id: int
    
    class Config:
        model_config = {
            'from_attributes': True
        }


class ClientsBase(BaseModel):
    username: str
    usersurname: str
    email: str

    
class ClientsCreate(ClientsBase):    
    password: str = Field(..., min_length=8)


class ClientsResponse(ClientsBase):
    id: int

    class Config:
        model_config = {
            'from_attributes': True
        }    