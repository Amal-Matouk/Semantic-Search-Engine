from annoy import AnnoyIndex

class AnnoyIndexBuilder:
    def __init__(self, vector_dim):
        self.vector_dim = vector_dim

    def build_annoy_index(self, embeddings, ids):
        index = AnnoyIndex(self.vector_dim, 'euclidean')
        for i, embedding in enumerate(embeddings):
            index.add_item(ids[i], embedding.tolist())
        index.build(10)
        return index

    def search(self, index, query_embedding, query_id, top_k=3):
        similar_item_ids = index.get_nns_by_vector(query_embedding, top_k + 1)

        if query_id is not None:
            similar_item_ids = [item_id for item_id in similar_item_ids if item_id != query_id]

        return similar_item_ids[:top_k]
