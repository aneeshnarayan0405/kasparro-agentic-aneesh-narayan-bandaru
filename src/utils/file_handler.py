"""
File handling utilities for reading and writing data
"""
import json
from pathlib import Path
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

def ensure_directory(directory_path: str) -> bool:
    """Ensure a directory exists, create if it doesn't"""
    try:
        Path(directory_path).mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        logger.error(f"Failed to create directory {directory_path}: {e}")
        return False

def save_output(filename: str, data: Dict[str, Any], indent: int = 2) -> bool:
    """
    Save data to JSON file with proper error handling
    """
    try:
        # Ensure directory exists
        filepath = Path(filename)
        ensure_directory(str(filepath.parent))
        
        # Save to file
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        
        logger.info(f"Successfully saved output to {filename}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to save {filename}: {e}")
        return False

def load_json(filename: str) -> Dict[str, Any]:
    """
    Load JSON file with error handling
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"File not found: {filename}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in {filename}: {e}")
        raise

def backup_file(filename: str, backup_suffix: str = ".bak") -> bool:
    """
    Create a backup of a file
    """
    try:
        path = Path(filename)
        if path.exists():
            backup_path = path.with_suffix(path.suffix + backup_suffix)
            path.rename(backup_path)
            logger.info(f"Created backup: {backup_path}")
            return True
    except Exception as e:
        logger.error(f"Failed to backup {filename}: {e}")
    
    return False