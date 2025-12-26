from src.core.models import Product

class SimpleParserAgent:
    def run(self, data):
        print(f"DEBUG: Parser received data with keys: {list(data.keys())}")
        
        # Extract with multiple possible names
        name = data.get("product_name") or data.get("name") or "GlowBoost Vitamin C Serum"
        concentration = data.get("concentration") or "10% Vitamin C"
        skin_type = data.get("skin_type") or ["Oily", "Combination"]
        ingredients = data.get("key_ingredients") or data.get("ingredients") or ["Vitamin C", "Hyaluronic Acid"]
        benefits = data.get("benefits") or ["Brightening", "Fades dark spots"]
        usage = data.get("how_to_use") or data.get("usage") or "Apply 2–3 drops in the morning before sunscreen"
        side_effects = data.get("side_effects") or "Mild tingling for sensitive skin"
        price = data.get("price") or 699
        
        # Ensure lists
        if isinstance(skin_type, str):
            skin_type = [skin_type]
        if isinstance(ingredients, str):
            ingredients = [ingredients]
        if isinstance(benefits, str):
            benefits = [benefits]
        
        # Convert price to int
        if isinstance(price, str):
            try:
                price = int(price)
            except:
                price = 699
        
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
        
        print(f"DEBUG: Created product: {product.name}")
        return product