# from openai import OpenAI
# import os
# from dotenv import load_dotenv

# load_dotenv()

# #client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# client = OpenAI(
#     #api_key=os.getenv("OPENAI_API_KEY"),
#     api_key="gl-U2FsdGVkX1+7FEHPAObTqppC4DUGIFEs6HLv4d1LHIOHpmeHF56DjtjaHtSORCK2",

#     base_url="https://aibe.mygreatlearning.com/openai/v1"
# )

# def get_response(messages):
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=messages
#     )
#     return response.choices[0].message.content

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")  # ✅ IMPORTANT
)

def get_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # ⚠️ may need change (see below)
        messages=messages
    )
    return response.choices[0].message.content