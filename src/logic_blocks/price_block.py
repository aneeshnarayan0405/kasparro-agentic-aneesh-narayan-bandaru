from typing import Dict, Any
from src.core.models import Product

def generate_price_block(product: Product) -> Dict[str, Any]:
    """
    Generate comprehensive price analysis and value proposition
    
    Args:
        product: Product object containing price data
        
    Returns:
        Dict containing price analysis and value information
    """
    
    price = product.price
    
    # Determine price category
    if price < 500:
        price_category = "Budget"
        category_description = "Affordable skincare option"
    elif price < 1000:
        price_category = "Mid-range"
        category_description = "Good value for quality ingredients"
    elif price < 2000:
        price_category = "Premium"
        category_description = "High-end formulation with advanced ingredients"
    else:
        price_category = "Luxury"
        category_description = "Premium skincare with exceptional quality"
    
    # Calculate value metrics
    ingredients_count = len(product.ingredients)
    benefits_count = len(product.benefits)
    
    # Simple value score calculation
    value_score = min(100, (ingredients_count * 10 + benefits_count * 15) - (price / 20))
    
    # Value assessment
    if value_score >= 80:
        value_assessment = "Excellent value"
        recommendation = "Highly recommended for the price"
    elif value_score >= 60:
        value_assessment = "Good value"
        recommendation = "Worth considering"
    elif value_score >= 40:
        value_assessment = "Fair value"
        recommendation = "Consider alternatives in same range"
    else:
        value_assessment = "Poor value"
        recommendation = "Explore other options"
    
    # Price comparison with market average
    # Assuming average Vitamin C serum price in India is around ₹800-1200
    market_average = 1000
    price_difference = price - market_average
    price_position = "below" if price_difference < 0 else "above"
    
    # Cost per use calculation (assuming 30ml bottle, 2-3 drops per use)
    estimated_uses = 150  # Typical for 30ml serum
    cost_per_use = round(price / estimated_uses, 2)
    
    # Return on investment (ROI) factors
    roi_factors = {
        "ingredient_quality": "High" if "Hyaluronic Acid" in product.ingredients else "Medium",
        "concentration": "Optimal" if "10%" in product.concentration else "Standard",
        "brand_reputation": "Established" if len(product.name.split()) > 1 else "Emerging",
        "clinical_backing": "Dermatologist recommended" if price > 700 else "User recommended"
    }
    
    # Purchase recommendations
    purchase_timing = {
        "best_time": "During festive sales or brand promotions",
        "discount_frequency": "Quarterly sales common",
        "bundle_offers": "Often available with moisturizer combos"
    }
    
    return {
        "price_details": {
            "amount": price,
            "currency": "INR",
            "formatted": f"₹{price}",
            "category": price_category,
            "category_description": category_description
        },
        "value_analysis": {
            "value_score": round(value_score),
            "value_assessment": value_assessment,
            "recommendation": recommendation,
            "ingredients_per_rupee": round(ingredients_count / (price / 100), 2),
            "benefits_per_rupee": round(benefits_count / (price / 100), 2)
        },
        "market_position": {
            "market_average": market_average,
            "price_difference": abs(price_difference),
            "position": f"{price_position} market average",
            "competitiveness": "Competitive" if abs(price_difference) < 200 else "Premium priced"
        },
        "cost_analysis": {
            "estimated_uses": estimated_uses,
            "cost_per_use": cost_per_use,
            "daily_cost": round(cost_per_use * (2 if "morning" in product.usage.lower() and "night" in product.usage.lower() else 1), 2),
            "monthly_cost": round(cost_per_use * 30, 2)
        },
        "roi_factors": roi_factors,
        "purchase_advice": purchase_timing,
        "payment_options": ["Credit/Debit Card", "UPI", "EMI available above ₹2000", "Cash on Delivery"]
    }