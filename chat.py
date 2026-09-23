import re

from supabase_db import get_supabase_client
from retriever import retrieve_documents
from gemini import generate_answer, generate_questions


def is_question_generation_request(query):
    """
    Detect whether the user wants questions generated
    from the document.
    """

    keywords = [
        "make questions",
        "generate questions",
        "create questions",
        "short questions",
        "give me questions",
        "question bana",
        "questions bana",
        "questions banao",
        "sawal bana",
        "sawaal bana",
    ]

    query_lower = query.lower()

    return any(keyword in query_lower for keyword in keywords)


def extract_question_count(query, default=10):
    """
    Extract the requested number of questions from the user's query.

    Examples:
        "5 questions bana do" -> 5
        "10 short questions" -> 10
        "20 questions generate karo" -> 20
        "questions bana do" -> 10
    """

    match = re.search(r"\b(\d+)\b", query)

    if match:
        count = int(match.group(1))

        # Prevent unreasonable requests
        if 1 <= count <= 50:
            return count

    return default


def main():
    client = get_supabase_client()

    print("=" * 50)
    print("🤖 Company RAG Chatbot")
    print("=" * 50)
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        query = input("You : ")

        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if not query.strip():
            continue

        # Retrieve relevant document chunks
        chunks = retrieve_documents(client, query)

        # Check user's intent
        if is_question_generation_request(query):

            # Detect requested number of questions
            question_count = extract_question_count(query)

            answer = generate_questions(
                query,
                chunks,
                number_of_questions=question_count
            )

        else:

            answer = generate_answer(
                query,
                chunks
            )

        print("\nAI:")
        print(answer)
        print("-" * 50)


if __name__ == "__main__":
    main()