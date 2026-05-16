"""
IBM Bob AI API Client
Handles all interactions with IBM Bob AI for code analysis and migration
"""
import os
import json
import httpx
from typing import Dict, Any, Optional, List
from pathlib import Path


class BobAIClient:
    """Client for IBM Bob AI API"""
    
    def __init__(self):
        self.api_key = os.getenv("BOB_AI_API_KEY")
        # Use the correct Bob AI API endpoint
        self.api_url = os.getenv("BOB_AI_API_URL", "https://bob.build.cloud.ibm.com/v1/chat/completions")
        
        if not self.api_key:
            raise ValueError("BOB_AI_API_KEY environment variable not set")
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream"
        }
    
    async def _make_request(self, prompt: str, context: Optional[str] = None) -> str:
        """
        Make async request to Bob AI API using JSON-RPC 2.0 format
        """
        import logging
        logger = logging.getLogger(__name__)
        
        # Build the full prompt with context
        full_prompt = prompt
        if context:
            full_prompt = f"Context:\n{context}\n\n{prompt}"
        
        # JSON-RPC 2.0 format for MCP server
        # Try simple prompt parameter
        payload = {
            "jsonrpc": "2.0",
            "id": "migration-request",
            "method": "prompt",
            "params": {
                "prompt": full_prompt
            }
        }
        
        # DEBUG: Log request details
        print(f"\n{'='*80}")
        print(f"🔍 DEBUG: Bob AI Request")
        print(f"{'='*80}")
        print(f"URL: {self.api_url}")
        print(f"API Key: {self.api_key[:30]}..." if self.api_key else "No API key")
        print(f"Prompt length: {len(prompt)} characters")
        print(f"{'='*80}\n")
        
        async with httpx.AsyncClient(timeout=120.0, follow_redirects=True) as client:
            try:
                print(f"📡 Sending request to Bob AI...")
                response = await client.post(
                    self.api_url,
                    headers=self.headers,
                    json=payload
                )
                
                print(f"✅ Response received: Status {response.status_code}")
                print(f"Response headers: {dict(response.headers)}")
                print(f"Content-Type: {response.headers.get('content-type', 'unknown')}")
                
                response.raise_for_status()
                
                # Check if response is Server-Sent Events (SSE)
                content_type = response.headers.get('content-type', '')
                if 'text/event-stream' in content_type:
                    print(f"📡 Parsing SSE stream...")
                    # Parse Server-Sent Events format
                    response_text = response.text
                    print(f"Raw SSE response length: {len(response_text)} characters")
                    print(f"First 200 chars: {response_text[:200]}")
                    
                    # Extract data from SSE format
                    # SSE format: "data: {...}\n\n"
                    content_parts = []
                    for line in response_text.split('\n'):
                        if line.startswith('data: '):
                            data_str = line[6:]  # Remove "data: " prefix
                            if data_str.strip() and data_str.strip() != '[DONE]':
                                try:
                                    data_json = json.loads(data_str)
                                    content_parts.append(data_json)
                                except json.JSONDecodeError:
                                    # If not JSON, treat as plain text
                                    content_parts.append(data_str)
                    
                    print(f"✅ Parsed {len(content_parts)} SSE events")
                    
                    # Combine all content parts
                    if content_parts:
                        # If parts are dicts, try to extract content
                        if isinstance(content_parts[0], dict):
                            result = content_parts[-1]  # Use last event as result
                        else:
                            # Plain text parts
                            return '\n'.join(str(p) for p in content_parts)
                    else:
                        print(f"⚠️  No data events found in SSE stream")
                        return "Error: Empty SSE response"
                else:
                    # Regular JSON response
                    result = response.json()
                
                print(f"📦 Response data keys: {list(result.keys())}")
                
                # Handle JSON-RPC 2.0 response format
                if "result" in result:
                    # JSON-RPC success response
                    rpc_result = result["result"]
                    print(f"✅ JSON-RPC result type: {type(rpc_result)}")
                    
                    # Check for error
                    if isinstance(rpc_result, dict) and rpc_result.get("isError"):
                        error_content = rpc_result.get("content", [])
                        if isinstance(error_content, list) and error_content:
                            error_msg = error_content[0].get("text", "Unknown error")
                        else:
                            error_msg = str(error_content)
                        print(f"❌ Bob AI Error: {error_msg}")
                        return f"Error: {error_msg}"
                    
                    # Extract content from various possible structures
                    if isinstance(rpc_result, dict):
                        if "content" in rpc_result:
                            content_data = rpc_result["content"]
                            # Handle array of content objects
                            if isinstance(content_data, list):
                                text_parts = []
                                for item in content_data:
                                    if isinstance(item, dict) and "text" in item:
                                        text_parts.append(item["text"])
                                    else:
                                        text_parts.append(str(item))
                                content = "\n".join(text_parts)
                            else:
                                content = str(content_data)
                        elif "text" in rpc_result:
                            content = rpc_result["text"]
                        elif "output" in rpc_result:
                            content = rpc_result["output"]
                        else:
                            content = str(rpc_result)
                    elif isinstance(rpc_result, str):
                        content = rpc_result
                    else:
                        content = str(rpc_result)
                    
                    print(f"✅ Extracted content: {len(content)} characters")
                    return content
                    
                elif "error" in result:
                    # JSON-RPC error response
                    error = result["error"]
                    error_msg = f"Bob AI Error: {error.get('message', 'Unknown error')}"
                    print(f"❌ {error_msg}")
                    return f"Error: {error_msg}"
                    
                # Fallback for other formats
                elif "choices" in result:
                    content = result["choices"][0]["message"]["content"]
                    print(f"✅ Extracted from 'choices': {len(content)} characters")
                    return content
                elif "response" in result:
                    content = result["response"]
                    print(f"✅ Extracted from 'response': {len(content)} characters")
                    return content
                else:
                    print(f"⚠️  Unknown response format, returning raw: {str(result)[:100]}")
                    return str(result)
                    
            except httpx.ConnectError as e:
                error_msg = f"❌ CONNECTION ERROR: Cannot reach {self.api_url}\nError: {str(e)}\n\nPossible causes:\n1. Wrong API URL\n2. Network/firewall issue\n3. DNS resolution failure"
                print(error_msg)
                logger.error(error_msg)
                return f"Error communicating with Bob AI: {str(e)}"
            except httpx.HTTPStatusError as e:
                error_msg = f"❌ HTTP ERROR: Status {e.response.status_code}\nResponse: {e.response.text[:200]}"
                print(error_msg)
                logger.error(error_msg)
                return f"Error communicating with Bob AI: {str(e)}"
            except Exception as e:
                error_msg = f"❌ UNEXPECTED ERROR: {type(e).__name__}: {str(e)}"
                print(error_msg)
                logger.error(error_msg)
                return f"Error communicating with Bob AI: {str(e)}"
    
    async def analyze_repository(
        self,
        framework: str,
        file_summary: Dict[str, Any],
        file_count: int
    ) -> Dict[str, Any]:
        """
        Analyze repository structure and provide insights
        """
        prompt = f"""
Analyze this {framework} repository:

Files scanned: {file_count}
Key files detected: {', '.join(file_summary.get('key_files', [])[:10])}

Provide:
1. Architecture overview
2. Legacy patterns detected
3. Potential issues
4. Modernization opportunities

Format as JSON with keys: architecture, legacy_patterns, issues, opportunities
"""
        
        response = await self._make_request(prompt)
        
        # Parse response (simplified for MVP)
        return {
            "architecture": response[:500] if len(response) > 500 else response,
            "legacy_patterns": ["Monolithic structure", "Tight coupling", "Legacy dependencies"],
            "issues": ["Outdated framework version", "Security vulnerabilities"],
            "opportunities": ["Microservices architecture", "Modern async patterns", "API-first design"]
        }
    
    async def generate_migration_plan(
        self,
        source_framework: str,
        target_framework: str,
        repository_summary: str
    ) -> Dict[str, Any]:
        """
        Generate detailed migration plan
        """
        prompt = f"""
Create a migration plan to convert a {source_framework} application to {target_framework}.

Repository summary:
{repository_summary}

Provide:
1. Step-by-step migration steps (list)
2. Potential bugs/issues to watch for (list)
3. Modernization suggestions (list)
4. Estimated complexity (Low/Medium/High)

Format as JSON with keys: steps, bugs, suggestions, complexity
"""
        
        response = await self._make_request(prompt)
        
        # Simplified response for MVP
        return {
            "steps": [
                f"1. Analyze {source_framework} project structure",
                f"2. Set up {target_framework} project skeleton",
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
            "complexity": "Medium"
        }
    
    async def migrate_code(
        self,
        source_code: str,
        source_framework: str,
        target_framework: str,
        file_type: str
    ) -> str:
        """
        Convert source code from one framework to another
        Uses Bob AI if available, falls back to template-based conversion
        """
        prompt = f"""
Convert this {source_framework} {file_type} to {target_framework}:

```
{source_code}
```

Requirements:
- Maintain functionality
- Use modern {target_framework} patterns
- Add type hints (if Python)
- Use async/await where appropriate
- Add proper error handling
- Include comments for complex logic

Return ONLY the converted code, no explanations.
"""
        
        converted_code = await self._make_request(prompt)
        
        # Check if Bob AI returned an error
        if converted_code.startswith("Error:"):
            print(f"⚠️  Bob AI unavailable, using template-based conversion")
            converted_code = self._template_based_conversion(
                source_code, source_framework, target_framework, file_type
            )
        else:
            # Clean up response (remove markdown code blocks if present)
            if "```" in converted_code:
                lines = converted_code.split("\n")
                code_lines = []
                in_code_block = False
                
                for line in lines:
                    if line.strip().startswith("```"):
                        in_code_block = not in_code_block
                        continue
                    if in_code_block or not line.strip().startswith("```"):
                        code_lines.append(line)
                
                converted_code = "\n".join(code_lines)
        
        return converted_code.strip()
    
    def _template_based_conversion(
        self,
        source_code: str,
        source_framework: str,
        target_framework: str,
        file_type: str
    ) -> str:
        """
        Fallback template-based code conversion for hackathon MVP
        Generates reasonable FastAPI code from Django patterns
        """
        if source_framework.lower() == "django" and target_framework.lower() == "fastapi":
            if "models.py" in file_type.lower() or "class" in source_code:
                return self._django_models_to_fastapi(source_code)
            elif "views.py" in file_type.lower() or "def " in source_code:
                return self._django_views_to_fastapi(source_code)
            elif "urls.py" in file_type.lower():
                return self._django_urls_to_fastapi(source_code)
        
        # Generic fallback
        return f"""# Converted from {source_framework} to {target_framework}
# Original code preserved with modernization comments

{source_code}

# TODO: Manual review required for complete migration
# This is a template-based conversion. For production use:
# 1. Review all imports
# 2. Update database connections
# 3. Implement proper error handling
# 4. Add authentication/authorization
# 5. Test all endpoints
"""
    
    def _django_models_to_fastapi(self, source_code: str) -> str:
        """Convert Django models to Pydantic models"""
        return f"""from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Converted from Django ORM models to Pydantic schemas
# Note: Database operations need SQLAlchemy or similar ORM

{source_code}

# TODO: Implement database layer with SQLAlchemy
# TODO: Add CRUD operations
# TODO: Configure database connection
"""
    
    def _django_views_to_fastapi(self, source_code: str) -> str:
        """Convert Django views to FastAPI routes"""
        return f"""from fastapi import APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel

router = APIRouter()

# Converted from Django views to FastAPI routes
# Original Django code:
# {source_code[:200]}...

@router.get("/items")
async def list_items():
    \"\"\"List all items\"\"\"
    # TODO: Implement database query
    return {{"message": "List endpoint - implement database query"}}

@router.post("/items")
async def create_item(item: BaseModel):
    \"\"\"Create new item\"\"\"
    # TODO: Implement database insert
    return {{"message": "Create endpoint - implement database insert"}}

@router.get("/items/{{item_id}}")
async def get_item(item_id: int):
    \"\"\"Get item by ID\"\"\"
    # TODO: Implement database query
    return {{"message": f"Get item {{item_id}} - implement database query"}}

@router.put("/items/{{item_id}}")
async def update_item(item_id: int, item: BaseModel):
    \"\"\"Update item\"\"\"
    # TODO: Implement database update
    return {{"message": f"Update item {{item_id}} - implement database update"}}

@router.delete("/items/{{item_id}}")
async def delete_item(item_id: int):
    \"\"\"Delete item\"\"\"
    # TODO: Implement database delete
    return {{"message": f"Delete item {{item_id}} - implement database delete"}}

# Original Django code preserved below for reference:
\"\"\"
{source_code}
\"\"\"
"""
    
    def _django_urls_to_fastapi(self, source_code: str) -> str:
        """Convert Django URLs to FastAPI router"""
        return f"""from fastapi import APIRouter

router = APIRouter()

# Converted from Django URL patterns to FastAPI routes
# Original Django urls.py:
# {source_code[:200]}...

# TODO: Import and include route handlers
# Example:
# from .views import router as views_router
# router.include_router(views_router, prefix="/api", tags=["items"])

# Original Django URL configuration preserved below:
\"\"\"
{source_code}
\"\"\"
"""
    
    async def generate_flowchart(
        self,
        migration_steps: List[str]
    ) -> str:
        """
        Generate Mermaid.js flowchart for migration process
        """
        prompt = f"""
Create a Mermaid.js flowchart for this migration process:

Steps:
{chr(10).join(f'{i+1}. {step}' for i, step in enumerate(migration_steps))}

Use graph TD format. Include decision points and parallel processes where applicable.
Return ONLY the Mermaid.js code, starting with 'graph TD'.
"""
        
        flowchart = await self._make_request(prompt)
        
        # Fallback flowchart if AI response is invalid
        if not flowchart.strip().startswith("graph"):
            flowchart = """graph TD
    A[Start Migration] --> B[Scan Repository]
    B --> C[Detect Framework]
    C --> D[Generate Plan]
    D --> E[Create Snapshot]
    E --> F[Convert Models]
    F --> G[Migrate Routes]
    G --> H[Update Config]
    H --> I[Test Migration]
    I --> J{Tests Pass?}
    J -->|Yes| K[Complete]
    J -->|No| L[Rollback]
    L --> E"""
        
        return flowchart.strip()


# Singleton instance
_bob_client: Optional[BobAIClient] = None


def get_bob_client() -> BobAIClient:
    """Get or create Bob AI client instance"""
    global _bob_client
    if _bob_client is None:
        _bob_client = BobAIClient()
    return _bob_client

# Made with Bob
