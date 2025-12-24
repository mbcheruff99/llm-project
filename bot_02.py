from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI()

user_input = input("Librarian: How can I help you today? \n\nUser:  ")


while user_input.lower() != "exit":
  response = llm.responses.create(
    model = "gpt-4.1-mini",
    temperature = 1,
    input = f" asnwer the following like a libarian without telling the user you're a librarian, and only answer book or library related questions{user_input}"
  )

  print(f"\nLibrarian: {response.output_text}")

  user_input = input("\nYou:  ")