from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ex.db_con import SessionLocal
from ex.models import User, Product, Order

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ex.schemas import UserGet, ProductGet, OrderGet
import logging

app = FastAPI()

def get_db():
    with SessionLocal() as db:
        return db


#@app.get("/")
#def say_hello():
 #   return "hello123"

# CRUD USER
@app.get("/users/all", response_model=List[UserGet])
def get_all_users( db: Session = Depends(get_db)):
   return db.query(User).all()

@app.post("/users/")
def create_user(first_name: str, last_name: str, address: str, email: str, db: Session = Depends(get_db)):
    try:
        user = User(first_name=first_name, last_name=last_name, address=address, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        logging.info(f"Added new user: {user.first_name}  {user.last_name}")
        return {"status": "success", "note": user}
    except Exception as e:
        logging.error(f"Error while adding user: {e}")
        raise HTTPException(status_code=500, detail="Error adding user")
@app.put("/users/{user_id}")
def update_user(user_id: int, first_name: str, last_name: str, address: str, email: str, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        user.first_name = first_name
        user.last_name = last_name
        user.address = address
        user.email = email
        db.commit()
        logging.info(f"Updated user: {user.first_name}  {user.last_name}")
        return {"status": "success", "note": user}
    except Exception as e:
        logging.error(f"Error while updating user: {e}")
        raise HTTPException(status_code=500, detail="Error updating user")
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        db.delete(user)
        db.commit()
        logging.info(f"Deleted user: {user.first_name}  {user.last_name}")
        return {"message": "User deleted successfully"}
    except Exception as e:
        logging.error(f"Error while deleting user: {e}")
        raise HTTPException(status_code=500, detail="Error deleting user")

# CRUD PRODUCT

@app.get("/products/all", response_model=List[ProductGet])
def get_all_products( db: Session = Depends(get_db)):
   return db.query(Product).all()

@app.post("/products/")
def create_product(name: str, description: str, price: int, db: Session = Depends(get_db)):
    try:
        product = Product(name=name,  description=description, price=price)
        db.add(product)
        db.commit()
        db.refresh(product)
        logging.info(f"Created product: {product.first_name}  {product.last_name}")
        return {"status": "success", "note": product}
    except Exception as e:
        logging.error(f"Error while creating product: {e}")
        raise HTTPException(status_code=500, detail="Error creating product")

@app.put("/products/{product_id}")
def update_product(product_id: int, name: str, description: str, price: int, db: Session = Depends(get_db)):
    try:
        product = db.query(Product).filter(Product.id == product_id).first()
        product.name = name
        product.description = description
        product.price = price
        db.commit()
        logging.info(f"Updated product: {product.first_name}  {product.last_name}")
        return {"status": "success", "note": product}
    except Exception as e:
        logging.error(f"Error while updating product: {e}")
        raise HTTPException(status_code=500, detail="Error updating product")
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    try:
        product = db.query(Product).filter(Product.id == product_id).first()
        db.delete(product)
        db.commit()
        logging.info(f"Deleted product: {product.first_name}  {product.last_name}")
        return {"message": "Product deleted successfully"}
    except Exception as e:
        logging.error(f"Error while deleting product: {e}")
        raise HTTPException(status_code=500, detail="Error deleting product")
# CRUD ORDER


@app.get("/orders/all", response_model=List[OrderGet])
def get_all_orders( db: Session = Depends(get_db)):
   return db.query(Order).all()

@app.post("/orders/")
def create_order(user_id: int, product_ordered: int, total_paid: int, db: Session = Depends(get_db)):
    try:
        order = Order(user_id=user_id,  product_ordered=product_ordered, total_paid=total_paid)
        db.add(order)
        db.commit()
        db.refresh(order)
        return {"status": "success", "note": order}
    except Exception as e:
        logging.error(f"Error while creating order: {e}")
        raise HTTPException(status_code=500, detail="Error creating order")
@app.put("/orders/{order_id}")
def update_order(order_id: int, user_id: int, product_ordered: int, total_paid: int, db: Session = Depends(get_db)):
    try:
        order = db.query(Order).filter(Order.id == order_id).first()
        order.user_id = user_id
        order.product_ordered = product_ordered
        order.total_paid = total_paid
        db.commit()
        logging.info(f"Updated order: {order.first_name}  {order.last_name}")
        return {"status": "success", "note": order}
    except Exception as e:
        logging.error(f"Error while updating order: {e}")
        raise HTTPException(status_code=500, detail="Error updating order")
@app.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    try:
        order = db.query(Order).filter(Order.id == order_id).first()
        db.delete(order)
        db.commit()
        logging.info(f"Deleted order: {order.first_name}  {order.last_name}")
        return {"message": "Order deleted successfully"}
    except Exception as e:
        logging.error(f"Error while deleting order: {e}")
        raise HTTPException(status_code=500, detail="Error deleting order")

logging.basicConfig(level=logging.INFO)
