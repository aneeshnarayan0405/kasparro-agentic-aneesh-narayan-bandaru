from src.agents.base_agent import BaseAgent, AgentInput, AgentOutput
from src.core.models import Product
from src.templates.faq_template import faq_template
from src.logic_blocks.benefits_block import generate_benefits_block
from src.logic_blocks.usage_block import generate_usage_block
from src.logic_blocks.safety_block import generate_safety_block
from src.logic_blocks.price_block import generate_price_block
from src.logic_blocks.seo_block import generate_seo_metadata

class FAQAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="FAQAgent", version="1.0.0")
        
    def process(self, input_data: AgentInput) -> dict:
        """Generate FAQ page from questions and product data"""
        context = input_data.data
        
        # Extract needed data from context
        questions_data = context.get("questions", {})
        product = context.get("product")
        
        if not product or not isinstance(product, Product):
            raise ValueError("Product data not available")
        
        if not questions_data or "questions" not in questions_data:
            raise ValueError("Questions data not available")
        
        questions = questions_data["questions"]
        
        # Generate answers using logic blocks
        safety_info = generate_safety_block(product)
        usage_info = generate_usage_block(product)
        benefits_info = generate_benefits_block(product)
        price_info = generate_price_block(product)
        seo_info = generate_seo_metadata(product.to_dict())
        
        # Create Q&A pairs (select questions from each category)
        qa_pairs = []
        
        # Informational questions
        if "informational" in questions and questions["informational"]:
            qa_pairs.append((
                questions["informational"][0],
                f"{product.name} is a {product.concentration} serum designed for {', '.join(product.skin_type)} skin types. It features {', '.join(product.ingredients)} for effective skincare."
            ))
        
        # Safety questions
        if "safety" in questions and questions["safety"]:
            qa_pairs.append((
                questions["safety"][0],
                safety_info.get("side_effects", product.side_effects)
            ))
        
        # Usage questions
        if "usage" in questions and questions["usage"]:
            qa_pairs.append((
                questions["usage"][0],
                usage_info.get("instructions", product.usage)
            ))
        
        # Purchase questions
        if "purchase" in questions and questions["purchase"]:
            qa_pairs.append((
                questions["purchase"][0],
                f"At ₹{product.price}, {price_info.get('value_verdict', 'it offers good value')} compared to similar serums with {product.concentration}."
            ))
        
        # Comparison questions
        if "comparison" in questions and questions["comparison"]:
            qa_pairs.append((
                questions["comparison"][0],
                f"{product.name} contains {len(product.ingredients)} key ingredients including {product.ingredients[0]}, making it more comprehensive than basic Vitamin C serums that typically have only one active ingredient."
            ))
        
        # Generate FAQ using template
        faq_content = faq_template(qa_pairs)
        
        # Add metadata
        result = {
            "page_type": "FAQ",
            "content": faq_content,
            "metadata": {
                "total_questions": len(qa_pairs),
                "categories_covered": list(questions.keys()),
                "seo": seo_info,
                "generated_by": self.name
            }
        }
        
        self.logger.info(f"Generated FAQ with {len(qa_pairs)} Q&A pairs")
        return result