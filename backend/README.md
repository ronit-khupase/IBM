# Legacy Code Surgeon AI - Backend

AI-powered legacy code modernization and migration platform built with FastAPI.

## Features

- 📦 **ZIP Upload & GitHub Clone**: Upload projects or clone from GitHub
- 🔍 **Smart Scanning**: Detect frameworks (Django, Spring, Flask, Express)
- 🤖 **AI-Powered Migration**: Convert legacy code using IBM Bob AI
- 📊 **Migration Plans**: Generate detailed migration strategies
- 🔄 **Rollback Support**: Snapshot and restore functionality
- 📈 **Flowcharts**: Mermaid.js visualization of migration process

## Supported Migrations

| Source Framework | Target Frameworks |
|-----------------|-------------------|
| Django | FastAPI, Express |
| Spring Framework | Spring Boot, FastAPI |
| Flask | FastAPI |
| Express | FastAPI |

## Prerequisites

- Python 3.11+
- IBM Bob AI API Key

## Installation

1. **Clone the repository**
```bash
cd backend
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env and add your BOB_AI_API_KEY
```

## Running the Server

```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://localhost:8000`

API Documentation: `http://localhost:8000/docs`

## API Endpoints

### 1. Upload Project (ZIP)
```bash
curl -X POST "http://localhost:8000/api/upload" \
  -F "file=@project.zip"
```

**Response:**
```json
{
  "project_id": "uuid",
  "message": "Project uploaded successfully",
  "files_extracted": 42
}
```

### 2. Clone GitHub Repository
```bash
curl -X POST "http://localhost:8000/api/github" \
  -H "Content-Type: application/json" \
  -d '{"repo_url": "https://github.com/user/repo"}'
```

**Response:**
```json
{
  "project_id": "uuid",
  "message": "Successfully cloned repository",
  "files_extracted": 156
}
```

### 3. Scan Repository
```bash
curl -X GET "http://localhost:8000/api/scan/{project_id}"
```

**Response:**
```json
{
  "project_id": "uuid",
  "framework": "django",
  "files_scanned": 42,
  "summary": "Detected DJANGO framework...",
  "detected_patterns": ["MVT", "ORM", "Admin Panel"]
}
```

### 4. Generate Migration Plan
```bash
curl -X POST "http://localhost:8000/api/plan/{project_id}" \
  -H "Content-Type: application/json" \
  -d '{"target_framework": "fastapi"}'
```

**Response:**
```json
{
  "project_id": "uuid",
  "steps": ["1. Analyze project...", "2. Convert models..."],
  "bugs": ["Database connection format differences"],
  "suggestions": ["Use async/await patterns"],
  "flowchart": "graph TD\n  A[Start]...",
  "estimated_complexity": "Medium"
}
```

### 5. Migrate Project
```bash
curl -X POST "http://localhost:8000/api/migrate/{project_id}" \
  -H "Content-Type: application/json" \
  -d '{"target_framework": "fastapi"}'
```

**Response:**
```json
{
  "project_id": "uuid",
  "converted_files": 15,
  "output_path": "/path/to/migrated",
  "target_framework": "fastapi",
  "status": "completed"
}
```

### 6. Rollback Migration
```bash
curl -X POST "http://localhost:8000/api/rollback/{project_id}"
```

**Response:**
```json
{
  "project_id": "uuid",
  "status": "rollback_successful",
  "message": "Project restored to pre-migration state"
}
```

### 7. Check Project Status
```bash
curl -X GET "http://localhost:8000/api/status/{project_id}"
```

**Response:**
```json
{
  "project_id": "uuid",
  "status": "migrated",
  "progress": 100,
  "details": {
    "migrated_files": 15,
    "output_path": "/path/to/migrated"
  }
}
```

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI application
│   ├── api/                 # API endpoints
│   │   ├── upload.py
│   │   ├── github.py
│   │   ├── scan.py
│   │   ├── plan.py
│   │   ├── migrate.py
│   │   ├── rollback.py
│   │   └── status.py
│   ├── core/                # Core functionality
│   │   ├── bob_client.py    # IBM Bob AI integration
│   │   ├── scanner.py       # Repository scanning
│   │   ├── detector.py      # Framework detection
│   │   ├── planner.py       # Migration planning
│   │   ├── migrator.py      # Code migration
│   │   ├── flowchart.py     # Flowchart generation
│   │   ├── snapshot.py      # Backup/rollback
│   │   └── github_clone.py  # GitHub cloning
│   ├── models/
│   │   └── schemas.py       # Pydantic models
│   ├── utils/
│   │   └── file_utils.py    # File utilities
│   └── storage/             # File storage
│       ├── uploads/         # Uploaded projects
│       ├── repos/           # Cloned repositories
│       ├── migrated/        # Migrated projects
│       └── snapshots/       # Backup snapshots
├── requirements.txt
├── .env.example
└── README.md
```

## IBM Bob AI Integration

The platform uses IBM Bob AI for:
- Repository analysis
- Migration plan generation
- Code transformation
- Flowchart generation

### Sample Bob AI Prompts

**Repository Analysis:**
```
Analyze this Django repository:
Files scanned: 42
Key files: views.py, models.py, urls.py
Provide architecture overview and modernization opportunities.
```

**Code Migration:**
```
Convert this Django view to FastAPI:
[source code]
Requirements:
- Maintain functionality
- Use modern FastAPI patterns
- Add type hints
- Use async/await
```

## Development

### Adding New Framework Support

1. Update `detector.py` with detection logic
2. Add migration patterns in `migrator.py`
3. Update `planner.py` for migration paths

### Testing

```bash
# Run with reload for development
uvicorn app.main:app --reload --port 8000

# Test endpoints
curl http://localhost:8000/health
```

## Storage

All project files are stored in `app/storage/`:
- `uploads/` - Uploaded ZIP projects
- `repos/` - Cloned GitHub repositories
- `migrated/` - Migrated output projects
- `snapshots/` - Pre-migration backups

## Error Handling

The API returns standard HTTP status codes:
- `200` - Success
- `400` - Bad request (invalid input)
- `404` - Project not found
- `500` - Server error

## Security Notes

⚠️ **This is a hackathon MVP**:
- No authentication implemented
- CORS allows all origins
- File uploads not sanitized
- No rate limiting

For production use, implement:
- Authentication & authorization
- Input validation & sanitization
- Rate limiting
- Proper CORS configuration
- File size limits
- Virus scanning

## Troubleshooting

**Import errors:**
```bash
pip install -r requirements.txt
```

**Bob AI errors:**
```bash
# Check .env file
cat .env
# Verify BOB_AI_API_KEY is set
```

**Storage permissions:**
```bash
# Ensure storage directories exist
mkdir -p app/storage/{uploads,repos,migrated,snapshots}
```

## License

MIT License - Hackathon MVP

## Support

For issues or questions, please open an issue on GitHub.