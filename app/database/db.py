from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:0745@localhost:5432/ai_job_agent"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
from app.database.base import Base
from app.database.models import Job

Base.metadata.create_all(bind=engine)