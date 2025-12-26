from src.agents.base_agent import BaseAgent, AgentInput, AgentOutput
from src.core.models import Product
from src.templates.product_template import product_template
from src.logic_blocks.benefits_block import generate_benefits_block
from src.logic_blocks.usage_block import generate_usage_block
from src.logic_blocks.safety_block import generate_safety_block
from src.logic_blocks.price_block import generate_price_block
from src.logic_blocks.seo_block import generate_seo_metadata

class ProductPageAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="ProductPageAgent", version="1.0.0")
        
    def process(self, input_data: AgentInput) -> dict:
        """Generate complete product page"""
        context = input_data.data
        product = context.get("product")
        
        if not product or not isinstance(product, Product):
            raise ValueError("Product data not available")
        
        # Generate all content blocks
        benefits_info = generate_benefits_block(product)
        usage_info = generate_usage_block(product)
        safety_info = generate_safety_block(product)
        price_info = generate_price_block(product)
        seo_info = generate_seo_metadata(product.to_dict())
        
        # Prepare sections for template
        sections = {
            "header": {
                "title": product.name,
                "subtitle": f"{product.concentration} for {', '.join(product.skin_type)} Skin",
                "tagline": "Advanced Skincare Serum"
            },
            "overview": {
                "description": f"A potent serum featuring {', '.join(product.ingredients)} for visible brightening and spot reduction.",
                "key_features": [
                    f"Concentration: {product.concentration}",
                    f"Skin Type: {', '.join(product.skin_type)}",
                    f"Key Ingredients: {', '.join(product.ingredients)}"
                ]
            },
            "benefits": benefits_info,
            "usage_instructions": usage_info,
            "safety_information": safety_info,
            "pricing": price_info,
            "call_to_action": {
                "primary": f"Get {product.name} for ₹{product.price}",
                "secondary": "Free shipping on orders above ₹999"
            }
        }
        
        # Generate page using template
        page_content = product_template(sections)
        
        result = {
            "page_type": "ProductPage",
            "content": page_content,
            "metadata": {
                "product_name": product.name,
                "generated_by": self.name,
                "seo": seo_info,
                "sections_generated": len(sections)
            }
        }
        
        self.logger.info(f"Generated product page for {product.name}")
        return result