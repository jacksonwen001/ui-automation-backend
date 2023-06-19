from sqlalchemy import Column, String
from sql_app.database import Base


class SuiteGroup(Base):
    __tablename__ = 'suite_groups'
    id=Column(String, primary_key=True, index=True)
    project_id=Column(String, nullable=False)
    suite_id=Column(String, nullable=False)
    group_id=Column(String, nullable=False)
    position=Column(String, nullable=False)

    