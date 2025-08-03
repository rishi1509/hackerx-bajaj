# Bajaj Hackathon - LLM Retrieval System

### ✅ Completed Modules
- PDF Parsing using `pdfplumber`
- Chunking with overlap logic
- FAISS Vector Indexing
- Semantic Query Answering using TinyLLaMA via Ollama

### 📁 Essential Files
- `main.py`: FastAPI application entry point
- `llm_logic_module.py`: Core LLM processing logic
- `parser.py`: Document parsing and chunking
- `embeddings.py`: FAISS vector indexing
- `requirements.txt`: Python dependencies
- `policy.pdf`: Sample insurance policy document
- `chunks.json`: Parsed document chunks
- `faiss.index`: Vector index file

### ⚠️ Notes
- Using `tinyllama` locally due to system RAM limits
- Planned upgrade to `llama3` or `GPT-4` in final version

### Installation Requirements
1. Install Python 3.10.11 (Some dependencies don't work well on Python 3.12/3.13)
   https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe

2. Create & activate virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

### Running the System
1. Install Ollama from https://ollama.com/download
2. Run the FastAPI server:
   ```bash
   python main.py
   ```
3. The server will start on: http://localhost:8000

### API Usage
#### Endpoint
```
POST http://localhost:8000/api/v1/hackrx/run
```

#### Sample Request
```json
{
    "documents": "https://hackrx.blob.core.windows.net/assets/policy.pdf?sv=2023-01-03&st=2025-07-04T09%3A11%3A24Z&se=2027-07-05T09%3A11%3A00Z&sr=b&sp=r&sig=N4a9OU0w0QXO6AOIBiu4bpl7AXvEZogeT%2FjUHNO7HzQ%3D",
    "questions": [
        "What is the grace period for premium payment under the National Parivar Mediclaim Plus Policy?"
    ]
}
