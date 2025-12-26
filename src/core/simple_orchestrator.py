from typing import Dict, List, Any
import time
from src.utils.logger import get_logger

class SimpleOrchestrator:
    def __init__(self):
        self.logger = get_logger("simple_orchestrator")
        
    def run(self, input_data: Dict) -> Dict:
        """Simple orchestrator that definitely works"""
        self.logger.info("Starting simple orchestrator")
        
        # Extract data - handle nested or direct
        if isinstance(input_data, dict) and 'input' in input_data:
            product_data = input_data['input']
        else:
            product_data = input_data
        
        self.logger.info(f"Processing product: {product_data.get('product_name', product_data.get('name', 'Unknown'))}")
        
        # Import agents
        from src.agents.parser_agent import SimpleParserAgent
        from src.agents.question_agent import SimpleQuestionAgent
        from src.agents.faq_agent import SimpleFAQAgent
        from src.agents.product_page_agent import SimpleProductPageAgent
        from src.agents.comparison_agent import SimpleComparisonAgent
        
        # Initialize simple agents
        agents = {
            "parser": SimpleParserAgent(),
            "questions": SimpleQuestionAgent(),
            "faq": SimpleFAQAgent(),
            "product": SimpleProductPageAgent(),
            "comparison": SimpleComparisonAgent()
        }
        
        # Run pipeline
        product = agents["parser"].run(product_data)
        questions = agents["questions"].run(product)
        faq_output = agents["faq"].run(questions, product)
        product_output = agents["product"].run(product)
        comparison_output = agents["comparison"].run(product)
        
        return {
            "success": True,
            "outputs": {
                "faq": faq_output,
                "product_page": product_output,
                "comparison": comparison_output
            },
            "errors": []
        }