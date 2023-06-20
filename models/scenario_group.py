import uuid
from sqlalchemy import Column, Integer, String
from sql_app.database import Base

class ScenarioGroup(Base):
    __tablename__ = 'scenario_groups'
    id = Column(String(length=36), primary_key=True, index=True, default=str(uuid.uuid4()))
    project_id = Column(String(length=36), nullable=False)
    group_id = Column(String(length=36), nullable=False)
    scenario_id = Column(String(length=36), nullable=False)
    order_no = Column(Integer, nullable=False)

    


    