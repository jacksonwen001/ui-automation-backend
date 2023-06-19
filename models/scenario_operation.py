import uuid
from sqlalchemy import Column, String
from sql_app.database import Base

class ScenarioPageOperation(Base):
    __tablename__ = 'scenario_page_operations'
    id=Column(String(length=36), primary_key=True, index=True, default=str(uuid.uuid4()))
    project_id=Column(String(length=36), nullable=False)
    scenario_page_id=Column(String(length=36), nullable=False)
    operation_id=Column(String(length=36), nullable=False)
    