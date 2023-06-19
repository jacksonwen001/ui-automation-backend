import uuid
from sqlalchemy import Column, Integer, String, Text
from sql_app.database import Base


class PageStep(Base):
    id = Column(String(length=36), primary_key=True, index=True, default=str(uuid.uuid4()))
    project_id = Column(String(length=36), nullable=False)
    page_id = Column(String(length=36), nullable=False)
    operation_id = Column(String(length=36), nullable=False)
    command = Column(String(100), nullable=False)
    element_id = Column(String(length=36), nullable=True)
    step_values = Column(Text, nullable=True)
    order_no = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<PageStep(name={self.command + self.order_no})>'