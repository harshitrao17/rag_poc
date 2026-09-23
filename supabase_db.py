import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()


def get_supabase_client() -> Client:
    """
    Create and return a Supabase client.
    """

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    print("SUPABASE URL Loaded:", url is not None)
    print("SUPABASE KEY Loaded:", key is not None)

    if not url or not key:
        raise ValueError(
            "SUPABASE_URL or SUPABASE_KEY is missing in the .env file."
        )

    return create_client(url, key)


def insert_documents(client, chunks, embeddings, source):
    """
    Insert document chunks, embeddings, and source filename
    into the Supabase documents table.
    """

    for chunk, embedding in zip(chunks, embeddings):

        document = {
            "chunk": chunk,
            "embedding": embedding.tolist(),
            "source": source
        }

        client.table("documents").insert(document).execute()

    return True