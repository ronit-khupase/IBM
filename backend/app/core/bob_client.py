"""
IBM Bob AI API Client
Handles all interactions with IBM Bob AI for code analysis and migration
"""
import os
import json
import re
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
        Generate detailed migration plan using Bob AI
        """
        prompt = f"""
You are an expert software architect specializing in framework migrations.

Analyze this {source_framework} application and create a detailed migration plan to {target_framework}.

Repository Analysis:
{repository_summary}

Generate a comprehensive migration plan with:

1. MIGRATION STEPS: Provide 8-12 specific, actionable steps for migrating this exact codebase from {source_framework} to {target_framework}. Be specific to the files and patterns detected in the repository summary.

2. POTENTIAL ISSUES: List 4-6 specific bugs, compatibility issues, or challenges that may arise during this migration based on the detected patterns and file structure.

3. MODERNIZATION SUGGESTIONS: Provide 4-6 concrete suggestions for improving the code during migration (async patterns, better architecture, modern libraries, etc.).

4. COMPLEXITY ASSESSMENT: Rate the migration complexity as "Low", "Medium", or "High" based on the repository size, patterns detected, and migration scope.

IMPORTANT: Base your response on the actual repository summary provided. Make it specific to this codebase, not generic.

Return your response in this exact JSON format:
{{
  "steps": ["step 1", "step 2", ...],
  "bugs": ["issue 1", "issue 2", ...],
  "suggestions": ["suggestion 1", "suggestion 2", ...],
  "complexity": "Low|Medium|High"
}}

Return ONLY valid JSON, no additional text.
"""
        
        response = await self._make_request(prompt)
        
        # Try to parse JSON response from Bob AI
        try:
            # Clean up response - remove markdown code blocks if present
            cleaned_response = response.strip()
            if "```json" in cleaned_response:
                # Extract JSON from markdown code block
                json_match = re.search(r'```json\s*(\{.*?\})\s*```', cleaned_response, re.DOTALL)
                if json_match:
                    cleaned_response = json_match.group(1)
            elif "```" in cleaned_response:
                # Extract from generic code block
                json_match = re.search(r'```\s*(\{.*?\})\s*```', cleaned_response, re.DOTALL)
                if json_match:
                    cleaned_response = json_match.group(1)
            
            # Try to find JSON object in response
            json_match = re.search(r'\{.*\}', cleaned_response, re.DOTALL)
            if json_match:
                cleaned_response = json_match.group(0)
            
            # Parse JSON
            plan_data = json.loads(cleaned_response)
            
            # Validate required keys
            if all(key in plan_data for key in ["steps", "bugs", "suggestions", "complexity"]):
                print(f"✅ Successfully parsed Bob AI migration plan")
                print(f"   Steps: {len(plan_data['steps'])}")
                print(f"   Issues: {len(plan_data['bugs'])}")
                print(f"   Suggestions: {len(plan_data['suggestions'])}")
                print(f"   Complexity: {plan_data['complexity']}")
                return plan_data
            else:
                print(f"⚠️  Bob AI response missing required keys")
                raise ValueError("Missing required keys in response")
                
        except (json.JSONDecodeError, ValueError) as e:
            print(f"⚠️  Failed to parse Bob AI response as JSON: {str(e)}")
            print(f"   Response preview: {response[:200]}")
            print(f"   Falling back to intelligent parsing...")
            
            # Fallback: Try to extract information from text response
            return self._parse_text_migration_plan(response, source_framework, target_framework)
    
    def _parse_text_migration_plan(
        self,
        response: str,
        source_framework: str,
        target_framework: str
    ) -> Dict[str, Any]:
        """
        Parse migration plan from text response when JSON parsing fails
        """
        import re
        
        # Try to extract sections from text
        steps = []
        bugs = []
        suggestions = []
        complexity = "Medium"
        
        # Extract steps (look for numbered lists)
        step_pattern = r'(?:^|\n)\s*\d+[\.\)]\s*(.+?)(?=\n\s*\d+[\.\)]|\n\n|$)'
        step_matches = re.findall(step_pattern, response, re.MULTILINE)
        if step_matches:
            steps = [step.strip() for step in step_matches[:12]]
        
        # Extract issues/bugs (look for keywords)
        if "issue" in response.lower() or "bug" in response.lower() or "problem" in response.lower():
            issue_section = re.search(r'(?:issues?|bugs?|problems?)[\s:]+(.+?)(?=\n\n|\n[A-Z]|$)', response, re.IGNORECASE | re.DOTALL)
            if issue_section:
                issue_text = issue_section.group(1)
                bug_matches = re.findall(r'[-•*]\s*(.+?)(?=\n[-•*]|\n\n|$)', issue_text, re.MULTILINE)
                if bug_matches:
                    bugs = [bug.strip() for bug in bug_matches[:6]]
        
        # Extract suggestions (look for keywords)
        if "suggest" in response.lower() or "recommend" in response.lower() or "improve" in response.lower():
            suggestion_section = re.search(r'(?:suggestions?|recommendations?|improvements?)[\s:]+(.+?)(?=\n\n|\n[A-Z]|$)', response, re.IGNORECASE | re.DOTALL)
            if suggestion_section:
                suggestion_text = suggestion_section.group(1)
                suggestion_matches = re.findall(r'[-•*]\s*(.+?)(?=\n[-•*]|\n\n|$)', suggestion_text, re.MULTILINE)
                if suggestion_matches:
                    suggestions = [sug.strip() for sug in suggestion_matches[:6]]
        
        # Extract complexity
        complexity_match = re.search(r'complexity[\s:]+(\w+)', response, re.IGNORECASE)
        if complexity_match:
            complexity_value = complexity_match.group(1).capitalize()
            if complexity_value in ["Low", "Medium", "High"]:
                complexity = complexity_value
        
        # If we couldn't extract enough information, use fallback
        if len(steps) < 5:
            steps = [
                f"Analyze {source_framework} project structure and dependencies",
                f"Set up {target_framework} project skeleton with proper structure",
                "Convert data models and schemas",
                "Migrate API routes and endpoints",
                "Update authentication and authorization logic",
                "Convert middleware and request/response handling",
                "Update configuration files and environment variables",
                "Implement async patterns where applicable",
                "Add comprehensive error handling",
                "Test all migrated endpoints",
                "Update documentation and deployment configs"
            ]
        
        if len(bugs) < 3:
            bugs = [
                "Database connection and ORM query differences",
                "Authentication middleware compatibility issues",
                "Session management and state handling changes",
                "Static file serving configuration differences",
                "Third-party library compatibility"
            ]
        
        if len(suggestions) < 3:
            suggestions = [
                "Implement async/await patterns for better performance",
                "Use dependency injection for better testability",
                "Add comprehensive API documentation with OpenAPI",
                "Implement proper request validation with Pydantic",
                "Use modern error handling and logging practices"
            ]
        
        print(f"✅ Parsed migration plan from text response")
        print(f"   Steps: {len(steps)}")
        print(f"   Issues: {len(bugs)}")
        print(f"   Suggestions: {len(suggestions)}")
        
        return {
            "steps": steps,
            "bugs": bugs,
            "suggestions": suggestions,
            "complexity": complexity
        }
    
    async def migrate_code(
        self,
        source_code: str,
        source_framework: str,
        target_framework: str,
        file_info: Dict[str, Any]
    ) -> str:
        """
        Convert source code from one framework to another
        Enhanced with validation and pattern-based transformation
        """
        from app.core.validators import validate_fastapi_code
        from app.core.transformer import get_enhanced_transformer
        
        print(f"\n{'='*60}")
        print(f"🔄 Converting {file_info.get('filename', 'file')}")
        print(f"   Category: {file_info.get('category', 'unknown')}")
        print(f"   Framework: {source_framework} → {target_framework}")
        print(f"{'='*60}\n")
        
        # Step 1: Try Bob AI conversion with enhanced prompt
        print("📡 Step 1: Attempting Bob AI conversion...")
        converted_code = await self._try_bob_ai_conversion(
            source_code, source_framework, target_framework, file_info
        )
        
        # Step 2: Validate the conversion
        print("✅ Step 2: Validating conversion...")
        validation = validate_fastapi_code(converted_code, file_info)
        
        if validation.is_valid:
            print(f"✅ Bob AI conversion successful and validated!")
            if validation.warnings:
                print(f"⚠️  Warnings: {len(validation.warnings)}")
                for warning in validation.warnings[:2]:
                    print(f"   - {warning}")
            return self._cleanup_code(converted_code)
        
        # Step 3: Bob AI failed validation, try with examples
        print(f"❌ Bob AI conversion failed validation:")
        for error in validation.errors[:3]:
            print(f"   - {error}")
        
        print("\n📡 Step 3: Retrying Bob AI with examples...")
        converted_code = await self._try_bob_ai_with_examples(
            source_code, source_framework, target_framework, file_info
        )
        
        validation = validate_fastapi_code(converted_code, file_info)
        if validation.is_valid:
            print(f"✅ Bob AI retry successful!")
            return self._cleanup_code(converted_code)
        
        # Step 4: Fall back to enhanced pattern-based transformation
        print(f"❌ Bob AI retry also failed")
        print(f"\n🔧 Step 4: Using enhanced pattern-based transformation...")
        
        transformer = get_enhanced_transformer()
        converted_code = transformer.transform(source_code, file_info)
        
        # Step 5: Final validation
        print("✅ Step 5: Final validation...")
        validation = validate_fastapi_code(converted_code, file_info)
        
        if validation.is_valid:
            print(f"✅ Pattern-based conversion successful!")
            return converted_code
        else:
            print(f"⚠️  Pattern-based conversion has issues:")
            for error in validation.errors[:2]:
                print(f"   - {error}")
            print(f"   Returning best effort conversion\n")
            return converted_code
    
    async def _try_bob_ai_conversion(
        self,
        source_code: str,
        source_framework: str,
        target_framework: str,
        file_info: Dict[str, Any]
    ) -> str:
        """Try Bob AI conversion with enhanced prompt"""
        
        category = file_info.get('category', 'code')
        filename = file_info.get('filename', 'file')
        
        prompt = f"""You are an expert at converting {source_framework} code to {target_framework}.

Convert this {source_framework} {category} file ({filename}) to {target_framework}:

```python
{source_code}
```

CRITICAL REQUIREMENTS:
1. Remove ALL Django imports (django.*, rest_framework.*)
2. Add FastAPI imports (from fastapi import ...)
3. Convert Django patterns to FastAPI equivalents:
   - APIView classes → @router.get/post/etc functions
   - models.Model → Pydantic BaseModel
   - Token auth → JWT dependencies
   - Django ORM → SQLAlchemy queries
4. Use async/await for route handlers
5. Return ONLY the converted FastAPI code
6. Do NOT preserve Django code
7. Do NOT add explanatory text

Return the complete, working FastAPI code now:
"""
        
        converted_code = await self._make_request(prompt)
        
        # Check if Bob AI returned an error
        if converted_code.startswith("Error:"):
            print(f"   ⚠️  Bob AI unavailable: {converted_code[:100]}")
            return converted_code
        
        return self._cleanup_code(converted_code)
    
    async def _try_bob_ai_with_examples(
        self,
        source_code: str,
        source_framework: str,
        target_framework: str,
        file_info: Dict[str, Any]
    ) -> str:
        """Retry Bob AI with conversion examples"""
        
        example = self._get_conversion_example(file_info.get('category', 'view'))
        
        prompt = f"""Convert {source_framework} to {target_framework}.

EXAMPLE CONVERSION:
{example}

Now convert this code following the same pattern:

```python
{source_code}
```

Return ONLY the converted FastAPI code:
"""
        
        converted_code = await self._make_request(prompt)
        
        if converted_code.startswith("Error:"):
            return converted_code
        
        return self._cleanup_code(converted_code)
    
    def _get_conversion_example(self, category: str) -> str:
        """Get example conversion for the given category"""
        
        if category == "view":
            return """
DJANGO CODE:
```python
from rest_framework.views import APIView
from rest_framework.response import Response

class ItemView(APIView):
    def get(self, request):
        items = Item.objects.all()
        return Response({'items': items})
```

FASTAPI CODE:
```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/items")
async def get_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return {"items": items}
```
"""
        elif category == "model":
            return """
DJANGO CODE:
```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
```

FASTAPI CODE:
```python
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    price: float

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int
    
    class Config:
        from_attributes = True
```
"""
        else:
            return "Convert Django code to FastAPI equivalents."
    
    def _cleanup_code(self, code: str) -> str:
        """Clean up converted code"""
        # Remove markdown code blocks
        if "```" in code:
            lines = code.split("\n")
            code_lines = []
            in_code_block = False
            
            for line in lines:
                if line.strip().startswith("```"):
                    in_code_block = not in_code_block
                    continue
                if in_code_block or not line.strip().startswith("```"):
                    code_lines.append(line)
            
            code = "\n".join(code_lines)
        
        # Remove leading/trailing whitespace
        code = code.strip()
        
        # Remove any explanatory text before imports
        lines = code.split('\n')
        first_import_idx = -1
        for i, line in enumerate(lines):
            if line.startswith('from ') or line.startswith('import '):
                first_import_idx = i
                break
        
        if first_import_idx > 0:
            # Remove lines before first import if they're comments
            if all(l.startswith('#') or not l.strip() for l in lines[:first_import_idx]):
                code = '\n'.join(lines[first_import_idx:])
        
        return code
    
    
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
