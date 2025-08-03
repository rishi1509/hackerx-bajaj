#!/usr/bin/env python3
"""
Lightweight LLM using Hugging Face transformers
Much faster and free vs OpenAI. Designed for insurance QA context.
"""

import json
import ast
from transformers import pipeline
import torch

class LightweightLLM:
    def __init__(self):
        print("🚀 Loading lightweight model...")

        try:
            self.generator = pipeline(
                "text-generation",
                model="microsoft/DialoGPT-small",  # Small and fast
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                device_map="auto" if torch.cuda.is_available() else None
            )
            print("✅ Loaded DialoGPT-small successfully.")
        except Exception as e:
            print(f"⚠️ Could not load DialoGPT: {e}")
            self.generator = None

    def generate_response(self, question, context):
        """Generate an answer using the context from chunks.json"""
        if self.generator is None:
            return self._fallback_response(question)

        try:
            # Improved instructional prompt
            prompt = f"""
You are an intelligent assistant for insurance queries. ONLY use the following context to answer the question.
If unsure, say "I don't know".

Context:
\"\"\"
{context}
\"\"\"

Question: {question}

Answer:"""

            response = self.generator(
                prompt,
                max_length=250,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                pad_token_id=self.generator.tokenizer.eos_token_id
            )

            # Extract answer from generation
            generated_text = response[0]['generated_text']
            answer = generated_text.split("Answer:")[-1].strip()

            return self._create_structured_response(question, answer, context)

        except Exception as e:
            print(f"⚠️ Error generating response: {e}")
            return self._fallback_response(question)

    def _create_structured_response(self, question, answer, context):
        # Extract evidence (3 top lines from context)
        evidence = []
        for line in context.split("\n"):
            if len(line.strip()) > 20:
                evidence.append(line.strip()[:100] + "...")
            if len(evidence) >= 3:
                break

        return {
            "question": question,
            "answer": answer,
            "evidence": evidence,
            "confidence": 0.75,
            "model": "DialoGPT-small"
        }

    def _fallback_response(self, question):
        return {
            "question": question,
            "answer": "⚠️ Lightweight model not available. Please check your setup.",
            "evidence": [],
            "confidence": 0.0,
            "error": "Model not loaded"
        }

# Global entry point
llm = LightweightLLM()

def ask_lightweight_llm(question, context):
    return llm.generate_response(question, context)
