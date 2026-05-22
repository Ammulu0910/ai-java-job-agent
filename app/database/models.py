from sqlalchemy import Column, Integer, String
from app.database.base import Base


class Job(Base):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    role = Column(String, nullable=False)

    company = Column(String, nullable=False)

    link = Column(String, unique=True, nullable=False)