import os
import google.generativeai as genai
from dotenv import load_dotenv
 # load environment variables
load_dotenv()

#configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

#create model
model = genai.GenerativeModel("gemini-2.5-flash")
def generate_answer(question, chunks):
# Convert retrieved chunks into a single context
    context = "\n\n".join(
        item["chunk"] for item in chunks
    )

# Create Prompt
    prompt = f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not available in the context, say:
"I couldn't find that information in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""
    response = model.generate_content(prompt)
    return response.text
