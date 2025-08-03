# Setup Guide: Local LLM with Ollama

## Overview
This project now uses **Ollama** for local LLM inference instead of paid OpenAI services. This means:
- ✅ **No API costs** - completely free to use
- ✅ **Privacy** - all processing happens locally
- ✅ **Offline capability** - works without internet
- ✅ **Lightweight** - uses efficient local models

## Installation Steps

### 1. Install Ollama
Visit [https://ollama.ai/](https://ollama.ai/) and download the installer for your operating system:
- **Windows**: Download the Windows installer
- **macOS**: Download the macOS installer  
- **Linux**: Follow the installation instructions

### 2. Install the Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the LLM Model
After installing Ollama, download the lightweight model:
```bash
ollama pull llama2:7b
```

### 4. Start Ollama Service
Ollama runs as a local service. Make sure it's running:
- **Windows/macOS**: The installer should start it automatically
- **Linux**: Run `ollama serve` in a terminal

### 5. Test the Setup
Run the test script to verify everything works:
```bash
python llm_logic.py
```

## Alternative Models

If you want to try different models, here are some lightweight options:

### Fast Models (Recommended for speed):
```bash
ollama pull llama2:7b    # 7B parameters - good balance
ollama pull llama2:3b     # 3B parameters - very fast
ollama pull phi2          # 2.7B parameters - very fast
```

### Better Quality Models (slower but more accurate):
```bash
ollama pull llama2:13b    # 13B parameters - better quality
ollama pull codellama:7b  # 7B parameters - good for code
```

## Troubleshooting

### Issue: "Connection refused" or "Ollama service unavailable"
**Solution**: Make sure Ollama is running:
1. Open a terminal/command prompt
2. Run `ollama serve`
3. Keep this terminal open

### Issue: "Model not found"
**Solution**: Download the model:
```bash
ollama pull llama2:7b
```

### Issue: Slow responses
**Solutions**:
1. Try a smaller model: `ollama pull llama2:3b`
2. Ensure you have enough RAM (8GB+ recommended)
3. Close other applications to free up memory

### Issue: Model quality not as good as GPT-4
**Solutions**:
1. Try a larger model: `ollama pull llama2:13b`
2. Refine your prompts to be more specific
3. Provide more context in your questions

## Performance Tips

1. **First run is slow**: The model loads into memory on first use
2. **Subsequent runs are faster**: The model stays in memory
3. **Use specific questions**: More specific questions get better answers
4. **Provide context**: Include relevant details in your questions

## Model Comparison

| Model | Size | Speed | Quality | RAM Usage |
|-------|------|-------|---------|-----------|
| llama2:3b | 3B | ⚡⚡⚡ | ⭐⭐ | 4GB |
| llama2:7b | 7B | ⚡⚡ | ⭐⭐⭐ | 8GB |
| llama2:13b | 13B | ⚡ | ⭐⭐⭐⭐ | 16GB |

## Next Steps

1. Test the API: `python main.py`
2. Try different questions to see the quality
3. Adjust the confidence threshold in the code if needed
4. Consider fine-tuning prompts for your specific use case

## Support

If you encounter issues:
1. Check the Ollama documentation: https://ollama.ai/docs
2. Ensure your system meets the minimum requirements
3. Try restarting the Ollama service 