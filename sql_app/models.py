from sqlalchemy import Boolean, Column, Integer, String, Text
from .database import Base

class User(Base): 
    __tablename__ = "users"
    id = Column('id', Integer, primary_key=True, index=True)
    email = Column(String(length=50), unique=True, index=True)
    hashed_password = Column(Text)
    age = Column(Integer)
    is_active = Column(Boolean, default=True)