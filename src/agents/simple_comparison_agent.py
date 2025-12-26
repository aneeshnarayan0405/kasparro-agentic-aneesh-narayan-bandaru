class SimpleComparisonAgent:
    def run(self, product_a):
        # Create fictional product B
        product_b_data = {
            "name": "RadiantX Serum",
            "concentration": "5% Vitamin C",
            "skin_type": ["All"],
            "ingredients": ["Vitamin C"],
            "benefits": ["Brightening"],
            "usage": "Apply once daily",
            "side_effects": "None reported",
            "price": 899
        }
        
        from src.core.models import Product
        product_b = Product(**product_b_data)
        
        comparison_output = {
            "page_type": "ComparisonPage",
            "content": {
                "metadata": {"generated_by": "SimpleComparisonAgent"},
                "product_a": {
                    "name": product_a.name,
                    "ingredients": product_a.ingredients,
                    "benefits": product_a.benefits,
                    "price": product_a.price
                },
                "product_b": {
                    "name": product_b.name,
                    "ingredients": product_b.ingredients,
                    "benefits": product_b.benefits,
                    "price": product_b.price
                },
                "recommendation": f"{product_a.name} if you need stronger ingredients; {product_b.name} for basic brightening."
            }
        }
        print(f"DEBUG: Created comparison: {product_a.name} vs {product_b.name}")
        return comparison_output