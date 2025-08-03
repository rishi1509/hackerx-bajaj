#!/usr/bin/env python3
"""
Lightweight LLM implementation using Hugging Face transformers
Uses a generative model for longer, more informative answers
"""

from transformers import pipeline
import torch

class LightweightLLM:
    def __init__(self):
        print("🚀 Loading FLAN-T5 model (google/flan-t5-base)...")
        try:
            self.generator = pipeline(
                "text2text-generation",
                model="google/flan-t5-base",
                device=0 if torch.cuda.is_available() else -1
            )
            print("✅ Loaded flan-t5-base successfully.")
        except Exception as e:
            print(f"❌ Could not load flan-t5-base: {e}")
            self.generator = None

    def generate_response(self, question, context):
        """Generate a longer, more structured answer"""
        if self.generator is None:
            return self._fallback_response(question)

        try:
            # Instruction-tuned prompt
            prompt = f"""You are an intelligent assistant. Using the information provided in the context below, answer the question thoroughly and clearly.

Context:
\"\"\"
{context}
\"\"\"

Question: {question}
Answer:"""

            response = self.generator(
                prompt,
                max_length=512,
                temperature=0.7,
                num_return_sequences=1,
                do_sample=True
            )

            generated_answer = response[0]["generated_text"].strip()

            return {
                "question": question,
                "answer": generated_answer,
                "evidence": [context[:200].replace('\n', ' ') + "..."],
                "confidence": 0.8,
                "model": "flan-t5-base"
            }

        except Exception as e:
            print(f"❌ Error generating response: {e}")
            return self._fallback_response(question)

    def _fallback_response(self, question):
        return {
            "question": question,
            "answer": "⚠️ Model not available or failed to generate.",
            "evidence": [],
            "confidence": 0.0,
            "model": "N/A"
        }

# Global instance
llm = LightweightLLM()

def ask_lightweight_llm(question, context):
    return llm.generate_response(question, context)
