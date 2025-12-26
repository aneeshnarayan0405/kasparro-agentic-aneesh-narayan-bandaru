"""
Integration tests for full system workflow with BaseAgent
"""
import sys
import os
import json
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.orchestrator import Orchestrator
from src.agents.parser_agent import DataParserAgent
from src.agents.question_agent import QuestionGenerationAgent
from src.agents.faq_agent import FAQAgent
from src.agents.product_page_agent import ProductPageAgent
from src.agents.comparison_agent import ComparisonAgent
from src.agents.validation_agent import ValidationAgent
from src.agents.base_agent import AgentInput

class TestFullPipelineWithBaseAgent:
    """Test the complete pipeline using BaseAgent architecture"""
    
    def setup_method(self):
        """Setup test data and agents"""
        self.test_data = {
            "product_name": "Integration Test Serum",
            "concentration": "15% Vitamin C",
            "skin_type": ["Normal", "Dry"],
            "key_ingredients": ["Vitamin C", "Hyaluronic Acid", "Niacinamide"],
            "benefits": ["Brightening", "Hydration", "Even Skin Tone"],
            "how_to_use": "Apply every morning and evening",
            "side_effects": "Rare irritation for sensitive skin",
            "price": 1299
        }
        
        # Initialize agents
        self.agents = {
            "parser": DataParserAgent(),
            "validation": ValidationAgent(),
            "questions": QuestionGenerationAgent(),
            "faq": FAQAgent(),
            "product": ProductPageAgent(),
            "comparison": ComparisonAgent()
        }
        
        self.orchestrator = Orchestrator(self.agents)
    
    def test_agent_initialization(self):
        """Test that all agents initialize correctly with BaseAgent"""
        for agent_name, agent in self.agents.items():
            assert hasattr(agent, 'name'), f"{agent_name} missing name attribute"
            assert hasattr(agent, 'version'), f"{agent_name} missing version attribute"
            assert hasattr(agent, 'logger'), f"{agent_name} missing logger"
            assert hasattr(agent, 'execute'), f"{agent_name} missing execute method"
            assert hasattr(agent, 'process'), f"{agent_name} missing process method"
    
    def test_agent_execution_flow(self):
        """Test individual agent execution with AgentInput"""
        # Test parser agent
        parser_agent = self.agents["parser"]
        agent_input = AgentInput(data=self.test_data)
        result = parser_agent.execute(agent_input)
        
        assert result.success == True
        assert "product" in result.data
        assert result.execution_time_ms > 0
    
    def test_complete_pipeline_execution(self):
        """Test that complete pipeline executes without errors"""
        result = self.orchestrator.run(self.test_data)
        
        assert result.success == True
        assert 'outputs' in result.__dict__
        assert 'faq' in result.outputs
        assert 'product_page' in result.outputs
        assert 'comparison' in result.outputs
        assert 'metrics' in result.__dict__
    
    def test_output_json_structure(self):
        """Test that outputs have correct JSON structure"""
        result = self.orchestrator.run(self.test_data)
        
        # Check all outputs have required structure
        for output_type in ['faq', 'product_page', 'comparison']:
            output = result.outputs[output_type]
            assert 'page_type' in output
            assert 'content' in output
            assert 'metadata' in output
            
            # Content should be valid for JSON serialization
            try:
                json.dumps(output['content'])
            except TypeError:
                assert False, f"{output_type} content is not JSON serializable"
    
    def test_pipeline_metrics(self):
        """Test that pipeline collects metrics"""
        result = self.orchestrator.run(self.test_data)
        
        assert 'metrics' in result
        metrics = result.metrics
        assert 'system' in metrics
        assert 'agents' in metrics
        
        # Check agent metrics were recorded
        assert len(metrics['agents']) > 0
        
        # Check system metrics
        system_metrics = metrics['system']
        assert 'total_executions' in system_metrics
        assert 'total_duration_ms' in system_metrics
        assert system_metrics['total_duration_ms'] > 0
    
    def test_error_handling(self):
        """Test that pipeline handles errors gracefully"""
        # Test with invalid data
        invalid_data = {"product_name": "Test"}  # Missing required fields
        
        # Create a new orchestrator with same agents
        orchestrator = Orchestrator(self.agents)
        result = orchestrator.run(invalid_data)
        
        # Pipeline should fail but not crash
        assert result.success == False
        assert len(result.errors) > 0
    
    def test_output_directory_creation(self, tmp_path):
        """Test that outputs can be saved to filesystem"""
        # Create temporary output directory
        output_dir = tmp_path / "test_outputs"
        output_dir.mkdir()
        
        # Run pipeline
        result = self.orchestrator.run(self.test_data)
        
        # Save outputs
        from src.utils.file_handler import save_output
        
        for output_type, content in result.outputs.items():
            filename = output_dir / f"{output_type}.json"
            success = save_output(str(filename), content)
            assert success == True
            assert filename.exists()
            
            # Verify JSON is valid
            with open(filename, 'r') as f:
                json_data = json.load(f)
            assert isinstance(json_data, dict)
            
            # Verify structure
            assert 'page_type' in json_data
            assert 'content' in json_data