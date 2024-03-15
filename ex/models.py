from sqlalchemy import TIMESTAMP, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ex.db_con import Base, SessionLocal, engine


class User(Base):
    __tablename__ = "users"
    #__table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, index=True, name="user_id")
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    email = Column(String)

class Product(Base):
    __tablename__ = "products"
   # __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, index=True,  name="product_id")
    name = Column(String, name="product_name")
    description = Column(String)
    price = Column(Integer)


class Order(Base):
    __tablename__ = "orders"
   # __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, index=True, name="order_id")
    user_id = Column(
        Integer, ForeignKey("users.user_id"), primary_key=True, name="user_id"
    )
    user = relationship("User", cascade="all, delete-orphan", single_parent=True)
    product_ordered = Column(
        Integer, ForeignKey("products.product_id"), primary_key=True
    )
    product= relationship("Product", cascade="all, delete-orphan", single_parent=True)
    total_paid = Column(Integer)


if __name__ == "__main__":
    session = SessionLocal()
