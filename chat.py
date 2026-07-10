from supabase_db import get_supabase_client
from retriever import retrieve_documents
from gemini import generate_answer
def main():
    client = get_supabase_client()
    print("=" * 50)
    print("🤖 Company RAG Chatbot")
    print("=" * 50)
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        query = input("You :")
        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        if not query.strip():
            continue
        chunks = retrieve_documents(client, query)

    # ____________DEBUG_____________________
    # print("\nRetrieved Chunks")
    # print("=" * 50)
    #
    # for i, chunk in enumerate(chunks, 1):
    #     print(f"\nChunk {i}")
    #     print(chunk["chunk"])
    #     print(f"Similarity: {chunk['similarity']}")

        answer = generate_answer(query, chunks)
        print("\nAI:")
        print(answer)
        print("-" * 50)
if __name__ == "__main__":
    main()

