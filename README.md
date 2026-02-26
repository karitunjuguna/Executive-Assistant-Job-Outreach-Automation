# Executive-Assistant-Job-Outreach-Automation

## Overview

This project automates the identification and qualification of remote Executive Assistant and Administrative Assistant roles, generates personalized outreach messages using an LLM, and stores structured results for downstream application workflows.

The objective is to simulate a scalable outbound job-application support pipeline for a founder-led team.

---

## System Architecture

The pipeline follows a modular structure:

1. **Scraping Layer**
   Collects job postings from We Work Remotely using Python and BeautifulSoup.

2. **Validation Layer**
   Filters postings based on:

   * Remote eligibility
   * Role relevance (Executive / Admin Assistant)
   * Keyword-based job qualification

3. **LLM Layer**
   Generates a personalized outreach message using OpenAI.

4. **Storage Layer**
   Saves validated jobs and generated messages to a structured CSV file that can be directly imported into Google Sheets.

---

## Project Structure

```
executive-assistant-outreach-automation/
│
├── main.py
├── scraper.py
├── filters.py
├── llm.py
├── storage.py
├── config.py
├── requirements.txt
├── output.csv
└── .gitignore
```

---

## How It Works

1. The scraper pulls job listings from We Work Remotely.
2. Each listing is parsed for title, company, description, and URL.
3. The validation module checks:

   * Remote status
   * Role alignment
   * Relevant administrative keywords
4. Qualified listings are passed to the LLM.
5. The LLM generates a tailored outreach message.
6. Results are appended to `output.csv`.

---

## Installation

### 1. Clone Repository

```
git clone https://github.com/YOUR_USERNAME/executive-assistant-outreach-automation.git
cd executive-assistant-outreach-automation
```

### 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate  (Mac/Linux)
venv\Scripts\activate     (Windows)
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key
```

---

## Running the Pipeline

```
python main.py
```

Upon execution:

* Job listings are scraped
* Relevant roles are filtered
* Outreach messages are generated
* Results are saved to `output.csv`

---

## Sample Output

`[output.csv]([url](https://docs.google.com/spreadsheets/d/18G9kcUlJ3-tQFhcoJSh7OjdBUcrJAnqXVtgqZfuRVI0/edit?gid=0#gid=0))` contains structured fields:

* Job Posting URL
* Job Title
* Company Name
* Location
* Job Description
* LLM Generated Outreach Message

This file can be uploaded directly into Google Sheets to serve as a review dashboard for a sales or recruiting team.

---

## Scheduling

For daily automation in production, use cron:

```
0 9 * * * /usr/bin/python3 /path/to/main.py
```

Or configure Windows Task Scheduler to run `python main.py` daily.

---

## Design Considerations

* Modular architecture for maintainability
* Easily adjustable keyword filters
* Interchangeable LLM prompt template
* CSV export for flexible dashboard integration
* Separation of scraping, filtering, intelligence, and storage concerns

---

## Future Improvements

* Add duplicate detection before writing output
* Add job scoring mechanism
* Expand to multiple job boards
* Deploy as a scheduled cloud function

---

## Conclusion

This project demonstrates a fully automated outbound job discovery and personalization workflow, integrating scraping, validation logic, AI-generated messaging, and structured storage.

