from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI()

user_input = input("I'm a librarian chatbot! Ask me anything: \n")

response = llm.responses.create(
  model = "gpt-4.1-mini",
  temperature = 1,
  input = f"answer the following like a librarian whithout actually informing the user you're a librarian, dont answer non book related questions: {user_input}" 
)

print(response.output_text)