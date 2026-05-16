**User:**

<task>
analyze project and rewrite requirements.txt
</task>
<environment_details>
# VSCode Visible Files
backend\app\storage\migrated\798bd2af-067c-4f1e-8491-8e5398c28b6c\info\models.py

# VSCode Open Tabs
backend/app/core/detector.py,backend/app/core/migrator.py,backend/app/core/validators.py,backend/app/core/transformer.py,backend/app/storage/migrated/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/models.py,backend/app/core/bob_client.py,backend/MIGRATION_GUIDE.md,backend/DIRECTORY_STRUCTURE.md,backend/app/core/flowchart.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-16T14:28:28.683Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.00

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>


# Current Workspace Directory (c:/IBM) Files
.DS_Store
.venv/
backend/
backend/.gitignore
backend/BOB_AI_INTEGRATION_STATUS.md
backend/DIRECTORY_STRUCTURE.md
backend/EXAMPLES.md
backend/MIGRATION_GUIDE.md
backend/POSTMAN_COLLECTION.md
backend/PYTHON_314_FIX.md
backend/README.md
backend/requirements.txt
backend/SETUP.md
backend/test_bob_api.py
backend/app/
backend/app/__init__.py
backend/app/main.py
backend/app/api/
backend/app/api/__init__.py
backend/app/api/github.py
backend/app/api/migrate.py
backend/app/api/plan.py
backend/app/api/rollback.py
backend/app/api/scan.py
backend/app/api/status.py
backend/app/api/upload.py
backend/app/core/
backend/app/core/__init__.py
backend/app/core/bob_client.py
backend/app/core/detector.py
backend/app/core/flowchart.py
backend/app/core/github_clone.py
backend/app/core/migrator.py
backend/app/core/planner.py
backend/app/core/scanner.py
backend/app/core/snapshot.py
backend/app/core/transformer.py
backend/app/core/validators.py
backend/app/models/
backend/app/models/__init__.py
backend/app/models/schemas.py
backend/app/storage/
backend/app/storage/migrated/
backend/app/storage/migrated/798bd2af-067c-4f1e-8491-8e5398c28b6c/
backend/app/storage/migrated/798bd2af-067c-4f1e-8491-8e5398c28b6c/apis/
backend/app/storage/migrated/798bd2af-067c-4f1e-8491-8e5398c28b6c/CollegeERP/
backend/app/storage/migrated/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/
backend/app/storage/repos/
backend/app/storage/repos/.gitkeep
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/apis/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/apis/migrations/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/CollegeERP/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/migrations/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/static/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/static/info/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/static/info/bootstrap/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/static/info/bootstrap/css/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/static/info/bootstrap/js/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/static/info/bootstrap/js/demo/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/static/info/bootstrap/scss/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/static/info/homepage/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/static/info/homepage/css/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/static/info/images/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/templates/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/templates/admin/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/templates/admin/attendance/
backend/app/storage/repos/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/templates/info/
backend/app/storage/snapshots/
backend/app/storage/snapshots/.gitkeep
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/apis/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/apis/migrations/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/CollegeERP/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/info/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/info/migrations/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/info/static/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/info/static/info/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/info/static/info/bootstrap/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/info/static/info/bootstrap/css/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/info/static/info/bootstrap/js/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/info/static/info/bootstrap/js/demo/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/info/static/info/bootstrap/scss/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/info/static/info/homepage/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/info/static/info/homepage/css/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/info/static/info/images/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/info/templates/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/info/templates/admin/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/info/templates/admin/attendance/
backend/app/storage/snapshots/4dce9f30-2157-43e5-a9c2-80fbe73cc2c4/20260516_131549/info/templates/info/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/apis/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/apis/migrations/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/CollegeERP/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/info/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/info/migrations/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/info/static/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/info/static/info/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/info/static/info/bootstrap/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/info/static/info/bootstrap/css/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/info/static/info/bootstrap/js/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/info/static/info/bootstrap/js/demo/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/info/static/info/bootstrap/scss/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/info/static/info/homepage/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/info/static/info/homepage/css/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/info/static/info/images/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/info/templates/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/info/templates/admin/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/info/templates/admin/attendance/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_190530/info/templates/info/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/apis/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/apis/migrations/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/CollegeERP/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/info/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/info/migrations/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/info/static/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/info/static/info/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/info/static/info/bootstrap/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/info/static/info/bootstrap/css/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/info/static/info/bootstrap/js/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/info/static/info/bootstrap/js/demo/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/info/static/info/bootstrap/scss/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/info/static/info/homepage/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/info/static/info/homepage/css/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/info/static/info/images/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/info/templates/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/info/templates/admin/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/info/templates/admin/attendance/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192227/info/templates/info/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/apis/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/apis/migrations/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/CollegeERP/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/info/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/info/migrations/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/info/static/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/info/static/info/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/info/static/info/bootstrap/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/info/static/info/bootstrap/css/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/info/static/info/bootstrap/js/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/info/static/info/bootstrap/js/demo/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/info/static/info/bootstrap/scss/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/info/static/info/homepage/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/info/static/info/homepage/css/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/info/static/info/images/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/info/templates/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/info/templates/admin/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/info/templates/admin/attendance/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_192431/info/templates/info/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/apis/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/apis/migrations/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/CollegeERP/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/info/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/info/migrations/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/info/static/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/info/static/info/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/info/static/info/bootstrap/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/info/static/info/bootstrap/css/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/info/static/info/bootstrap/js/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/info/static/info/bootstrap/js/demo/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/info/static/info/bootstrap/scss/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/info/static/info/homepage/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/info/static/info/homepage/css/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/info/static/info/images/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/info/templates/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/info/templates/admin/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/info/templates/admin/attendance/
backend/app/storage/snapshots/798bd2af-067c-4f1e-8491-8e5398c28b6c/20260516_195722/info/templates/info/
backend/app/storage/uploads/
backend/app/storage/uploads/.gitkeep
backend/app/utils/
backend/app/utils/__init__.py
backend/app/utils/file_utils.py
bob_sessions/
bob_sessions/bob_task_may-16-2026_1-01-13-am.md
bob_sessions/bob_task_may-16-2026_7-56-08-pm.md
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

I'll analyze the project structure and dependencies to rewrite the requirements.txt file. Let me start by examining the current requirements.txt and the project's Python files to understand what dependencies are actually being used.

<read_file>
<args>
<file>
<path>backend/requirements.txt</path>
</file>
</args>
</read_file>

---

**User:**

[read_file for 'backend/requirements.txt'. Reading multiple files at once is more efficient for the LLM. If other files are relevant to your current task, please read them simultaneously.] Result:
<files>
<file><path>backend/requirements.txt</path>
<content lines="1-9">
1 | fastapi==0.115.0
2 | uvicorn[standard]==0.32.0
3 | python-multipart==0.0.12
4 | aiofiles==24.1.0
5 | httpx==0.27.2
6 | pydantic==2.10.3
7 | pydantic-settings==2.6.1
8 | python-dotenv==1.0.1
9 | GitPython==3.1.43
</content>
</file>
</files>
<environment_details>
# VSCode Visible Files
backend\app\storage\migrated\798bd2af-067c-4f1e-8491-8e5398c28b6c\info\models.py

# VSCode Open Tabs
backend/app/core/detector.py,backend/app/core/migrator.py,backend/app/core/validators.py,backend/app/core/transformer.py,backend/app/storage/migrated/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/models.py,backend/app/core/bob_client.py,backend/MIGRATION_GUIDE.md,backend/DIRECTORY_STRUCTURE.md,backend/app/core/flowchart.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-16T14:28:38.160Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.02

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

Now let me examine the main application files to understand all the dependencies being used:

<read_file>
<args>
<file>
<path>backend/app/main.py</path>
</file>
<file>
<path>backend/app/core/bob_client.py</path>
</file>
<file>
<path>backend/app/core/detector.py</path>
</file>
<file>
<path>backend/app/core/migrator.py</path>
</file>
<file>
<path>backend/app/core/transformer.py</path>
</file>
</args>
</read_file>

---

**User:**

[read_file for 5 files] Result:
<files>
<file><path>backend/app/main.py</path>
<content lines="1-67">
 1 | """
 2 | Legacy Code Surgeon AI - FastAPI Backend
 3 | Main application entry point
 4 | """
 5 | from fastapi import FastAPI
 6 | from fastapi.middleware.cors import CORSMiddleware
 7 | from dotenv import load_dotenv
 8 | import os
 9 | 
10 | # Load environment variables
11 | load_dotenv()
12 | 
13 | # Import routers
14 | from app.api import upload, github, scan, plan, migrate, rollback, status
15 | 
16 | # Create FastAPI app
17 | app = FastAPI(
18 |     title="Legacy Code Surgeon AI",
19 |     description="AI-powered legacy code modernization and migration platform",
20 |     version="1.0.0"
21 | )
22 | 
23 | # CORS configuration
24 | app.add_middleware(
25 |     CORSMiddleware,
26 |     allow_origins=["*"],  # In production, specify actual origins
27 |     allow_credentials=True,
28 |     allow_methods=["*"],
29 |     allow_headers=["*"],
30 | )
31 | 
32 | # Include routers
33 | app.include_router(upload.router, prefix="/api", tags=["Upload"])
34 | app.include_router(github.router, prefix="/api", tags=["GitHub"])
35 | app.include_router(scan.router, prefix="/api", tags=["Scan"])
36 | app.include_router(plan.router, prefix="/api", tags=["Plan"])
37 | app.include_router(migrate.router, prefix="/api", tags=["Migrate"])
38 | app.include_router(rollback.router, prefix="/api", tags=["Rollback"])
39 | app.include_router(status.router, prefix="/api", tags=["Status"])
40 | 
41 | 
42 | @app.get("/")
43 | async def root():
44 |     """Root endpoint"""
45 |     return {
46 |         "message": "Legacy Code Surgeon AI API",
47 |         "version": "1.0.0",
48 |         "status": "running"
49 |     }
50 | 
51 | 
52 | @app.get("/health")
53 | async def health_check():
54 |     """Health check endpoint"""
55 |     bob_api_key = os.getenv("BOB_AI_API_KEY")
56 |     
57 |     return {
58 |         "status": "healthy",
59 |         "bob_ai_configured": bool(bob_api_key)
60 |     }
61 | 
62 | 
63 | if __name__ == "__main__":
64 |     import uvicorn
65 |     uvicorn.run(app, host="0.0.0.0", port=8000)
66 | 
67 | # Made with Bob
</content>
</file>
<file><path>backend/app/core/bob_client.py</path>
<content lines="1-585">
  1 | """
  2 | IBM Bob AI API Client
  3 | Handles all interactions with IBM Bob AI for code analysis and migration
  4 | """
  5 | import os
  6 | import json
  7 | import httpx
  8 | from typing import Dict, Any, Optional, List
  9 | from pathlib import Path
 10 | 
 11 | 
 12 | class BobAIClient:
 13 |     """Client for IBM Bob AI API"""
 14 |     
 15 |     def __init__(self):
 16 |         self.api_key = os.getenv("BOB_AI_API_KEY")
 17 |         # Use the correct Bob AI API endpoint
 18 |         self.api_url = os.getenv("BOB_AI_API_URL", "https://bob.build.cloud.ibm.com/v1/chat/completions")
 19 |         
 20 |         if not self.api_key:
 21 |             raise ValueError("BOB_AI_API_KEY environment variable not set")
 22 |         
 23 |         self.headers = {
 24 |             "Authorization": f"Bearer {self.api_key}",
 25 |             "Content-Type": "application/json",
 26 |             "Accept": "application/json, text/event-stream"
 27 |         }
 28 |     
 29 |     async def _make_request(self, prompt: str, context: Optional[str] = None) -> str:
 30 |         """
 31 |         Make async request to Bob AI API using JSON-RPC 2.0 format
 32 |         """
 33 |         import logging
 34 |         logger = logging.getLogger(__name__)
 35 |         
 36 |         # Build the full prompt with context
 37 |         full_prompt = prompt
 38 |         if context:
 39 |             full_prompt = f"Context:\n{context}\n\n{prompt}"
 40 |         
 41 |         # JSON-RPC 2.0 format for MCP server
 42 |         # Try simple prompt parameter
 43 |         payload = {
 44 |             "jsonrpc": "2.0",
 45 |             "id": "migration-request",
 46 |             "method": "prompt",
 47 |             "params": {
 48 |                 "prompt": full_prompt
 49 |             }
 50 |         }
 51 |         
 52 |         # DEBUG: Log request details
 53 |         print(f"\n{'='*80}")
 54 |         print(f"🔍 DEBUG: Bob AI Request")
 55 |         print(f"{'='*80}")
 56 |         print(f"URL: {self.api_url}")
 57 |         print(f"API Key: {self.api_key[:30]}..." if self.api_key else "No API key")
 58 |         print(f"Prompt length: {len(prompt)} characters")
 59 |         print(f"{'='*80}\n")
 60 |         
 61 |         async with httpx.AsyncClient(timeout=120.0, follow_redirects=True) as client:
 62 |             try:
 63 |                 print(f"📡 Sending request to Bob AI...")
 64 |                 response = await client.post(
 65 |                     self.api_url,
 66 |                     headers=self.headers,
 67 |                     json=payload
 68 |                 )
 69 |                 
 70 |                 print(f"✅ Response received: Status {response.status_code}")
 71 |                 print(f"Response headers: {dict(response.headers)}")
 72 |                 print(f"Content-Type: {response.headers.get('content-type', 'unknown')}")
 73 |                 
 74 |                 response.raise_for_status()
 75 |                 
 76 |                 # Check if response is Server-Sent Events (SSE)
 77 |                 content_type = response.headers.get('content-type', '')
 78 |                 if 'text/event-stream' in content_type:
 79 |                     print(f"📡 Parsing SSE stream...")
 80 |                     # Parse Server-Sent Events format
 81 |                     response_text = response.text
 82 |                     print(f"Raw SSE response length: {len(response_text)} characters")
 83 |                     print(f"First 200 chars: {response_text[:200]}")
 84 |                     
 85 |                     # Extract data from SSE format
 86 |                     # SSE format: "data: {...}\n\n"
 87 |                     content_parts = []
 88 |                     for line in response_text.split('\n'):
 89 |                         if line.startswith('data: '):
 90 |                             data_str = line[6:]  # Remove "data: " prefix
 91 |                             if data_str.strip() and data_str.strip() != '[DONE]':
 92 |                                 try:
 93 |                                     data_json = json.loads(data_str)
 94 |                                     content_parts.append(data_json)
 95 |                                 except json.JSONDecodeError:
 96 |                                     # If not JSON, treat as plain text
 97 |                                     content_parts.append(data_str)
 98 |                     
 99 |                     print(f"✅ Parsed {len(content_parts)} SSE events")
100 |                     
101 |                     # Combine all content parts
102 |                     if content_parts:
103 |                         # If parts are dicts, try to extract content
104 |                         if isinstance(content_parts[0], dict):
105 |                             result = content_parts[-1]  # Use last event as result
106 |                         else:
107 |                             # Plain text parts
108 |                             return '\n'.join(str(p) for p in content_parts)
109 |                     else:
110 |                         print(f"⚠️  No data events found in SSE stream")
111 |                         return "Error: Empty SSE response"
112 |                 else:
113 |                     # Regular JSON response
114 |                     result = response.json()
115 |                 
116 |                 print(f"📦 Response data keys: {list(result.keys())}")
117 |                 
118 |                 # Handle JSON-RPC 2.0 response format
119 |                 if "result" in result:
120 |                     # JSON-RPC success response
121 |                     rpc_result = result["result"]
122 |                     print(f"✅ JSON-RPC result type: {type(rpc_result)}")
123 |                     
124 |                     # Check for error
125 |                     if isinstance(rpc_result, dict) and rpc_result.get("isError"):
126 |                         error_content = rpc_result.get("content", [])
127 |                         if isinstance(error_content, list) and error_content:
128 |                             error_msg = error_content[0].get("text", "Unknown error")
129 |                         else:
130 |                             error_msg = str(error_content)
131 |                         print(f"❌ Bob AI Error: {error_msg}")
132 |                         return f"Error: {error_msg}"
133 |                     
134 |                     # Extract content from various possible structures
135 |                     if isinstance(rpc_result, dict):
136 |                         if "content" in rpc_result:
137 |                             content_data = rpc_result["content"]
138 |                             # Handle array of content objects
139 |                             if isinstance(content_data, list):
140 |                                 text_parts = []
141 |                                 for item in content_data:
142 |                                     if isinstance(item, dict) and "text" in item:
143 |                                         text_parts.append(item["text"])
144 |                                     else:
145 |                                         text_parts.append(str(item))
146 |                                 content = "\n".join(text_parts)
147 |                             else:
148 |                                 content = str(content_data)
149 |                         elif "text" in rpc_result:
150 |                             content = rpc_result["text"]
151 |                         elif "output" in rpc_result:
152 |                             content = rpc_result["output"]
153 |                         else:
154 |                             content = str(rpc_result)
155 |                     elif isinstance(rpc_result, str):
156 |                         content = rpc_result
157 |                     else:
158 |                         content = str(rpc_result)
159 |                     
160 |                     print(f"✅ Extracted content: {len(content)} characters")
161 |                     return content
162 |                     
163 |                 elif "error" in result:
164 |                     # JSON-RPC error response
165 |                     error = result["error"]
166 |                     error_msg = f"Bob AI Error: {error.get('message', 'Unknown error')}"
167 |                     print(f"❌ {error_msg}")
168 |                     return f"Error: {error_msg}"
169 |                     
170 |                 # Fallback for other formats
171 |                 elif "choices" in result:
172 |                     content = result["choices"][0]["message"]["content"]
173 |                     print(f"✅ Extracted from 'choices': {len(content)} characters")
174 |                     return content
175 |                 elif "response" in result:
176 |                     content = result["response"]
177 |                     print(f"✅ Extracted from 'response': {len(content)} characters")
178 |                     return content
179 |                 else:
180 |                     print(f"⚠️  Unknown response format, returning raw: {str(result)[:100]}")
181 |                     return str(result)
182 |                     
183 |             except httpx.ConnectError as e:
184 |                 error_msg = f"❌ CONNECTION ERROR: Cannot reach {self.api_url}\nError: {str(e)}\n\nPossible causes:\n1. Wrong API URL\n2. Network/firewall issue\n3. DNS resolution failure"
185 |                 print(error_msg)
186 |                 logger.error(error_msg)
187 |                 return f"Error communicating with Bob AI: {str(e)}"
188 |             except httpx.HTTPStatusError as e:
189 |                 error_msg = f"❌ HTTP ERROR: Status {e.response.status_code}\nResponse: {e.response.text[:200]}"
190 |                 print(error_msg)
191 |                 logger.error(error_msg)
192 |                 return f"Error communicating with Bob AI: {str(e)}"
193 |             except Exception as e:
194 |                 error_msg = f"❌ UNEXPECTED ERROR: {type(e).__name__}: {str(e)}"
195 |                 print(error_msg)
196 |                 logger.error(error_msg)
197 |                 return f"Error communicating with Bob AI: {str(e)}"
198 |     
199 |     async def analyze_repository(
200 |         self,
201 |         framework: str,
202 |         file_summary: Dict[str, Any],
203 |         file_count: int
204 |     ) -> Dict[str, Any]:
205 |         """
206 |         Analyze repository structure and provide insights
207 |         """
208 |         prompt = f"""
209 | Analyze this {framework} repository:
210 | 
211 | Files scanned: {file_count}
212 | Key files detected: {', '.join(file_summary.get('key_files', [])[:10])}
213 | 
214 | Provide:
215 | 1. Architecture overview
216 | 2. Legacy patterns detected
217 | 3. Potential issues
218 | 4. Modernization opportunities
219 | 
220 | Format as JSON with keys: architecture, legacy_patterns, issues, opportunities
221 | """
222 |         
223 |         response = await self._make_request(prompt)
224 |         
225 |         # Parse response (simplified for MVP)
226 |         return {
227 |             "architecture": response[:500] if len(response) > 500 else response,
228 |             "legacy_patterns": ["Monolithic structure", "Tight coupling", "Legacy dependencies"],
229 |             "issues": ["Outdated framework version", "Security vulnerabilities"],
230 |             "opportunities": ["Microservices architecture", "Modern async patterns", "API-first design"]
231 |         }
232 |     
233 |     async def generate_migration_plan(
234 |         self,
235 |         source_framework: str,
236 |         target_framework: str,
237 |         repository_summary: str
238 |     ) -> Dict[str, Any]:
239 |         """
240 |         Generate detailed migration plan
241 |         """
242 |         prompt = f"""
243 | Create a migration plan to convert a {source_framework} application to {target_framework}.
244 | 
245 | Repository summary:
246 | {repository_summary}
247 | 
248 | Provide:
249 | 1. Step-by-step migration steps (list)
250 | 2. Potential bugs/issues to watch for (list)
251 | 3. Modernization suggestions (list)
252 | 4. Estimated complexity (Low/Medium/High)
253 | 
254 | Format as JSON with keys: steps, bugs, suggestions, complexity
255 | """
256 |         
257 |         response = await self._make_request(prompt)
258 |         
259 |         # Simplified response for MVP
260 |         return {
261 |             "steps": [
262 |                 f"1. Analyze {source_framework} project structure",
263 |                 f"2. Set up {target_framework} project skeleton",
264 |                 "3. Convert models/entities",
265 |                 "4. Migrate routes/controllers to modern endpoints",
266 |                 "5. Update configuration and dependencies",
267 |                 "6. Implement async patterns where applicable",
268 |                 "7. Add error handling and validation",
269 |                 "8. Test migrated endpoints",
270 |                 "9. Update documentation"
271 |             ],
272 |             "bugs": [
273 |                 "Database connection string format differences",
274 |                 "Authentication middleware compatibility",
275 |                 "Session management changes",
276 |                 "Static file serving configuration"
277 |             ],
278 |             "suggestions": [
279 |                 "Use async/await for better performance",
280 |                 "Implement proper dependency injection",
281 |                 "Add comprehensive API documentation",
282 |                 "Use modern validation libraries",
283 |                 "Implement proper error handling"
284 |             ],
285 |             "complexity": "Medium"
286 |         }
287 |     
288 |     async def migrate_code(
289 |         self,
290 |         source_code: str,
291 |         source_framework: str,
292 |         target_framework: str,
293 |         file_info: Dict[str, Any]
294 |     ) -> str:
295 |         """
296 |         Convert source code from one framework to another
297 |         Enhanced with validation and pattern-based transformation
298 |         """
299 |         from app.core.validators import validate_fastapi_code
300 |         from app.core.transformer import get_enhanced_transformer
301 |         
302 |         print(f"\n{'='*60}")
303 |         print(f"🔄 Converting {file_info.get('filename', 'file')}")
304 |         print(f"   Category: {file_info.get('category', 'unknown')}")
305 |         print(f"   Framework: {source_framework} → {target_framework}")
306 |         print(f"{'='*60}\n")
307 |         
308 |         # Step 1: Try Bob AI conversion with enhanced prompt
309 |         print("📡 Step 1: Attempting Bob AI conversion...")
310 |         converted_code = await self._try_bob_ai_conversion(
311 |             source_code, source_framework, target_framework, file_info
312 |         )
313 |         
314 |         # Step 2: Validate the conversion
315 |         print("✅ Step 2: Validating conversion...")
316 |         validation = validate_fastapi_code(converted_code, file_info)
317 |         
318 |         if validation.is_valid:
319 |             print(f"✅ Bob AI conversion successful and validated!")
320 |             if validation.warnings:
321 |                 print(f"⚠️  Warnings: {len(validation.warnings)}")
322 |                 for warning in validation.warnings[:2]:
323 |                     print(f"   - {warning}")
324 |             return self._cleanup_code(converted_code)
325 |         
326 |         # Step 3: Bob AI failed validation, try with examples
327 |         print(f"❌ Bob AI conversion failed validation:")
328 |         for error in validation.errors[:3]:
329 |             print(f"   - {error}")
330 |         
331 |         print("\n📡 Step 3: Retrying Bob AI with examples...")
332 |         converted_code = await self._try_bob_ai_with_examples(
333 |             source_code, source_framework, target_framework, file_info
334 |         )
335 |         
336 |         validation = validate_fastapi_code(converted_code, file_info)
337 |         if validation.is_valid:
338 |             print(f"✅ Bob AI retry successful!")
339 |             return self._cleanup_code(converted_code)
340 |         
341 |         # Step 4: Fall back to enhanced pattern-based transformation
342 |         print(f"❌ Bob AI retry also failed")
343 |         print(f"\n🔧 Step 4: Using enhanced pattern-based transformation...")
344 |         
345 |         transformer = get_enhanced_transformer()
346 |         converted_code = transformer.transform(source_code, file_info)
347 |         
348 |         # Step 5: Final validation
349 |         print("✅ Step 5: Final validation...")
350 |         validation = validate_fastapi_code(converted_code, file_info)
351 |         
352 |         if validation.is_valid:
353 |             print(f"✅ Pattern-based conversion successful!")
354 |             return converted_code
355 |         else:
356 |             print(f"⚠️  Pattern-based conversion has issues:")
357 |             for error in validation.errors[:2]:
358 |                 print(f"   - {error}")
359 |             print(f"   Returning best effort conversion\n")
360 |             return converted_code
361 |     
362 |     async def _try_bob_ai_conversion(
363 |         self,
364 |         source_code: str,
365 |         source_framework: str,
366 |         target_framework: str,
367 |         file_info: Dict[str, Any]
368 |     ) -> str:
369 |         """Try Bob AI conversion with enhanced prompt"""
370 |         
371 |         category = file_info.get('category', 'code')
372 |         filename = file_info.get('filename', 'file')
373 |         
374 |         prompt = f"""You are an expert at converting {source_framework} code to {target_framework}.
375 | 
376 | Convert this {source_framework} {category} file ({filename}) to {target_framework}:
377 | 
378 | ```python
379 | {source_code}
380 | ```
381 | 
382 | CRITICAL REQUIREMENTS:
383 | 1. Remove ALL Django imports (django.*, rest_framework.*)
384 | 2. Add FastAPI imports (from fastapi import ...)
385 | 3. Convert Django patterns to FastAPI equivalents:
386 |    - APIView classes → @router.get/post/etc functions
387 |    - models.Model → Pydantic BaseModel
388 |    - Token auth → JWT dependencies
389 |    - Django ORM → SQLAlchemy queries
390 | 4. Use async/await for route handlers
391 | 5. Return ONLY the converted FastAPI code
392 | 6. Do NOT preserve Django code
393 | 7. Do NOT add explanatory text
394 | 
395 | Return the complete, working FastAPI code now:
396 | """
397 |         
398 |         converted_code = await self._make_request(prompt)
399 |         
400 |         # Check if Bob AI returned an error
401 |         if converted_code.startswith("Error:"):
402 |             print(f"   ⚠️  Bob AI unavailable: {converted_code[:100]}")
403 |             return converted_code
404 |         
405 |         return self._cleanup_code(converted_code)
406 |     
407 |     async def _try_bob_ai_with_examples(
408 |         self,
409 |         source_code: str,
410 |         source_framework: str,
411 |         target_framework: str,
412 |         file_info: Dict[str, Any]
413 |     ) -> str:
414 |         """Retry Bob AI with conversion examples"""
415 |         
416 |         example = self._get_conversion_example(file_info.get('category', 'view'))
417 |         
418 |         prompt = f"""Convert {source_framework} to {target_framework}.
419 | 
420 | EXAMPLE CONVERSION:
421 | {example}
422 | 
423 | Now convert this code following the same pattern:
424 | 
425 | ```python
426 | {source_code}
427 | ```
428 | 
429 | Return ONLY the converted FastAPI code:
430 | """
431 |         
432 |         converted_code = await self._make_request(prompt)
433 |         
434 |         if converted_code.startswith("Error:"):
435 |             return converted_code
436 |         
437 |         return self._cleanup_code(converted_code)
438 |     
439 |     def _get_conversion_example(self, category: str) -> str:
440 |         """Get example conversion for the given category"""
441 |         
442 |         if category == "view":
443 |             return """
444 | DJANGO CODE:
445 | ```python
446 | from rest_framework.views import APIView
447 | from rest_framework.response import Response
448 | 
449 | class ItemView(APIView):
450 |     def get(self, request):
451 |         items = Item.objects.all()
452 |         return Response({'items': items})
453 | ```
454 | 
455 | FASTAPI CODE:
456 | ```python
457 | from fastapi import APIRouter, Depends
458 | from sqlalchemy.orm import Session
459 | 
460 | router = APIRouter()
461 | 
462 | @router.get("/items")
463 | async def get_items(db: Session = Depends(get_db)):
464 |     items = db.query(Item).all()
465 |     return {"items": items}
466 | ```
467 | """
468 |         elif category == "model":
469 |             return """
470 | DJANGO CODE:
471 | ```python
472 | from django.db import models
473 | 
474 | class Item(models.Model):
475 |     name = models.CharField(max_length=100)
476 |     price = models.FloatField()
477 | ```
478 | 
479 | FASTAPI CODE:
480 | ```python
481 | from pydantic import BaseModel
482 | 
483 | class ItemBase(BaseModel):
484 |     name: str
485 |     price: float
486 | 
487 | class ItemCreate(ItemBase):
488 |     pass
489 | 
490 | class ItemResponse(ItemBase):
491 |     id: int
492 |     
493 |     class Config:
494 |         from_attributes = True
495 | ```
496 | """
497 |         else:
498 |             return "Convert Django code to FastAPI equivalents."
499 |     
500 |     def _cleanup_code(self, code: str) -> str:
501 |         """Clean up converted code"""
502 |         # Remove markdown code blocks
503 |         if "```" in code:
504 |             lines = code.split("\n")
505 |             code_lines = []
506 |             in_code_block = False
507 |             
508 |             for line in lines:
509 |                 if line.strip().startswith("```"):
510 |                     in_code_block = not in_code_block
511 |                     continue
512 |                 if in_code_block or not line.strip().startswith("```"):
513 |                     code_lines.append(line)
514 |             
515 |             code = "\n".join(code_lines)
516 |         
517 |         # Remove leading/trailing whitespace
518 |         code = code.strip()
519 |         
520 |         # Remove any explanatory text before imports
521 |         lines = code.split('\n')
522 |         first_import_idx = -1
523 |         for i, line in enumerate(lines):
524 |             if line.startswith('from ') or line.startswith('import '):
525 |                 first_import_idx = i
526 |                 break
527 |         
528 |         if first_import_idx > 0:
529 |             # Remove lines before first import if they're comments
530 |             if all(l.startswith('#') or not l.strip() for l in lines[:first_import_idx]):
531 |                 code = '\n'.join(lines[first_import_idx:])
532 |         
533 |         return code
534 |     
535 |     
536 |     async def generate_flowchart(
537 |         self,
538 |         migration_steps: List[str]
539 |     ) -> str:
540 |         """
541 |         Generate Mermaid.js flowchart for migration process
542 |         """
543 |         prompt = f"""
544 | Create a Mermaid.js flowchart for this migration process:
545 | 
546 | Steps:
547 | {chr(10).join(f'{i+1}. {step}' for i, step in enumerate(migration_steps))}
548 | 
549 | Use graph TD format. Include decision points and parallel processes where applicable.
550 | Return ONLY the Mermaid.js code, starting with 'graph TD'.
551 | """
552 |         
553 |         flowchart = await self._make_request(prompt)
554 |         
555 |         # Fallback flowchart if AI response is invalid
556 |         if not flowchart.strip().startswith("graph"):
557 |             flowchart = """graph TD
558 |     A[Start Migration] --> B[Scan Repository]
559 |     B --> C[Detect Framework]
560 |     C --> D[Generate Plan]
561 |     D --> E[Create Snapshot]
562 |     E --> F[Convert Models]
563 |     F --> G[Migrate Routes]
564 |     G --> H[Update Config]
565 |     H --> I[Test Migration]
566 |     I --> J{Tests Pass?}
567 |     J -->|Yes| K[Complete]
568 |     J -->|No| L[Rollback]
569 |     L --> E"""
570 |         
571 |         return flowchart.strip()
572 | 
573 | 
574 | # Singleton instance
575 | _bob_client: Optional[BobAIClient] = None
576 | 
577 | 
578 | def get_bob_client() -> BobAIClient:
579 |     """Get or create Bob AI client instance"""
580 |     global _bob_client
581 |     if _bob_client is None:
582 |         _bob_client = BobAIClient()
583 |     return _bob_client
584 | 
585 | # Made with Bob
</content>
</file>
<file><path>backend/app/core/detector.py</path>
<content lines="1-190">
  1 | """
  2 | Framework detection logic
  3 | Detects Django, Spring Framework, and other frameworks
  4 | """
  5 | from pathlib import Path
  6 | from typing import Dict, List, Optional
  7 | from app.utils.file_utils import scan_directory, read_file_content
  8 | 
  9 | 
 10 | class FrameworkDetector:
 11 |     """Detect framework type from repository structure"""
 12 |     
 13 |     def __init__(self, project_path: Path):
 14 |         self.project_path = project_path
 15 |         self.files = scan_directory(project_path)
 16 |     
 17 |     def detect(self) -> Dict[str, any]:
 18 |         """
 19 |         Detect framework and return details
 20 |         """
 21 |         # Check for Django
 22 |         if self._is_django():
 23 |             return {
 24 |                 "framework": "django",
 25 |                 "version": self._detect_django_version(),
 26 |                 "key_files": self._get_django_files(),
 27 |                 "patterns": ["MVT", "ORM", "Admin Panel"]
 28 |             }
 29 |         
 30 |         # Check for Spring
 31 |         if self._is_spring():
 32 |             return {
 33 |                 "framework": "spring",
 34 |                 "version": self._detect_spring_version(),
 35 |                 "key_files": self._get_spring_files(),
 36 |                 "patterns": ["MVC", "Dependency Injection", "Annotations"]
 37 |             }
 38 |         
 39 |         # Check for Flask
 40 |         if self._is_flask():
 41 |             return {
 42 |                 "framework": "flask",
 43 |                 "version": "unknown",
 44 |                 "key_files": self._get_flask_files(),
 45 |                 "patterns": ["Microframework", "Decorators"]
 46 |             }
 47 |         
 48 |         # Check for Express
 49 |         if self._is_express():
 50 |             return {
 51 |                 "framework": "express",
 52 |                 "version": "unknown",
 53 |                 "key_files": self._get_express_files(),
 54 |                 "patterns": ["Middleware", "Routes"]
 55 |             }
 56 |         
 57 |         # Unknown framework
 58 |         return {
 59 |             "framework": "unknown",
 60 |             "version": "unknown",
 61 |             "key_files": [],
 62 |             "patterns": []
 63 |         }
 64 |     
 65 |     def _is_django(self) -> bool:
 66 |         """Check if project is Django"""
 67 |         indicators = [
 68 |             "manage.py",
 69 |             "settings.py",
 70 |             "wsgi.py"
 71 |         ]
 72 |         return self._has_files(indicators, min_count=2)
 73 |     
 74 |     def _is_spring(self) -> bool:
 75 |         """Check if project is Spring Framework"""
 76 |         indicators = [
 77 |             "pom.xml",
 78 |             "build.gradle",
 79 |             "application.properties",
 80 |             "application.yml"
 81 |         ]
 82 |         
 83 |         if not self._has_files(indicators, min_count=1):
 84 |             return False
 85 |         
 86 |         # Check for Spring annotations in Java files
 87 |         java_files = [f for f in self.files if f.suffix == '.java']
 88 |         for java_file in java_files[:10]:  # Check first 10 files
 89 |             content = read_file_content(java_file)
 90 |             if any(annotation in content for annotation in [
 91 |                 "@RestController",
 92 |                 "@Controller",
 93 |                 "@SpringBootApplication",
 94 |                 "@Entity",
 95 |                 "@Service"
 96 |             ]):
 97 |                 return True
 98 |         
 99 |         return False
100 |     
101 |     def _is_flask(self) -> bool:
102 |         """Check if project is Flask"""
103 |         for file in self.files:
104 |             if file.suffix == '.py':
105 |                 content = read_file_content(file)
106 |                 if "from flask import" in content or "import flask" in content:
107 |                     return True
108 |         return False
109 |     
110 |     def _is_express(self) -> bool:
111 |         """Check if project is Express.js"""
112 |         if self._has_files(["package.json"]):
113 |             package_json = self.project_path / "package.json"
114 |             if package_json.exists():
115 |                 content = read_file_content(package_json)
116 |                 return "express" in content.lower()
117 |         return False
118 |     
119 |     def _has_files(self, filenames: List[str], min_count: int = 1) -> bool:
120 |         """Check if project has specified files"""
121 |         found = 0
122 |         for filename in filenames:
123 |             for file in self.files:
124 |                 if file.name == filename:
125 |                     found += 1
126 |                     break
127 |         return found >= min_count
128 |     
129 |     def _detect_django_version(self) -> str:
130 |         """Detect Django version from requirements or imports"""
131 |         # Check requirements.txt
132 |         req_file = self.project_path / "requirements.txt"
133 |         if req_file.exists():
134 |             content = read_file_content(req_file)
135 |             for line in content.split('\n'):
136 |                 if 'django' in line.lower():
137 |                     return line.strip()
138 |         return "unknown"
139 |     
140 |     def _detect_spring_version(self) -> str:
141 |         """Detect Spring version from pom.xml or build.gradle"""
142 |         pom_file = self.project_path / "pom.xml"
143 |         if pom_file.exists():
144 |             content = read_file_content(pom_file)
145 |             if "spring-boot" in content:
146 |                 return "Spring Boot"
147 |             return "Spring Framework"
148 |         return "unknown"
149 |     
150 |     def _get_django_files(self) -> List[str]:
151 |         """Get key Django files"""
152 |         key_patterns = ["manage.py", "settings.py", "urls.py", "models.py", "views.py", "admin.py"]
153 |         return self._find_files_by_name(key_patterns)
154 |     
155 |     def _get_spring_files(self) -> List[str]:
156 |         """Get key Spring files"""
157 |         key_files = []
158 |         for file in self.files:
159 |             if file.suffix == '.java':
160 |                 content = read_file_content(file)
161 |                 if any(annotation in content for annotation in [
162 |                     "@RestController", "@Controller", "@Entity", "@Service", "@Repository"
163 |                 ]):
164 |                     key_files.append(str(file.relative_to(self.project_path)))
165 |         return key_files[:20]  # Limit to 20 files
166 |     
167 |     def _get_flask_files(self) -> List[str]:
168 |         """Get key Flask files"""
169 |         flask_files = []
170 |         for file in self.files:
171 |             if file.suffix == '.py':
172 |                 content = read_file_content(file)
173 |                 if "flask" in content.lower():
174 |                     flask_files.append(str(file.relative_to(self.project_path)))
175 |         return flask_files[:10]
176 |     
177 |     def _get_express_files(self) -> List[str]:
178 |         """Get key Express files"""
179 |         return self._find_files_by_name(["package.json", "app.js", "server.js", "index.js"])
180 |     
181 |     def _find_files_by_name(self, names: List[str]) -> List[str]:
182 |         """Find files by name patterns"""
183 |         found = []
184 |         for name in names:
185 |             for file in self.files:
186 |                 if name in file.name:
187 |                     found.append(str(file.relative_to(self.project_path)))
188 |         return found
189 | 
190 | # Made with Bob
</content>
</file>
<file><path>backend/app/core/migrator.py</path>
<content lines="1-370">
  1 | """
  2 | Code migration engine
  3 | Converts legacy code to modern frameworks using IBM Bob AI
  4 | """
  5 | from pathlib import Path
  6 | from typing import Dict, Any, List
  7 | from app.core.bob_client import get_bob_client
  8 | from app.core.snapshot import SnapshotManager
  9 | from app.utils.file_utils import (
 10 |     get_project_path,
 11 |     scan_directory,
 12 |     read_file_content,
 13 |     write_file_content,
 14 |     get_relative_path
 15 | )
 16 | 
 17 | 
 18 | class CodeMigrator:
 19 |     """Migrate code from one framework to another"""
 20 |     
 21 |     def __init__(self, project_id: str):
 22 |         self.project_id = project_id
 23 |         self.bob_client = get_bob_client()
 24 |         self.snapshot_manager = SnapshotManager(project_id)
 25 |     
 26 |     async def migrate(
 27 |         self,
 28 |         source_framework: str,
 29 |         target_framework: str,
 30 |         source_path: Path
 31 |     ) -> Dict[str, Any]:
 32 |         """
 33 |         Perform migration from source to target framework
 34 |         """
 35 |         print(f"\n{'='*80}")
 36 |         print(f"🚀 STARTING MIGRATION")
 37 |         print(f"{'='*80}")
 38 |         print(f"Project ID: {self.project_id}")
 39 |         print(f"Source Framework: {source_framework}")
 40 |         print(f"Target Framework: {target_framework}")
 41 |         print(f"Source Path: {source_path}")
 42 |         print(f"{'='*80}\n")
 43 |         
 44 |         # Create snapshot before migration
 45 |         print("📸 Creating snapshot...")
 46 |         await self.snapshot_manager.create_snapshot(source_path)
 47 |         print("✅ Snapshot created\n")
 48 |         
 49 |         # Get files to migrate
 50 |         print("🔍 Finding files to migrate...")
 51 |         files_to_migrate = self._get_migration_files(source_framework, source_path)
 52 |         print(f"✅ Found {len(files_to_migrate)} files to migrate\n")
 53 |         
 54 |         for i, f in enumerate(files_to_migrate[:5], 1):
 55 |             print(f"  {i}. {f.name}")
 56 |         if len(files_to_migrate) > 5:
 57 |             print(f"  ... and {len(files_to_migrate) - 5} more files\n")
 58 |         
 59 |         # Prepare output directory
 60 |         output_path = get_project_path(self.project_id, "migrated")
 61 |         output_path.mkdir(parents=True, exist_ok=True)
 62 |         print(f"📁 Output directory: {output_path}\n")
 63 |         
 64 |         # Migrate files
 65 |         converted_files = []
 66 |         print(f"🔄 Starting file conversion...\n")
 67 |         
 68 |         for idx, file_path in enumerate(files_to_migrate, 1):
 69 |             try:
 70 |                 print(f"[{idx}/{len(files_to_migrate)}] Converting: {file_path.name}")
 71 |                 converted = await self._migrate_file(
 72 |                     file_path=file_path,
 73 |                     source_framework=source_framework,
 74 |                     target_framework=target_framework,
 75 |                     source_path=source_path,
 76 |                     output_path=output_path
 77 |                 )
 78 |                 if converted:
 79 |                     converted_files.append(converted)
 80 |                     print(f"  ✅ Converted successfully\n")
 81 |                 else:
 82 |                     print(f"  ⚠️  Conversion returned None\n")
 83 |             except Exception as e:
 84 |                 print(f"  ❌ Error: {str(e)}\n")
 85 |         
 86 |         # Generate project structure files
 87 |         print("📝 Generating project structure files...")
 88 |         await self._generate_project_files(target_framework, output_path)
 89 |         print("✅ Project files generated\n")
 90 |         
 91 |         print(f"{'='*80}")
 92 |         print(f"✅ MIGRATION COMPLETE")
 93 |         print(f"{'='*80}")
 94 |         print(f"Converted Files: {len(converted_files)}")
 95 |         print(f"Output Path: {output_path}")
 96 |         print(f"{'='*80}\n")
 97 |         
 98 |         return {
 99 |             "converted_files": len(converted_files),
100 |             "output_path": str(output_path),
101 |             "target_framework": target_framework,
102 |             "files": converted_files
103 |         }
104 |     
105 |     def _get_migration_files(
106 |         self,
107 |         framework: str,
108 |         source_path: Path
109 |     ) -> List[Path]:
110 |         """
111 |         Get list of files to migrate based on framework
112 |         """
113 |         if framework.lower() == "django":
114 |             return self._get_django_files(source_path)
115 |         elif framework.lower() == "spring":
116 |             return self._get_spring_files(source_path)
117 |         elif framework.lower() == "flask":
118 |             return self._get_flask_files(source_path)
119 |         else:
120 |             # Default: get all Python or Java files
121 |             return scan_directory(source_path, extensions=['.py', '.java'])
122 |     
123 |     def _get_django_files(self, source_path: Path) -> List[Path]:
124 |         """Get Django files to migrate"""
125 |         target_files = []
126 |         all_files = scan_directory(source_path)
127 |         
128 |         for file in all_files:
129 |             if file.suffix == '.py':
130 |                 filename = file.name
131 |                 # Focus on key Django files
132 |                 if any(pattern in filename for pattern in [
133 |                     'views', 'models', 'urls', 'serializers', 'forms'
134 |                 ]):
135 |                     target_files.append(file)
136 |         
137 |         return target_files[:20]  # Limit for MVP
138 |     
139 |     def _get_spring_files(self, source_path: Path) -> List[Path]:
140 |         """Get Spring files to migrate"""
141 |         target_files = []
142 |         all_files = scan_directory(source_path)
143 |         
144 |         for file in all_files:
145 |             if file.suffix == '.java':
146 |                 content = read_file_content(file)
147 |                 # Look for Spring annotations
148 |                 if any(annotation in content for annotation in [
149 |                     '@RestController', '@Controller', '@Entity', '@Service'
150 |                 ]):
151 |                     target_files.append(file)
152 |         
153 |         return target_files[:20]  # Limit for MVP
154 |     
155 |     def _get_flask_files(self, source_path: Path) -> List[Path]:
156 |         """Get Flask files to migrate"""
157 |         target_files = []
158 |         all_files = scan_directory(source_path)
159 |         
160 |         for file in all_files:
161 |             if file.suffix == '.py':
162 |                 content = read_file_content(file)
163 |                 if 'flask' in content.lower():
164 |                     target_files.append(file)
165 |         
166 |         return target_files[:15]
167 |     
168 |     async def _migrate_file(
169 |         self,
170 |         file_path: Path,
171 |         source_framework: str,
172 |         target_framework: str,
173 |         source_path: Path,
174 |         output_path: Path
175 |     ) -> Dict[str, str]:
176 |         """
177 |         Migrate a single file
178 |         """
179 |         # Read source code
180 |         source_code = read_file_content(file_path)
181 |         
182 |         # Determine file type with enhanced metadata
183 |         file_info = self._determine_file_type(file_path, source_code)
184 |         
185 |         # Convert using Bob AI with file info
186 |         converted_code = await self.bob_client.migrate_code(
187 |             source_code=source_code,
188 |             source_framework=source_framework,
189 |             target_framework=target_framework,
190 |             file_info=file_info
191 |         )
192 |         
193 |         # Determine output path
194 |         relative_path = get_relative_path(file_path, source_path)
195 |         output_file = output_path / relative_path
196 |         
197 |         # Adjust extension if needed
198 |         if target_framework.lower() == "fastapi" and output_file.suffix == '.java':
199 |             output_file = output_file.with_suffix('.py')
200 |         
201 |         # Write converted code
202 |         write_file_content(output_file, converted_code)
203 |         
204 |         return {
205 |             "source": relative_path,
206 |             "target": str(output_file.relative_to(output_path)),
207 |             "type": file_info.get("category", "general")
208 |         }
209 |     
210 |     def _determine_file_type(self, file_path: Path, content: str) -> Dict[str, Any]:
211 |         """
212 |         Determine file type with enhanced metadata for accurate conversion
213 |         Returns structured information about the file
214 |         """
215 |         filename = file_path.name.lower()
216 |         
217 |         # Detect Django-specific patterns
218 |         is_django_view = any(pattern in content for pattern in [
219 |             'APIView', 'viewsets.', 'from rest_framework.views',
220 |             '@login_required', 'render(request'
221 |         ])
222 |         
223 |         is_django_model = any(pattern in content for pattern in [
224 |             'models.Model', 'from django.db import models',
225 |             'models.CharField', 'models.ForeignKey'
226 |         ])
227 |         
228 |         is_django_serializer = any(pattern in content for pattern in [
229 |             'serializers.', 'from rest_framework import serializers',
230 |             'ModelSerializer'
231 |         ])
232 |         
233 |         is_django_urls = any(pattern in content for pattern in [
234 |             'urlpatterns', 'path(', 'url(', 'from django.urls'
235 |         ])
236 |         
237 |         # Determine category based on filename and content
238 |         category = self._get_category(filename, content, is_django_view, is_django_model,
239 |                                       is_django_serializer, is_django_urls)
240 |         
241 |         return {
242 |             "filename": file_path.name,
243 |             "path": str(file_path),
244 |             "category": category,
245 |             "has_classes": "class " in content,
246 |             "has_functions": "def " in content,
247 |             "is_django_view": is_django_view,
248 |             "is_django_model": is_django_model,
249 |             "is_django_serializer": is_django_serializer,
250 |             "is_django_urls": is_django_urls,
251 |             "line_count": len(content.split('\n'))
252 |         }
253 |     
254 |     def _get_category(self, filename: str, content: str, is_view: bool,
255 |                      is_model: bool, is_serializer: bool, is_urls: bool) -> str:
256 |         """
257 |         Determine file category based on filename and content analysis
258 |         """
259 |         # Check filename patterns first
260 |         if 'model' in filename and not 'test' in filename:
261 |             return "model"
262 |         elif 'view' in filename:
263 |             return "view"
264 |         elif 'url' in filename or 'route' in filename:
265 |             return "urls"
266 |         elif 'serializer' in filename:
267 |             return "serializer"
268 |         elif 'service' in filename:
269 |             return "service"
270 |         elif 'form' in filename:
271 |             return "form"
272 |         
273 |         # Fall back to content analysis
274 |         if is_model:
275 |             return "model"
276 |         elif is_view:
277 |             return "view"
278 |         elif is_urls:
279 |             return "urls"
280 |         elif is_serializer:
281 |             return "serializer"
282 |         else:
283 |             return "general"
284 |     
285 |     async def _generate_project_files(
286 |         self,
287 |         target_framework: str,
288 |         output_path: Path
289 |     ) -> None:
290 |         """
291 |         Generate necessary project files for target framework
292 |         """
293 |         if target_framework.lower() == "fastapi":
294 |             await self._generate_fastapi_files(output_path)
295 |         elif target_framework.lower() == "springboot":
296 |             await self._generate_springboot_files(output_path)
297 |     
298 |     async def _generate_fastapi_files(self, output_path: Path) -> None:
299 |         """Generate FastAPI project files"""
300 |         
301 |         # main.py
302 |         main_content = '''"""
303 | FastAPI Application - Migrated from legacy framework
304 | """
305 | from fastapi import FastAPI
306 | from fastapi.middleware.cors import CORSMiddleware
307 | 
308 | app = FastAPI(title="Migrated API")
309 | 
310 | # CORS
311 | app.add_middleware(
312 |     CORSMiddleware,
313 |     allow_origins=["*"],
314 |     allow_credentials=True,
315 |     allow_methods=["*"],
316 |     allow_headers=["*"],
317 | )
318 | 
319 | @app.get("/")
320 | async def root():
321 |     return {"message": "Migrated API is running"}
322 | 
323 | # Import your migrated routes here
324 | '''
325 |         write_file_content(output_path / "main.py", main_content)
326 |         
327 |         # requirements.txt
328 |         requirements = '''fastapi==0.109.0
329 | uvicorn[standard]==0.27.0
330 | pydantic==2.5.3
331 | '''
332 |         write_file_content(output_path / "requirements.txt", requirements)
333 |         
334 |         # README.md
335 |         readme = '''# Migrated FastAPI Application
336 | 
337 | This application was automatically migrated from a legacy framework.
338 | 
339 | ## Setup
340 | 
341 | ```bash
342 | pip install -r requirements.txt
343 | ```
344 | 
345 | ## Run
346 | 
347 | ```bash
348 | uvicorn main:app --reload
349 | ```
350 | 
351 | ## Notes
352 | 
353 | - Review all migrated code
354 | - Update database connections
355 | - Configure environment variables
356 | - Test all endpoints
357 | '''
358 |         write_file_content(output_path / "README.md", readme)
359 |     
360 |     async def _generate_springboot_files(self, output_path: Path) -> None:
361 |         """Generate Spring Boot project files"""
362 |         
363 |         # application.properties
364 |         properties = '''server.port=8080
365 | spring.application.name=migrated-app
366 | '''
367 |         config_dir = output_path / "src" / "main" / "resources"
368 |         write_file_content(config_dir / "application.properties", properties)
369 | 
370 | # Made with Bob
</content>
</file>
<file><path>backend/app/core/transformer.py</path>
<content lines="1-838">
  1 | """
  2 | Enhanced Code Transformation Engine
  3 | Generates 60-70% complete functional code with:
  4 | - SQLAlchemy database models
  5 | - Working CRUD operations  
  6 | - JWT authentication
  7 | - Preserved business logic patterns
  8 | - Database connection setup
  9 | """
 10 | import re
 11 | from typing import Dict, Any, List, Tuple, Optional
 12 | from pathlib import Path
 13 | 
 14 | 
 15 | class EnhancedDjangoToFastAPITransformer:
 16 |     """
 17 |     Enhanced transformer that generates functional FastAPI code
 18 |     Target: 60-70% complete with working implementations
 19 |     """
 20 |     
 21 |     def __init__(self):
 22 |         self.generated_models = []  # Track generated SQLAlchemy models
 23 |         self.generated_schemas = []  # Track generated Pydantic schemas
 24 |     
 25 |     def transform(self, source_code: str, file_info: Dict[str, Any]) -> str:
 26 |         """Main transformation with enhanced logic preservation"""
 27 |         category = file_info.get("category", "general")
 28 |         
 29 |         if category == "view" or file_info.get("is_django_view"):
 30 |             return self.transform_views_enhanced(source_code, file_info)
 31 |         elif category == "model" or file_info.get("is_django_model"):
 32 |             return self.transform_models_enhanced(source_code, file_info)
 33 |         elif category == "urls" or file_info.get("is_django_urls"):
 34 |             return self.transform_urls_enhanced(source_code, file_info)
 35 |         elif category == "serializer" or file_info.get("is_django_serializer"):
 36 |             return self.transform_serializers_enhanced(source_code, file_info)
 37 |         else:
 38 |             return self.transform_general(source_code, file_info)
 39 |     
 40 |     def transform_models_enhanced(self, source_code: str, file_info: Dict[str, Any]) -> str:
 41 |         """
 42 |         Generate BOTH SQLAlchemy models AND Pydantic schemas
 43 |         This provides ~70% complete database layer
 44 |         """
 45 |         # Extract Django models
 46 |         django_models = self._extract_django_models(source_code)
 47 |         
 48 |         if not django_models:
 49 |             return self._generate_empty_models_template()
 50 |         
 51 |         # Generate imports
 52 |         imports = """from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey, Text
 53 | from sqlalchemy.orm import relationship, declarative_base
 54 | from sqlalchemy.ext.declarative import declarative_base
 55 | from pydantic import BaseModel, Field, EmailStr, validator
 56 | from typing import Optional, List
 57 | from datetime import datetime
 58 | from enum import Enum
 59 | 
 60 | Base = declarative_base()
 61 | 
 62 | # Database Models (SQLAlchemy)
 63 | """
 64 |         
 65 |         # Generate SQLAlchemy models
 66 |         sqlalchemy_models = []
 67 |         pydantic_schemas = []
 68 |         
 69 |         for model in django_models:
 70 |             # Generate SQLAlchemy model
 71 |             sa_model = self._generate_sqlalchemy_model(model)
 72 |             sqlalchemy_models.append(sa_model)
 73 |             
 74 |             # Generate Pydantic schemas
 75 |             schemas = self._generate_pydantic_schemas(model)
 76 |             pydantic_schemas.append(schemas)
 77 |         
 78 |         # Generate CRUD operations
 79 |         crud_operations = self._generate_crud_operations(django_models)
 80 |         
 81 |         result = f"""{imports}
 82 | 
 83 | {chr(10).join(sqlalchemy_models)}
 84 | 
 85 | # Pydantic Schemas (for API validation)
 86 | 
 87 | {chr(10).join(pydantic_schemas)}
 88 | 
 89 | # CRUD Operations
 90 | 
 91 | {crud_operations}
 92 | 
 93 | # Database Setup
 94 | # Add this to your main.py or database.py:
 95 | # 
 96 | # from sqlalchemy import create_engine
 97 | # from sqlalchemy.orm import sessionmaker
 98 | # 
 99 | # DATABASE_URL = "postgresql://user:password@localhost/dbname"
100 | # # or for SQLite: "sqlite:///./app.db"
101 | # 
102 | # engine = create_engine(DATABASE_URL)
103 | # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
104 | # Base.metadata.create_all(bind=engine)
105 | # 
106 | # def get_db():
107 | #     db = SessionLocal()
108 | #     try:
109 | #         yield db
110 | #     finally:
111 | #         db.close()
112 | """
113 |         return result
114 |     
115 |     def _extract_django_models(self, source_code: str) -> List[Dict[str, Any]]:
116 |         """Extract Django models with full field information"""
117 |         models = []
118 |         
119 |         # Pattern to match Django model classes
120 |         pattern = r'class\s+(\w+)\(models\.Model\):(.*?)(?=\nclass\s|\Z)'
121 |         
122 |         for match in re.finditer(pattern, source_code, re.DOTALL):
123 |             model_name = match.group(1)
124 |             model_body = match.group(2)
125 |             
126 |             # Extract fields with types
127 |             fields = self._extract_model_fields_detailed(model_body)
128 |             
129 |             # Extract Meta class
130 |             meta = self._extract_model_meta(model_body)
131 |             
132 |             # Extract methods
133 |             methods = self._extract_model_methods(model_body)
134 |             
135 |             models.append({
136 |                 "name": model_name,
137 |                 "fields": fields,
138 |                 "meta": meta,
139 |                 "methods": methods,
140 |                 "body": model_body
141 |             })
142 |         
143 |         return models
144 |     
145 |     def _extract_model_fields_detailed(self, model_body: str) -> List[Dict[str, Any]]:
146 |         """Extract fields with complete type information"""
147 |         fields = []
148 |         
149 |         # Field patterns with detailed extraction
150 |         field_patterns = [
151 |             (r'(\w+)\s*=\s*models\.CharField\((.*?)\)', 'String', 'CharField'),
152 |             (r'(\w+)\s*=\s*models\.TextField\((.*?)\)', 'Text', 'TextField'),
153 |             (r'(\w+)\s*=\s*models\.EmailField\((.*?)\)', 'String', 'EmailField'),
154 |             (r'(\w+)\s*=\s*models\.IntegerField\((.*?)\)', 'Integer', 'IntegerField'),
155 |             (r'(\w+)\s*=\s*models\.FloatField\((.*?)\)', 'Float', 'FloatField'),
156 |             (r'(\w+)\s*=\s*models\.BooleanField\((.*?)\)', 'Boolean', 'BooleanField'),
157 |             (r'(\w+)\s*=\s*models\.DateTimeField\((.*?)\)', 'DateTime', 'DateTimeField'),
158 |             (r'(\w+)\s*=\s*models\.DateField\((.*?)\)', 'DateTime', 'DateField'),
159 |             (r'(\w+)\s*=\s*models\.ForeignKey\((.*?)\)', 'ForeignKey', 'ForeignKey'),
160 |             (r'(\w+)\s*=\s*models\.OneToOneField\((.*?)\)', 'ForeignKey', 'OneToOneField'),
161 |             (r'(\w+)\s*=\s*models\.ManyToManyField\((.*?)\)', 'ManyToMany', 'ManyToManyField'),
162 |         ]
163 |         
164 |         for pattern, sa_type, django_type in field_patterns:
165 |             for match in re.finditer(pattern, model_body):
166 |                 field_name = match.group(1)
167 |                 field_args = match.group(2)
168 |                 
169 |                 # Parse field arguments
170 |                 is_primary = 'primary_key' in field_args and 'True' in field_args
171 |                 is_nullable = 'null=True' in field_args or 'blank=True' in field_args
172 |                 is_unique = 'unique=True' in field_args
173 |                 max_length = self._extract_max_length(field_args)
174 |                 default = self._extract_default(field_args)
175 |                 foreign_model = self._extract_foreign_model(field_args) if sa_type == 'ForeignKey' else None
176 |                 
177 |                 fields.append({
178 |                     "name": field_name,
179 |                     "sa_type": sa_type,
180 |                     "django_type": django_type,
181 |                     "is_primary": is_primary,
182 |                     "is_nullable": is_nullable,
183 |                     "is_unique": is_unique,
184 |                     "max_length": max_length,
185 |                     "default": default,
186 |                     "foreign_model": foreign_model
187 |                 })
188 |         
189 |         return fields
190 |     
191 |     def _extract_max_length(self, field_args: str) -> Optional[int]:
192 |         """Extract max_length from field arguments"""
193 |         match = re.search(r'max_length\s*=\s*(\d+)', field_args)
194 |         return int(match.group(1)) if match else None
195 |     
196 |     def _extract_default(self, field_args: str) -> Optional[str]:
197 |         """Extract default value from field arguments"""
198 |         match = re.search(r'default\s*=\s*["\']([^"\']+)["\']', field_args)
199 |         if match:
200 |             return f'"{match.group(1)}"'
201 |         match = re.search(r'default\s*=\s*(\d+)', field_args)
202 |         if match:
203 |             return match.group(1)
204 |         return None
205 |     
206 |     def _extract_foreign_model(self, field_args: str) -> Optional[str]:
207 |         """Extract foreign model name"""
208 |         match = re.search(r'["\']?(\w+)["\']?\s*,', field_args)
209 |         return match.group(1) if match else None
210 |     
211 |     def _extract_model_meta(self, model_body: str) -> Dict[str, Any]:
212 |         """Extract Meta class information"""
213 |         meta_match = re.search(r'class Meta:(.*?)(?=\n    def|\n    \w+\s*=|\Z)', model_body, re.DOTALL)
214 |         if not meta_match:
215 |             return {}
216 |         
217 |         meta_body = meta_match.group(1)
218 |         return {
219 |             "verbose_name": self._extract_meta_value(meta_body, 'verbose_name'),
220 |             "verbose_name_plural": self._extract_meta_value(meta_body, 'verbose_name_plural'),
221 |             "ordering": self._extract_meta_value(meta_body, 'ordering'),
222 |         }
223 |     
224 |     def _extract_meta_value(self, meta_body: str, key: str) -> Optional[str]:
225 |         """Extract value from Meta class"""
226 |         match = re.search(f'{key}\s*=\s*["\']([^"\']+)["\']', meta_body)
227 |         return match.group(1) if match else None
228 |     
229 |     def _extract_model_methods(self, model_body: str) -> List[Dict[str, str]]:
230 |         """Extract model methods"""
231 |         methods = []
232 |         method_pattern = r'def\s+(\w+)\(self[^)]*\):(.*?)(?=\n    def|\Z)'
233 |         
234 |         for match in re.finditer(method_pattern, model_body, re.DOTALL):
235 |             method_name = match.group(1)
236 |             method_body = match.group(2)
237 |             
238 |             if method_name not in ['__str__', '__repr__', 'save', 'delete']:
239 |                 methods.append({
240 |                     "name": method_name,
241 |                     "body": method_body.strip()
242 |                 })
243 |         
244 |         return methods
245 |     
246 |     def _generate_sqlalchemy_model(self, model: Dict[str, Any]) -> str:
247 |         """Generate complete SQLAlchemy model"""
248 |         model_name = model["name"]
249 |         fields = model["fields"]
250 |         
251 |         # Generate table name
252 |         table_name = model_name.lower() + 's'
253 |         
254 |         # Generate field definitions
255 |         field_defs = []
256 |         relationships = []
257 |         
258 |         for field in fields:
259 |             if field["sa_type"] == "ForeignKey":
260 |                 # Foreign key field
261 |                 fk_table = field["foreign_model"].lower() + 's' if field["foreign_model"] else 'unknown'
262 |                 field_def = f'    {field["name"]}_id = Column(Integer, ForeignKey("{fk_table}.id"))'
263 |                 field_defs.append(field_def)
264 |                 
265 |                 # Relationship
266 |                 rel_def = f'    {field["name"]} = relationship("{field["foreign_model"]}", back_populates="{table_name}")'
267 |                 relationships.append(rel_def)
268 |             
269 |             elif field["sa_type"] == "ManyToMany":
270 |                 # Skip many-to-many for now (requires association table)
271 |                 field_defs.append(f'    # TODO: Implement many-to-many for {field["name"]}')
272 |             
273 |             else:
274 |                 # Regular field
275 |                 col_type = field["sa_type"]
276 |                 if field["max_length"] and col_type == "String":
277 |                     col_type = f"String({field['max_length']})"
278 |                 
279 |                 constraints = []
280 |                 if field["is_primary"]:
281 |                     constraints.append("primary_key=True")
282 |                 if not field["is_nullable"]:
283 |                     constraints.append("nullable=False")
284 |                 if field["is_unique"]:
285 |                     constraints.append("unique=True")
286 |                 if field["default"]:
287 |                     constraints.append(f"default={field['default']}")
288 |                 
289 |                 constraint_str = ", ".join(constraints)
290 |                 field_def = f'    {field["name"]} = Column({col_type}{", " + constraint_str if constraint_str else ""})'
291 |                 field_defs.append(field_def)
292 |         
293 |         # Add default id if no primary key
294 |         has_primary = any(f["is_primary"] for f in fields)
295 |         if not has_primary:
296 |             field_defs.insert(0, '    id = Column(Integer, primary_key=True, index=True)')
297 |         
298 |         # Combine everything
299 |         model_code = f'''
300 | class {model_name}(Base):
301 |     """SQLAlchemy model for {model_name}"""
302 |     __tablename__ = "{table_name}"
303 |     
304 | {chr(10).join(field_defs)}
305 | {chr(10).join(relationships) if relationships else ""}
306 |     
307 |     def __repr__(self):
308 |         return f"<{model_name}(id={{self.id}})>"
309 | '''
310 |         return model_code
311 |     
312 |     def _generate_pydantic_schemas(self, model: Dict[str, Any]) -> str:
313 |         """Generate Pydantic schemas for API validation"""
314 |         model_name = model["name"]
315 |         fields = model["fields"]
316 |         
317 |         # Generate field definitions for Pydantic
318 |         base_fields = []
319 |         for field in fields:
320 |             if field["sa_type"] == "ForeignKey":
321 |                 # Foreign key as integer ID
322 |                 field_type = "int"
323 |             elif field["sa_type"] == "String":
324 |                 field_type = "str"
325 |             elif field["sa_type"] == "Text":
326 |                 field_type = "str"
327 |             elif field["sa_type"] == "Integer":
328 |                 field_type = "int"
329 |             elif field["sa_type"] == "Float":
330 |                 field_type = "float"
331 |             elif field["sa_type"] == "Boolean":
332 |                 field_type = "bool"
333 |             elif field["sa_type"] == "DateTime":
334 |                 field_type = "datetime"
335 |             else:
336 |                 field_type = "Any"
337 |             
338 |             if field["is_nullable"]:
339 |                 field_type = f"Optional[{field_type}]"
340 |                 default = " = None"
341 |             else:
342 |                 default = ""
343 |             
344 |             base_fields.append(f"    {field['name']}: {field_type}{default}")
345 |         
346 |         base_fields_str = "\n".join(base_fields) if base_fields else "    pass"
347 |         
348 |         schemas = f'''
349 | class {model_name}Base(BaseModel):
350 |     """Base schema for {model_name}"""
351 | {base_fields_str}
352 | 
353 | class {model_name}Create({model_name}Base):
354 |     """Schema for creating {model_name}"""
355 |     pass
356 | 
357 | class {model_name}Update(BaseModel):
358 |     """Schema for updating {model_name}"""
359 | {base_fields_str.replace(": ", ": Optional[").replace("Optional[Optional[", "Optional[") if base_fields_str != "    pass" else "    pass"}
360 | 
361 | class {model_name}Response({model_name}Base):
362 |     """Schema for {model_name} response"""
363 |     id: int
364 |     
365 |     class Config:
366 |         from_attributes = True
367 | '''
368 |         return schemas
369 |     
370 |     def _generate_crud_operations(self, models: List[Dict[str, Any]]) -> str:
371 |         """Generate CRUD operations for all models"""
372 |         crud_code = """from sqlalchemy.orm import Session
373 | from fastapi import HTTPException
374 | 
375 | """
376 |         
377 |         for model in models[:3]:  # Generate for first 3 models as example
378 |             model_name = model["name"]
379 |             crud_code += f'''
380 | # CRUD for {model_name}
381 | 
382 | def create_{model_name.lower()}(db: Session, {model_name.lower()}: {model_name}Create) -> {model_name}:
383 |     """Create new {model_name}"""
384 |     db_{model_name.lower()} = {model_name}(**{model_name.lower()}.dict())
385 |     db.add(db_{model_name.lower()})
386 |     db.commit()
387 |     db.refresh(db_{model_name.lower()})
388 |     return db_{model_name.lower()}
389 | 
390 | def get_{model_name.lower()}(db: Session, {model_name.lower()}_id: int) -> Optional[{model_name}]:
391 |     """Get {model_name} by ID"""
392 |     return db.query({model_name}).filter({model_name}.id == {model_name.lower()}_id).first()
393 | 
394 | def get_{model_name.lower()}s(db: Session, skip: int = 0, limit: int = 100) -> List[{model_name}]:
395 |     """Get list of {model_name}s"""
396 |     return db.query({model_name}).offset(skip).limit(limit).all()
397 | 
398 | def update_{model_name.lower()}(db: Session, {model_name.lower()}_id: int, {model_name.lower()}: {model_name}Update) -> Optional[{model_name}]:
399 |     """Update {model_name}"""
400 |     db_{model_name.lower()} = db.query({model_name}).filter({model_name}.id == {model_name.lower()}_id).first()
401 |     if not db_{model_name.lower()}:
402 |         return None
403 |     
404 |     update_data = {model_name.lower()}.dict(exclude_unset=True)
405 |     for key, value in update_data.items():
406 |         setattr(db_{model_name.lower()}, key, value)
407 |     
408 |     db.commit()
409 |     db.refresh(db_{model_name.lower()})
410 |     return db_{model_name.lower()}
411 | 
412 | def delete_{model_name.lower()}(db: Session, {model_name.lower()}_id: int) -> bool:
413 |     """Delete {model_name}"""
414 |     db_{model_name.lower()} = db.query({model_name}).filter({model_name}.id == {model_name.lower()}_id).first()
415 |     if not db_{model_name.lower()}:
416 |         return False
417 |     
418 |     db.delete(db_{model_name.lower()})
419 |     db.commit()
420 |     return True
421 | '''
422 |         
423 |         if len(models) > 3:
424 |             crud_code += f"\n# TODO: Generate CRUD operations for remaining {len(models) - 3} models\n"
425 |         
426 |         return crud_code
427 |     
428 |     def _generate_empty_models_template(self) -> str:
429 |         """Generate template when no models found"""
430 |         return """from sqlalchemy import Column, Integer, String, DateTime
431 | from sqlalchemy.ext.declarative import declarative_base
432 | from pydantic import BaseModel
433 | from datetime import datetime
434 | 
435 | Base = declarative_base()
436 | 
437 | # No Django models detected in this file
438 | # Add your SQLAlchemy models here
439 | 
440 | # Example:
441 | # class User(Base):
442 | #     __tablename__ = "users"
443 | #     
444 | #     id = Column(Integer, primary_key=True, index=True)
445 | #     username = Column(String(50), unique=True, nullable=False)
446 | #     email = Column(String(100), unique=True, nullable=False)
447 | #     created_at = Column(DateTime, default=datetime.utcnow)
448 | """
449 |     
450 |     def transform_views_enhanced(self, source_code: str, file_info: Dict[str, Any]) -> str:
451 |         """
452 |         Transform views with preserved business logic
453 |         Target: 60-70% functional with actual implementations
454 |         """
455 |         # Extract Django views
456 |         view_classes = self._extract_django_view_classes(source_code)
457 |         function_views = self._extract_django_function_views(source_code)
458 |         
459 |         if not view_classes and not function_views:
460 |             return self._generate_empty_views_template()
461 |         
462 |         # Generate complete FastAPI setup
463 |         imports = self._generate_complete_fastapi_imports()
464 |         
465 |         # Generate authentication setup
466 |         auth_setup = self._generate_jwt_auth_setup()
467 |         
468 |         # Convert class-based views
469 |         routes = []
470 |         for view_class in view_classes:
471 |             route = self._convert_view_to_functional_route(view_class, source_code)
472 |             routes.append(route)
473 |         
474 |         # Convert function-based views
475 |         for func_view in function_views:
476 |             route = self._convert_function_view_to_route(func_view, source_code)
477 |             routes.append(route)
478 |         
479 |         result = f"""{imports}
480 | 
481 | {auth_setup}
482 | 
483 | {chr(10).join(routes)}
484 | 
485 | # Migration Notes:
486 | # - Business logic preserved where possible
487 | # - Database queries need SQLAlchemy models (see models.py)
488 | # - Authentication uses JWT (configure SECRET_KEY in .env)
489 | # - Test all endpoints with actual database
490 | """
491 |         return result
492 |     
493 |     def _extract_django_view_classes(self, source_code: str) -> List[Dict[str, Any]]:
494 |         """Extract Django class-based views with methods"""
495 |         classes = []
496 |         pattern = r'class\s+(\w+)\((?:APIView|viewsets\.\w+|View)\):(.*?)(?=\nclass\s|\Z)'
497 |         
498 |         for match in re.finditer(pattern, source_code, re.DOTALL):
499 |             class_name = match.group(1)
500 |             class_body = match.group(2)
501 |             
502 |             # Extract HTTP methods with their bodies
503 |             methods = []
504 |             method_pattern = r'def\s+(get|post|put|patch|delete)\(self,\s*request[^)]*\):(.*?)(?=\n    def\s|\Z)'
505 |             
506 |             for method_match in re.finditer(method_pattern, class_body, re.DOTALL):
507 |                 method_name = method_match.group(1)
508 |                 method_body = method_match.group(2)
509 |                 
510 |                 # Extract business logic patterns
511 |                 has_db_query = '.objects.' in method_body
512 |                 has_filter = '.filter(' in method_body
513 |                 has_get = '.get(' in method_body
514 |                 returns_response = 'Response(' in method_body or 'return ' in method_body
515 |                 
516 |                 methods.append({
517 |                     "name": method_name,
518 |                     "body": method_body,
519 |                     "has_db_query": has_db_query,
520 |                     "has_filter": has_filter,
521 |                     "has_get": has_get,
522 |                     "returns_response": returns_response
523 |                 })
524 |             
525 |             # Extract permissions
526 |             perm_match = re.search(r'permission_classes\s*=\s*\[(.*?)\]', class_body)
527 |             permissions = perm_match.group(1).split(',') if perm_match else []
528 |             
529 |             classes.append({
530 |                 "name": class_name,
531 |                 "methods": methods,
532 |                 "permissions": permissions,
533 |                 "body": class_body
534 |             })
535 |         
536 |         return classes
537 |     
538 |     def _extract_django_function_views(self, source_code: str) -> List[Dict[str, Any]]:
539 |         """Extract Django function-based views"""
540 |         functions = []
541 |         pattern = r'@login_required.*?\ndef\s+(\w+)\(request[^)]*\):(.*?)(?=\n@|\ndef\s|\Z)'
542 |         
543 |         for match in re.finditer(pattern, source_code, re.DOTALL):
544 |             func_name = match.group(1)
545 |             func_body = match.group(2)
546 |             
547 |             functions.append({
548 |                 "name": func_name,
549 |                 "body": func_body,
550 |                 "requires_auth": True
551 |             })
552 |         
553 |         return functions
554 |     
555 |     def _generate_complete_fastapi_imports(self) -> str:
556 |         """Generate complete FastAPI imports"""
557 |         return """from fastapi import APIRouter, HTTPException, Depends, status, Query
558 | from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
559 | from sqlalchemy.orm import Session
560 | from typing import List, Optional
561 | from pydantic import BaseModel
562 | from datetime import datetime, timedelta
563 | import jwt
564 | from passlib.context import CryptContext
565 | 
566 | router = APIRouter()
567 | security = HTTPBearer()
568 | 
569 | # Password hashing
570 | pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
571 | 
572 | # JWT Configuration (set these in .env file)
573 | SECRET_KEY = "your-secret-key-change-this-in-production"
574 | ALGORITHM = "HS256"
575 | ACCESS_TOKEN_EXPIRE_MINUTES = 30
576 | """
577 |     
578 |     def _generate_jwt_auth_setup(self) -> str:
579 |         """Generate JWT authentication setup"""
580 |         return """
581 | # Database dependency
582 | def get_db():
583 |     # TODO: Import your SessionLocal from database.py
584 |     # db = SessionLocal()
585 |     # try:
586 |     #     yield db
587 |     # finally:
588 |     #     db.close()
589 |     pass
590 | 
591 | # Authentication functions
592 | def verify_password(plain_password: str, hashed_password: str) -> bool:
593 |     \"\"\"Verify password against hash\"\"\"
594 |     return pwd_context.verify(plain_password, hashed_password)
595 | 
596 | def get_password_hash(password: str) -> str:
597 |     \"\"\"Hash password\"\"\"
598 |     return pwd_context.hash(password)
599 | 
600 | def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
601 |     \"\"\"Create JWT access token\"\"\"
602 |     to_encode = data.copy()
603 |     if expires_delta:
604 |         expire = datetime.utcnow() + expires_delta
605 |     else:
606 |         expire = datetime.utcnow() + timedelta(minutes=15)
607 |     to_encode.update({"exp": expire})
608 |     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
609 |     return encoded_jwt
610 | 
611 | async def get_current_user(
612 |     credentials: HTTPAuthorizationCredentials = Depends(security),
613 |     db: Session = Depends(get_db)
614 | ):
615 |     \"\"\"Get current user from JWT token\"\"\"
616 |     credentials_exception = HTTPException(
617 |         status_code=status.HTTP_401_UNAUTHORIZED,
618 |         detail="Could not validate credentials",
619 |         headers={"WWW-Authenticate": "Bearer"},
620 |     )
621 |     try:
622 |         token = credentials.credentials
623 |         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
624 |         user_id: str = payload.get("sub")
625 |         if user_id is None:
626 |             raise credentials_exception
627 |     except jwt.PyJWTError:
628 |         raise credentials_exception
629 |     
630 |     # TODO: Query user from database
631 |     # user = db.query(User).filter(User.id == user_id).first()
632 |     # if user is None:
633 |     #     raise credentials_exception
634 |     # return user
635 |     
636 |     # Temporary: return user data from token
637 |     return {"id": user_id, "username": payload.get("username")}
638 | """
639 |     
640 |     def _convert_view_to_functional_route(self, view_class: Dict[str, Any], source_code: str) -> str:
641 |         """Convert Django class view to functional FastAPI route with logic"""
642 |         class_name = view_class["name"]
643 |         base_path = self._infer_route_path(class_name)
644 |         
645 |         routes = []
646 |         for method in view_class["methods"]:
647 |             http_method = method["name"]
648 |             method_body = method["body"]
649 |             
650 |             # Determine if auth is needed
651 |             needs_auth = "IsAuthenticated" in str(view_class.get("permissions", []))
652 |             auth_param = "current_user: dict = Depends(get_current_user),\n    " if needs_auth else ""
653 |             
654 |             # Try to preserve business logic
655 |             logic = self._extract_and_convert_logic(method_body)
656 |             
657 |             route_code = f'''
658 | @router.{http_method}("{base_path}")
659 | async def {class_name.lower()}_{http_method}(
660 |     {auth_param}db: Session = Depends(get_db)
661 | ):
662 |     """
663 |     {class_name} - {http_method.upper()} endpoint
664 |     Converted from Django {class_name}.{http_method}()
665 |     """
666 |     try:
667 | {logic}
668 |     except Exception as e:
669 |         raise HTTPException(status_code=400, detail=str(e))
670 | '''
671 |             routes.append(route_code)
672 |         
673 |         return "\n".join(routes)
674 |     
675 |     def _extract_and_convert_logic(self, method_body: str) -> str:
676 |         """Extract and convert business logic from Django to FastAPI"""
677 |         # This is a simplified conversion - preserves structure
678 |         lines = method_body.split('\n')
679 |         converted_lines = []
680 |         
681 |         for line in lines:
682 |             # Skip empty lines and comments at start
683 |             if not line.strip() or line.strip().startswith('#'):
684 |                 continue
685 |             
686 |             # Convert Django ORM to SQLAlchemy patterns
687 |             if '.objects.get(' in line:
688 |                 # Example: stud = Student.objects.get(USN=stud_id)
689 |                 converted = line.replace('.objects.get(', '.query(').replace(')', ').first()')
690 |                 converted_lines.append(f"        # TODO: Convert to SQLAlchemy: {line.strip()}")
691 |                 converted_lines.append(f"        # {converted.strip()}")
692 |             elif '.objects.filter(' in line:
693 |                 converted = line.replace('.objects.filter(', '.query(').replace(')', ').all()')
694 |                 converted_lines.append(f"        # TODO: Convert to SQLAlchemy: {line.strip()}")
695 |                 converted_lines.append(f"        # {converted.strip()}")
696 |             elif 'Response(' in line:
697 |                 # Convert Django Response to FastAPI return
698 |                 converted = line.replace('Response(', 'return ')
699 |                 converted_lines.append(f"        {converted.strip()}")
700 |             else:
701 |                 # Preserve other logic as comments for manual review
702 |                 if line.strip():
703 |                     converted_lines.append(f"        # {line.strip()}")
704 |         
705 |         if not converted_lines:
706 |             converted_lines = [
707 |                 "        # TODO: Implement business logic from Django view",
708 |                 '        return {"message": "Endpoint converted - implement logic"}'
709 |             ]
710 |         
711 |         return '\n'.join(converted_lines)
712 |     
713 |     def _convert_function_view_to_route(self, func_view: Dict[str, Any], source_code: str) -> str:
714 |         """Convert Django function view to FastAPI route"""
715 |         func_name = func_view["name"]
716 |         func_body = func_view["body"]
717 |         
718 |         logic = self._extract_and_convert_logic(func_body)
719 |         
720 |         return f'''
721 | @router.get("/{func_name}")
722 | async def {func_name}(
723 |     current_user: dict = Depends(get_current_user),
724 |     db: Session = Depends(get_db)
725 | ):
726 |     """Converted from Django function view: {func_name}"""
727 |     try:
728 | {logic}
729 |     except Exception as e:
730 |         raise HTTPException(status_code=400, detail=str(e))
731 | '''
732 |     
733 |     def _infer_route_path(self, class_name: str) -> str:
734 |         """Infer REST API path from class name"""
735 |         name = re.sub(r'View$', '', class_name)
736 |         name = re.sub(r'([a-z])([A-Z])', r'\1-\2', name).lower()
737 |         return f"/{name}"
738 |     
739 |     def _generate_empty_views_template(self) -> str:
740 |         """Generate template when no views found"""
741 |         return """from fastapi import APIRouter, HTTPException, Depends
742 | from sqlalchemy.orm import Session
743 | 
744 | router = APIRouter()
745 | 
746 | # No Django views detected in this file
747 | # Add your FastAPI routes here
748 | 
749 | @router.get("/")
750 | async def root():
751 |     return {"message": "API is running"}
752 | """
753 |     
754 |     def transform_urls_enhanced(self, source_code: str, file_info: Dict[str, Any]) -> str:
755 |         """Generate FastAPI router configuration"""
756 |         return """from fastapi import APIRouter
757 | 
758 | router = APIRouter()
759 | 
760 | # Import your route modules here
761 | # Example:
762 | # from .views import router as views_router
763 | # router.include_router(views_router, prefix="/api/v1", tags=["items"])
764 | 
765 | # Or include individual routers:
766 | # from . import auth, users, items
767 | # router.include_router(auth.router, prefix="/auth", tags=["authentication"])
768 | # router.include_router(users.router, prefix="/users", tags=["users"])
769 | # router.include_router(items.router, prefix="/items", tags=["items"])
770 | """
771 |     
772 |     def transform_serializers_enhanced(self, source_code: str, file_info: Dict[str, Any]) -> str:
773 |         """Convert Django serializers to Pydantic schemas"""
774 |         return """from pydantic import BaseModel, Field, validator
775 | from typing import Optional, List
776 | from datetime import datetime
777 | 
778 | # Django serializers are replaced by Pydantic schemas
779 | # These provide the same validation and serialization functionality
780 | 
781 | # Example schema:
782 | # class ItemSchema(BaseModel):
783 | #     id: int
784 | #     name: str = Field(..., min_length=1, max_length=100)
785 | #     description: Optional[str] = None
786 | #     price: float = Field(..., gt=0)
787 | #     created_at: datetime
788 | #     
789 | #     @validator('price')
790 | #     def price_must_be_positive(cls, v):
791 | #         if v <= 0:
792 | #             raise ValueError('Price must be positive')
793 | #         return v
794 | #     
795 | #     class Config:
796 | #         from_attributes = True
797 | 
798 | # TODO: Convert your Django serializers to Pydantic schemas above
799 | """
800 |     
801 |     def transform_general(self, source_code: str, file_info: Dict[str, Any]) -> str:
802 |         """Handle general Python files"""
803 |         has_django = any(pattern in source_code for pattern in [
804 |             'from django', 'import django', 'from rest_framework'
805 |         ])
806 |         
807 |         if has_django:
808 |             return f"""# This file contained Django-specific code
809 | # Manual conversion required for: {file_info.get('filename', 'unknown')}
810 | 
811 | # Common conversions:
812 | # - Django settings → FastAPI config/environment variables
813 | # - Django middleware → FastAPI middleware
814 | # - Django signals → FastAPI event handlers
815 | # - Django management commands → Separate CLI scripts
816 | 
817 | # Original code preserved below for reference:
818 | \"\"\"
819 | {source_code}
820 | \"\"\"
821 | """
822 |         
823 |         return source_code
824 | 
825 | 
826 | # Singleton instance
827 | _enhanced_transformer: Optional[EnhancedDjangoToFastAPITransformer] = None
828 | 
829 | 
830 | def get_enhanced_transformer() -> EnhancedDjangoToFastAPITransformer:
831 |     """Get or create enhanced transformer instance"""
832 |     global _enhanced_transformer
833 |     if _enhanced_transformer is None:
834 |         _enhanced_transformer = EnhancedDjangoToFastAPITransformer()
835 |     return _enhanced_transformer
836 | 
837 | 
838 | # Made with Bob - Enhanced Version
</content>
</file>
</files>
<environment_details>
# VSCode Visible Files
backend\app\storage\migrated\798bd2af-067c-4f1e-8491-8e5398c28b6c\info\models.py

# VSCode Open Tabs
backend/app/core/detector.py,backend/app/core/migrator.py,backend/app/core/validators.py,backend/app/core/transformer.py,backend/app/storage/migrated/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/models.py,backend/app/core/bob_client.py,backend/MIGRATION_GUIDE.md,backend/DIRECTORY_STRUCTURE.md,backend/app/core/flowchart.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-16T14:28:43.585Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.05

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

Now let me check the remaining core files and API endpoints to identify all dependencies:

<read_file>
<args>
<file>
<path>backend/app/core/validators.py</path>
</file>
<file>
<path>backend/app/core/flowchart.py</path>
</file>
<file>
<path>backend/app/api/migrate.py</path>
</file>
<file>
<path>backend/app/models/schemas.py</path>
</file>
<file>
<path>backend/app/utils/file_utils.py</path>
</file>
</args>
</read_file>

---

**User:**

[read_file for 5 files] Result:
<files>
<file><path>backend/app/core/validators.py</path>
<content lines="1-208">
  1 | """
  2 | Code validation module
  3 | Validates that converted code meets target framework requirements
  4 | """
  5 | from typing import Dict, Any, List, Tuple
  6 | import re
  7 | 
  8 | 
  9 | class ValidationResult:
 10 |     """Result of code validation"""
 11 |     
 12 |     def __init__(self, is_valid: bool, errors: List[str] = None, warnings: List[str] = None):
 13 |         self.is_valid = is_valid
 14 |         self.errors = errors or []
 15 |         self.warnings = warnings or []
 16 |     
 17 |     def __bool__(self):
 18 |         return self.is_valid
 19 |     
 20 |     def __repr__(self):
 21 |         return f"ValidationResult(valid={self.is_valid}, errors={len(self.errors)}, warnings={len(self.warnings)})"
 22 | 
 23 | 
 24 | class CodeValidator:
 25 |     """Validates converted code against target framework requirements"""
 26 |     
 27 |     def validate_fastapi_code(self, code: str, file_info: Dict[str, Any]) -> ValidationResult:
 28 |         """
 29 |         Validate that code is proper FastAPI and not Django
 30 |         """
 31 |         errors = []
 32 |         warnings = []
 33 |         
 34 |         # Check 1: Must not be empty or error message
 35 |         if not code or len(code.strip()) < 20:
 36 |             errors.append("Converted code is empty or too short")
 37 |             return ValidationResult(False, errors, warnings)
 38 |         
 39 |         if code.strip().startswith("Error:") or code.strip().startswith("# ERROR:"):
 40 |             errors.append("Conversion returned an error message")
 41 |             return ValidationResult(False, errors, warnings)
 42 |         
 43 |         # Check 2: Must have FastAPI imports
 44 |         has_fastapi_import = self._check_fastapi_imports(code)
 45 |         if not has_fastapi_import:
 46 |             errors.append("Missing FastAPI imports (from fastapi import ...)")
 47 |         
 48 |         # Check 3: Must NOT have Django imports
 49 |         django_imports = self._check_django_imports(code)
 50 |         if django_imports:
 51 |             errors.append(f"Still contains Django imports: {', '.join(django_imports[:3])}")
 52 |         
 53 |         # Check 4: For view files, must have route decorators
 54 |         if file_info.get("category") == "view" or file_info.get("is_django_view"):
 55 |             has_routes = self._check_route_decorators(code)
 56 |             if not has_routes:
 57 |                 errors.append("View file missing FastAPI route decorators (@router.get, @app.post, etc.)")
 58 |         
 59 |         # Check 5: For model files, should use Pydantic
 60 |         if file_info.get("category") == "model" or file_info.get("is_django_model"):
 61 |             has_pydantic = self._check_pydantic_models(code)
 62 |             if not has_pydantic:
 63 |                 warnings.append("Model file should use Pydantic BaseModel instead of Django models")
 64 |         
 65 |         # Check 6: Should not have Django-specific patterns
 66 |         django_patterns = self._check_django_patterns(code)
 67 |         if django_patterns:
 68 |             errors.append(f"Contains Django-specific patterns: {', '.join(django_patterns[:3])}")
 69 |         
 70 |         # Check 7: Should have async functions for FastAPI
 71 |         if file_info.get("category") == "view":
 72 |             has_async = "async def" in code
 73 |             if not has_async:
 74 |                 warnings.append("Consider using async functions for better FastAPI performance")
 75 |         
 76 |         is_valid = len(errors) == 0
 77 |         return ValidationResult(is_valid, errors, warnings)
 78 |     
 79 |     def _check_fastapi_imports(self, code: str) -> bool:
 80 |         """Check if code has FastAPI imports"""
 81 |         fastapi_patterns = [
 82 |             r'from fastapi import',
 83 |             r'import fastapi',
 84 |             r'from fastapi\.',
 85 |         ]
 86 |         return any(re.search(pattern, code) for pattern in fastapi_patterns)
 87 |     
 88 |     def _check_django_imports(self, code: str) -> List[str]:
 89 |         """Check for Django imports and return list of found imports"""
 90 |         django_imports = []
 91 |         
 92 |         django_patterns = [
 93 |             (r'from django\.', 'from django.*'),
 94 |             (r'import django', 'import django'),
 95 |             (r'from rest_framework', 'from rest_framework'),
 96 |             (r'import rest_framework', 'import rest_framework'),
 97 |         ]
 98 |         
 99 |         for pattern, display in django_patterns:
100 |             if re.search(pattern, code):
101 |                 django_imports.append(display)
102 |         
103 |         return django_imports
104 |     
105 |     def _check_route_decorators(self, code: str) -> bool:
106 |         """Check if code has FastAPI route decorators"""
107 |         route_patterns = [
108 |             r'@router\.(get|post|put|delete|patch)',
109 |             r'@app\.(get|post|put|delete|patch)',
110 |         ]
111 |         return any(re.search(pattern, code) for pattern in route_patterns)
112 |     
113 |     def _check_pydantic_models(self, code: str) -> bool:
114 |         """Check if code uses Pydantic models"""
115 |         pydantic_patterns = [
116 |             r'from pydantic import.*BaseModel',
117 |             r'class \w+\(BaseModel\)',
118 |         ]
119 |         return any(re.search(pattern, code) for pattern in pydantic_patterns)
120 |     
121 |     def _check_django_patterns(self, code: str) -> List[str]:
122 |         """Check for Django-specific code patterns"""
123 |         patterns_found = []
124 |         
125 |         django_patterns = [
126 |             (r'\.objects\.(get|filter|all|create)', 'Django ORM queries (.objects.)'),
127 |             (r'models\.Model', 'Django Model inheritance'),
128 |             (r'APIView', 'Django REST Framework APIView'),
129 |             (r'@login_required', 'Django @login_required decorator'),
130 |             (r'render\(request', 'Django render() function'),
131 |             (r'HttpResponse', 'Django HttpResponse'),
132 |             (r'Token\.objects', 'Django Token authentication'),
133 |             (r'permission_classes\s*=', 'Django permission_classes'),
134 |         ]
135 |         
136 |         for pattern, description in django_patterns:
137 |             if re.search(pattern, code):
138 |                 patterns_found.append(description)
139 |         
140 |         return patterns_found
141 |     
142 |     def validate_conversion_quality(self, original_code: str, converted_code: str) -> Tuple[int, List[str]]:
143 |         """
144 |         Assess quality of conversion
145 |         Returns: (quality_score 0-100, list of issues)
146 |         """
147 |         issues = []
148 |         score = 100
149 |         
150 |         # Check if code was actually transformed
151 |         similarity = self._calculate_similarity(original_code, converted_code)
152 |         if similarity > 0.9:
153 |             issues.append("Code appears unchanged (>90% similar to original)")
154 |             score -= 50
155 |         
156 |         # Check if converted code is longer (good sign of proper conversion)
157 |         original_lines = len(original_code.split('\n'))
158 |         converted_lines = len(converted_code.split('\n'))
159 |         
160 |         if converted_lines < original_lines * 0.5:
161 |             issues.append("Converted code is significantly shorter than original")
162 |             score -= 20
163 |         
164 |         # Check for TODO comments (indicates incomplete conversion)
165 |         todo_count = converted_code.lower().count('todo')
166 |         if todo_count > 3:
167 |             issues.append(f"Too many TODO comments ({todo_count}) - conversion may be incomplete")
168 |             score -= 10
169 |         
170 |         return max(0, score), issues
171 |     
172 |     def _calculate_similarity(self, text1: str, text2: str) -> float:
173 |         """Calculate simple similarity ratio between two texts"""
174 |         # Remove whitespace and comments for comparison
175 |         clean1 = re.sub(r'#.*$', '', text1, flags=re.MULTILINE)
176 |         clean1 = re.sub(r'\s+', '', clean1)
177 |         clean2 = re.sub(r'#.*$', '', text2, flags=re.MULTILINE)
178 |         clean2 = re.sub(r'\s+', '', clean2)
179 |         
180 |         if not clean1 or not clean2:
181 |             return 0.0
182 |         
183 |         # Simple character-level similarity
184 |         matches = sum(1 for a, b in zip(clean1, clean2) if a == b)
185 |         max_len = max(len(clean1), len(clean2))
186 |         
187 |         return matches / max_len if max_len > 0 else 0.0
188 | 
189 | 
190 | # Singleton instance
191 | _validator: CodeValidator = None
192 | 
193 | 
194 | def get_validator() -> CodeValidator:
195 |     """Get or create validator instance"""
196 |     global _validator
197 |     if _validator is None:
198 |         _validator = CodeValidator()
199 |     return _validator
200 | 
201 | 
202 | def validate_fastapi_code(code: str, file_info: Dict[str, Any]) -> ValidationResult:
203 |     """Convenience function to validate FastAPI code"""
204 |     validator = get_validator()
205 |     return validator.validate_fastapi_code(code, file_info)
206 | 
207 | 
208 | # Made with Bob
</content>
</file>
<file><path>backend/app/core/flowchart.py</path>
<content lines="1-121">
  1 | """
  2 | Flowchart generation using Mermaid.js
  3 | """
  4 | from typing import List, Dict, Any
  5 | 
  6 | 
  7 | class FlowchartGenerator:
  8 |     """Generate Mermaid.js flowcharts"""
  9 |     
 10 |     @staticmethod
 11 |     def generate_migration_flowchart(steps: List[str]) -> str:
 12 |         """
 13 |         Generate flowchart from migration steps
 14 |         """
 15 |         if not steps:
 16 |             return FlowchartGenerator.get_default_flowchart()
 17 |         
 18 |         # Build flowchart
 19 |         lines = ["graph TD"]
 20 |         
 21 |         # Start node
 22 |         lines.append("    A[Start Migration] --> B[Scan Repository]")
 23 |         
 24 |         # Add steps
 25 |         prev_node = "B"
 26 |         for i, step in enumerate(steps[:8], start=3):  # Limit to 8 steps for clarity
 27 |             node_id = chr(65 + i)  # C, D, E, etc.
 28 |             step_text = step.replace('"', "'").strip()
 29 |             if step_text.startswith(f"{i-2}."):
 30 |                 step_text = step_text.split(".", 1)[1].strip()
 31 |             
 32 |             lines.append(f"    {prev_node} --> {node_id}[{step_text[:40]}]")
 33 |             prev_node = node_id
 34 |         
 35 |         # Add decision and end
 36 |         final_node = chr(65 + len(steps[:8]) + 2)
 37 |         lines.append(f"    {prev_node} --> {final_node}{{Tests Pass?}}")
 38 |         lines.append(f"    {final_node} -->|Yes| Z[Migration Complete]")
 39 |         lines.append(f"    {final_node} -->|No| R[Rollback]")
 40 |         lines.append(f"    R --> B")
 41 |         
 42 |         return "\n".join(lines)
 43 |     
 44 |     @staticmethod
 45 |     def get_default_flowchart() -> str:
 46 |         """
 47 |         Get default migration flowchart
 48 |         """
 49 |         return """graph TD
 50 |     A[Start Migration] --> B[Upload/Clone Repository]
 51 |     B --> C[Scan & Detect Framework]
 52 |     C --> D[Generate Migration Plan]
 53 |     D --> E[Create Snapshot]
 54 |     E --> F[Convert Models/Entities]
 55 |     F --> G[Migrate Controllers/Views]
 56 |     G --> H[Update Routes/URLs]
 57 |     H --> I[Generate Config Files]
 58 |     I --> J[Run Tests]
 59 |     J --> K{Tests Pass?}
 60 |     K -->|Yes| L[Migration Complete]
 61 |     K -->|No| M[Rollback to Snapshot]
 62 |     M --> D"""
 63 |     
 64 |     @staticmethod
 65 |     def generate_architecture_diagram(framework_info: Dict[str, Any]) -> str:
 66 |         """
 67 |         Generate architecture diagram
 68 |         """
 69 |         framework = framework_info.get("framework", "unknown")
 70 |         
 71 |         if framework.lower() == "django":
 72 |             return """graph LR
 73 |     A[Client] --> B[URLs]
 74 |     B --> C[Views]
 75 |     C --> D[Models]
 76 |     D --> E[Database]
 77 |     C --> F[Templates]
 78 |     F --> A"""
 79 |         
 80 |         elif framework.lower() == "spring":
 81 |             return """graph LR
 82 |     A[Client] --> B[Controller]
 83 |     B --> C[Service]
 84 |     C --> D[Repository]
 85 |     D --> E[Database]
 86 |     B --> F[View]
 87 |     F --> A"""
 88 |         
 89 |         else:
 90 |             return """graph LR
 91 |     A[Client] --> B[API Layer]
 92 |     B --> C[Business Logic]
 93 |     C --> D[Data Layer]
 94 |     D --> E[Database]"""
 95 |     
 96 |     @staticmethod
 97 |     def generate_comparison_chart(
 98 |         source_framework: str,
 99 |         target_framework: str
100 |     ) -> str:
101 |         """
102 |         Generate comparison flowchart
103 |         """
104 |         return f"""graph LR
105 |     subgraph Source["{source_framework.upper()}"]
106 |         A1[Legacy Patterns]
107 |         A2[Monolithic]
108 |         A3[Synchronous]
109 |     end
110 |     
111 |     subgraph Target["{target_framework.upper()}"]
112 |         B1[Modern Patterns]
113 |         B2[Modular]
114 |         B3[Async/Await]
115 |     end
116 |     
117 |     A1 -.Migration.-> B1
118 |     A2 -.Migration.-> B2
119 |     A3 -.Migration.-> B3"""
120 | 
121 | # Made with Bob
</content>
</file>
<file><path>backend/app/api/migrate.py</path>
<content lines="1-62">
 1 | """
 2 | Code migration endpoint
 3 | """
 4 | from fastapi import APIRouter, HTTPException
 5 | from app.models.schemas import MigrateRequest, MigrateResponse
 6 | from app.utils.file_utils import get_project_path
 7 | from app.core.scanner import RepositoryScanner
 8 | from app.core.migrator import CodeMigrator
 9 | 
10 | router = APIRouter()
11 | 
12 | 
13 | @router.post("/migrate/{project_id}", response_model=MigrateResponse)
14 | async def migrate_project(
15 |     project_id: str,
16 |     request: MigrateRequest
17 | ):
18 |     """
19 |     Migrate project to target framework
20 |     """
21 |     # Find project
22 |     project_path = get_project_path(project_id, "uploads")
23 |     if not project_path.exists():
24 |         project_path = get_project_path(project_id, "repos")
25 |     
26 |     if not project_path.exists():
27 |         raise HTTPException(status_code=404, detail="Project not found")
28 |     
29 |     try:
30 |         # Scan to detect source framework
31 |         scanner = RepositoryScanner(project_path)
32 |         scan_results = await scanner.scan()
33 |         source_framework = scan_results["framework"]
34 |         
35 |         if source_framework == "unknown":
36 |             raise HTTPException(
37 |                 status_code=400,
38 |                 detail="Unable to detect source framework"
39 |             )
40 |         
41 |         # Perform migration
42 |         migrator = CodeMigrator(project_id)
43 |         migration_result = await migrator.migrate(
44 |             source_framework=source_framework,
45 |             target_framework=request.target_framework,
46 |             source_path=project_path
47 |         )
48 |         
49 |         return MigrateResponse(
50 |             project_id=project_id,
51 |             converted_files=migration_result["converted_files"],
52 |             output_path=migration_result["output_path"],
53 |             target_framework=request.target_framework,
54 |             status="completed"
55 |         )
56 |     
57 |     except HTTPException:
58 |         raise
59 |     except Exception as e:
60 |         raise HTTPException(status_code=500, detail=f"Migration failed: {str(e)}")
61 | 
62 | # Made with Bob
</content>
</file>
<file><path>backend/app/models/schemas.py</path>
<content lines="1-80">
 1 | """
 2 | Pydantic models for Legacy Code Surgeon AI
 3 | """
 4 | from typing import List, Optional, Dict, Any
 5 | from pydantic import BaseModel, Field
 6 | 
 7 | 
 8 | class GitHubCloneRequest(BaseModel):
 9 |     """Request model for cloning GitHub repository"""
10 |     repo_url: str = Field(..., description="GitHub repository URL")
11 | 
12 | 
13 | class ScanResponse(BaseModel):
14 |     """Response model for repository scan"""
15 |     project_id: str
16 |     framework: str
17 |     files_scanned: int
18 |     summary: str
19 |     detected_patterns: Optional[List[str]] = []
20 | 
21 | 
22 | class MigrationPlanRequest(BaseModel):
23 |     """Request model for generating migration plan"""
24 |     target_framework: Optional[str] = "fastapi"
25 | 
26 | 
27 | class MigrationPlanResponse(BaseModel):
28 |     """Response model for migration plan"""
29 |     project_id: str
30 |     steps: List[str]
31 |     bugs: List[str]
32 |     suggestions: List[str]
33 |     flowchart: str
34 |     estimated_complexity: str
35 | 
36 | 
37 | class MigrateRequest(BaseModel):
38 |     """Request model for migration"""
39 |     target_framework: str = Field(..., description="Target framework (fastapi, springboot, express)")
40 | 
41 | 
42 | class MigrateResponse(BaseModel):
43 |     """Response model for migration"""
44 |     project_id: str
45 |     converted_files: int
46 |     output_path: str
47 |     target_framework: str
48 |     status: str
49 | 
50 | 
51 | class RollbackResponse(BaseModel):
52 |     """Response model for rollback"""
53 |     project_id: str
54 |     status: str
55 |     message: str
56 | 
57 | 
58 | class StatusResponse(BaseModel):
59 |     """Response model for project status"""
60 |     project_id: str
61 |     status: str
62 |     framework: Optional[str] = None
63 |     target_framework: Optional[str] = None
64 |     progress: Optional[int] = 0
65 |     details: Optional[Dict[str, Any]] = {}
66 | 
67 | 
68 | class UploadResponse(BaseModel):
69 |     """Response model for file upload"""
70 |     project_id: str
71 |     message: str
72 |     files_extracted: int
73 | 
74 | 
75 | class ErrorResponse(BaseModel):
76 |     """Error response model"""
77 |     error: str
78 |     detail: Optional[str] = None
79 | 
80 | # Made with Bob
</content>
</file>
<file><path>backend/app/utils/file_utils.py</path>
<content lines="1-145">
  1 | """
  2 | File utility functions for Legacy Code Surgeon AI
  3 | """
  4 | import os
  5 | import shutil
  6 | import zipfile
  7 | import uuid
  8 | from pathlib import Path
  9 | from typing import List, Optional
 10 | 
 11 | 
 12 | # Storage paths
 13 | BASE_DIR = Path(__file__).parent.parent
 14 | STORAGE_DIR = BASE_DIR / "storage"
 15 | UPLOADS_DIR = STORAGE_DIR / "uploads"
 16 | REPOS_DIR = STORAGE_DIR / "repos"
 17 | MIGRATED_DIR = STORAGE_DIR / "migrated"
 18 | SNAPSHOTS_DIR = STORAGE_DIR / "snapshots"
 19 | 
 20 | # Ensure directories exist
 21 | for directory in [UPLOADS_DIR, REPOS_DIR, MIGRATED_DIR, SNAPSHOTS_DIR]:
 22 |     directory.mkdir(parents=True, exist_ok=True)
 23 | 
 24 | 
 25 | def generate_project_id() -> str:
 26 |     """Generate unique project ID"""
 27 |     return str(uuid.uuid4())
 28 | 
 29 | 
 30 | def get_project_path(project_id: str, storage_type: str = "uploads") -> Path:
 31 |     """Get path for a project"""
 32 |     storage_map = {
 33 |         "uploads": UPLOADS_DIR,
 34 |         "repos": REPOS_DIR,
 35 |         "migrated": MIGRATED_DIR,
 36 |         "snapshots": SNAPSHOTS_DIR
 37 |     }
 38 |     return storage_map.get(storage_type, UPLOADS_DIR) / project_id
 39 | 
 40 | 
 41 | async def extract_zip(zip_path: Path, extract_to: Path) -> int:
 42 |     """
 43 |     Extract ZIP file to destination
 44 |     Returns number of files extracted
 45 |     """
 46 |     extract_to.mkdir(parents=True, exist_ok=True)
 47 |     
 48 |     with zipfile.ZipFile(zip_path, 'r') as zip_ref:
 49 |         zip_ref.extractall(extract_to)
 50 |         file_count = len(zip_ref.namelist())
 51 |     
 52 |     return file_count
 53 | 
 54 | 
 55 | def should_ignore(path: Path) -> bool:
 56 |     """
 57 |     Check if path should be ignored during scanning
 58 |     """
 59 |     ignore_patterns = [
 60 |         'node_modules',
 61 |         '.git',
 62 |         'venv',
 63 |         '__pycache__',
 64 |         'target',
 65 |         'build',
 66 |         'dist',
 67 |         '.idea',
 68 |         '.vscode',
 69 |         '*.pyc',
 70 |         '*.class',
 71 |         '.DS_Store'
 72 |     ]
 73 |     
 74 |     path_str = str(path)
 75 |     for pattern in ignore_patterns:
 76 |         if pattern in path_str:
 77 |             return True
 78 |     return False
 79 | 
 80 | 
 81 | def scan_directory(directory: Path, extensions: Optional[List[str]] = None) -> List[Path]:
 82 |     """
 83 |     Recursively scan directory for files
 84 |     Optionally filter by extensions
 85 |     """
 86 |     files = []
 87 |     
 88 |     for item in directory.rglob('*'):
 89 |         if item.is_file() and not should_ignore(item):
 90 |             if extensions:
 91 |                 if item.suffix in extensions:
 92 |                     files.append(item)
 93 |             else:
 94 |                 files.append(item)
 95 |     
 96 |     return files
 97 | 
 98 | 
 99 | def copy_directory(src: Path, dst: Path) -> None:
100 |     """
101 |     Copy entire directory tree
102 |     """
103 |     if dst.exists():
104 |         shutil.rmtree(dst)
105 |     shutil.copytree(src, dst)
106 | 
107 | 
108 | def delete_directory(path: Path) -> None:
109 |     """
110 |     Delete directory and all contents
111 |     """
112 |     if path.exists():
113 |         shutil.rmtree(path)
114 | 
115 | 
116 | def read_file_content(file_path: Path) -> str:
117 |     """
118 |     Read file content safely
119 |     """
120 |     try:
121 |         with open(file_path, 'r', encoding='utf-8') as f:
122 |             return f.read()
123 |     except Exception as e:
124 |         return f"# Error reading file: {str(e)}"
125 | 
126 | 
127 | def write_file_content(file_path: Path, content: str) -> None:
128 |     """
129 |     Write content to file
130 |     """
131 |     file_path.parent.mkdir(parents=True, exist_ok=True)
132 |     with open(file_path, 'w', encoding='utf-8') as f:
133 |         f.write(content)
134 | 
135 | 
136 | def get_relative_path(file_path: Path, base_path: Path) -> str:
137 |     """
138 |     Get relative path from base
139 |     """
140 |     try:
141 |         return str(file_path.relative_to(base_path))
142 |     except ValueError:
143 |         return str(file_path)
144 | 
145 | # Made with Bob
</content>
</file>
</files>
<environment_details>
# VSCode Visible Files
backend\app\storage\migrated\798bd2af-067c-4f1e-8491-8e5398c28b6c\info\models.py

# VSCode Open Tabs
backend/app/core/detector.py,backend/app/core/migrator.py,backend/app/core/validators.py,backend/app/core/transformer.py,backend/app/storage/migrated/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/models.py,backend/app/core/bob_client.py,backend/MIGRATION_GUIDE.md,backend/DIRECTORY_STRUCTURE.md,backend/app/core/flowchart.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-16T14:28:49.904Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.14

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

Now let me check a few more API files to complete the dependency analysis:

<read_file>
<args>
<file>
<path>backend/app/core/scanner.py</path>
</file>
<file>
<path>backend/app/core/github_clone.py</path>
</file>
<file>
<path>backend/app/api/upload.py</path>
</file>
</args>
</read_file>

---

**User:**

[read_file for 'backend/app/core/scanner.py', 'backend/app/core/github_clone.py', 'backend/app/api/upload.py'] Result:
<files>
<file><path>backend/app/core/scanner.py</path>
<content lines="1-134">
  1 | """
  2 | Repository scanner
  3 | Scans and analyzes repository structure
  4 | """
  5 | from pathlib import Path
  6 | from typing import Dict, Any, List
  7 | from app.utils.file_utils import scan_directory, read_file_content
  8 | from app.core.detector import FrameworkDetector
  9 | 
 10 | 
 11 | class RepositoryScanner:
 12 |     """Scan and analyze repository"""
 13 |     
 14 |     def __init__(self, project_path: Path):
 15 |         self.project_path = project_path
 16 |         self.detector = FrameworkDetector(project_path)
 17 |     
 18 |     async def scan(self) -> Dict[str, Any]:
 19 |         """
 20 |         Perform full repository scan
 21 |         """
 22 |         # Detect framework
 23 |         framework_info = self.detector.detect()
 24 |         
 25 |         # Scan all files
 26 |         all_files = scan_directory(self.project_path)
 27 |         
 28 |         # Categorize files
 29 |         file_categories = self._categorize_files(all_files)
 30 |         
 31 |         # Generate summary
 32 |         summary = self._generate_summary(framework_info, file_categories)
 33 |         
 34 |         return {
 35 |             "framework": framework_info["framework"],
 36 |             "version": framework_info.get("version", "unknown"),
 37 |             "files_scanned": len(all_files),
 38 |             "key_files": framework_info.get("key_files", []),
 39 |             "patterns": framework_info.get("patterns", []),
 40 |             "file_categories": file_categories,
 41 |             "summary": summary
 42 |         }
 43 |     
 44 |     def _categorize_files(self, files: List[Path]) -> Dict[str, int]:
 45 |         """
 46 |         Categorize files by type
 47 |         """
 48 |         categories = {
 49 |             "python": 0,
 50 |             "java": 0,
 51 |             "javascript": 0,
 52 |             "typescript": 0,
 53 |             "html": 0,
 54 |             "css": 0,
 55 |             "config": 0,
 56 |             "other": 0
 57 |         }
 58 |         
 59 |         for file in files:
 60 |             ext = file.suffix.lower()
 61 |             
 62 |             if ext == ".py":
 63 |                 categories["python"] += 1
 64 |             elif ext == ".java":
 65 |                 categories["java"] += 1
 66 |             elif ext == ".js":
 67 |                 categories["javascript"] += 1
 68 |             elif ext in [".ts", ".tsx"]:
 69 |                 categories["typescript"] += 1
 70 |             elif ext in [".html", ".htm"]:
 71 |                 categories["html"] += 1
 72 |             elif ext in [".css", ".scss", ".sass"]:
 73 |                 categories["css"] += 1
 74 |             elif ext in [".json", ".xml", ".yml", ".yaml", ".properties", ".conf"]:
 75 |                 categories["config"] += 1
 76 |             else:
 77 |                 categories["other"] += 1
 78 |         
 79 |         return categories
 80 |     
 81 |     def _generate_summary(
 82 |         self,
 83 |         framework_info: Dict[str, Any],
 84 |         file_categories: Dict[str, int]
 85 |     ) -> str:
 86 |         """
 87 |         Generate human-readable summary
 88 |         """
 89 |         framework = framework_info.get("framework", "unknown")
 90 |         total_files = sum(file_categories.values())
 91 |         
 92 |         summary = f"Detected {framework.upper()} framework. "
 93 |         summary += f"Scanned {total_files} files. "
 94 |         
 95 |         # Add file type breakdown
 96 |         main_types = []
 97 |         for ftype, count in file_categories.items():
 98 |             if count > 0 and ftype != "other":
 99 |                 main_types.append(f"{count} {ftype}")
100 |         
101 |         if main_types:
102 |             summary += f"Contains: {', '.join(main_types)}. "
103 |         
104 |         # Add patterns
105 |         patterns = framework_info.get("patterns", [])
106 |         if patterns:
107 |             summary += f"Patterns: {', '.join(patterns)}."
108 |         
109 |         return summary
110 |     
111 |     def get_file_structure(self) -> Dict[str, Any]:
112 |         """
113 |         Get detailed file structure
114 |         """
115 |         structure = {
116 |             "directories": [],
117 |             "files": []
118 |         }
119 |         
120 |         for item in self.project_path.rglob('*'):
121 |             relative_path = str(item.relative_to(self.project_path))
122 |             
123 |             if item.is_dir():
124 |                 structure["directories"].append(relative_path)
125 |             else:
126 |                 structure["files"].append({
127 |                     "path": relative_path,
128 |                     "size": item.stat().st_size,
129 |                     "extension": item.suffix
130 |                 })
131 |         
132 |         return structure
133 | 
134 | # Made with Bob
</content>
</file>
<file><path>backend/app/core/github_clone.py</path>
<content lines="1-49">
 1 | """
 2 | GitHub repository cloning functionality
 3 | """
 4 | import git
 5 | from pathlib import Path
 6 | from typing import Tuple
 7 | from app.utils.file_utils import generate_project_id, get_project_path
 8 | 
 9 | 
10 | async def clone_github_repo(repo_url: str) -> Tuple[str, Path, str]:
11 |     """
12 |     Clone GitHub repository
13 |     
14 |     Returns:
15 |         Tuple of (project_id, repo_path, message)
16 |     """
17 |     project_id = generate_project_id()
18 |     repo_path = get_project_path(project_id, "repos")
19 |     
20 |     try:
21 |         # Clone repository
22 |         git.Repo.clone_from(repo_url, repo_path)
23 |         
24 |         # Count files
25 |         file_count = len(list(repo_path.rglob('*')))
26 |         
27 |         message = f"Successfully cloned repository from {repo_url}"
28 |         
29 |         return project_id, repo_path, message
30 |         
31 |     except git.GitCommandError as e:
32 |         raise Exception(f"Failed to clone repository: {str(e)}")
33 |     except Exception as e:
34 |         raise Exception(f"Error during cloning: {str(e)}")
35 | 
36 | 
37 | def validate_github_url(url: str) -> bool:
38 |     """
39 |     Validate GitHub URL format
40 |     """
41 |     valid_patterns = [
42 |         "github.com",
43 |         "https://github.com/",
44 |         "git@github.com:"
45 |     ]
46 |     
47 |     return any(pattern in url for pattern in valid_patterns)
48 | 
49 | # Made with Bob
</content>
</file>
<file><path>backend/app/api/upload.py</path>
<content lines="1-51">
 1 | """
 2 | File upload endpoint
 3 | Handles ZIP file uploads
 4 | """
 5 | from fastapi import APIRouter, UploadFile, File, HTTPException
 6 | from pathlib import Path
 7 | import aiofiles
 8 | from app.models.schemas import UploadResponse
 9 | from app.utils.file_utils import generate_project_id, get_project_path, extract_zip
10 | 
11 | router = APIRouter()
12 | 
13 | 
14 | @router.post("/upload", response_model=UploadResponse)
15 | async def upload_project(file: UploadFile = File(...)):
16 |     """
17 |     Upload ZIP file containing project
18 |     """
19 |     # Validate file type
20 |     if not file.filename.endswith('.zip'):
21 |         raise HTTPException(status_code=400, detail="Only ZIP files are allowed")
22 |     
23 |     # Generate project ID
24 |     project_id = generate_project_id()
25 |     project_path = get_project_path(project_id, "uploads")
26 |     project_path.mkdir(parents=True, exist_ok=True)
27 |     
28 |     # Save uploaded file
29 |     zip_path = project_path / "upload.zip"
30 |     
31 |     try:
32 |         async with aiofiles.open(zip_path, 'wb') as f:
33 |             content = await file.read()
34 |             await f.write(content)
35 |         
36 |         # Extract ZIP
37 |         files_extracted = await extract_zip(zip_path, project_path)
38 |         
39 |         # Remove ZIP file after extraction
40 |         zip_path.unlink()
41 |         
42 |         return UploadResponse(
43 |             project_id=project_id,
44 |             message="Project uploaded and extracted successfully",
45 |             files_extracted=files_extracted
46 |         )
47 |     
48 |     except Exception as e:
49 |         raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")
50 | 
51 | # Made with Bob
</content>
</file>
</files>
<environment_details>
# VSCode Visible Files
backend\app\storage\migrated\798bd2af-067c-4f1e-8491-8e5398c28b6c\info\models.py

# VSCode Open Tabs
backend/app/core/detector.py,backend/app/core/migrator.py,backend/app/core/validators.py,backend/app/core/transformer.py,backend/app/storage/migrated/798bd2af-067c-4f1e-8491-8e5398c28b6c/info/models.py,backend/app/core/bob_client.py,backend/MIGRATION_GUIDE.md,backend/DIRECTORY_STRUCTURE.md,backend/app/core/flowchart.py

# Current Time
Current time in ISO 8601 UTC format: 2026-05-16T14:28:55.195Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.26

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

Based on my analysis of the project, I can now rewrite the requirements.txt file with all the necessary dependencies. The project uses:

1. **FastAPI** - Web framework
2. **Uvicorn** - ASGI server
3. **Pydantic** - Data validation
4. **HTTPX** - Async HTTP client (for Bob AI API calls)
5. **GitPython** - Git repository cloning
6. **Aiofiles** - Async file operations
7. **Python-multipart** - File upload handling
8. **Python-dotenv** - Environment variable management
9. **Pydantic-settings** - Settings management
10. **PyJWT** - JWT token handling (used in transformer.py)
11. **Passlib[bcrypt]** - Password hashing (used in transformer.py)
12. **SQLAlchemy** - Database ORM (generated in transformed code)

<write_to_file>
<path>backend/requirements.txt</path>
<content># FastAPI Backend Requirements
# Legacy Code Surgeon AI - Django to FastAPI Migration Tool

# Core Web Framework
fastapi==0.115.0
uvicorn[standard]==0.32.0

# Data Validation & Settings
pydantic==2.10.3
pydantic-settings==2.6.1

# HTTP Client (for IBM Bob AI API)
httpx==0.27.2

# File Handling
python-multipart==0.0.12
aiofiles==24.1.0

# Git Operations
GitPython==3.1.43

# Environment Variables
python-dotenv==1.0.1

# Authentication & Security
PyJWT==2.9.0
passlib[bcrypt]==1.7.4

# Database ORM (for generated migrations)
SQLAlchemy==2.0.36
</content>
<line_count>28</line_count>
</write_to_file>

---

**User:**

[write_to_file for 'backend/requirements.txt'] Result:
<file_write_result>
<path>backend/requirements.txt</path>
<operation>modified</operation>
<notice>
<i>You do not need to re-read the file, as you have seen all changes</i>
<i>Proceed with the task using these changes as the new baseline.</i>
</notice>
</file_write_result>

<environment_details>
# VSCode Visible Files
backend\requirements.txt

# VSCode Open Tabs
backend/app/core/detector.py,backend/app/core/migrator.py,backend/app/core/validators.py,backend/app/core/transformer.py,backend/requirements.txt,backend/app/core/bob_client.py,backend/MIGRATION_GUIDE.md,backend/DIRECTORY_STRUCTURE.md,backend/app/core/flowchart.py

# Recently Modified Files
These files have been modified since you last accessed them (file was just edited so you may need to re-read it before editing):
backend/requirements.txt

# Current Time
Current time in ISO 8601 UTC format: 2026-05-16T14:29:37.602Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.39

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

<attempt_completion>
<result>
Successfully analyzed the project and rewrote requirements.txt with all necessary dependencies:

**Added Dependencies:**
- **PyJWT==2.9.0** - JWT token handling (used in authentication setup in transformer.py)
- **passlib[bcrypt]==1.7.4** - Password hashing (used in JWT auth setup)
- **SQLAlchemy==2.0.36** - Database ORM (generated in migrated code for models)

**Existing Dependencies (kept with current versions):**
- FastAPI 0.115.0 - Core web framework
- Uvicorn 0.32.0 - ASGI server
- Pydantic 2.10.3 - Data validation
- Pydantic-settings 2.6.1 - Settings management
- HTTPX 0.27.2 - Async HTTP client for Bob AI API
- Python-multipart 0.0.12 - File upload handling
- Aiofiles 24.1.0 - Async file operations
- GitPython 3.1.43 - Git repository cloning
- Python-dotenv 1.0.1 - Environment variables

The requirements.txt now includes all dependencies used throughout the codebase, including those needed for:
- Core FastAPI application
- IBM Bob AI integration
- File upload/download operations
- Git repository cloning
- JWT authentication (generated in migrated code)
- SQLAlchemy database models (generated in migrated code)
</result>
</attempt_completion>

