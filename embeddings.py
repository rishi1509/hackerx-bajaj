import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load Hugging Face embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')  # 384-dim vector

def load_chunks(filename="chunks.json"):
    with open(filename, "r") as f:
        return json.load(f)

def create_faiss_index(chunks):
    dimension = 384  # embedding dimension for this model
    index = faiss.IndexFlatL2(dimension)
    embeddings = []
    metadata = []

    for chunk in chunks:
        emb = model.encode(chunk["text"])
        embeddings.append(emb)
        metadata.append(chunk)

    index.add(np.array(embeddings).astype("float32"))
    return index, metadata

def save_index(index, metadata, index_file="faiss.index", meta_file="metadata.json"):
    faiss.write_index(index, index_file)
    with open(meta_file, "w") as f:
        json.dump(metadata, f, indent=2)

# Optional: Query interface
def search(query, index_file="faiss.index", meta_file="metadata.json", k=3):
    index = faiss.read_index(index_file)
    with open(meta_file, "r") as f:
        metadata = json.load(f)

    query_emb = model.encode(query)
    D, I = index.search(np.array([query_emb]).astype("float32"), k)

    results = []
    for i in I[0]:
        results.append(metadata[i]["text"])

    return results

if __name__ == "__main__":
    print("🔄 Loading chunks...")
    chunks = load_chunks()

    print("🔄 Creating FAISS index...")
    index, metadata = create_faiss_index(chunks)

    print("💾 Saving index and metadata...")
    save_index(index, metadata)

    print("✅ Done! You can now search your documents semantically.")

    # Optional test
    test_query = "Does the policy cover maternity expenses?"
    print("\n🔍 Example Query:")
    for i, res in enumerate(search(test_query)):
        print(f"\nResult {i+1}:")
        print(res)
