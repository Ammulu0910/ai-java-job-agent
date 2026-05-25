from playwright.sync_api import sync_playwright
from app.matcher.job_filter import is_java_job
from app.database.crud import save_job
from app.matcher.job_filter import (
        is_java_job,
        calculate_job_score
    )

def scrape_jobs():

    jobs_data = []

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        
        page.goto(
            
            "https://remoteok.com/remote-java-jobs",
            timeout=60000,
            wait_until="domcontentloaded"
        )
        page.wait_for_timeout(5000)
        jobs = page.locator("tr.job[data-id]")
        count = jobs.count()
        

        for i in range(min(count, 5)):

            try:

                job = jobs.nth(i)

                title = job.locator("h2").text_content()
                title = title.strip()
               
                company = job.locator(
                    "h3[itemprop='name']"
                ).inner_text()
                company = company.strip()
                link = job.locator("a").first.get_attribute("href")

                print("Checking title:", title)

                if is_java_job(title):

                    print("Matched Java Job")

                    job_info = {
                        "role": title,
                        "company": company,
                        "link": f"https://remoteok.com{link}",
                        "score": calculate_job_score(title)
                    }

                    save_job(job_info)

                    jobs_data.append(job_info)

                else:

                    print("Skipped:", title)

            except Exception:

                continue

        browser.close()

    return jobs_data