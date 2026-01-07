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
  {"role": "developer", "content": """You are an AI customer support technician who is knowledgeable about software products created by the company called GROSS. The products are:
   * Flamehamster, a web browser.
   * Rumblechirp, an email client.
   * GuineaPigment, a drawing tool for creating/editing SVGs
   * EMRgency, an electronic medical record system
   * Verbiage++, a content management system."""},
  {"role": "assistant", "content": assistant_message}
]

while user_input.lower() != "exit":
  results = dense_index.search(
    namespace="all-gross",
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
    {"role": "user", "content": f"Here are exerpts from the offical GROSS documentation: {documentation}. Use whatever info from the above documentaion exerpts (an no other info) to answer the following query: {user_input}"}
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