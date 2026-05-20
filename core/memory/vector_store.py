import chromadb

class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="database"
        )

        self.collection = self.client.get_or_create_collection(
            name="memory"
        )

    def add_memory(
        self,
        memory_id,
        text,
        embedding
    ):

        self.collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=[memory_id]
        )

    def search(
        self,
        query_embedding,
        n_results=3
    ):

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        return results