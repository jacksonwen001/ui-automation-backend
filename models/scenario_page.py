import uuid
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sql_app.database import Base

class ScenarioPage(Base):
    __tablename__ = 'scenario_pages'
    __table_args__ = (UniqueConstraint('scenario_id', 'order_no'),)

    id = Column(String(length=36), primary_key=True, index=True, default=str(uuid.uuid4()))
    project_id = Column(String(length=36), nullable=False)
    scenario_id = Column(String(length=36), nullable=False)
    page_id = Column(String(length=36), nullable=False)
    order_no = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<ScenarioPage (name={self.id + self.order_no})>'