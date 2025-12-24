from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI()

assistant_message = "Hello there, type in a question for me."
user_input = input(f": {assistant_message} \n")
history = [
  {"role": "developer", "content": "you're a chatbot that talks like benjamin franklin and gives witty comments and advice to the user based on what they say. dont overdo the old language"},
  {"role": "assistant", "content": assistant_message},
  {"role": "user", "content": user_input}
]

while user_input.lower() != "exit":
  response = llm.responses.create(
    model = "gpt-4.1-mini",
    temperature = 0.5,
    input = history
  )

  print(f"\nBen: {response.output_text}")

  user_input = input("\nYou:  ")

  history += [
    {"role": "assistant", "content": response.output_text},
    {"role": "user", "content": user_input}
  ]