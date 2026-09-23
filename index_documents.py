from pathlib import Path

from supabase_db import get_supabase_client, insert_documents
from pdf_loader import load_pdf
from chunker import chunk_text
from embedding import create_embeddings


def main():

    # PDF folder
    data_folder = Path("data")

    # Find all PDF files
    pdf_files = list(data_folder.glob("*.pdf"))

    if not pdf_files:
        print("❌ No PDF files found in the data folder.")
        return

    print("\n" + "=" * 50)
    print(f"Found {len(pdf_files)} PDF file(s)")
    print("=" * 50)

    # Connect to Supabase
    print("\nConnecting to Supabase...")

    client = get_supabase_client()

    print("✅ Connected Successfully!")

    total_chunks = 0

    # Process every PDF
    for pdf_path in pdf_files:

        print("\n" + "-" * 50)
        print(f"📄 Processing: {pdf_path.name}")
        print("-" * 50)

        # Load PDF
        text = load_pdf(pdf_path)

        if not text.strip():
            print(f"⚠️ No text found in {pdf_path.name}")
            continue

        # Create chunks
        chunks = chunk_text(text)

        print(f"Created {len(chunks)} chunks")

        # Create embeddings
        embeddings = create_embeddings(chunks)

        print(f"Created {len(embeddings)} embeddings")

        # Store documents
        success = insert_documents(
            client,
            chunks,
            embeddings,
            source=pdf_path.name
        )

        if success:
            print(f"✅ {pdf_path.name} inserted successfully!")
            total_chunks += len(chunks)
        else:
            print(f"❌ Failed to insert {pdf_path.name}")

    print("\n" + "=" * 50)
    print("INDEXING COMPLETED")
    print("=" * 50)

    print(f"PDFs processed : {len(pdf_files)}")
    print(f"Total chunks   : {total_chunks}")
    print("=" * 50)


if __name__ == "__main__":
    main()