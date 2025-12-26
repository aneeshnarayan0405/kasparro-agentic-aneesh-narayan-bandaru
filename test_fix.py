# test_fix.py
import json
import sys
sys.path.insert(0, 'src')

print("=" * 60)
print(" TESTING THE FIX")
print("=" * 60)

# 1. Test the JSON file
print("\n1. Testing JSON file...")
try:
    with open('data/product_input.json', 'r') as f:
        data = json.load(f)
    print(f" JSON loaded successfully!")
    print(f"   Keys: {list(data.keys())}")
    for key, value in data.items():
        print(f"   {key}: {value}")
except Exception as e:
    print(f" JSON error: {e}")

# 2. Test the parser agent
print("\n2. Testing DataParserAgent...")
try:
    from agents.parser_agent import DataParserAgent
    from agents.base_agent import AgentInput
    
    agent = DataParserAgent()
    result = agent.execute(AgentInput(data=data))
    
    if result.success:
        print(f" Agent SUCCESS!")
        product = result.data["product"]
        print(f"   Product: {product.name}")
        print(f"   Price: ₹{product.price}")
        print(f"   Ingredients: {product.ingredients}")
    else:
        print(f" Agent failed: {result.error}")
        
except Exception as e:
    print(f" Agent test error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)