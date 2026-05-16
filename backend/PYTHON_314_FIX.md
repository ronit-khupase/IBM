# Python 3.14 Compatibility Fix

## The Problem
Python 3.14 is too new! PyO3 (required by pydantic-core) only supports up to Python 3.13.

Error: `the configured Python interpreter version (3.14) is newer than PyO3's maximum supported version (3.13)`

## Solution Options

### Option 1: Use Forward Compatibility Flag (Quick Fix)
```bash
# Set environment variable to force compatibility
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1

# Then install
pip3 install -r requirements.txt
```

### Option 2: Use Python 3.13 (Recommended)
Install Python 3.13 and create a new virtual environment:

```bash
# Install Python 3.13 via Homebrew
brew install python@3.13

# Create new venv with Python 3.13
cd /Users/shubham/Desktop/IBM-BOB-Project
python3.13 -m venv .venv313

# Activate it
source .venv313/bin/activate

# Install dependencies
cd backend
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload
```

### Option 3: Use Pre-built Wheels (Fastest)
```bash
# Install without building from source
pip3 install --only-binary :all: -r requirements.txt
```

If that fails, install pydantic separately with forward compatibility:
```bash
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 pip3 install pydantic==2.10.3
pip3 install -r requirements.txt
```

## Recommended: Quick Start with Forward Compatibility

Run these commands in your terminal:

```bash
cd backend

# Set the compatibility flag
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1

# Install dependencies
pip3 install -r requirements.txt

# Create .env
cp .env.example .env
echo "BOB_AI_API_KEY=test_key" >> .env

# Run server
uvicorn app.main:app --reload
```

## Alternative: Install Without Pydantic (Testing Only)

For quick testing without pydantic:

```bash
# Install everything except pydantic
pip3 install fastapi==0.115.0 uvicorn[standard]==0.32.0 python-multipart==0.0.12 aiofiles==24.1.0 httpx==0.27.2 python-dotenv==1.0.1 GitPython==3.1.43

# Then try with forward compatibility
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 pip3 install pydantic==2.10.3 pydantic-settings==2.6.1
```

## Why This Happens

Python 3.14 was released in 2026 and is very new. The Rust-based pydantic-core library (via PyO3) hasn't been updated to officially support it yet. The forward compatibility flag tells PyO3 to use the stable ABI and assume compatibility.

## Verification

After installation, verify:
```bash
python3 -c "import pydantic; print(f'✅ Pydantic {pydantic.__version__}')"
python3 -c "import fastapi; print(f'✅ FastAPI {fastapi.__version__}')"
```

## If All Else Fails

Use Python 3.11 or 3.12 (most stable):
```bash
# Install Python 3.12
brew install python@3.12

# Create new venv
python3.12 -m venv ../.venv312
source ../.venv312/bin/activate

# Install and run
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Success Indicators

When working, you'll see:
```
Successfully installed fastapi-0.115.0 pydantic-2.10.3 uvicorn-0.32.0 ...
```

Then:
```
INFO:     Uvicorn running on http://127.0.0.1:8000