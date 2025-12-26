from typing import Dict, Any
from src.core.models import Product

def generate_usage_block(product: Product) -> Dict[str, Any]:
    """
    Generate detailed usage instructions
    
    Args:
        product: Product object containing usage data
        
    Returns:
        Dict containing comprehensive usage information
    """
    
    # Parse the usage instruction
    usage_text = product.usage
    
    # Enhanced usage breakdown
    steps = []
    if "drops" in usage_text.lower():
        steps.append("Cleanse your face thoroughly and pat dry")
        steps.append("Dispense 2-3 drops onto your fingertips")
        steps.append("Gently pat and press onto face and neck")
        steps.append("Allow to absorb for 1-2 minutes")
        steps.append("Follow with moisturizer and sunscreen")
    else:
        steps = ["Apply as directed by the instructions"]
    
    # Determine frequency
    frequency = "Daily"
    if "morning" in usage_text.lower() and "night" not in usage_text.lower():
        frequency = "Once daily (morning)"
    elif "night" in usage_text.lower() and "morning" not in usage_text.lower():
        frequency = "Once daily (night)"
    elif "morning" in usage_text.lower() and "night" in usage_text.lower():
        frequency = "Twice daily (morning and night)"
    
    # Best time for application
    best_time = "Morning" if "morning" in usage_text.lower() else "Evening"
    
    # Precautions and tips
    precautions = [
        "Perform a patch test before first use",
        "Avoid contact with eyes",
        "Store in a cool, dry place away from direct sunlight",
        "Use within 6 months of opening"
    ]
    
    # Compatibility with other products
    compatible_with = ["Moisturizers", "Sunscreens", "Most serums"]
    incompatible_with = ["Strong acids (AHA/BHA) in same routine", "Retinol (unless specified)"]
    
    # Expected results timeline
    results_timeline = {
        "immediate": "Instant hydration and glow",
        "1_week": "Improved skin texture",
        "4_weeks": "Visible brightening and even tone",
        "8_weeks": "Reduced dark spots and full benefits"
    }
    
    return {
        "basic_instruction": usage_text,
        "detailed_steps": steps,
        "frequency": frequency,
        "best_time": best_time,
        "precautions": precautions,
        "product_compatibility": {
            "compatible_with": compatible_with,
            "incompatible_with": incompatible_with,
            "recommended_order": "After cleansing, before moisturizing"
        },
        "results_timeline": results_timeline,
        "storage_instructions": "Keep lid tightly closed, store below 25°C",
        "shelf_life": "24 months unopened, 6 months after opening"
    }