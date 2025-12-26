from src.agents.base_agent import BaseAgent, AgentInput, AgentOutput
from src.core.models import Product
from src.templates.comparison_template import comparison_template
from src.logic_blocks.comparison_block import generate_comparison_block

class ComparisonAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="ComparisonAgent", version="1.0.0")
        
    def process(self, input_data: AgentInput) -> dict:
        """Generate comparison page with fictional product"""
        context = input_data.data
        product_a = context.get("product")
        
        if not product_a or not isinstance(product_a, Product):
            raise ValueError("Product A data not available")
        
        # Create fictional Product B
        product_b = Product(
            name="RadiantX Serum",
            concentration="5% Vitamin C",
            skin_type=["All Skin Types"],
            ingredients=["Vitamin C", "Glycerin"],
            benefits=["Basic Brightening", "Light Hydration"],
            usage="Apply once daily, preferably in the morning",
            side_effects="Minimal to none for most users",
            price=899
        )
        
        # Generate comparison data
        comparison_data = generate_comparison_block(product_a, product_b)
        
        # Generate page using template
        page_content = comparison_template(product_a, product_b, comparison_data)
        
        result = {
            "page_type": "ComparisonPage",
            "content": page_content,
            "metadata": {
                "compared_products": [product_a.name, product_b.name],
                "generated_by": self.name,
                "analysis_depth": "comprehensive"
            }
        }
        
        self.logger.info(f"Generated comparison: {product_a.name} vs {product_b.name}")
        return result