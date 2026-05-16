# Legacy Code Surgeon AI - Postman API Collection

## Base URL
```
http://localhost:8000
```

---

## 📋 All API Endpoints

### 1. Root Endpoint
**GET** `/`

**Description:** Check if API is running

**Response:**
```json
{
  "message": "Legacy Code Surgeon AI API",
  "version": "1.0.0",
  "status": "running"
}
```

---

### 2. Health Check
**GET** `/health`

**Description:** Check API health and Bob AI configuration

**Response:**
```json
{
  "status": "healthy",
  "bob_ai_configured": true
}
```

---

## 🔄 Migration Workflow Endpoints

### 3. Upload ZIP Project
**POST** `/api/upload`

**Description:** Upload a ZIP file containing your project

**Headers:**
- None required (multipart/form-data is automatic)

**Body:** `form-data`
- Key: `file`
- Type: `File`
- Value: Select your `.zip` file

**Response:**
```json
{
  "project_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "message": "Project uploaded and extracted successfully",
  "files_extracted": 42
}
```

**Postman Setup:**
1. Method: POST
2. URL: `http://localhost:8000/api/upload`
3. Body → form-data
4. Key: `file` (change type to File)
5. Value: Click "Select Files" and choose your ZIP

---

### 4. Clone GitHub Repository
**POST** `/api/github`

**Description:** Clone a GitHub repository

**Headers:**
```
Content-Type: application/json
```

**Body:** `raw (JSON)`
```json
{
  "repo_url": "https://github.com/username/repository"
}
```

**Response:**
```json
{
  "project_id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
  "message": "Successfully cloned repository from https://github.com/username/repository",
  "files_extracted": 156
}
```

**Postman Setup:**
1. Method: POST
2. URL: `http://localhost:8000/api/github`
3. Headers: `Content-Type: application/json`
4. Body → raw → JSON
5. Paste the JSON above

---

### 5. Scan Repository
**GET** `/api/scan/{project_id}`

**Description:** Scan uploaded/cloned repository to detect framework

**Path Parameters:**
- `project_id` (string, required) - The project ID from upload/clone response

**Example URL:**
```
http://localhost:8000/api/scan/a1b2c3d4-e5f6-7890-abcd-ef1234567890
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

**Postman Setup:**
1. Method: GET
2. URL: `http://localhost:8000/api/scan/{{project_id}}`
3. Replace `{{project_id}}` with actual ID

---

### 6. Generate Migration Plan
**POST** `/api/plan/{project_id}`

**Description:** Generate AI-powered migration plan

**Path Parameters:**
- `project_id` (string, required)

**Headers:**
```
Content-Type: application/json
```

**Body:** `raw (JSON)`
```json
{
  "target_framework": "fastapi"
}
```

**Target Framework Options:**
- `fastapi`
- `springboot`
- `express`

**Example URL:**
```
http://localhost:8000/api/plan/a1b2c3d4-e5f6-7890-abcd-ef1234567890
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
  "flowchart": "graph TD\n    A[Start Migration] --> B[Scan Repository]\n    B --> C[Detect Framework]\n    ...",
  "estimated_complexity": "Medium"
}
```

**Postman Setup:**
1. Method: POST
2. URL: `http://localhost:8000/api/plan/{{project_id}}`
3. Headers: `Content-Type: application/json`
4. Body → raw → JSON

---

### 7. Migrate Project
**POST** `/api/migrate/{project_id}`

**Description:** Perform actual code migration

**Path Parameters:**
- `project_id` (string, required)

**Headers:**
```
Content-Type: application/json
```

**Body:** `raw (JSON)`
```json
{
  "target_framework": "fastapi"
}
```

**Example URL:**
```
http://localhost:8000/api/migrate/a1b2c3d4-e5f6-7890-abcd-ef1234567890
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

**Postman Setup:**
1. Method: POST
2. URL: `http://localhost:8000/api/migrate/{{project_id}}`
3. Headers: `Content-Type: application/json`
4. Body → raw → JSON

---

### 8. Rollback Migration
**POST** `/api/rollback/{project_id}`

**Description:** Rollback to pre-migration snapshot

**Path Parameters:**
- `project_id` (string, required)

**Example URL:**
```
http://localhost:8000/api/rollback/a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

**Response:**
```json
{
  "project_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "status": "rollback_successful",
  "message": "Project restored to pre-migration state"
}
```

**Postman Setup:**
1. Method: POST
2. URL: `http://localhost:8000/api/rollback/{{project_id}}`
3. No body required

---

### 9. Check Project Status
**GET** `/api/status/{project_id}`

**Description:** Get current project status

**Path Parameters:**
- `project_id` (string, required)

**Example URL:**
```
http://localhost:8000/api/status/a1b2c3d4-e5f6-7890-abcd-ef1234567890
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

**Status Values:**
- `uploaded` - Project uploaded/cloned
- `migration_in_progress` - Migration is running
- `migrated` - Migration completed
- `unknown` - Project not found

**Postman Setup:**
1. Method: GET
2. URL: `http://localhost:8000/api/status/{{project_id}}`

---

## 📊 Complete Workflow Example

### Step-by-Step Testing in Postman

1. **Upload Project**
   - POST `/api/upload`
   - Upload your ZIP file
   - Save the `project_id` from response

2. **Scan Repository**
   - GET `/api/scan/{project_id}`
   - Verify framework detection

3. **Generate Plan**
   - POST `/api/plan/{project_id}`
   - Body: `{"target_framework": "fastapi"}`
   - Review migration steps

4. **Perform Migration**
   - POST `/api/migrate/{project_id}`
   - Body: `{"target_framework": "fastapi"}`
   - Wait for completion

5. **Check Status**
   - GET `/api/status/{project_id}`
   - Verify migration completed

6. **Rollback (if needed)**
   - POST `/api/rollback/{project_id}`
   - Restore original state

---

## 🔧 Postman Environment Variables

Create these variables in Postman for easier testing:

| Variable | Initial Value | Current Value |
|----------|--------------|---------------|
| `base_url` | `http://localhost:8000` | `http://localhost:8000` |
| `project_id` | (empty) | (set after upload) |

**Usage in Postman:**
- URL: `{{base_url}}/api/scan/{{project_id}}`

---

## 📥 Import to Postman

### Quick Import JSON

Create a new collection in Postman and import this JSON:

```json
{
  "info": {
    "name": "Legacy Code Surgeon AI",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Health Check",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "{{base_url}}/health",
          "host": ["{{base_url}}"],
          "path": ["health"]
        }
      }
    },
    {
      "name": "Upload ZIP",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "formdata",
          "formdata": [
            {
              "key": "file",
              "type": "file",
              "src": []
            }
          ]
        },
        "url": {
          "raw": "{{base_url}}/api/upload",
          "host": ["{{base_url}}"],
          "path": ["api", "upload"]
        }
      }
    },
    {
      "name": "Clone GitHub",
      "request": {
        "method": "POST",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"repo_url\": \"https://github.com/username/repo\"\n}"
        },
        "url": {
          "raw": "{{base_url}}/api/github",
          "host": ["{{base_url}}"],
          "path": ["api", "github"]
        }
      }
    },
    {
      "name": "Scan Repository",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "{{base_url}}/api/scan/{{project_id}}",
          "host": ["{{base_url}}"],
          "path": ["api", "scan", "{{project_id}}"]
        }
      }
    },
    {
      "name": "Generate Plan",
      "request": {
        "method": "POST",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"target_framework\": \"fastapi\"\n}"
        },
        "url": {
          "raw": "{{base_url}}/api/plan/{{project_id}}",
          "host": ["{{base_url}}"],
          "path": ["api", "plan", "{{project_id}}"]
        }
      }
    },
    {
      "name": "Migrate Project",
      "request": {
        "method": "POST",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"target_framework\": \"fastapi\"\n}"
        },
        "url": {
          "raw": "{{base_url}}/api/migrate/{{project_id}}",
          "host": ["{{base_url}}"],
          "path": ["api", "migrate", "{{project_id}}"]
        }
      }
    },
    {
      "name": "Rollback",
      "request": {
        "method": "POST",
        "header": [],
        "url": {
          "raw": "{{base_url}}/api/rollback/{{project_id}}",
          "host": ["{{base_url}}"],
          "path": ["api", "rollback", "{{project_id}}"]
        }
      }
    },
    {
      "name": "Check Status",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "{{base_url}}/api/status/{{project_id}}",
          "host": ["{{base_url}}"],
          "path": ["api", "status", "{{project_id}}"]
        }
      }
    }
  ],
  "variable": [
    {
      "key": "base_url",
      "value": "http://localhost:8000"
    },
    {
      "key": "project_id",
      "value": ""
    }
  ]
}
```

---

## 🎯 Quick Test Checklist

- [ ] GET `/health` - Verify API is running
- [ ] POST `/api/upload` - Upload test ZIP
- [ ] GET `/api/scan/{project_id}` - Check framework detection
- [ ] POST `/api/plan/{project_id}` - Generate migration plan
- [ ] POST `/api/migrate/{project_id}` - Perform migration
- [ ] GET `/api/status/{project_id}` - Check completion
- [ ] POST `/api/rollback/{project_id}` - Test rollback

---

## 📝 Notes

- All endpoints support CORS (any origin)
- No authentication required (hackathon MVP)
- Replace `{project_id}` with actual UUID from responses
- Interactive API docs available at: `http://localhost:8000/docs`
- Alternative docs at: `http://localhost:8000/redoc`

---

## 🐛 Common Errors

### 404 - Project Not Found
```json
{
  "detail": "Project not found"
}
```
**Solution:** Check project_id is correct

### 400 - Invalid Migration Path
```json
{
  "detail": "Migration from django to unsupported is not supported"
}
```
**Solution:** Use supported target framework (fastapi, springboot, express)

### 500 - Server Error
```json
{
  "detail": "Migration failed: ..."
}
```
**Solution:** Check server logs for details