from typing import List, Tuple, Dict, Any
from datetime import datetime

def faq_template(qa_pairs: List[Tuple[str, str]]) -> Dict[str, Any]:
    """
    Template for FAQ page generation
    
    Args:
        qa_pairs: List of (question, answer) tuples
        
    Returns:
        Dict with structured FAQ content
    """
    
    # Create FAQ items
    faq_items = []
    for idx, (question, answer) in enumerate(qa_pairs, 1):
        faq_items.append({
            "id": f"faq_{idx:03d}",
            "question": question,
            "answer": answer,
            "category": _categorize_question(question),
            "importance": "high" if idx <= 3 else "medium",
            "last_updated": datetime.utcnow().isoformat()
        })
    
    # Create FAQ categories
    categories = {}
    for item in faq_items:
        category = item["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(item["id"])
    
    # Generate FAQ summary
    summary = {
        "total_questions": len(faq_items),
        "categories_count": len(categories),
        "most_common_category": max(categories, key=lambda k: len(categories[k])) if categories else "general",
        "coverage_score": min(100, len(faq_items) * 10)  # Simple coverage metric
    }
    
    # Generate structured response
    return {
        "metadata": {
            "template_version": "1.0.0",
            "generated_at": datetime.utcnow().isoformat(),
            "content_type": "faq"
        },
        "summary": summary,
        "categories": [
            {
                "name": category,
                "question_count": len(questions),
                "question_ids": questions
            }
            for category, questions in categories.items()
        ],
        "questions": faq_items,
        "navigation": {
            "by_category": {cat: [q["id"] for q in faq_items if q["category"] == cat] for cat in categories},
            "by_importance": {
                "high": [q["id"] for q in faq_items if q["importance"] == "high"],
                "medium": [q["id"] for q in faq_items if q["importance"] == "medium"],
                "low": [q["id"] for q in faq_items if q["importance"] == "low"]
            }
        }
    }

def _categorize_question(question: str) -> str:
    """Categorize question based on keywords"""
    question_lower = question.lower()
    
    if any(word in question_lower for word in ["what is", "what does", "explain", "describe"]):
        return "informational"
    elif any(word in question_lower for word in ["how to", "how do i", "instructions", "apply"]):
        return "usage"
    elif any(word in question_lower for word in ["safe", "side effect", "risk", "pregnant"]):
        return "safety"
    elif any(word in question_lower for word in ["price", "buy", "purchase", "cost", "worth"]):
        return "purchase"
    elif any(word in question_lower for word in ["compare", "vs", "difference", "alternative"]):
        return "comparison"
    elif any(word in question_lower for word in ["ingredient", "formula", "composition"]):
        return "ingredients"
    else:
        return "general"