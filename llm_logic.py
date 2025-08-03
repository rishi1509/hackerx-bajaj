# llm_logic.py

import json
import faiss
import numpy as np
import ast
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
from lightweight_llm import ask_lightweight_llm

# === PDF Reader ===
def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

# === Chunker ===
def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# === Embed PDF Chunks ===
model = SentenceTransformer("all-MiniLM-L6-v2")

raw_text = extract_text_from_pdf("policy.pdf")
chunks = chunk_text(raw_text)
chunk_embeddings = model.encode(chunks)
index = faiss.IndexFlatL2(len(chunk_embeddings[0]))
index.add(np.array(chunk_embeddings))

# === Ask LLM ===
def ask_llm(question, context):
    return ask_lightweight_llm(question, context)

# === CLI Tester ===
if __name__ == "__main__":
    user_query = input("🔍 Enter your query: ")

    # Retrieve top chunks
    query_vector = model.encode([user_query])
    D, I = index.search(np.array(query_vector), 3)
    retrieved_chunks = [chunks[i] for i in I[0]]
    context = "\n\n".join(retrieved_chunks)

    # Ask LLM
    result = ask_llm(user_query, context)

    try:
        if isinstance(result, dict):
            parsed = result
        else:
            parsed = ast.literal_eval(result)
    except Exception as e:
        parsed = {
            "question": user_query,
            "answer": "⚠️ Failed to parse model response.",
            "error": str(e),
            "raw": result
        }

    with open("llm_response.json", "w") as f:
        json.dump(parsed, f, indent=2)

    print("\n✅ Final LLM response saved to `llm_response.json`:\n")
    print(json.dumps(parsed, indent=2))
