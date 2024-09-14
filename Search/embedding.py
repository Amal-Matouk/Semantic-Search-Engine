from sentence_transformers import SentenceTransformer

class DocumentEmbedder:
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, documents):
        embeddings = []
        for doc in documents:
            embedding = self.model.encode([doc], show_progress_bar=False, batch_size=32)[0]
            embeddings.append(embedding)
        return embeddings

    def embed_query(self, query):
        query_embedding = self.model.encode([query], show_progress_bar=True, batch_size=32)[0]
        return query_embedding
