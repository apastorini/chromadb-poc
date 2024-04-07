import chromadb

def main():
    client = chromadb.PersistentClient(path="./db")

    collection = client.create_collection(name="collection_local")
    collection.add(
        documents=["This is a document", "This is another document"],
        metadatas=[{"source": "my_source"}, {"source": "my_source"}],
        ids=["id1", "id2"]
    )
    results = collection.query(
        query_texts=["This is a query document local"],
        n_results=2
    )
    print(results)



if __name__ == "__main__":
  main()