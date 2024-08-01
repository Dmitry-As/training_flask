from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Goods(Base):
    __tablename__ = 'goods'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), index=True)
    definition = Column(String(256), index=True)
    price = Column(Float)
    
    orders = relationship('Orders', back_populates='goods')


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    goods_id = Column(Integer, ForeignKey('goods.id'))
    order_date = Column(DateTime)
    status = Column(String(20), index=True)

    goods = relationship('Goods', back_populates='orders')
    clients = relationship('Clients', back_populates='orders')
    

class Clients(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(48), index=True)
    usersurname = Column(String(48), index=True)
    email = Column(String(128), unique=True, index=True)
    password = Column(String(128))
    
    orders = relationship('Orders', back_populates='clients')    