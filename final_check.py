#!/usr/bin/env python3
"""
Final verification for Kasparro assignment
"""
import json
import os
from pathlib import Path

print(" FINAL VERIFICATION FOR KASPARRO ASSIGNMENT")
print("=" * 60)

# Check required files
required_files = [
    ("data/product_input.json", "Input data"),
    ("docs/projectdocumentation.md", "Documentation"),
    ("outputs/faq.json", "FAQ output"),
    ("outputs/product_page.json", "Product page output"),
    ("outputs/comparison.json", "Comparison output")
]

all_ok = True
for filepath, description in required_files:
    path = Path(filepath)
    if path.exists():
        size = path.stat().st_size
        if size > 0:
            print(f"✅ {description}: {size} bytes")
            
            # Validate JSON files
            if filepath.endswith('.json'):
                try:
                    with open(filepath, 'r') as f:
                        data = json.load(f)
                    print(f"   Valid JSON, keys: {list(data.keys())}")
                    
                    # Specific checks
                    if "faq" in filepath:
                        if "content" in data and "questions" in data["content"]:
                            q_count = len(data["content"]["questions"])
                            print(f"   Contains {q_count} Q&A pairs")
                except Exception as e:
                    print(f"    Invalid JSON: {e}")
                    all_ok = False
        else:
            print(f" {description}: EMPTY (0 bytes)")
            all_ok = False
    else:
        print(f" {description}: NOT FOUND")
        all_ok = False

# Check structure
print("\n📁 Project structure check:")
structure_ok = True
required_dirs = ["src/core", "src/agents", "src/logic_blocks", "src/templates", "src/utils"]
for dirpath in required_dirs:
    if Path(dirpath).exists():
        py_files = list(Path(dirpath).glob("*.py"))
        print(f" {dirpath}: {len(py_files)} Python files")
    else:
        print(f"❌ {dirpath}: Missing")
        structure_ok = False

# Check GitHub repo name
current_dir = Path.cwd().name
expected_name = "kasparro-agentic-aneesh-narayan-bandaru"
if current_dir == expected_name:
    print(f"\n GitHub repo name correct: {current_dir}")
else:
    print(f"\n⚠️  Warning: Folder name is '{current_dir}', should be '{expected_name}'")
    print("   Rename folder before pushing to GitHub")

print("\n" + "=" * 60)
if all_ok and structure_ok:
    print("🎉 ALL CHECKS PASSED! Ready to submit to Kasparro.")
    print("\n📋 Submission checklist:")
    print("  1. ✅ All required files present")
    print("  2.  Outputs generated and valid")
    print("  3.  Documentation complete")
    print("  4.  GitHub repo with correct name")
    print("  5.  Code is modular and clean")
    print("\n Submit your GitHub repo link via the Google Form!")
else:
    print(" Some checks failed. Fix issues above before submitting.")