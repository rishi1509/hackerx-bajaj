#!/usr/bin/env python3
"""
Test script for the FastAPI insurance Q&A endpoint
"""

import requests
import json

def test_api():
    url = "http://localhost:8000/hackrx/run"
    
    # Test questions
    test_data = {
        "documents": "chunks.json",
        "questions": [
            "What is covered under the health insurance policy?",
            "What are the exclusions in the policy?",
            "How do I file a claim?"
        ]
    }
    
    print("🔍 Testing FastAPI endpoint...")
    print(f"URL: {url}")
    print(f"Questions: {test_data['questions']}")
    print("\n" + "="*50)
    
    try:
        response = requests.post(url, json=test_data)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ API is working!")
            print("\n📋 Responses:")
            
            for i, answer in enumerate(result['answers'], 1):
                print(f"\n--- Question {i} ---")
                print(f"Q: {answer.get('question', 'N/A')}")
                print(f"A: {answer.get('answer', 'N/A')}")
                print(f"Confidence: {answer.get('confidence', 'N/A')}")
                
                if answer.get('evidence'):
                    print("Evidence:")
                    for evidence in answer['evidence'][:2]:  # Show first 2 pieces
                        print(f"  • {evidence[:100]}...")
                        
        else:
            print(f"❌ API Error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Make sure the server is running:")
        print("   uvicorn main:app --reload --host 0.0.0.0 --port 8000")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_api() 