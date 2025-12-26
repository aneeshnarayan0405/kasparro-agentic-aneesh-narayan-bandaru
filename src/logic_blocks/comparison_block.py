from typing import Dict, Any, List
from src.core.models import Product

def generate_comparison_block(product_a: Product, product_b: Product) -> Dict[str, Any]:
    """
    Generate detailed comparison between two products
    
    Args:
        product_a: First product (main product)
        product_b: Second product (comparison product)
        
    Returns:
        Dict containing comprehensive comparison data
    """
    
    # Ingredients comparison
    ingredients_a = set(ing.lower() for ing in product_a.ingredients)
    ingredients_b = set(ing.lower() for ing in product_b.ingredients)
    
    common_ingredients = ingredients_a.intersection(ingredients_b)
    unique_to_a = ingredients_a - ingredients_b
    unique_to_b = ingredients_b - ingredients_a
    
    # Benefits comparison
    benefits_a = set(ben.lower() for ben in product_a.benefits)
    benefits_b = set(ben.lower() for ben in product_b.benefits)
    
    common_benefits = benefits_a.intersection(benefits_b)
    unique_benefits_a = benefits_a - benefits_b
    unique_benefits_b = benefits_b - benefits_a
    
    # Price comparison
    price_difference = product_b.price - product_a.price
    price_ratio = product_a.price / product_b.price if product_b.price > 0 else float('inf')
    
    # Value comparison
    ingredients_per_rupee_a = len(product_a.ingredients) / product_a.price if product_a.price > 0 else 0
    ingredients_per_rupee_b = len(product_b.ingredients) / product_b.price if product_b.price > 0 else 0
    
    benefits_per_rupee_a = len(product_a.benefits) / product_a.price if product_a.price > 0 else 0
    benefits_per_rupee_b = len(product_b.benefits) / product_b.price if product_b.price > 0 else 0
    
    # Determine winner in each category
    winners = {
        "ingredients_count": "A" if len(product_a.ingredients) > len(product_b.ingredients) else "B",
        "benefits_count": "A" if len(product_a.benefits) > len(product_b.benefits) else "B",
        "price": "A" if product_a.price < product_b.price else "B",
        "value_score": "A" if (ingredients_per_rupee_a + benefits_per_rupee_a) > (ingredients_per_rupee_b + benefits_per_rupee_b) else "B"
    }
    
    # Overall recommendation
    total_score_a = sum([1 for winner in winners.values() if winner == "A"])
    total_score_b = sum([1 for winner in winners.values() if winner == "B"])
    
    if total_score_a > total_score_b:
        overall_recommendation = f"{product_a.name} is recommended for better overall value"
        winner = "A"
    elif total_score_b > total_score_a:
        overall_recommendation = f"{product_b.name} is recommended for better overall value"
        winner = "B"
    else:
        overall_recommendation = "Both products are comparable; choose based on specific needs"
        winner = "Tie"
    
    # Detailed category analysis
    category_analysis = {
        "for_budget_shoppers": f"{product_a.name if product_a.price < product_b.price else product_b.name} (lower price)",
        "for_ingredient_conscious": f"{product_a.name if len(unique_to_a) > len(unique_to_b) else product_b.name} (more unique ingredients)",
        "for_sensitive_skin": "Consult ingredient list for potential irritants",
        "for_quick_results": f"{product_a.name if 'Brightening' in product_a.benefits else product_b.name} (specific targeting)"
    }
    
    # Pros and Cons
    pros_cons = {
        product_a.name: {
            "pros": [
                f"₹{product_a.price} - more affordable" if product_a.price < product_b.price else f"₹{product_a.price} - premium formulation",
                f"{len(product_a.ingredients)} key ingredients",
                f"Specifically for {', '.join(product_a.skin_type)} skin",
                f"Benefits: {', '.join(product_a.benefits[:2])}"
            ],
            "cons": [
                f"{product_a.side_effects}",
                f"Limited to {', '.join(product_a.skin_type)} skin types" if len(product_a.skin_type) < 3 else None
            ]
        },
        product_b.name: {
            "pros": [
                f"₹{product_b.price} - competitive pricing",
                f"Suitable for {', '.join(product_b.skin_type)}",
                f"Benefits: {', '.join(product_b.benefits[:2])}",
                f"{product_b.concentration} concentration"
            ],
            "cons": [
                f"{len(product_b.ingredients)} ingredients (fewer than {product_a.name})" if len(product_b.ingredients) < len(product_a.ingredients) else None,
                "Fictional product for comparison purposes"
            ]
        }
    }
    
    # Clean up None values
    for product in [product_a.name, product_b.name]:
        pros_cons[product]["pros"] = [p for p in pros_cons[product]["pros"] if p]
        pros_cons[product]["cons"] = [c for c in pros_cons[product]["cons"] if c]
    
    return {
        "summary": {
            "total_score_a": total_score_a,
            "total_score_b": total_score_b,
            "overall_winner": winner,
            "recommendation": overall_recommendation
        },
        "ingredients_analysis": {
            "common_ingredients": list(common_ingredients),
            "unique_to_a": list(unique_to_a),
            "unique_to_b": list(unique_to_b),
            "total_a": len(product_a.ingredients),
            "total_b": len(product_b.ingredients),
            "winner": winners["ingredients_count"]
        },
        "benefits_analysis": {
            "common_benefits": list(common_benefits),
            "unique_to_a": list(unique_benefits_a),
            "unique_to_b": list(unique_benefits_b),
            "total_a": len(product_a.benefits),
            "total_b": len(product_b.benefits),
            "winner": winners["benefits_count"]
        },
        "price_analysis": {
            "price_a": product_a.price,
            "price_b": product_b.price,
            "difference": abs(price_difference),
            "percentage_difference": round(abs(price_ratio - 1) * 100, 1) if price_ratio != float('inf') else 0,
            "value_score_a": round(ingredients_per_rupee_a + benefits_per_rupee_a, 3),
            "value_score_b": round(ingredients_per_rupee_b + benefits_per_rupee_b, 3),
            "winner": winners["price"]
        },
        "category_recommendations": category_analysis,
        "pros_and_cons": pros_cons,
        "final_verdict": {
            "best_for_budget": product_a.name if product_a.price < product_b.price else product_b.name,
            "best_for_ingredients": product_a.name if len(product_a.ingredients) > len(product_b.ingredients) else product_b.name,
            "best_for_skin_type": product_a.name if "Combination" in product_a.skin_type else product_b.name,
            "overall_value": product_a.name if winner == "A" else product_b.name
        }
    }