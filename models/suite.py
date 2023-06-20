import datetime
import uuid
from sqlalchemy import Column, String
from sql_app.database import Base

class Suite(Base):
    __tablename__ = 'suites'
    id = Column(String(length=36), primary_key=True, index=True, default=str(uuid.uuid4()))
    project_id = Column(String(length=36), nullable=False)
    name = Column(String(length=50), unique=True, primary_key=True, index=True)
    created_at = Column(datetime, default=datetime.datetime.now)
    