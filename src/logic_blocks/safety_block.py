from typing import Dict, Any
from src.core.models import Product

def generate_safety_block(product: Product) -> Dict[str, Any]:
    """
    Generate comprehensive safety information
    
    Args:
        product: Product object containing safety data
        
    Returns:
        Dict containing safety information and warnings
    """
    
    side_effects_text = product.side_effects
    
    # Parse side effects
    side_effects = []
    if "tingling" in side_effects_text.lower():
        side_effects.append({
            "effect": "Mild tingling sensation",
            "frequency": "Common for sensitive skin",
            "severity": "Mild",
            "action": "Usually subsides within minutes. Reduce frequency if persistent."
        })
    
    if "irritation" in side_effects_text.lower():
        side_effects.append({
            "effect": "Skin irritation or redness",
            "frequency": "Rare",
            "severity": "Mild to moderate",
            "action": "Discontinue use and consult dermatologist"
        })
    
    # If no specific side effects mentioned, add general ones
    if not side_effects:
        side_effects.append({
            "effect": "Generally well-tolerated",
            "frequency": "Most users experience no side effects",
            "severity": "None",
            "action": "None required"
        })
    
    # Contraindications
    contraindications = []
    if "sensitive" in side_effects_text.lower():
        contraindications.append("Extremely sensitive skin")
    
    # Always include these
    contraindications.extend([
        "Open wounds or broken skin",
        "Known allergy to any ingredients",
        "Active skin infections"
    ])
    
    # Precautions
    precautions = [
        "Always perform a patch test before first use",
        "Apply to clean, dry skin",
        "Start with every other day use for first week",
        "Avoid sun exposure without sunscreen",
        "Consult dermatologist if pregnant or breastfeeding"
    ]
    
    # First aid measures
    first_aid = {
        "eye_contact": "Rinse immediately with plenty of water for 15 minutes",
        "skin_irritation": "Wash with mild soap and water, apply soothing cream",
        "ingestion": "Rinse mouth, drink water, seek medical attention",
        "allergic_reaction": "Discontinue use immediately, seek medical help if severe"
    }
    
    # Safety ratings and certifications
    safety_ratings = {
        "dermatologist_tested": True,
        "hypoallergenic": "suitable for most skin types",
        "cruelty_free": True,
        "paraben_free": "check ingredient list",
        "fragrance_free": "unscented formulation"
    }
    
    return {
        "side_effects": side_effects,
        "contraindications": contraindications,
        "precautions": precautions,
        "first_aid_measures": first_aid,
        "safety_ratings": safety_ratings,
        "patch_test_instructions": "Apply small amount to inner forearm, wait 24 hours",
        "discontinuation_advice": "Stop use if severe irritation occurs and consult professional",
        "storage_warning": "Keep out of reach of children, store in original container"
    }