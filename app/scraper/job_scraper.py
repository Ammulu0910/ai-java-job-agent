from playwright.sync_api import sync_playwright


def scrape_jobs():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        print("Opening RemoteOK...")

        page.goto(
            "https://remoteok.com/remote-java-jobs",
            timeout=60000
        )

        print("Website loaded successfully")

        job_titles = page.locator("tr.job h2")

        companies = page.locator("h3[itemprop='name']")

        title_count = job_titles.count()

        company_count = companies.count()

        print(f"Total Titles Found: {title_count}")
        print(f"Total Companies Found: {company_count}")

        total = min(title_count, company_count, 5)

        for i in range(total):

            title = job_titles.nth(i).inner_text()

            company = companies.nth(i).inner_text()

            print("----------------------")
            print("Role:", title)
            print("Company:", company)

        input("Press Enter to close browser...")

        browser.close()


scrape_jobs()