from sqlalchemy.orm import Session
from models import *
from schemas import *
from typing import List
from passlib.context import CryptContext


passwd_cotext = CryptContext(schemes=["sha256_crypt", "md5_crypt"])


def set_passwd(passwd: str) -> str:
    return passwd_cotext.hash(passwd)
        

def create_goods(db: Session, goods: GoodsCreate) -> GoodsResponse:
    db_goods = Goods(**goods.model_dump())
    db.add(db_goods)
    db.commit()
    db.refresh(db_goods)
    return db_goods


def get_commodity(db: Session, goods_id: int) -> GoodsResponse:
    db_goods = db.query(Goods).filter(Goods.id == goods_id).first()
    if db_goods:
        return db_goods
    return None


def get_goods(db: Session, skip: int = 0, limit: int = 100) -> List[GoodsResponse]:
    db_goods = db.query(Goods).offset(skip).limit(limit).all()
    return [goods for goods in db_goods]


def delete_goods(db: Session, goods_id: int) -> GoodsResponse:
    db_goods = db.query(Goods).filter(Goods.id == goods_id).first()
    if db_goods:
        db.delete(db_goods)
        db.commit()
        return db_goods
    return None


def create_order(db: Session, order: OrdersCreate) -> OrdersResponse:
    db_orders = Orders(**order.model_dump())
    db.add(db_orders)
    db.commit()
    db.refresh(db_orders)
    return db_orders


def get_order(db: Session, order_id: int) -> OrdersResponse:
    db_orders = db.query(Orders).filter(Orders.id == order_id).first
    if db_orders:
        return db_orders
    return None


def get_orders(db: Session, skip: int = 0, limit: int = 100) -> List[OrdersResponse]:
    db_orders = db.query(Orders).offset(skip).limit(limit).all()
    return [order for order in db_orders]


def delete_order(db: Session, order_id: int) -> OrdersResponse:
    db_order = db.query(Orders).filter(Orders.id == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
        return db_order
    return None


def create_client(db: Session, client: ClientsCreate) -> ClientsResponse:
    db_client = Clients(
        username = client.username,
        usersurname = client.usersurname,
        email = client.email,
        password = set_passwd(client.password)
        )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client
    



def get_client(db: Session, client_id: int) -> ClientsResponse:
    db_client = db.query(Clients).filter(Clients.id == client_id).first()
    if db_client:
        return db_client
    return None


def get_client_by_email(db: Session, email: str):
    return db.query(Clients).filter(Clients.email == email).first()


def get_clients(db: Session, skip: int = 0, limit: int = 100) -> List[ClientsResponse]:
    db_client = db.query(Clients).offset(skip).limit(limit).all()
    return [client for client in db_client]


def delete_client(db: Session, client_id: int) -> ClientsResponse:
    db_client = db.query(Clients).filter(Clients.id == client_id).first()
    if db_client:
        db.delete(db_client)
        db.commit()
        return db_client
    return None