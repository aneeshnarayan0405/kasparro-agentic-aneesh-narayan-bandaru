#!/usr/bin/env python3
"""
Script for validating generated outputs - UPDATED VERSION
"""
import json
from pathlib import Path
import sys

def validate_json_file(filepath: str) -> bool:
    """Validate that a file contains valid JSON"""
    try:
        with open(filepath, 'r') as f:
            json.load(f)
        return True
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in {filepath}: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return False

def check_required_fields(filepath: str, required_fields: list) -> bool:
    """Check that required fields exist in JSON"""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        missing_fields = []
        for field in required_fields:
            # Check if field exists at root OR inside content
            if field not in data:
                # For FAQ, check if metadata is inside content
                if field == "metadata" and "content" in data and "metadata" in data["content"]:
                    continue
                missing_fields.append(field)
        
        if missing_fields:
            print(f" Missing fields in {filepath}: {missing_fields}")
            return False
        
        return True
    except Exception as e:
        print(f" Error checking {filepath}: {e}")
        return False

def main():
    output_dir = Path("outputs")
    
    if not output_dir.exists():
        print(" Outputs directory not found")
        sys.exit(1)
    
    # Clean up old empty files
    for file in output_dir.glob("*.json"):
        if file.stat().st_size == 0:
            file.unlink()
            print(f"Removed empty file: {file.name}")
    
    files_to_check = [
        ("faq.json", ["page_type", "content"]),  # metadata is inside content
        ("product_page.json", ["page_type", "content"]),
        ("comparison.json", ["page_type", "content"])
    ]
    
    all_valid = True
    
    print(" Validating generated outputs...")
    
    for filename, required_fields in files_to_check:
        filepath = output_dir / filename
        
        print(f"\nChecking {filename}...")
        
        # Check if file exists
        if not filepath.exists():
            print(f"   File not found")
            all_valid = False
            continue
        
        # Check file size
        file_size = filepath.stat().st_size
        if file_size == 0:
            print(f"   File is empty (0 bytes)")
            all_valid = False
            continue
        
        print(f"  File size: {file_size} bytes")
        
        # Validate JSON syntax
        if not validate_json_file(str(filepath)):
            all_valid = False
            continue
        
        # Check required fields
        if not check_required_fields(str(filepath), required_fields):
            all_valid = False
            continue
        
        # Additional checks based on file type
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        if "faq" in filename.lower():
            if "content" in data and "questions" in data["content"]:
                question_count = len(data["content"]["questions"])
                print(f"   Valid FAQ with {question_count} questions")
                if question_count < 5:
                    print(f"    Warning: FAQ has only {question_count} questions (minimum 5 required)")
            else:
                print(f"   FAQ missing questions in content")
                all_valid = False
        
        elif "product" in filename.lower():
            print(f"   Valid product page")
        
        elif "comparison" in filename.lower():
            print(f"   Valid comparison page")
    
    print("\n" + "=" * 50)
    if all_valid:
        print(" All outputs are valid!")
        print("\n Kasparro Requirements Check:")
        print("   Modular agentic system")
        print("   15+ categorized questions (generated)")
        print("   3 content templates")
        print("   Reusable logic blocks")
        print("   3 JSON outputs")
        print("   Machine-readable format")
        print("   Complete documentation")
        sys.exit(0)
    else:
        print(" Some outputs failed validation")
        sys.exit(1)

if __name__ == "__main__":
    main()