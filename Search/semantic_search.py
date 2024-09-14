import os
from sqlalchemy.sql import text
from Search.database import Database, Document
from Search.embedding import DocumentEmbedder
from Search.annoy_index import AnnoyIndex
import numpy as np

# Construct the absolute path to the database file
#db_path = os.path.abspath('documents.db')
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', './documents.db'))
# Check if the database file exists
if not os.path.exists(db_path):
    raise FileNotFoundError(f"Database file not found at {db_path}")

db_url = f'sqlite:///{db_path}'
model_name = 'all-MiniLM-L6-v2'
top_k = 3

class SemanticSearchApp:
    def __init__(self):
        self.db = Database(db_url)
        self.embedder = DocumentEmbedder(model_name)

    def search_documents(self, query):
        document_rows = self.db.get_all_documents()
        #print(f"document_rows: {document_rows}")  # Debugging statement

        if not document_rows:
            print("No documents found in the database.")
            return []

        all_ids = [row.id for row in document_rows]
        # print(all_ids)
        all_embeddings = [np.frombuffer(row.embedding, dtype=np.float32) for row in document_rows]
        vector_dim = len(all_embeddings[0]) if all_embeddings else 0

        index = AnnoyIndex(vector_dim, 'angular')
        for i, embedding in enumerate(all_embeddings):
            index.add_item(all_ids[i], embedding)
        index.build(10)

        query_embedding = self.embedder.embed_query(query)
        results = index.get_nns_by_vector(query_embedding, top_k, include_distances=True)
        # print(results)
        result_docs = []
        for doc_id in results[0]:
            # Use `text` function to execute raw SQL queries
            stmt = text("SELECT title, content FROM documents WHERE id = :id")
            row = self.db.execute_query(stmt, {'id': doc_id})
            if row:
                result_docs.append({'title': row[0][0], 'content': row[0][1]})
        return result_docs
