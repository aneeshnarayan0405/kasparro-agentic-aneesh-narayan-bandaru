# debug.py - Debug script to find the issue
import json
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from src.agents.parser_agent import DataParserAgent
from src.agents.base_agent import AgentInput

def debug_input_data():
    print("🔍 Debugging Input Data Issue")
    print("=" * 50)
    
    # Check if file exists
    input_file = Path("data/product_input.json")
    if not input_file.exists():
        print(f"❌ File not found: {input_file}")
        return
    
    # Load data
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    print(f"📁 File loaded: {input_file}")
    print(f"📊 Data keys: {list(data.keys())}")
    print(f"📦 Data preview: {str(data)[:200]}...")
    
    # Check required fields
    required_fields = [
        "product_name", "concentration", "skin_type",
        "key_ingredients", "benefits", "how_to_use",
        "side_effects", "price"
    ]
    
    print("\n✅ Checking required fields:")
    for field in required_fields:
        if field in data:
            print(f"  ✓ {field}: {data[field]}")
        else:
            print(f"  ❌ {field}: MISSING")
    
    # Test the agent
    print("\n🤖 Testing DataParserAgent...")
    try:
        agent = DataParserAgent()
        agent_input = AgentInput(data=data)
        result = agent.execute(agent_input)
        
        if result.success:
            print(f"  ✅ Agent executed successfully")
            print(f"  ⏱️  Execution time: {result.execution_time_ms:.2f}ms")
        else:
            print(f"  ❌ Agent failed: {result.error}")
            
    except Exception as e:
        print(f"  ❌ Exception: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_input_data()