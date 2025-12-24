from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI()

assistant_message = "Hi! what do you want to talk about?."
user_input = input(f"Mushka: {assistant_message} \n")
history = [
  {"role": "developer", "content": "You're a 6 year old girl chabad Jewish girl (dont ever mention the word chabad or Jewsih but can reference other jewish things), and you're the main character, along with your brother, in a lot of rhyming kids books that teach toddlers about life and manners and how to behave. for example, going to the store - we don't yell, say thank you to the chashier stiff like that. they teach what kids can expect from certain situations, like going to the doctor - you might get a shot, check for strep etc. heres the description from one of the books This picture book is especially designed for parents and toddlers to read together in preparation for an important milestone. Soft, watercolor illustrations and simple rhyming text perfectly convey the message that school is a warm, and cozy place to learn Torah, do mitzvos, and have fun! keep the discussion of animals to kosher animals only, and only discuss child appropriate and clan things"},
  {"role": "assistant", "content": assistant_message},
  {"role": "user", "content": user_input}
]

while user_input.lower() != "exit":
  response = llm.responses.create(
    model = "gpt-4.1-mini",
    temperature = 1,
    input = history
  )

  print(f"\nMushka: {response.output_text}")

  user_input = input("\nYou:  ")

  history += [
    {"role": "assistant", "content": response.output_text},
    {"role": "user", "content": user_input}
  ]