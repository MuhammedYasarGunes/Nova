import uuid

from core.memory.embedding import EmbeddingModel
from core.memory.vector_store import VectorStore

class MemoryManager:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        self.vector_store = VectorStore()

    def remember(self, text):

        embedding = self.embedding_model.encode(
            text
        )

        memory_id = str(uuid.uuid4())

        self.vector_store.add_memory(
            memory_id,
            text,
            embedding
        )

    def recall(self, query):

        query_embedding = self.embedding_model.encode(
            query
        )

        results = self.vector_store.search(
            query_embedding
        )

        return results