import os
import chromadb
from chromadb.config import Settings


#levanatr servidor en docker con ui y puerto api
# docker run -p 8000:8000 -p 3000:3000 chromadb/chroma
#https://github.com/flanker/chromadb-admin


# Si la lista `ids` se genera automáticamente:
def generate_ids(num_documents):
    # Lógica para generar cadenas válidas como IDs
    return ["ID_" + str(i + 1) for i in range(num_documents)]


def main():
  DIR = os.path.dirname(os.path.abspath(__file__))
  DB_PATH = os.path.join(DIR, 'data')

  chroma_client = chromadb.PersistentClient(path=DB_PATH, settings=Settings(allow_reset=True, anonymized_telemetry=False))
  sample_collection = chroma_client.get_or_create_collection(name="sample_collection")

  documents = [
      "Mars, often called the 'Red Planet', has captured the imagination of scientists and space enthusiasts alike.",
      # ... (rest of the documents)
  ]
  metadatas = []
  category = "Space"  # Adjust category based on your logic

  # Loop through documents and create corresponding metadata dictionaries
  for _ in documents:
    metadatas.append({'category': category})
  #ids = ["1", "2", "3", ...]  # (repeat for all documents)

  ids = generate_ids(len(documents))
  sample_collection.add(documents=documents, metadatas=metadatas, ids=ids)

  query_result = sample_collection.query(query_texts="Give me some facts about space", n_results=3)
  result_documents = query_result["documents"][0]

  for doc in result_documents:
      print(doc)

if __name__ == "__main__":
  main()