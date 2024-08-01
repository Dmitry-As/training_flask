from fastapi import Depends, FastAPI, HTTPException, Path
from sqlalchemy.orm import Session
from crud import *
from models import *
from schemas import *
from database import SessionLocal, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def welcome():
    return {'msg': 'Welcome'}


@app.post('/clients/', response_model=ClientsResponse)
def create_client_ep(client: ClientsCreate, db: Session = Depends(get_db)):
    db_client = get_client_by_email(db, email=client.email)
    if db_client:
        raise HTTPException(status_code=400, detail='Email alredy exists')
    return create_client(db=db, client=client)


@app.get('/clients/', response_model=List[ClientsResponse])
def read_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_clients(db=db, skip=skip, limit=limit)

@app.get('/clients/{client_id}', response_model=ClientsResponse)
def read_data(client_id: int = Path(..., ge=1), db: Session = Depends(get_db)):
    db_client = get_client(db=db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail='Client not found')
    return db_client


@app.delete('/clients/{client_id}', response_model=ClientsResponse)
def delete_client_ep(client_id: int = Path(..., ge=1), db: Session = Depends(get_db)):
    db_client = delete_client(db=db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail='Client not found')
    return db_client


@app.post('/goods/', response_model=GoodsResponse)
def create_goods_ep(goods: GoodsCreate, db: Session = Depends(get_db)):
    return create_goods(db=db, goods=goods)


@app.get('/goods/', response_model=List[GoodsResponse])
def read_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_goods(db=db, skip=skip, limit=limit)


@app.get('/goods/{goods_id}', response_model=GoodsResponse)
def read_data(goods_id: int = Path(..., ge=1), db: Session = Depends(get_db)):
    db_goods = get_commodity(db=db, goods_id=goods_id)
    if db_goods is None:
        raise HTTPException(status_code=404, detail='Commodity not found')
    return db_goods


@app.delete('/goods/{goods_id}', response_model=GoodsResponse)
def delete_goods_ep(goods_id: int = Path(..., ge=1), db: Session = Depends(get_db)):
    db_goods = delete_goods(db=db, goods_id=goods_id)
    if db_goods is None:
        raise HTTPException(status_code=404, detail='Commodity not found')
    return db_goods


@app.post('/orders/', response_model=OrdersResponse)
def create_order_ep(order: OrdersCreate, db: Session = Depends(get_db)):
    return create_order(db=db, order=order)


@app.get('/orders/', response_model=List[OrdersResponse])
def read_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_orders(db=db, skip=skip, limit=limit)


@app.get('/orders/{order_id}', response_model=OrdersResponse)
def read_data(order_id: int = Path(..., ge=1), db: Session = Depends(get_db)):
    db_orders = get_order(db=db, order_id=order_id)
    if db_orders is None:
        raise HTTPException(status_code=404, detail='Order not found')
    return db_orders


@app.delete('/orders/{order_id}', response_model=OrdersResponse)
def delete_order_ep(order_id: int = Path(..., ge=1), db: Session = Depends(get_db)):
    db_orders = delete_order(db=db, order_id=order_id)
    if db_orders is None:
        raise HTTPException(status_code=404, detail='Order not found')
    return db_orders