from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

# create database connection
db = create_engine("sqlite:///database.db")

# create a base class for our models
Base = declarative_base()

# create the tables in the database
# Users table
class User(Base):
    __tablename__ = "users"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    email = Column("email", String, nullable=False)
    password = Column("password", String)
    active = Column("active", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, name, email, password, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin

# Orders table
class Order(Base):
    __tablename__ = "orders"

    # ORDER_STATUS = (
    #     ("PENDING", "PENDING"),
    #     ("COMPLETED", "COMPLETED"),
    #     ("CANCELLED", "CANCELLED")
    # )
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) # pending, completed, cancelled
    user_id = Column("user_id", Integer, ForeignKey("users.id"))
    price = Column("price", Float)
    # itens =

    def __init__(self, user_id, status="PENDING", price=0.0):
        self.status = status
        self.user_id = user_id
        self.price = price

# Itens table
class Item(Base):
    __tablename__ = "items"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantity = Column("quantity", Integer)
    flavor = Column("flavor", String)
    size = Column("size", String)
    unitary_price = Column("unitary_price", Float)
    order_id = Column("order_id", Integer, ForeignKey("orders.id"))

    def __init__(self, order_id, quantity, flavor, size, unitary_price=0.0):
        self.quantity = quantity
        self.flavor = flavor
        self.size = size
        self.unitary_price = unitary_price
        self.order_id = order_id

# execute metadata to create database
# run alembic revision  --autogenerate -m "Initial Migration" to create the migration file
# run alembic upgrade head to apply the migration and create the tables in the database