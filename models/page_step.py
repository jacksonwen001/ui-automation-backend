import uuid
from sqlalchemy import Column, Integer, String, Text, UniqueConstraint
from sql_app.database import Base


class PageStep(Base):
    __tablename__ = 'page_steps'
    __table_args__ = (UniqueConstraint('operation_id', 'order_no'),)
    
    id = Column(String(length=36), primary_key=True, index=True, default=str(uuid.uuid4()))
    project_id = Column(String(length=36), nullable=False)
    page_id = Column(String(length=36), nullable=False)
    operation_id = Column(String(length=36), nullable=False)
    command = Column(String(100), nullable=False)
    element_id = Column(String(length=36), nullable=True)
    value = Column(Text, nullable=True)
    order_no = Column(Integer, nullable=False)


    def __repr__(self):
        return f'<PageStep(name={self.command + self.order_no})>'


class PageStepView:
    id = Column(String(length=36))