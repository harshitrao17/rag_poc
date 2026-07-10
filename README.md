# 🤖 RAG POC

A Proof of Concept (POC) implementation of a Retrieval-Augmented Generation (RAG) chatbot built completely from scratch using Python, Supabase (pgvector), Sentence Transformers, and Gemini AI.

The chatbot retrieves the most relevant information from a PDF document using semantic vector search and then generates accurate responses using Gemini AI. Instead of relying only on the LLM's knowledge, every response is grounded in the retrieved document context.

The goal of this project was to understand every component of the RAG pipeline without using frameworks like LangChain, implementing each module individually to gain a deeper understanding of how Retrieval-Augmented Generation works.

---

## 🚀 Features

- 📄 Load and extract text from PDF documents
- ✂️ Split documents into meaningful chunks
- 🧠 Generate embeddings using Sentence Transformers
- 🗄️ Store embeddings in Supabase (pgvector)
- 🔍 Retrieve relevant chunks using semantic similarity search
- 🤖 Generate answers using Gemini AI
- 💬 Interactive command-line chatbot
- 🏗️ Clean and modular project structure

---

## 🛠️ Tech Stack

- Python
- Supabase
- PostgreSQL + pgvector
- Sentence Transformers
- Gemini AI
- PyPDF
- NumPy

---

## 📂 Project Structure

```text
rag_poc/
│
├── data/
│   └── company.pdf
│
├── database/
│   ├── 01_enable_pgvector.sql
│   ├── 02_create_documents_table.sql
│   └── 03_similarity_search.sql
│
├── chat.py
├── index_documents.py
├── pdf_loader.py
├── chunker.py
├── embedding.py
├── retriever.py
├── gemini.py
├── supabase_db.py
│
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

---

## 🏗️ RAG Workflow

```text
PDF
 │
 ▼
Load PDF
 │
 ▼
Chunk Text
 │
 ▼
Generate Embeddings
 │
 ▼
Store in Supabase
 │
 ▼
────────────────────────────────────

User Question
 │
 ▼
Create Query Embedding
 │
 ▼
Similarity Search
 │
 ▼
Retrieve Top-K Chunks
 │
 ▼
Gemini AI
 │
 ▼
Final Answer
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>

cd RAG_POC
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
SUPABASE_URL=your_supabase_url

SUPABASE_KEY=your_supabase_key

GEMINI_API_KEY=your_gemini_api_key
```

---

## ▶️ Running the Project

### Step 1 — Index the PDF

```bash
python index_documents.py
```

This reads the PDF, creates text chunks, generates embeddings, and stores them in Supabase.

---

### Step 2 — Start the Chatbot

```bash
python chat.py
```

Ask questions related to the uploaded PDF.

Type:

```text
exit
```

or

```text
quit
```

to close the chatbot.

---

## 📌 Future Improvements

- Support multiple PDF documents
- Add conversation memory
- Display source citations
- Build a Streamlit web interface
- Improve retrieval with hybrid search
- Add metadata filtering

---

## 👨‍💻 Author

Harshit Singh

This project was built as a learning-focused Proof of Concept to understand the complete Retrieval-Augmented Generation (RAG) pipeline by implementing every component from scratch.