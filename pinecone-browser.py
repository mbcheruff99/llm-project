import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
dense_index = pc.Index("llm-project")

user_query = "How can i remove a bookmark?" #!!!!!!

results = dense_index.search(
  namespace="flamehamster",
  query={
    "top_k": 3,
    "inputs": {
      "text": user_query
    }
  }
)

print(results)