"""
Unit tests for logic blocks
"""
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.logic_blocks.benefits_block import generate_benefits_block
from src.logic_blocks.usage_block import generate_usage_block
from src.logic_blocks.price_block import generate_price_block

class TestBenefitsBlock:
    def test_benefits_block_formatting(self):
        """Test benefits block generates correct format"""
        mock_product = type('Product', (), {
            'benefits': ['Brightening', 'Hydration'],
            'name': 'Test Serum'
        })()
        
        result = generate_benefits_block(mock_product)
        
        assert 'benefits_list' in result
        assert 'benefits_description' in result
        assert len(result['benefits_list']) == 2
        assert 'Brightening' in result['benefits_description']

class TestUsageBlock:
    def test_usage_block_structure(self):
        """Test usage block has correct structure"""
        mock_product = type('Product', (), {
            'usage': 'Apply 2-3 drops daily',
            'name': 'Test Serum'
        })()
        
        result = generate_usage_block(mock_product)
        
        assert 'instructions' in result
        assert 'frequency' in result
        assert 'best_time' in result
        assert 'note' in result
        assert result['instructions'] == 'Apply 2-3 drops daily'

class TestPriceBlock:
    def test_price_analysis_categories(self):
        """Test price block categorizes correctly"""
        mock_product = type('Product', (), {
            'price': 699
        })()
        
        result = generate_price_block(mock_product)
        
        assert 'value' in result
        assert 'currency' in result
        assert 'category' in result
        assert 'value_verdict' in result
        assert result['currency'] == 'INR'