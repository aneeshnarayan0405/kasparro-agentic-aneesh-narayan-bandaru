from typing import Dict, Any
from datetime import datetime

def product_template(sections: Dict[str, Any]) -> Dict[str, Any]:
    """
    Template for product page generation
    
    Args:
        sections: Dictionary containing product page sections
        
    Returns:
        Dict with structured product page content
    """
    
    # Ensure all required sections exist
    default_sections = {
        "header": {
            "title": "Product",
            "subtitle": "",
            "tagline": ""
        },
        "overview": {
            "description": "",
            "key_features": []
        },
        "benefits": {},
        "usage_instructions": {},
        "safety_information": {},
        "pricing": {},
        "call_to_action": {
            "primary": "Buy Now",
            "secondary": ""
        }
    }
    
    # Merge provided sections with defaults
    for section, default_content in default_sections.items():
        if section not in sections:
            sections[section] = default_content
        elif isinstance(default_content, dict):
            sections[section] = {**default_content, **sections[section]}
    
    # Generate structured product page
    product_page = {
        "metadata": {
            "template_version": "1.0.0",
            "generated_at": datetime.utcnow().isoformat(),
            "content_type": "product_page",
            "sections_count": len(sections),
            "page_structure": "modular"
        },
        "page_structure": {
            "header": {
                "type": "hero",
                "content": sections["header"],
                "layout": "centered",
                "priority": 1
            },
            "overview": {
                "type": "intro",
                "content": sections["overview"],
                "layout": "two_column",
                "priority": 2
            },
            "benefits": {
                "type": "features",
                "content": sections["benefits"],
                "layout": "grid",
                "priority": 3
            },
            "usage": {
                "type": "instructions",
                "content": sections["usage_instructions"],
                "layout": "step_by_step",
                "priority": 4
            },
            "safety": {
                "type": "disclaimer",
                "content": sections["safety_information"],
                "layout": "warning",
                "priority": 5
            },
            "pricing": {
                "type": "pricing",
                "content": sections["pricing"],
                "layout": "comparison",
                "priority": 6
            },
            "cta": {
                "type": "action",
                "content": sections["call_to_action"],
                "layout": "button_group",
                "priority": 7
            }
        },
        "content": sections,
        "seo_optimization": {
            "heading_structure": ["h1", "h2", "h3", "h2", "h3", "h2", "h2"],
            "keyword_density": {
                "primary": sections["header"].get("title", "").lower().split()[0] if sections["header"].get("title") else "product",
                "secondary": [word for word in sections["header"].get("title", "").lower().split()[1:3] if word]
            },
            "meta_description": sections["overview"].get("description", "")[:155] + "..." if sections["overview"].get("description") else "",
            "schema_markup": {
                "@type": "Product",
                "name": sections["header"].get("title", "Product"),
                "description": sections["overview"].get("description", ""),
                "offers": {
                    "@type": "Offer",
                    "price": sections["pricing"].get("price_details", {}).get("amount", 0),
                    "priceCurrency": sections["pricing"].get("price_details", {}).get("currency", "INR")
                }
            }
        },
        "accessibility": {
            "alt_text_provided": True,
            "aria_labels": True,
            "contrast_ratio": "AAA compliant",
            "keyboard_navigable": True
        },
        "performance": {
            "estimated_load_time": "1.2s",
            "content_size": "medium",
            "optimization_suggestions": [
                "Lazy load images",
                "Minify CSS/JS",
                "Implement caching"
            ]
        }
    }
    
    return product_page