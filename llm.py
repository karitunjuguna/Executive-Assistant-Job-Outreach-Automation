from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

PROMPT_TEMPLATE = """
You are writing a personalized outreach message for an Executive Assistant role.

Job Title: {title}
Company: {company}

Job Description:
{description}

Write a concise, professional outreach message expressing strong alignment and interest.
"""

def generate_message(job):
    prompt = PROMPT_TEMPLATE.format(
        title=job["title"],
        company=job["company"],
        description=job["description"][:1500]
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
