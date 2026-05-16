"""
Flowchart generation using Mermaid.js
"""
from typing import List, Dict, Any


class FlowchartGenerator:
    """Generate Mermaid.js flowcharts"""
    
    @staticmethod
    def generate_migration_flowchart(steps: List[str]) -> str:
        """
        Generate flowchart from migration steps
        """
        if not steps:
            return FlowchartGenerator.get_default_flowchart()
        
        # Build flowchart
        lines = ["graph TD"]
        
        # Start node
        lines.append("    A[Start Migration] --> B[Scan Repository]")
        
        # Add steps
        prev_node = "B"
        for i, step in enumerate(steps[:8], start=3):  # Limit to 8 steps for clarity
            node_id = chr(65 + i)  # C, D, E, etc.
            step_text = step.replace('"', "'").strip()
            if step_text.startswith(f"{i-2}."):
                step_text = step_text.split(".", 1)[1].strip()
            
            lines.append(f"    {prev_node} --> {node_id}[{step_text[:40]}]")
            prev_node = node_id
        
        # Add decision and end
        final_node = chr(65 + len(steps[:8]) + 2)
        lines.append(f"    {prev_node} --> {final_node}{{Tests Pass?}}")
        lines.append(f"    {final_node} -->|Yes| Z[Migration Complete]")
        lines.append(f"    {final_node} -->|No| R[Rollback]")
        lines.append(f"    R --> B")
        
        return "\n".join(lines)
    
    @staticmethod
    def get_default_flowchart() -> str:
        """
        Get default migration flowchart
        """
        return """graph TD
    A[Start Migration] --> B[Upload/Clone Repository]
    B --> C[Scan & Detect Framework]
    C --> D[Generate Migration Plan]
    D --> E[Create Snapshot]
    E --> F[Convert Models/Entities]
    F --> G[Migrate Controllers/Views]
    G --> H[Update Routes/URLs]
    H --> I[Generate Config Files]
    I --> J[Run Tests]
    J --> K{Tests Pass?}
    K -->|Yes| L[Migration Complete]
    K -->|No| M[Rollback to Snapshot]
    M --> D"""
    
    @staticmethod
    def generate_architecture_diagram(framework_info: Dict[str, Any]) -> str:
        """
        Generate architecture diagram
        """
        framework = framework_info.get("framework", "unknown")
        
        if framework.lower() == "django":
            return """graph LR
    A[Client] --> B[URLs]
    B --> C[Views]
    C --> D[Models]
    D --> E[Database]
    C --> F[Templates]
    F --> A"""
        
        elif framework.lower() == "spring":
            return """graph LR
    A[Client] --> B[Controller]
    B --> C[Service]
    C --> D[Repository]
    D --> E[Database]
    B --> F[View]
    F --> A"""
        
        else:
            return """graph LR
    A[Client] --> B[API Layer]
    B --> C[Business Logic]
    C --> D[Data Layer]
    D --> E[Database]"""
    
    @staticmethod
    def generate_comparison_chart(
        source_framework: str,
        target_framework: str
    ) -> str:
        """
        Generate comparison flowchart
        """
        return f"""graph LR
    subgraph Source["{source_framework.upper()}"]
        A1[Legacy Patterns]
        A2[Monolithic]
        A3[Synchronous]
    end
    
    subgraph Target["{target_framework.upper()}"]
        B1[Modern Patterns]
        B2[Modular]
        B3[Async/Await]
    end
    
    A1 -.Migration.-> B1
    A2 -.Migration.-> B2
    A3 -.Migration.-> B3"""

# Made with Bob
