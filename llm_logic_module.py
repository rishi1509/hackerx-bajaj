import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from ollama import chat  # pip install ollama
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LLMPolicyAnalyzer:
    def __init__(self):
        """Initialize the LLM policy analyzer with pre-loaded embeddings and model."""
        try:
            logger.info("Initializing LLMPolicyAnalyzer...")
            
            # Load the sentence transformer model
            self.model = SentenceTransformer("all-MiniLM-L6-v2")
            logger.info("Loaded sentence transformer model")
            
            # Load embeddings and index
            with open("chunks.json", "r") as f:
                self.chunks = json.load(f)
            logger.info(f"Loaded {len(self.chunks)} chunks from chunks.json")
            
            self.chunk_texts = [chunk["text"] for chunk in self.chunks]
            self.chunk_embeddings = self.model.encode(self.chunk_texts)
            self.index = faiss.IndexFlatL2(len(self.chunk_embeddings[0]))
            self.index.add(np.array(self.chunk_embeddings))
            logger.info("FAISS index created successfully")
            
        except Exception as e:
            logger.error(f"Error initializing LLMPolicyAnalyzer: {e}")
            raise

    def search_chunks(self, query, top_k=3):
        """
        Search for relevant chunks based on the query.
        
        Args:
            query (str): The user's query
            top_k (int): Number of top chunks to retrieve
            
        Returns:
            list: List of relevant chunk texts
        """
        try:
            query_vector = self.model.encode([query])
            D, I = self.index.search(np.array(query_vector), top_k)
            retrieved_chunks = [self.chunk_texts[i] for i in I[0]]
            return retrieved_chunks
        except Exception as e:
            logger.error(f"Error searching chunks: {e}")
            return []

    def get_answer_with_evidence(self, question, top_k=3):
        """
        Get an answer to a question with evidence from the policy document.
        
        Args:
            question (str): The question to answer
            top_k (int): Number of top chunks to retrieve for context
            
        Returns:
            dict: Dictionary containing question, answer, evidence, and confidence
        """
        try:
            logger.info(f"Processing question: {question}")
            
            # Search for relevant chunks
            retrieved_chunks = self.search_chunks(question, top_k)
            context = "\n\n".join(retrieved_chunks)
            
            # Create the prompt
            prompt = f"""You are an insurance expert. Based on the following policy text, answer the question clearly and concisely.
Provide a direct, precise answer to the question in 1-2 sentences maximum. Do not provide lengthy explanations.
Respond in JSON format like this:
{{
  "question": "...",
  "answer": "...",
  "evidence": ["...", "..."],
  "confidence": 0.xx
}}

Context:
\"\"\"
{context}
\"\"\"

Question: {question}

Answer directly and concisely:
"""

            # Call Ollama with tinyllama model
            logger.info("Calling Ollama with tinyllama model...")
            response = chat(model="tinyllama", messages=[{"role": "user", "content": prompt}])
            answer_text = response["message"]["content"]
            
            # Try to parse the response as JSON
            try:
                # Clean up the response to make it valid JSON
                cleaned_response = answer_text.strip()
                if cleaned_response.startswith("```json"):
                    cleaned_response = cleaned_response[7:]
                if cleaned_response.startswith("```"):
                    cleaned_response = cleaned_response[3:]
                if cleaned_response.endswith("```"):
                    cleaned_response = cleaned_response[:-3]
                
                # Try to parse as JSON
                import json as json_parser
                answer_dict = json_parser.loads(cleaned_response)
                return answer_dict
            except:
                # If parsing fails, return a simplified response
                return {
                    "question": question,
                    "answer": answer_text,
                    "evidence": retrieved_chunks[:2],  # Return top 2 chunks as evidence
                    "confidence": 0.8
                }
                
        except Exception as e:
            logger.error(f"Error getting answer: {e}")
            return {
                "question": question,
                "answer": f"Error processing this question: {str(e)}",
                "evidence": [],
                "confidence": 0.0
            }

# Create a global instance
analyzer = None

def initialize_analyzer():
    """Initialize the global analyzer instance."""
    global analyzer
    if analyzer is None:
        analyzer = LLMPolicyAnalyzer()
    return analyzer

def get_answer_with_evidence(question, top_k=3):
    """
    Get an answer to a question with evidence from the policy document.
    
    Args:
        question (str): The question to answer
        top_k (int): Number of top chunks to retrieve for context
        
    Returns:
        dict: Dictionary containing question, answer, evidence, and confidence
    """
    analyzer = initialize_analyzer()
    return analyzer.get_answer_with_evidence(question, top_k)

# For testing purposes
if __name__ == "__main__":
    # Test the module
    question = "What is the waiting period for pre-existing diseases?"
    result = get_answer_with_evidence(question)
    print(json.dumps(result, indent=2))
