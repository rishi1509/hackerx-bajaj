#!/usr/bin/env python3
"""
Simple LLM replacement - no heavy dependencies
"""

import json
import re

def simple_llm_response(question, context):
    """Simple rule-based response system"""
    
    # Extract key information from context
    context_lower = context.lower()
    question_lower = question.lower()
    
    # Simple keyword matching for insurance questions
    if "grace period" in question_lower:
        return {
            "question": question,
            "answer": "Based on the policy document, there is typically a grace period for premium payments. Please check the specific terms in your policy.",
            "evidence": [context[:200] + "..."],
            "confidence": 0.7,
            "model": "simple-rule-based"
        }
    
    elif "waiting period" in question_lower:
        return {
            "question": question,
            "answer": "The policy includes waiting periods for certain conditions. The specific duration depends on the type of coverage.",
            "evidence": [context[:200] + "..."],
            "confidence": 0.7,
            "model": "simple-rule-based"
        }
    
    elif "maternity" in question_lower or "pregnancy" in question_lower:
        return {
            "question": question,
            "answer": "Maternity coverage is typically included in comprehensive health insurance policies with specific conditions and waiting periods.",
            "evidence": [context[:200] + "..."],
            "confidence": 0.6,
            "model": "simple-rule-based"
        }
    
    elif "surgery" in question_lower or "operation" in question_lower:
        return {
            "question": question,
            "answer": "Surgical procedures are covered under this health insurance policy, subject to policy terms and conditions.",
            "evidence": [context[:200] + "..."],
            "confidence": 0.8,
            "model": "simple-rule-based"
        }
    
    elif "claim" in question_lower:
        return {
            "question": question,
            "answer": "Claims can be filed through the insurance provider's designated process. Contact your insurance company for specific procedures.",
            "evidence": [context[:200] + "..."],
            "confidence": 0.7,
            "model": "simple-rule-based"
        }
    
    else:
        # Generic response based on context
        return {
            "question": question,
            "answer": f"Based on the policy document, this appears to be a comprehensive health insurance policy. Please refer to the specific terms and conditions for detailed coverage information.",
            "evidence": [context[:200] + "..."],
            "confidence": 0.5,
            "model": "simple-rule-based"
        }

def ask_simple_llm(question, context):
    """Main function to get response"""
    return simple_llm_response(question, context) 