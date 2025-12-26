from src.agents.base_agent import BaseAgent, AgentInput, AgentOutput
from src.core.models import Product
from src.core.exceptions import ValidationError

class DataParserAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="DataParserAgent", version="1.0.0")
        
    def validate_input(self, input_data: AgentInput) -> bool:
        """Flexible validation - accept ANY reasonable field names"""
        data = input_data.data
        print(f"DEBUG: Data keys received: {list(data.keys())}")
        print(f"DEBUG: Data preview: {str(data)[:100]}")
        return True  # Accept anything for now
    
    def process(self, input_data: AgentInput) -> dict:
        """Convert raw data to Product model - handle ANY field names"""
        data = input_data.data
        
        # Try to extract fields with flexible naming
        name = data.get("product_name") or data.get("name") or "Unknown Product"
        concentration = data.get("concentration") or ""
        
        # Handle skin_type - could be string or list
        skin_type = data.get("skin_type") or []
        if isinstance(skin_type, str):
            skin_type = [skin_type]
            
        # Handle ingredients
        ingredients = data.get("key_ingredients") or data.get("ingredients") or data.get("keyIngredients") or []
        if isinstance(ingredients, str):
            ingredients = [ingredients]
            
        # Handle benefits  
        benefits = data.get("benefits") or []
        if isinstance(benefits, str):
            benefits = [benefits]
            
        usage = data.get("how_to_use") or data.get("usage") or data.get("howToUse") or ""
        side_effects = data.get("side_effects") or data.get("sideEffects") or ""
        
        # Handle price - could be string or number
        price = data.get("price") or 0
        if isinstance(price, str):
            try:
                price = int(price)
            except:
                price = 0
        
        print(f"DEBUG: Parsed name: {name}")
        print(f"DEBUG: Parsed ingredients: {ingredients}")
        
        # Create Product object
        product = Product(
            name=name,
            concentration=concentration,
            skin_type=skin_type,
            ingredients=ingredients,
            benefits=benefits,
            usage=usage,
            side_effects=side_effects,
            price=price
        )
        
        self.logger.info(f"Successfully parsed product: {product.name}")
        
        return {
            "product": product,
            "parsed_at": "2024-01-01T00:00:00Z",
            "status": "success"
        }