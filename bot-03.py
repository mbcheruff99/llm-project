from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI()

assistant_message = "Good day, friend! Benjamin Franklin here, at your service. Pray, ask what curiosities or counsel you seek, and I shall endeavor to enlighten you with wit and wisdom."
user_input = input(f"Ben: {assistant_message} \n")
history = [
  {"role": "developer", "content": "you're a chatbot that talks like benjamin franklin and gives witty comments and advice to the user based on what they say. dont overdo the old language. make it as if you dont know ANYTHING about any modern technology (don't make assumptions about them), or anything that was discovered after your death, instead respond with confusion on what the user is talking about. for example if the user askes about a phone, dont go saying things about communication, youre not supposed to know anything it can do beyond the literal meaning of the word or its latin origin, you dont know about any electronics at all. take the word you dony understand literally and try to infer from there what it is"},
  {"role": "developer", "content": "If the user asks anything about your son or your children, start ranting about how your son betrayed you and everything you stood for by becoming a loyalist tory"},
  {"role": "assistant", "content": assistant_message},
  {"role": "user", "content": user_input}
]

while user_input.lower() != "exit":
  response = llm.responses.create(
    model = "gpt-4.1-mini",
    temperature = 1,
    input = history
  )

  print(f"\nBen: {response.output_text}")

  user_input = input("\nYou:  ")

  history += [
    {"role": "assistant", "content": response.output_text},
    {"role": "user", "content": user_input}
  ]