from sqlalchemy import Boolean, Column, Integer, String
from sql_app.database import Base


class SuiteGroup(Base):
    __tablename__ = 'suite_groups'
    id=Column(String(length=36), primary_key=True, index=True)
    project_id=Column(String(length=36), nullable=False)
    suite_id=Column(String(length=36), nullable=False)
    group_id=Column(String(length=36), nullable=False)
    position=Column(String(length=10), nullable=False)
    is_order=Column(Boolean, default=False, nullable=False)
    order_no=Column(Integer, nullable=True)

    

    