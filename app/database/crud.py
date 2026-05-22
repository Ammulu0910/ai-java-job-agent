from app.database.db import SessionLocal
from app.database.models import Job


def save_job(job_data):

   

    db = SessionLocal()

    existing_job = db.query(Job).filter(
        Job.link == job_data["link"]
    ).first()

    if existing_job:

        
        db.close()

        return

    new_job = Job(
        role=job_data["role"],
        company=job_data["company"],
        link=job_data["link"]
    )

    db.add(new_job)

    db.commit()

   

    db.close()