from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Any
from retrieve import process_documents

app = FastAPI()

class QueryRequest(BaseModel):
    documents: str  # placeholder — not used here
    questions: List[str]

@app.post("/hackrx/run")
def run_query(request: QueryRequest):
    try:
        answers = process_documents(request.documents, request.questions)
        return {"answers": answers}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "LLM-powered retrieval API is running."}
