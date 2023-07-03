import uuid
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sql_app.database import Base

class ScenarioOperation(Base):
    __tablename__ = 'scenario_operations'
    __table_args__ = (UniqueConstraint('scenario_page_id', 'operation_id', 'order_no'),)

    id = Column(String(length=36), primary_key=True, index=True, default=str(uuid.uuid4()))
    project_id = Column(String(length=36), nullable=False)
    scenario_page_id = Column(String(length=36), nullable=False)
    operation_id = Column(String(length=36), nullable=False)
    order_no = Column(Integer, nullable=True)

    def __repr__(self):
        return f'<ScenarioOperation (name={self.id + self.order_no})>'