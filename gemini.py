import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(question, chunks):
    """
    Generate an answer using the retrieved document chunks.
    """

    context = "\n\n".join(
        item["chunk"] for item in chunks
    )

    prompt = f"""
    Answer the user's question ONLY using the provided context.

    Context:
    {context}

    Question:
    {question}

    If the answer is not present in the context, say:
    "I couldn't find that information in the provided document."

    Answer:
    """

    response = model.generate_content(prompt)

    return response.text
def generate_questions(topic, chunks, number_of_questions: int = 10):
    """
    Generate short-answer questions with answers
    using retrieved document chunks.
    """

    context = "\n\n".join(
        item["chunk"] for item in chunks
    )

    prompt = f"""
    You are a question-generation assistant.

    Generate {number_of_questions} short-answer questions about the topic:
    {topic}

    IMPORTANT RULES:
    1. Use ONLY the information provided in the context.
    2. Do not use outside knowledge.
    3. Do not invent facts.
    4. Every question must be directly supported by the context.
    5. Keep the questions short, clear, and easy to understand.
    6. Provide a short and accurate answer immediately below each question.
    7. Answers must ONLY come from the provided context.
    8. Do not add information that is not present in the context.
    9. If the context does not contain enough information about the topic, say:
       "I couldn't find enough information about this topic in the provided documents."

    Use exactly this format:

    1. Question: <question>
       Answer: <answer>

    2. Question: <question>
       Answer: <answer>

    Context:
    {context}

    Generate the questions and answers:
    """

    response = model.generate_content(prompt)

    return response.text