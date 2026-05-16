# Setup Instructions - Legacy Code Surgeon AI

## Quick Fix for Your Error

You're getting `ModuleNotFoundError: No module named 'dotenv'` because the dependencies aren't installed in your virtual environment.

### Solution:

Since you already have `.venv` activated, run:

```bash
cd backend
python -m pip install -r requirements.txt
```

Or if that doesn't work:

```bash
cd backend
python3 -m pip install -r requirements.txt
```

## Complete Setup Steps

### 1. Navigate to Backend Directory
```bash
cd backend
```

### 2. Activate Your Virtual Environment
You already have `.venv` activated (you can see `(.venv)` in your prompt), so skip this step.

If you need to activate it again:
```bash
source ../.venv/bin/activate
```

### 3. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

This will install:
- fastapi
- uvicorn
- python-multipart
- aiofiles
- httpx
- pydantic
- pydantic-settings
- python-dotenv
- GitPython

### 4. Create Environment File
```bash
cp .env.example .env
```

Then edit `.env` and add your IBM Bob AI API key:
```bash
nano .env
# or
vim .env
# or open in any text editor
```

Add:
```
BOB_AI_API_KEY=your_actual_api_key_here
```

### 5. Run the Server
```bash
uvicorn app.main:app --reload
```

Or with specific host/port:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 6. Verify It's Running
Open your browser:
- API: http://localhost:8000
- Interactive Docs: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

## Troubleshooting

### Error: "No module named 'dotenv'"
**Solution:** Install dependencies
```bash
python -m pip install -r requirements.txt
```

### Error: "No module named 'fastapi'"
**Solution:** Make sure you're in the backend directory and venv is activated
```bash
cd backend
source ../.venv/bin/activate
python -m pip install -r requirements.txt
```

### Error: "pip: command not found"
**Solution:** Use python -m pip instead
```bash
python -m pip install -r requirements.txt
```

### Error: "BOB_AI_API_KEY environment variable not set"
**Solution:** Create .env file
```bash
cp .env.example .env
# Edit .env and add your API key
```

### Port Already in Use
**Solution:** Use a different port
```bash
uvicorn app.main:app --reload --port 8001
```

## Verify Installation

After installing dependencies, verify:

```bash
python -c "import fastapi; print('FastAPI:', fastapi.__version__)"
python -c "import uvicorn; print('Uvicorn installed')"
python -c "import httpx; print('httpx installed')"
python -c "import git; print('GitPython installed')"
```

All should print without errors.

## Running Without .env File (Testing)

If you don't have a Bob AI API key yet, you can still test the server:

```bash
export BOB_AI_API_KEY="test_key_for_development"
uvicorn app.main:app --reload
```

The server will start, but AI features won't work until you add a real API key.

## Development Mode

For development with auto-reload:
```bash
uvicorn app.main:app --reload --log-level debug
```

## Production Mode

For production (no auto-reload):
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## Testing the API

Once running, test with curl:

```bash
# Health check
curl http://localhost:8000/health

# Root endpoint
curl http://localhost:8000/

# API docs (open in browser)
open http://localhost:8000/docs
```

## Next Steps

1. ✅ Install dependencies
2. ✅ Create .env file with API key
3. ✅ Start the server
4. 📝 Read README.md for API documentation
5. 📝 Check EXAMPLES.md for usage examples
6. 🚀 Start testing the endpoints!

## Common Commands Reference

```bash
# Activate venv
source ../.venv/bin/activate

# Install dependencies
python -m pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload

# Run on different port
uvicorn app.main:app --reload --port 8001

# Check if server is running
curl http://localhost:8000/health

# View logs with debug info
uvicorn app.main:app --reload --log-level debug

# Deactivate venv when done
deactivate
```

## File Structure Check

Make sure you're in the right directory:
```bash
pwd
# Should show: /Users/shubham/Desktop/IBM-BOB-Project/backend

ls -la
# Should show: app/, requirements.txt, .env.example, README.md, etc.
```

## Still Having Issues?

1. Make sure you're in the `backend` directory
2. Make sure `.venv` is activated (you'll see `(.venv)` in prompt)
3. Make sure all dependencies are installed
4. Check Python version: `python --version` (should be 3.11+)
5. Try reinstalling: `pip install --force-reinstall -r requirements.txt`

## Success Indicators

When everything is working, you should see:
```
INFO:     Will watch for changes in these directories: ['/Users/shubham/Desktop/IBM-BOB-Project/backend']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxxx] using WatchFiles
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Then visit http://localhost:8000/docs to see the interactive API documentation! 🎉