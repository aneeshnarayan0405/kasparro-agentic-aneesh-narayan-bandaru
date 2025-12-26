#!/usr/bin/env python3
"""
Demo script to showcase the system capabilities
"""
import sys
import time
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.orchestrator import Orchestrator
from src.agents.parser_agent import DataParserAgent
from src.agents.question_agent import QuestionGenerationAgent
from src.agents.faq_agent import FAQAgent
from src.agents.product_page_agent import ProductPageAgent
from src.agents.comparison_agent import ComparisonAgent
from src.agents.validation_agent import ValidationAgent
from src.utils.file_handler import save_output

def run_demo():
    """Run a comprehensive demo of the system"""
    print("🚀 Multi-Agent Content Generation System - DEMO")
    print("=" * 60)
    
    # Test data
    demo_data = {
        "product_name": "GlowBoost Vitamin C Serum",
        "concentration": "10% Vitamin C",
        "skin_type": ["Oily", "Combination"],
        "key_ingredients": ["Vitamin C", "Hyaluronic Acid"],
        "benefits": ["Brightening", "Fades dark spots"],
        "how_to_use": "Apply 2–3 drops in the morning before sunscreen",
        "side_effects": "Mild tingling for sensitive skin",
        "price": 699
    }
    
    print("\n📋 Input Data:")
    for key, value in demo_data.items():
        print(f"  {key}: {value}")
    
    print("\n🤖 Initializing Agents...")
    agents = {
        "parser": DataParserAgent(),
        "validation": ValidationAgent(),
        "questions": QuestionGenerationAgent(),
        "faq": FAQAgent(),
        "product": ProductPageAgent(),
        "comparison": ComparisonAgent()
    }
    
    print(f"  ✓ {len(agents)} agents initialized")
    
    print("\n🔧 Creating Orchestrator...")
    orchestrator = Orchestrator(agents)
    print("  ✓ Orchestrator ready")
    
    print("\n⚡ Executing Pipeline...")
    start_time = time.time()
    result = orchestrator.run(demo_data)
    execution_time = time.time() - start_time
    
    if result.success:
        print(f"  ✓ Pipeline completed in {execution_time:.2f}s")
        
        # Show metrics
        print("\n📊 Performance Metrics:")
        metrics = result.metrics
        print(f"  Total Executions: {metrics['system']['total_executions']}")
        print(f"  Total Duration: {metrics['system']['total_duration_ms']:.2f}ms")
        
        print(f"  Agent Performance:")
        for agent_name, agent_metrics in metrics['agents'].items():
            print(f"    {agent_name}: {agent_metrics['success_rate']*100:.1f}% success, "
                  f"{agent_metrics['avg_duration_ms']:.1f}ms avg")
        
        # Save outputs
        print("\n💾 Saving Outputs...")
        outputs_dir = Path("demo_outputs")
        outputs_dir.mkdir(exist_ok=True)
        
        for output_type, content in result.outputs.items():
            filename = outputs_dir / f"{output_type}.json"
            save_output(str(filename), content)
            print(f"  ✓ Saved {filename}")
        
        # Show previews
        print("\n👁️  Output Previews:")
        for output_type, content in result.outputs.items():
            print(f"\n  {output_type.upper()}:")
            if 'content' in content and 'metadata' in content['content']:
                metadata = content['content']['metadata']
                print(f"    Type: {metadata.get('content_type', 'N/A')}")
                print(f"    Generated: {metadata.get('generated_at', 'N/A')[:19]}")
            
            if output_type == 'faq' and 'content' in content and 'questions' in content['content']:
                questions = content['content']['questions']
                print(f"    Questions: {len(questions)}")
                if questions:
                    print(f"    Sample: {questions[0].get('question', 'N/A')[:50]}...")
        
        print("\n✅ DEMO COMPLETED SUCCESSFULLY!")
        print(f"📁 Check 'demo_outputs/' folder for generated files")
        
    else:
        print(f"\n❌ Pipeline failed with errors:")
        for error in result.errors:
            print(f"  - {error}")

if __name__ == "__main__":
    run_demo()