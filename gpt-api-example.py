import os
from openai import OpenAI

API_KEY = os.getenv("SORUXGPT_GPT_AUTH_TOKEN")
BASE_URL = "https://ai.soruxgpt.com/v1"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

prompt = "Say a short story in one short sentence."

# model="gpt-5.6-sol"
# model="gpt-5.6-luna"
# model="gpt-5.6-terra"

response = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[
        {"role": "user", "content": prompt},
    ],
)

print(response.choices[0].message.content)