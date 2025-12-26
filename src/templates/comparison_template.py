from typing import Dict, Any
from datetime import datetime
from src.core.models import Product

def comparison_template(product_a: Product, product_b: Product, comparison_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Template for comparison page generation
    
    Args:
        product_a: First product
        product_b: Second product
        comparison_data: Pre-computed comparison analysis
        
    Returns:
        Dict with structured comparison page content
    """
    
    # Create comparison table
    comparison_table = {
        "headers": ["Feature", product_a.name, product_b.name, "Winner"],
        "rows": [
            {
                "feature": "Price",
                "value_a": f"₹{product_a.price}",
                "value_b": f"₹{product_b.price}",
                "winner": comparison_data["price_analysis"]["winner"],
                "difference": f"₹{abs(product_b.price - product_a.price)}",
                "importance": "high"
            },
            {
                "feature": "Ingredients",
                "value_a": f"{len(product_a.ingredients)}",
                "value_b": f"{len(product_b.ingredients)}",
                "winner": comparison_data["ingredients_analysis"]["winner"],
                "difference": f"{abs(len(product_a.ingredients) - len(product_b.ingredients))}",
                "importance": "high"
            },
            {
                "feature": "Benefits",
                "value_a": f"{len(product_a.benefits)}",
                "value_b": f"{len(product_b.benefits)}",
                "winner": comparison_data["benefits_analysis"]["winner"],
                "difference": f"{abs(len(product_a.benefits) - len(product_b.benefits))}",
                "importance": "medium"
            },
            {
                "feature": "Skin Type",
                "value_a": ", ".join(product_a.skin_type),
                "value_b": ", ".join(product_b.skin_type),
                "winner": "A" if "Combination" in product_a.skin_type else "B" if "Combination" in product_b.skin_type else "Tie",
                "difference": "Specialized vs General",
                "importance": "medium"
            },
            {
                "feature": "Concentration",
                "value_a": product_a.concentration,
                "value_b": product_b.concentration,
                "winner": "A" if "10%" in product_a.concentration else "B" if "10%" in product_b.concentration else "Tie",
                "difference": "Higher is better for efficacy",
                "importance": "medium"
            }
        ]
    }
    
    # Generate summary
    summary = {
        "total_comparisons": len(comparison_table["rows"]),
        "a_wins": sum(1 for row in comparison_table["rows"] if row["winner"] == "A"),
        "b_wins": sum(1 for row in comparison_table["rows"] if row["winner"] == "B"),
        "ties": sum(1 for row in comparison_table["rows"] if row["winner"] == "Tie"),
        "overall_winner": comparison_data["summary"]["overall_winner"],
        "confidence_score": min(100, (max(comparison_data["summary"]["total_score_a"], comparison_data["summary"]["total_score_b"]) / 4) * 100)
    }
    
    # Create recommendation section
    recommendations = [
        {
            "audience": "Budget-conscious buyers",
            "recommendation": comparison_data["category_recommendations"]["for_budget_shoppers"],
            "reasoning": "Based on price comparison and value analysis",
            "priority": "high"
        },
        {
            "audience": "Ingredient-focused users",
            "recommendation": comparison_data["category_recommendations"]["for_ingredient_conscious"],
            "reasoning": "Based on unique ingredient analysis",
            "priority": "medium"
        },
        {
            "audience": "First-time users",
            "recommendation": f"Start with {product_a.name if product_a.price < product_b.price else product_b.name}",
            "reasoning": "Lower investment for trying Vitamin C serums",
            "priority": "medium"
        }
    ]
    
    # Generate structured comparison page
    comparison_page = {
        "metadata": {
            "template_version": "1.0.0",
            "generated_at": datetime.utcnow().isoformat(),
            "content_type": "comparison_page",
            "products_compared": [product_a.name, product_b.name],
            "analysis_depth": "comprehensive"
        },
        "summary": summary,
        "products": {
            product_a.name: product_a.to_dict(),
            product_b.name: product_b.to_dict()
        },
        "comparison_table": comparison_table,
        "detailed_analysis": comparison_data,
        "recommendations": {
            "by_audience": recommendations,
            "final_verdict": {
                "winner": comparison_data["final_verdict"]["overall_value"],
                "reason": f"Wins {summary['a_wins'] if summary['overall_winner'] == 'A' else summary['b_wins']} out of {summary['total_comparisons']} categories",
                "confidence": f"{summary['confidence_score']}%"
            }
        },
        "methodology": {
            "scoring_system": "Category-based comparison with weighted scoring",
            "factors_considered": ["Price", "Ingredients", "Benefits", "Skin Compatibility", "Value"],
            "weight_assignment": "Equal weighting for simplicity",
            "limitations": [
                "Does not consider personal skin sensitivity",
                "Brand reputation not factored",
                "User reviews not included in analysis"
            ]
        },
        "interactive_features": {
            "sortable_table": True,
            "filter_by_category": True,
            "export_options": ["JSON", "CSV", "PDF"],
            "shareable": True
        },
        "seo_optimization": {
            "title": f"{product_a.name} vs {product_b.name} - Detailed Comparison 2024",
            "meta_description": f"Comprehensive comparison between {product_a.name} and {product_b.name}. We analyze price, ingredients, benefits, and determine which is better for your needs.",
            "keywords": [
                f"{product_a.name} vs {product_b.name}",
                "comparison",
                "which is better",
                "skincare serum comparison"
            ],
            "schema_markup": {
                "@type": "ComparativeAnalysis",
                "comparedProducts": [
                    {"@type": "Product", "name": product_a.name},
                    {"@type": "Product", "name": product_b.name}
                ],
                "datePublished": datetime.utcnow().isoformat()
            }
        }
    }
    
    return comparison_page