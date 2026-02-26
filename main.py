import schedule
import time
from scraper import scrape_jobs
from filters import validate_job
from llm import generate_message
from sheets import connect_sheet, save_job


def run_pipeline():
    print("Starting job pipeline...")

    jobs = scrape_jobs()
    sheet = connect_sheet()

    for job in jobs:
        if validate_job(job):
            message = generate_message(job)
            save_job(sheet, job, message)

    print("Pipeline complete.")


schedule.every().day.at("09:00").do(run_pipeline)

if __name__ == "__main__":
    run_pipeline()

    while True:
        schedule.run_pending()
        time.sleep(60)
