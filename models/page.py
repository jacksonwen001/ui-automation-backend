import datetime
import uuid
from sqlalchemy import Column, DateTime, String, UniqueConstraint
from sql_app.database import Base

class Page(Base):
    __tablename__ = 'pages'
    __table_args__ = (UniqueConstraint('project_id', 'name'),)
    
    id = Column('id', String(length=36), primary_key=True, index=True, default=str(uuid.uuid4()))
    project_id = Column('project_id', String(length=36), nullable=False)
    name = Column(String(length=50), unique=True, index=True)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    def __repr__(self):
        return f'<Page(name={self.name})>'



    