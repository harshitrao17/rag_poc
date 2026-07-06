from supabase_db import get_supabase_client, insert_documents
from pdf_loader import load_pdf
from chunker import chunk_text
from embedding import create_embeddings

# PDF Path
pdf_path = "data/company.pdf"

# Load PDF
text = load_pdf(pdf_path)

# Create Chunks
chunks = chunk_text(text)

# Create Embeddings
embeddings = create_embeddings(chunks)

 # Print Total Chunks
print("=" * 50)
print(f"Total Chunks: {len(chunks)}")
print("=" * 50)

# Print Each Chunk
for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print("-" * 30)
    print(chunk)

print("\n" + "=" * 50)
print("Embeddings Created Successfully")
print("=" * 50)

print(f"Total Embeddings: {len(embeddings)}")
print(f"Embedding Dimension: {len(embeddings[0])}")

print("\nFirst 10 Values of First Embedding:")
print(embeddings[0][:10])
print("\n" + "=" * 50)
print("Connecting to Supabase...")
print("=" * 50)

client = get_supabase_client()
print("✅ Connected Successfully!")
print(client)
# Store Documents in Supabase

success = insert_documents(client, chunks, embeddings)
if success:
    print("\n" + "=" * 50)
    print("Documents Inserted Successfully!")
    print("=" * 50)

