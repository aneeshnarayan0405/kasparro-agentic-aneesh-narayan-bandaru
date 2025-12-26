from typing import Dict, Any
from src.core.models import Product

def generate_benefits_block(product: Product) -> Dict[str, Any]:
    """
    Generate structured benefits information from product data
    
    Args:
        product: Product object containing benefits data
        
    Returns:
        Dict containing formatted benefits information
    """
    
    # Enhanced benefits description
    benefits_list = product.benefits
    
    # Create detailed descriptions for each benefit
    detailed_benefits = []
    benefit_descriptions = {
        "Brightening": "Reduces dullness and evens out skin tone for a radiant glow",
        "Fades dark spots": "Targets hyperpigmentation and sun spots over time",
        "Hydration": "Locks in moisture for plump, supple skin",
        "Anti-aging": "Reduces appearance of fine lines and wrinkles",
        "Protection": "Provides antioxidant protection against environmental damage"
    }
    
    for benefit in benefits_list:
        detailed = benefit_descriptions.get(
            benefit,
            f"Provides {benefit.lower()} benefits for improved skin health"
        )
        detailed_benefits.append({
            "benefit": benefit,
            "description": detailed,
            "timeframe": "Visible results in 4-8 weeks with regular use"
        })
    
    # Create overall benefits summary
    benefits_summary = f"{product.name} offers comprehensive skincare benefits including "
    if len(benefits_list) > 1:
        benefits_summary += f"{', '.join(benefits_list[:-1])}, and {benefits_list[-1].lower()}"
    else:
        benefits_summary += benefits_list[0].lower()
    benefits_summary += " through its advanced formulation."
    
    return {
        "benefits_list": benefits_list,
        "detailed_benefits": detailed_benefits,
        "benefits_summary": benefits_summary,
        "key_advantage": f"Combines {len(product.ingredients)} active ingredients for multiple benefits",
        "usage_tip": "For best results, use consistently as part of your daily skincare routine"
    }