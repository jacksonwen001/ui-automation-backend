import datetime
from typing import Annotated
import uuid
from sqlalchemy import Column, DateTime, String
from sql_app.database import Base

class Project(Base):
    __tablename__ = 'projects'
    id = Column('id', String(length=36), primary_key=True, index=True, default=str(uuid.uuid4()))
    name = Column('name', String(length=50), unique=True, index=True)
    created_at = Column('created_at', DateTime, nullable=False, default=datetime.datetime.now())

    def __repr__(self):
        return f'<Project(name={self.name})>'


    