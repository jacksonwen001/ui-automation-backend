import datetime
import uuid
from sqlalchemy import Column, DateTime, String
from sql_app.database import Base

class Page(Base):
    __tablename__ = 'pages'
    id = Column('id', String(length=36), primary_key=True, index=True, default=str(uuid.uuid4()))
    project_id = Column('project_id', String(length=26), nullable=False)
    name = Column(String(length=50), unique=True, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    def __repr__(self):
        return f'<Page(name={self.name})>'



    