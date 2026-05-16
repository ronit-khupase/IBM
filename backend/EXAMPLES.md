# Legacy Code Surgeon AI - API Examples

## Complete Workflow Example

### 1. Upload a Django Project

```bash
# Create a test Django project ZIP
curl -X POST "http://localhost:8000/api/upload" \
  -F "file=@django-blog.zip"
```

**Response:**
```json
{
  "project_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "message": "Project uploaded and extracted successfully",
  "files_extracted": 42
}
```

### 2. Scan the Project

```bash
curl -X GET "http://localhost:8000/api/scan/a1b2c3d4-e5f6-7890-abcd-ef1234567890"
```

**Response:**
```json
{
  "project_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "framework": "django",
  "files_scanned": 42,
  "summary": "Detected DJANGO framework. Scanned 42 files. Contains: 25 python, 8 html, 3 css, 6 config. Patterns: MVT, ORM, Admin Panel.",
  "detected_patterns": ["MVT", "ORM", "Admin Panel"]
}
```

### 3. Generate Migration Plan

```bash
curl -X POST "http://localhost:8000/api/plan/a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
  -H "Content-Type: application/json" \
  -d '{
    "target_framework": "fastapi"
  }'
```

**Response:**
```json
{
  "project_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "steps": [
    "1. Analyze Django project structure",
    "2. Set up FastAPI project skeleton",
    "3. Convert models/entities",
    "4. Migrate routes/controllers to modern endpoints",
    "5. Update configuration and dependencies",
    "6. Implement async patterns where applicable",
    "7. Add error handling and validation",
    "8. Test migrated endpoints",
    "9. Update documentation"
  ],
  "bugs": [
    "Database connection string format differences",
    "Authentication middleware compatibility",
    "Session management changes",
    "Static file serving configuration"
  ],
  "suggestions": [
    "Use async/await for better performance",
    "Implement proper dependency injection",
    "Add comprehensive API documentation",
    "Use modern validation libraries",
    "Implement proper error handling"
  ],
  "flowchart": "graph TD\n    A[Start Migration] --> B[Scan Repository]\n    B --> C[Detect Framework]\n    C --> D[Generate Plan]\n    D --> E[Create Snapshot]\n    E --> F[Convert Models]\n    F --> G[Migrate Routes]\n    G --> H[Update Config]\n    H --> I[Test Migration]\n    I --> J{Tests Pass?}\n    J -->|Yes| K[Complete]\n    J -->|No| L[Rollback]\n    L --> E",
  "estimated_complexity": "Medium"
}
```

### 4. Perform Migration

```bash
curl -X POST "http://localhost:8000/api/migrate/a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
  -H "Content-Type: application/json" \
  -d '{
    "target_framework": "fastapi"
  }'
```

**Response:**
```json
{
  "project_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "converted_files": 15,
  "output_path": "/path/to/storage/migrated/a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "target_framework": "fastapi",
  "status": "completed"
}
```

### 5. Check Status

```bash
curl -X GET "http://localhost:8000/api/status/a1b2c3d4-e5f6-7890-abcd-ef1234567890"
```

**Response:**
```json
{
  "project_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "status": "migrated",
  "framework": null,
  "target_framework": null,
  "progress": 100,
  "details": {
    "migrated_files": 15,
    "output_path": "/path/to/storage/migrated/a1b2c3d4-e5f6-7890-abcd-ef1234567890"
  }
}
```

### 6. Rollback (if needed)

```bash
curl -X POST "http://localhost:8000/api/rollback/a1b2c3d4-e5f6-7890-abcd-ef1234567890"
```

**Response:**
```json
{
  "project_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "status": "rollback_successful",
  "message": "Project restored to pre-migration state"
}
```

---

## GitHub Repository Example

### Clone Spring Boot Repository

```bash
curl -X POST "http://localhost:8000/api/github" \
  -H "Content-Type: application/json" \
  -d '{
    "repo_url": "https://github.com/spring-projects/spring-petclinic"
  }'
```

**Response:**
```json
{
  "project_id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
  "message": "Successfully cloned repository from https://github.com/spring-projects/spring-petclinic",
  "files_extracted": 256
}
```

### Scan Spring Project

```bash
curl -X GET "http://localhost:8000/api/scan/b2c3d4e5-f6a7-8901-bcde-f12345678901"
```

**Response:**
```json
{
  "project_id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
  "framework": "spring",
  "files_scanned": 256,
  "summary": "Detected SPRING framework. Scanned 256 files. Contains: 120 java, 45 xml, 30 html, 15 css, 46 config. Patterns: MVC, Dependency Injection, Annotations.",
  "detected_patterns": ["MVC", "Dependency Injection", "Annotations"]
}
```

### Migrate Spring to FastAPI

```bash
curl -X POST "http://localhost:8000/api/migrate/b2c3d4e5-f6a7-8901-bcde-f12345678901" \
  -H "Content-Type: application/json" \
  -d '{
    "target_framework": "fastapi"
  }'
```

---

## Python Script Example

```python
import requests
import time

BASE_URL = "http://localhost:8000/api"

def migrate_project(zip_file_path):
    """Complete migration workflow"""
    
    # 1. Upload project
    print("📦 Uploading project...")
    with open(zip_file_path, 'rb') as f:
        response = requests.post(
            f"{BASE_URL}/upload",
            files={'file': f}
        )
    
    project_id = response.json()['project_id']
    print(f"✅ Project uploaded: {project_id}")
    
    # 2. Scan project
    print("\n🔍 Scanning project...")
    response = requests.get(f"{BASE_URL}/scan/{project_id}")
    scan_data = response.json()
    print(f"✅ Framework detected: {scan_data['framework']}")
    print(f"   Files scanned: {scan_data['files_scanned']}")
    
    # 3. Generate plan
    print("\n📋 Generating migration plan...")
    response = requests.post(
        f"{BASE_URL}/plan/{project_id}",
        json={"target_framework": "fastapi"}
    )
    plan_data = response.json()
    print(f"✅ Plan generated with {len(plan_data['steps'])} steps")
    print(f"   Complexity: {plan_data['estimated_complexity']}")
    
    # 4. Perform migration
    print("\n🔄 Starting migration...")
    response = requests.post(
        f"{BASE_URL}/migrate/{project_id}",
        json={"target_framework": "fastapi"}
    )
    migrate_data = response.json()
    print(f"✅ Migration complete!")
    print(f"   Converted files: {migrate_data['converted_files']}")
    print(f"   Output: {migrate_data['output_path']}")
    
    # 5. Check status
    print("\n📊 Checking status...")
    response = requests.get(f"{BASE_URL}/status/{project_id}")
    status_data = response.json()
    print(f"✅ Status: {status_data['status']}")
    print(f"   Progress: {status_data['progress']}%")
    
    return project_id

# Usage
if __name__ == "__main__":
    project_id = migrate_project("django-blog.zip")
    print(f"\n🎉 Migration complete! Project ID: {project_id}")
```

---

## JavaScript/Node.js Example

```javascript
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

const BASE_URL = 'http://localhost:8000/api';

async function migrateProject(zipFilePath) {
  try {
    // 1. Upload project
    console.log('📦 Uploading project...');
    const formData = new FormData();
    formData.append('file', fs.createReadStream(zipFilePath));
    
    const uploadResponse = await axios.post(`${BASE_URL}/upload`, formData, {
      headers: formData.getHeaders()
    });
    
    const projectId = uploadResponse.data.project_id;
    console.log(`✅ Project uploaded: ${projectId}`);
    
    // 2. Scan project
    console.log('\n🔍 Scanning project...');
    const scanResponse = await axios.get(`${BASE_URL}/scan/${projectId}`);
    console.log(`✅ Framework: ${scanResponse.data.framework}`);
    
    // 3. Generate plan
    console.log('\n📋 Generating migration plan...');
    const planResponse = await axios.post(`${BASE_URL}/plan/${projectId}`, {
      target_framework: 'fastapi'
    });
    console.log(`✅ Plan generated with ${planResponse.data.steps.length} steps`);
    
    // 4. Migrate
    console.log('\n🔄 Starting migration...');
    const migrateResponse = await axios.post(`${BASE_URL}/migrate/${projectId}`, {
      target_framework: 'fastapi'
    });
    console.log(`✅ Converted ${migrateResponse.data.converted_files} files`);
    
    return projectId;
  } catch (error) {
    console.error('❌ Error:', error.response?.data || error.message);
    throw error;
  }
}

// Usage
migrateProject('django-blog.zip')
  .then(projectId => console.log(`\n🎉 Success! Project ID: ${projectId}`))
  .catch(err => console.error('Failed:', err));
```

---

## cURL Complete Workflow

```bash
#!/bin/bash

# Configuration
BASE_URL="http://localhost:8000/api"
ZIP_FILE="django-blog.zip"

echo "🚀 Starting Legacy Code Migration"

# 1. Upload
echo -e "\n📦 Step 1: Uploading project..."
UPLOAD_RESPONSE=$(curl -s -X POST "$BASE_URL/upload" -F "file=@$ZIP_FILE")
PROJECT_ID=$(echo $UPLOAD_RESPONSE | jq -r '.project_id')
echo "✅ Project ID: $PROJECT_ID"

# 2. Scan
echo -e "\n🔍 Step 2: Scanning repository..."
SCAN_RESPONSE=$(curl -s -X GET "$BASE_URL/scan/$PROJECT_ID")
FRAMEWORK=$(echo $SCAN_RESPONSE | jq -r '.framework')
echo "✅ Detected framework: $FRAMEWORK"

# 3. Plan
echo -e "\n📋 Step 3: Generating migration plan..."
PLAN_RESPONSE=$(curl -s -X POST "$BASE_URL/plan/$PROJECT_ID" \
  -H "Content-Type: application/json" \
  -d '{"target_framework": "fastapi"}')
STEPS=$(echo $PLAN_RESPONSE | jq -r '.steps | length')
echo "✅ Generated plan with $STEPS steps"

# 4. Migrate
echo -e "\n🔄 Step 4: Performing migration..."
MIGRATE_RESPONSE=$(curl -s -X POST "$BASE_URL/migrate/$PROJECT_ID" \
  -H "Content-Type: application/json" \
  -d '{"target_framework": "fastapi"}')
CONVERTED=$(echo $MIGRATE_RESPONSE | jq -r '.converted_files')
echo "✅ Converted $CONVERTED files"

# 5. Status
echo -e "\n📊 Step 5: Checking final status..."
STATUS_RESPONSE=$(curl -s -X GET "$BASE_URL/status/$PROJECT_ID")
STATUS=$(echo $STATUS_RESPONSE | jq -r '.status')
echo "✅ Status: $STATUS"

echo -e "\n🎉 Migration complete! Project ID: $PROJECT_ID"
```

---

## Sample Bob AI Prompts

### Repository Analysis Prompt
```
Analyze this Django repository:

Files scanned: 42
Key files detected: views.py, models.py, urls.py, settings.py, admin.py

Provide:
1. Architecture overview
2. Legacy patterns detected
3. Potential issues
4. Modernization opportunities

Format as JSON with keys: architecture, legacy_patterns, issues, opportunities
```

### Code Migration Prompt
```
Convert this Django view to FastAPI:

```python
from django.shortcuts import render
from django.http import JsonResponse
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    data = [{'id': p.id, 'title': p.title} for p in posts]
    return JsonResponse(data, safe=False)
```

Requirements:
- Maintain functionality
- Use modern FastAPI patterns
- Add type hints
- Use async/await where appropriate
- Add proper error handling
- Include comments for complex logic

Return ONLY the converted code, no explanations.
```

### Expected FastAPI Output
```python
from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

router = APIRouter()

class PostResponse(BaseModel):
    id: int
    title: str

@router.get("/posts", response_model=List[PostResponse])
async def get_posts():
    """Get all posts"""
    try:
        # TODO: Replace with actual database query
        posts = await Post.get_all()
        return [PostResponse(id=p.id, title=p.title) for p in posts]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

---

## Health Check

```bash
curl http://localhost:8000/health
```

**Response:**
```json
{
  "status": "healthy",
  "bob_ai_configured": true
}
```

---

## Error Handling Examples

### Project Not Found
```bash
curl -X GET "http://localhost:8000/api/scan/invalid-id"
```

**Response (404):**
```json
{
  "detail": "Project not found"
}
```

### Invalid Migration Path
```bash
curl -X POST "http://localhost:8000/api/plan/project-id" \
  -H "Content-Type: application/json" \
  -d '{"target_framework": "unsupported"}'
```

**Response (400):**
```json
{
  "detail": "Migration from django to unsupported is not supported"
}