import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load .env file
load_dotenv()


def get_supabase_client() -> Client:
    """
    Create and return a Supabase client.
    """

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise ValueError(
            "SUPABASE_URL or SUPABASE_KEY is missing in the .env file."
        )

    return create_client(url, key)
def insert_documents(client, chunks, embeddings):

    for chunk, embedding in zip(chunks, embeddings):
        document = {
            "chunk": chunk,
            "embedding": embedding.tolist()
        }
        response = client.table("documents").insert(document).execute()
    return True
