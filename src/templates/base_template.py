"""
Base template class with validation and rendering capabilities
"""
from abc import ABC, abstractmethod
from typing import Dict, Any
from datetime import datetime
import json

class BaseTemplate(ABC):
    def __init__(self, template_name: str):
        self.template_name = template_name
        self.created_at = datetime.utcnow().isoformat()
        
    @abstractmethod
    def render(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Render template with provided data"""
        pass
    
    def validate_data(self, data: Dict[str, Any], required_fields: list) -> bool:
        """Validate that required fields are present"""
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        return True
    
    def add_metadata(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """Add system metadata to output"""
        return {
            "metadata": {
                "template": self.template_name,
                "generated_at": self.created_at,
                "version": "1.0.0",
                "system": "Multi-Agent Content Generation System"
            },
            "content": content
        }
    
    def to_json(self, data: Dict[str, Any], indent: int = 2) -> str:
        """Convert rendered template to JSON string"""
        rendered = self.render(data)
        return json.dumps(rendered, indent=indent, ensure_ascii=False)