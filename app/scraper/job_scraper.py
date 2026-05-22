from playwright.sync_api import sync_playwright
from app.matcher.job_filter import is_java_job
from app.database.crud import save_job

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

        jobs = page.locator("tr.job")

        count = jobs.count()

        for i in range(min(count, 5)):

            try:

                job = jobs.nth(i)

                title = job.locator("h2").inner_text()

                company = job.locator(
                    "h3[itemprop='name']"
                ).inner_text()

                link = job.locator("a").first.get_attribute("href")

                # if is_java_job(title):

                #     job_info = {
                #         "role": title,
                #         "company": company,
                #         "link": f"https://remoteok.com{link}"
                #     }
                #     save_job(job_info)
                #     jobs_data.append(job_info)
                print("Checking title:", title)

                if is_java_job(title):

                    print("Matched Java Job")

                    job_info = {
                        "role": title,
                        "company": company,
                        "link": f"https://remoteok.com{link}"
                    }

                    save_job(job_info)

                    jobs_data.append(job_info)

                else:

                    print("Skipped:", title)

            except Exception:

                continue

        browser.close()

    return jobs_data