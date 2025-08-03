import pdfplumber
import re
import json

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return clean_text(text)

def clean_text(raw_text):
    return re.sub(r'\s+', ' ', raw_text).strip()

def chunk_text(text, max_tokens=300, overlap=50):
    words = text.split()
    chunks = []
    start = 0
    chunk_id = 0
    while start < len(words):
        end = min(start + max_tokens, len(words))
        chunk = " ".join(words[start:end])
        chunks.append({"id": chunk_id, "text": chunk})
        chunk_id += 1
        start += max_tokens - overlap
    return chunks

def save_chunks_to_json(chunks, filename="chunks.json"):
    with open(filename, "w") as f:
        json.dump(chunks, f, indent=2)

# === MAIN RUNNER ===
if __name__ == "__main__":
    file_path = "policy.pdf"  # <- change this to your PDF filename
    full_text = extract_text_from_pdf(file_path)
    chunks = chunk_text(full_text)
    save_chunks_to_json(chunks)
    print(f"✅ Processed and saved {len(chunks)} chunks to chunks.json")
