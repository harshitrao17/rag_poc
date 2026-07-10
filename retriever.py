from embedding import create_query_embedding


def retrieve_documents(client, query, top_k=3):
    """
    Retrieve the most relevant document chunks.
    """

    query_embedding = create_query_embedding(query).tolist()

    response = (
        client.rpc(
            "match_documents",
            {
                "query_embedding": query_embedding,
                "top_k": top_k,
            }
        )
        .execute()
    )

    chunks = response.data

    return chunks