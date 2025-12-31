import os
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone

load_dotenv()
llm = OpenAI()
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
dense_index = pc.Index("llm-project")

assistant_message = "How can I help you today?"
print(f"{assistant_message} \n")
user_input = input("User:  ")
history = [
  {"role": "developer", "content": "You are an AI customer support chatbot that is knowledgeable about software products created by a company called GROSS. One product is Flamehamster - a web browser. You are talking to a user on the frontend, so try to answer the questions with the information given to you, and if you can't just let them know where to look and find the info. DONT MENTION YOURE BEING GIVEN DOCUMENTATION OR INFORMATION"},
  {"role": "assistant", "content": assistant_message}
]

while user_input.lower() != "exit":
  results = dense_index.search(
    namespace="flamehamster",
    query={
      "top_k": 3,
      "inputs": {
        'text': user_input
      }
    }
  )

  documentation = ""

  for hit in results['result']['hits']:
    fields = hit.get('fields')
    chunk_text = fields.get('chunk_text')
    documentation += chunk_text

  history += [
    {"role": "user", "content": f"You have access to the following internal reference material about Flamehamster. Use it silently to answer the user's question. Never mention documents, information, references, or sources.: {documentation}. use the information given, and only that information to answer the users question to the best of your ability without ever mentioning that there is documentation being given to you: {user_input}"}
  ]

  response = llm.responses.create(
    model = "gpt-4.1-mini",
    temperature = 0,
    input = history
  )

  print(f"\nAssistant: {response.output_text}\n")

  history += [
    {"role": "assistant", "content": response.output_text}
  ]

  user_input = input("User:  ")

