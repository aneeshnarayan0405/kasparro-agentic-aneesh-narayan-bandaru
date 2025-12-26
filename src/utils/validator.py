"""
Validation utilities for data and schemas
"""
import json
from typing import Dict, Any
from pathlib import Path

def validate_json_schema(data: Dict[str, Any], schema: Dict[str, Any]) -> bool:
    """
    Validate data against JSON schema
    Simplified version - in production use jsonschema library
    """
    # Check required fields
    if 'required' in schema:
        for field in schema['required']:
            if field not in data:
                return False
    
    # Check types
    if 'properties' in schema:
        for field, prop_schema in schema['properties'].items():
            if field in data:
                expected_type = prop_schema.get('type')
                if expected_type:
                    if expected_type == 'array' and not isinstance(data[field], list):
                        return False
                    elif expected_type == 'string' and not isinstance(data[field], str):
                        return False
                    elif expected_type == 'integer' and not isinstance(data[field], int):
                        return False
                    elif expected_type == 'object' and not isinstance(data[field], dict):
                        return False
    
    return True

def validate_product_data(data: Dict[str, Any]) -> tuple[bool, str]:
    """Validate product-specific business rules"""
    errors = []
    
    # Price validation
    if 'price' in data and data['price'] <= 0:
        errors.append("Price must be positive")
    
    # Ingredients validation
    if 'key_ingredients' in data and len(data['key_ingredients']) == 0:
        errors.append("Product must have at least one ingredient")
    
    # Benefits validation
    if 'benefits' in data and len(data['benefits']) == 0:
        errors.append("Product must have at least one benefit")
    
    return len(errors) == 0, "; ".join(errors) if errors else "Valid"

def load_and_validate_schema(schema_path: str) -> Dict[str, Any]:
    """Load JSON schema from file"""
    path = Path(schema_path)
    if not path.exists():
        raise FileNotFoundError(f"Schema file not found: {schema_path}")
    
    with open(path, 'r') as f:
        return json.load(f)