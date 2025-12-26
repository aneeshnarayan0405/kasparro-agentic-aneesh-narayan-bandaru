"""
SEO metadata generation logic block
"""
from typing import Dict, Any

def generate_seo_metadata(product_data: Dict[str, Any]) -> Dict[str, Any]:
    """Generate SEO metadata for content pages"""
    
    title = f"{product_data.get('name', 'Product')} - Benefits, Usage & Review"
    
    description_parts = []
    if 'benefits' in product_data:
        benefits = product_data['benefits']
        if isinstance(benefits, list):
            description_parts.append(f"Benefits include {', '.join(benefits[:2])}")
    
    if 'ingredients' in product_data:
        ingredients = product_data['ingredients']
        if isinstance(ingredients, list):
            description_parts.append(f"Key ingredients: {', '.join(ingredients)}")
    
    description = ". ".join(description_parts) + f". Price: ₹{product_data.get('price', 'N/A')}"
    
    # Generate keywords
    keywords = set()
    if product_data.get('name'):
        keywords.update(product_data['name'].lower().split())
    if product_data.get('ingredients'):
        keywords.update([ing.lower() for ing in product_data['ingredients']])
    if product_data.get('benefits'):
        keywords.update([benefit.lower() for benefit in product_data['benefits']])
    
    return {
        "title": title,
        "meta_description": description[:160],  # Truncate for SEO
        "keywords": list(keywords)[:10],  # Top 10 keywords
        "og_tags": {
            "og:title": title,
            "og:description": description[:300],
            "og:type": "product"
        }
    }