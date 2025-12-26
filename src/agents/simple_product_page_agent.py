from src.logic_blocks.benefits_block import generate_benefits_block
from src.logic_blocks.usage_block import generate_usage_block

class SimpleProductPageAgent:
    def run(self, product):
        try:
            benefits = generate_benefits_block(product)
            usage = generate_usage_block(product)
        except:
            benefits = {"benefits_list": product.benefits}
            usage = {"instructions": product.usage}
        
        product_output = {
            "page_type": "ProductPage",
            "content": {
                "metadata": {"generated_by": "SimpleProductPageAgent"},
                "product_name": product.name,
                "description": f"{product.concentration} serum with {', '.join(product.ingredients)}",
                "benefits": benefits,
                "usage": usage,
                "price": product.price
            }
        }
        print(f"DEBUG: Created product page for {product.name}")
        return product_output