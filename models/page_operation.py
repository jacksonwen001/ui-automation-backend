import datetime
import uuid
from sqlalchemy import Column, DateTime, String
from sql_app.database import Base

class PageOperation(Base):
    __tablename__ = 'page_operations'
    id=Column(String(length=36), primary_key=True, index=True, default=str(uuid.uuid4()))
    project_id=Column(String(length=36), nullable=False)
    page_id=Column(String(length=36), nullable=False)
    name=Column(String(length=50), unique=True)
    created_at=Column(DateTime, nullable=False, default=datetime.datetime.now)
    def __repr__(self):
        return f'<PageOperation (name={self.name})>'



    