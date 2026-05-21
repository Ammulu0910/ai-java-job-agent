from fastapi import FastAPI
from app.scraper.job_data import jobs

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "AI Java Job Agent Running Successfully"
    }

@app.get("/jobs")
def get_jobs():
    return jobs