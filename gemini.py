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
You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not available in the context, reply exactly:

"I couldn't find that information in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text