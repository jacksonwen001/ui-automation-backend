import uuid
from sqlalchemy import Column, DateTime, String
from sql_app.database import Base

class Scenario(Base):
    __tablename__ = 'scenarios'
    id=Column(String(length=36), primary_key=True, index=True, default=str(uuid.uuid4()))
    project_id=Column(String(length=36), nullable=False)
    name=Column(String(length=50), unique=True, primary_key=True, index=True)
    created_at=Column(DateTime, nullable=False)

    def __repr__(self):
            return f'<Scenario (name={self.name})>'


    