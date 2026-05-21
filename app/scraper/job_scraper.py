from playwright.sync_api import sync_playwright


def scrape_jobs():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        print("Opening website...")

        page.goto(
            "https://example.com",
            timeout=60000
        )

        print("Website opened successfully")

        title = page.title()

        print("Website Title:", title)

        input("Press Enter to close browser...")

        browser.close()


scrape_jobs()