from fastapi import FastAPI
from app.scraper.job_scraper import scrape_jobs

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "AI Java Job Agent Running Successfully"
    }


@app.get("/jobs")
def get_jobs():

    jobs = scrape_jobs()

    return jobs