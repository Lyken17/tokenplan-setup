import os
from openai import OpenAI

API_KEY = os.getenv("SORUXGPT_CLAUDE_AUTH_TOKEN")
BASE_URL = "https://ai.soruxgpt.com/v1"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

prompt = "Say a short story in one short sentence."

# model="claude-opus-4-7"
# model="claude-opus-4-8"
# model="claude-opus-5"
# model="claude-fable-5"


response = client.chat.completions.create(
    model="claude-opus-5",
    messages=[
        {"role": "user", "content": prompt},
    ],
)

print(response.choices[0].message.content)