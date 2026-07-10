from supabase_db import get_supabase_client, insert_documents
from pdf_loader import load_pdf
from chunker import chunk_text
from embedding import create_embeddings
def main():
   # PDF Path
   pdf_path = "data/company.pdf"

   # Load PDF
   text = load_pdf(pdf_path)

   # Create Chunks
   chunks = chunk_text(text)

   # Create Embeddings
   embeddings = create_embeddings(chunks)

   print("\n" + "=" * 50)
   print("Connecting to Supabase...")
   print("=" * 50)

   client = get_supabase_client()
   print("✅ Connected Successfully!")
   
   # Store Documents in Supabase
   success = insert_documents(client, chunks, embeddings)
   if success:
      print("\n" + "=" * 50)
      print("Documents Inserted Successfully! ")
      print("=" * 50)
if __name__ == "__main__":
   main()


