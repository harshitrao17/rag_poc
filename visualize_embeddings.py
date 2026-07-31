import matplotlib.pyplot as plt
import umap

from pdf_loader import load_pdf
from chunker import chunk_text
from embedding import create_embeddings

def visualize_embeddings_3d(pdf_path):
    print("=" * 60)
    print("Loading PDF...")
    print("=" * 60)

    text = load_pdf(pdf_path)

    print(f"PDF Loaded Successfully!")

    print("\n" + "=" * 60)
    print("Creating Chunks...")
    print("=" * 60)

    chunks = chunk_text(text)

    print(f"Total Chunks : {len(chunks)}")

    print("\n" + "=" * 60)
    print("Generating Embeddings...")
    print("=" * 60)

    embeddings = create_embeddings(chunks)

    print(f"Embedding Shape : {embeddings.shape}")

    print("\nReducing 384 Dimensions → 3 Dimensions using UMAP...")

    reducer = umap.UMAP(
        n_components=3,
        random_state=42
    )

    embedding_3d = reducer.fit_transform(embeddings)

    print("Visualization Ready!")

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    ax.scatter(
        embedding_3d[:, 0],
        embedding_3d[:, 1],
        embedding_3d[:, 2],
        s=80
    )

    # Label each point
    for i in range(len(chunks)):
        ax.text(
            embedding_3d[i, 0],
            embedding_3d[i, 1],
            embedding_3d[i, 2],
            f"C{i+1}",
            fontsize=8
        )

    ax.set_title("3D Visualization of PDF Embeddings")

    ax.set_xlabel("Dimension 1")
    ax.set_ylabel("Dimension 2")
    ax.set_zlabel("Dimension 3")
    plt.show()
if __name__ == "__main__":
    visualize_embeddings_3d("data/company.pdf")