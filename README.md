# RAG_POC

A simple Retrieval-Augmented Generation (RAG) chatbot built using Python, Sentence Transformers, Supabase (pgvector), and Google Gemini.

The chatbot retrieves relevant information from PDF documents using semantic search and generates context-aware answers using Gemini.

---

## Features

- PDF text extraction
- Text chunking
- Embedding generation using Sentence Transformers
- Vector storage with Supabase (pgvector)
- Semantic similarity search
- Gemini-powered answer generation
- Prevents hallucinations by answering only from retrieved context

---

## Tech Stack

- Python
- Sentence Transformers
- Supabase
- pgvector
- Google Gemini
- PyPDF
- NumPy

---

## Project Structure

```text
RAG_POC/
│
├── data/
│   └── company.pdf
│
├── pdf_loader.py
├── chunker.py
├── embedding.py
├── supabase_db.py
├── retriever.py
├── gemini.py
├── index_documents.py
├── chat.py
│
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

## Workflow

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
Store Embeddings in Supabase
   │
   ▼
User Query
   │
   ▼
Generate Query Embedding
   │
   ▼
Similarity Search (Top K)
   │
   ▼
Retrieved Context
   │
   ▼
Google Gemini
   │
   ▼
Final Answer
```

---

## Installation

```bash
git clone <repository-url>

cd RAG_POC

pip install -r requirements.txt
```

Create a `.env` file:

```env
SUPABASE_URL=YOUR_SUPABASE_URL
SUPABASE_KEY=YOUR_SUPABASE_KEY
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Run

Index the PDF:

```bash
python index_documents.py
```

Start the chatbot:

```bash
python chat.py
```

---

## Example

**Question**

```
What are the working hours?
```

**Answer**

```
Employees work Monday to Friday from 9:00 AM to 6:00 PM.
Lunch break is 1 hour.
```

---

## Future Improvements

- Multiple PDF support
- FastAPI backend
- React frontend
- Chat history
- Metadata filtering
- Hybrid search
- Docker deployment

---

## Author

Harshit Singh