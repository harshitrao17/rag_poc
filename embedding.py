from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    embeddings = model.encode(chunks)
    return embeddings
def create_query_embedding(query):
    embeddings = model.encode(query)
    return embeddings