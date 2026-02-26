import requests
from bs4 import BeautifulSoup

SEARCH_URLS = [
    "https://weworkremotely.com/remote-jobs/search?term=executive+assistant",
    "https://weworkremotely.com/remote-jobs/search?term=admin+assistant"
]

def scrape_jobs():
    jobs = []

    for url in SEARCH_URLS:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        listings = soup.select("section.jobs li")

        for listing in listings:
            try:
                title = listing.select_one("span.title").text.strip()
                company = listing.select_one("span.company").text.strip()
                location = listing.select_one("span.region.company").text.strip()
                job_url = "https://weworkremotely.com" + listing.find("a")["href"]

                job_description = fetch_job_description(job_url)

                jobs.append({
                    "title": title,
                    "company": company,
                    "location": location,
                    "description": job_description,
                    "url": job_url
                })

            except Exception:
                continue

    return jobs


def fetch_job_description(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    description_section = soup.select_one("div.listing-container")
    return description_section.text.strip() if description_section else ""
