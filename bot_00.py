from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI()

response = llm.responses.create(
  model="gpt-4.1-mini",
  temperature=0.7,
  input="list all the US presidents"
)

print(response.output_text)