import datetime
import uuid
from sqlalchemy import Column, DateTime, String, Text, UniqueConstraint
from sql_app.database import Base

class PageElement(Base):
    __tablename__ = 'page_elements'
    __table_args__ = (UniqueConstraint('page_id', 'name'),)

    id = Column(String(length=36), primary_key=True, index=True, default=str(uuid.uuid4()))
    project_id = Column(String(length=36), nullable=False)
    page_id = Column(String(length=36), nullable=False)
    name = Column(String(length=50), nullable=False)
    selector = Column(String(length=20), nullable=False)
    target = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    def __repr__(self):
            return f'<PageElement (name={self.name})>'

    