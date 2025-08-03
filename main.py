from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import our existing modules
try:
    from llm_logic_module import get_answer_with_evidence
    logger.info("Successfully imported llm_logic_module")
except Exception as e:
    logger.error(f"Error importing llm_logic_module: {e}")
    raise

app = FastAPI(
    title="HackRx LLM-Powered Intelligent Query–Retrieval System",
    description="An API for processing insurance policy documents and answering questions using semantic search and LLM",
    version="1.0.0"
)

class QuestionRequest(BaseModel):
    documents: str  # URL to the document (not used in this implementation since we're using a local PDF)
    questions: List[str]

class AnswerResponse(BaseModel):
    question: str
    answer: str
    evidence: List[str]
    confidence: float

class RunResponse(BaseModel):
    answers: List[str]

@app.get("/")
async def root():
    return {"message": "HackRx LLM-Powered Intelligent Query–Retrieval System API"}

@app.post("/api/v1/hackrx/run", response_model=RunResponse)
async def run_submission(request: QuestionRequest):
    """
    Process questions and return answers based on the policy document.
    
    This endpoint takes a list of questions and returns structured answers
    based on semantic search of the policy document.
    """
    try:
        logger.info(f"Processing {len(request.questions)} questions")
        
        answers = []
        
        # Process each question
        for question in request.questions:
            logger.info(f"Processing question: {question}")
            
            try:
                # Get answer using our existing logic
                result = get_answer_with_evidence(question)
                
                # Extract the answer from the result
                if isinstance(result, dict) and "answer" in result:
                    answers.append(result["answer"])
                else:
                    answers.append(str(result))
                    
            except Exception as e:
                logger.error(f"Error processing question '{question}': {e}")
                answers.append(f"Error processing this question: {str(e)}")
        
        logger.info(f"Successfully processed {len(answers)} answers")
        # Return in the sample response format
        return {
            "answers": answers
        }
        
    except Exception as e:
        logger.error(f"Error in run_submission: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.post("/api/v1/hackrx/run_detailed", response_model=List[AnswerResponse])
async def run_submission_detailed(request: QuestionRequest):
    """
    Process questions and return detailed answers with evidence and confidence scores.
    """
    try:
        logger.info(f"Processing {len(request.questions)} questions with detailed response")
        
        detailed_answers = []
        
        # Process each question
        for question in request.questions:
            logger.info(f"Processing question: {question}")
            
            try:
                # Get detailed answer using our existing logic
                result = get_answer_with_evidence(question)
                
                # Format the result
                if isinstance(result, dict):
                    detailed_answers.append(AnswerResponse(
                        question=question,
                        answer=result.get("answer", "No answer found"),
                        evidence=result.get("evidence", []),
                        confidence=result.get("confidence", 0.0)
                    ))
                else:
                    detailed_answers.append(AnswerResponse(
                        question=question,
                        answer=str(result),
                        evidence=[],
                        confidence=0.5
                    ))
                    
            except Exception as e:
                logger.error(f"Error processing question '{question}': {e}")
                detailed_answers.append(AnswerResponse(
                    question=question,
                    answer=f"Error processing this question: {str(e)}",
                    evidence=[],
                    confidence=0.0
                ))
        
        logger.info(f"Successfully processed {len(detailed_answers)} detailed answers")
        return detailed_answers
        
    except Exception as e:
        logger.error(f"Error in run_submission_detailed: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
