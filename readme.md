# Bajaj Hackathon - LLM Retrieval System

### ✅ Completed Modules
- PDF Parsing using `pdfplumber`
- Chunking with overlap logic
- FAISS Vector Indexing
- Semantic Query Answering using TinyLLaMA via Ollama

### 📁 Files
- `parser.py`: Extracts and chunks document
- `embeddings.py`: Creates FAISS index
- `llm_logic.py`: Loads model and answers user query
- `chunks.json`: Parsed chunks used for embeddings

### ⚠️ Notes
- Using `tinyllama` locally due to system RAM limits
- Planned upgrade to `llama3` or `GPT-4` in final version

###  Install Python 3.10.11 ( Some dependencies (e.g., older PyTorch versions) don’t work well on Python 3.12/3.13)
https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe

### 2. Create & activate virtual environment
python -m venv venv
venv\Scripts\activate
put the above in terminal ,


### this is the command u need to put in the terminal and then run the code.
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
### for running the code - python llm_logic.py
install ollama if you want to test it for that , i have used for training purpose , we can shift to gpt4 later
🔗 https://ollama.com/download link 
i have provided requirements.txt below.


