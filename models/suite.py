from sqlalchemy import Column, String
from sql_app.database import Base

class Suite(Base):
    __tablename__ = 'suites'
    id=Column(String, primary_key=True, index=True)
    project_id=Column(String, nullable=False)
    name=Column(String(length=50), unique=True, primary_key=True, index=True)
    