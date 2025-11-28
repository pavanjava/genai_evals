import os

from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SYSTEM_PROMPT = """
You are a helpful assistant. I will provide a movie review and you will classify it as either positive or negative.
Please respond with "positive" or "negative" only.
"""


def trigger_openai(prompt: str):
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1000
    )
    response = (
        response.choices[0].message.content.strip()
        if response.choices[0].message.content
        else ""
    )
    return response


def trigger_claude(prompt: str):
    client = Anthropic()

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1000,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )
    print(message.content)
