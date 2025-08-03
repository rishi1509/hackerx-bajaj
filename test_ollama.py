#!/usr/bin/env python3
"""
Simple test script to verify Ollama is working correctly
"""

import ollama
import json

def test_ollama():
    print("🔍 Testing Ollama connection...")
    
    try:
        # Test basic connection
        print("1. Testing connection to Ollama...")
        response = ollama.chat(model='llama2:7b', messages=[
            {
                'role': 'user',
                'content': 'Say "Hello, Ollama is working!" and nothing else.'
            }
        ])
        
        print("✅ Ollama is working!")
        print(f"Response: {response['message']['content']}")
        
        # Test JSON response
        print("\n2. Testing JSON response capability...")
        response = ollama.chat(model='llama2:7b', messages=[
            {
                'role': 'user',
                'content': 'Return only this JSON: {"status": "success", "message": "test"}'
            }
        ])
        
        print("✅ JSON response test completed!")
        print(f"Response: {response['message']['content']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n🔧 Troubleshooting steps:")
        print("1. Make sure Ollama is installed: https://ollama.ai/")
        print("2. Make sure Ollama service is running: ollama serve")
        print("3. Make sure the model is downloaded: ollama pull llama2:7b")
        return False

if __name__ == "__main__":
    success = test_ollama()
    if success:
        print("\n🎉 All tests passed! Your setup is ready.")
    else:
        print("\n⚠️  Setup incomplete. Please follow the troubleshooting steps.") 