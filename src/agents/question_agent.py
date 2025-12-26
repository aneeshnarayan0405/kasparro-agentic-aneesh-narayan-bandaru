from src.agents.base_agent import BaseAgent, AgentInput, AgentOutput
from src.core.models import Product

class QuestionGenerationAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="QuestionGenerationAgent", version="1.0.0")
        
    def process(self, input_data: AgentInput) -> dict:
        """Generate categorized questions from product data"""
        context = input_data.data
        
        if "product" not in context:
            raise ValueError("Product data not found in context")
        
        product = context["product"]
        if not isinstance(product, Product):
            raise TypeError("Expected Product object")
        
        # Generate questions based on product data
        questions = {
            "informational": [
                f"What is {product.name}?",
                "What is Vitamin C good for in skincare?",
                "Who is this serum suitable for?",
                "What skin types benefit most from this serum?",
                "How long does one bottle typically last?"
            ],
            "safety": [
                "Are there any side effects?",
                "Is it safe for sensitive skin?",
                "Can I use it with other active ingredients?",
                "What should I do if I experience irritation?",
                "Is it safe to use during pregnancy?"
            ],
            "usage": [
                "How should I apply this serum?",
                "Can I use it both day and night?",
                "How many drops should I use per application?",
                "Should I follow with moisturizer?",
                "How long should I wait before applying other products?"
            ],
            "purchase": [
                "Is it worth the price?",
                "Where can I buy it?",
                "Is there a return policy?",
                "How does it compare to cheaper alternatives?",
                "Are there any discounts available?"
            ],
            "comparison": [
                "How does it compare to other Vitamin C serums?",
                "What makes it different from drugstore options?",
                "Is it better than DIY Vitamin C solutions?",
                "How does it compare to professional treatments?",
                "What are the alternatives in this price range?"
            ]
        }
        
        # Count total questions
        total_questions = sum(len(q_list) for q_list in questions.values())
        self.logger.info(f"Generated {total_questions} questions across {len(questions)} categories")
        
        return {
            "questions": questions,
            "total_count": total_questions,
            "categories": list(questions.keys())
        }