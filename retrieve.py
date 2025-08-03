import json
import faiss
import numpy as np
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
from lightweight_llm import ask_lightweight_llm
import os
import ast
import re



# === Load & Process PDF ===
def load_pdf_chunks(file_path, chunk_size=500):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    # Chunk text
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        if len(chunk.strip()) > 50:
            chunks.append(chunk.strip())
    return chunks

pdf_path = "policy.pdf"
chunk_texts = load_pdf_chunks(pdf_path)

# === Embed Chunks ===
model = SentenceTransformer("all-MiniLM-L6-v2")
chunk_embeddings = model.encode(chunk_texts)

# === Build FAISS Index ===
index = faiss.IndexFlatL2(len(chunk_embeddings[0]))
index.add(np.array(chunk_embeddings))

# === LLM Call ===
def ask_llm(question, context):
    return ask_lightweight_llm(question, context)

# === Main Function ===
def process_documents(document_id, questions):
    answers = []

    for question in questions:
        query_vector = model.encode([question])
        D, I = index.search(np.array(query_vector), 3)

        retrieved_chunks = [chunk_texts[i] for i in I[0]]
        context = "\n\n".join(retrieved_chunks)

        result = ask_llm(question, context)

        try:
            if isinstance(result, dict):
                parsed = result
            else:
                parsed = ast.literal_eval(result)
        except Exception as e:
            parsed = {
                "question": question,
                "answer": "⚠️ Error parsing response.",
                "error": str(e),
                "raw": result
            }

        answers.append(parsed)

    return answers
