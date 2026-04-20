from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")  #  IMPORTANT
)

def get_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  #  according to your deployment
        messages=messages
    )
    return response.choices[0].message.content