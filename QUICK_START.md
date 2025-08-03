# 🚀 Quick Start Guide

## Step-by-Step Instructions

### 1. **Activate Virtual Environment**
```bash
venv\Scripts\activate
```
You should see `(venv)` at the start of your command prompt.

### 2. **Start Ollama Service** (if not already running)
Open a **new terminal window** and run:
```bash
ollama serve
```
Keep this terminal open.

### 3. **Start FastAPI Server**
In your main terminal (with venv activated), run:
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### 4. **Test the API**
Open a **third terminal** and run:
```bash
python test_api.py
```

## 🔧 Alternative Methods

### Method 1: Using Python Script
```bash
venv\Scripts\activate
python start_server.py
```

### Method 2: Direct Command
```bash
venv\Scripts\activate
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## 📋 What Should Happen

1. **Ollama**: Should show "Starting Ollama server..."
2. **FastAPI**: Should show "INFO: Application startup complete"
3. **Test**: Should show API responses with insurance answers

## 🌐 Access Points

- **API Root**: http://localhost:8000
- **API Endpoint**: http://localhost:8000/hackrx/run
- **Auto-docs**: http://localhost:8000/docs

## 🚨 Common Issues

### Issue: "uvicorn not found"
**Solution**: Make sure virtual environment is activated
```bash
venv\Scripts\activate
```

### Issue: "Ollama connection refused"
**Solution**: Start Ollama in a separate terminal
```bash
ollama serve
```

### Issue: "Model not found"
**Solution**: Download the model
```bash
ollama pull llama2:7b
```

## ✅ Success Indicators

- ✅ Virtual environment shows `(venv)`
- ✅ Ollama service is running
- ✅ FastAPI shows "Application startup complete"
- ✅ API test returns insurance answers
- ✅ No error messages in any terminal

## 🎯 Next Steps

Once everything is running:
1. Try different insurance questions
2. Check the API documentation at http://localhost:8000/docs
3. Integrate with your frontend application 