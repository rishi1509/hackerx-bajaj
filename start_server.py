#!/usr/bin/env python3
"""
Simple script to start the FastAPI server
"""

import subprocess
import sys
import os

def start_server():
    print("🚀 Starting FastAPI server...")
    print("Make sure your virtual environment is activated!")
    print("Command: uvicorn main:app --reload --host 127.0.0.1 --port 8000")
    print("\n" + "="*50)
    
    try:
        # Start the server
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "main:app", 
            "--reload", 
            "--host", "127.0.0.1", 
            "--port", "8000"
        ])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure virtual environment is activated: venv\\Scripts\\activate")
        print("2. Make sure all dependencies are installed: pip install -r requirements.txt")
        print("3. Make sure Ollama is running: ollama serve")

if __name__ == "__main__":
    start_server() 