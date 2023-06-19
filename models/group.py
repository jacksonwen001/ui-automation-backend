import uuid
from sqlalchemy import Column, String
from sql_app.database import Base

class Group(Base):
    __tablename__ = 'groups'
    id=Column(String(length=36), primary_key=True, index=True, default=str(uuid.uuid4()))
    project_id=Column(String(length=36), nullable=False)
    name=Column(String(length=50), unique=True, primary_key=True, index=True)

    def __repr__(self):
            return f'<Group (name={self.name})>'

    