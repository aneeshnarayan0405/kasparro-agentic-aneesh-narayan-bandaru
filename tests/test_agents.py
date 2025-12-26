"""
Unit tests for agent implementations
"""
import pytest
from unittest.mock import Mock, patch
import sys
import os

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.agents.parser_agent import DataParserAgent
from src.agents.question_agent import QuestionGenerationAgent
from src.agents.validation_agent import ValidationAgent
from src.core.models import Product

class TestDataParserAgent:
    def test_parser_creates_product_object(self):
        """Test that parser creates proper Product object"""
        agent = DataParserAgent()
        test_data = {
            "product_name": "Test Serum",
            "concentration": "10% Vitamin C",
            "skin_type": ["Oily"],
            "key_ingredients": ["Vitamin C"],
            "benefits": ["Brightening"],
            "how_to_use": "Apply daily",
            "side_effects": "None",
            "price": 500
        }
        
        result = agent.run(test_data)
        
        assert isinstance(result, Product)
        assert result.name == "Test Serum"
        assert result.price == 500
        assert "Oily" in result.skin_type

class TestQuestionGenerationAgent:
    def test_generates_minimum_questions(self):
        """Test that agent generates at least 15 questions"""
        agent = QuestionGenerationAgent()
        
        # Create a mock product
        product = Product(
            name="Test Product",
            concentration="10%",
            skin_type=["Normal"],
            ingredients=["Ingredient"],
            benefits=["Benefit"],
            usage="Use daily",
            side_effects="None",
            price=100
        )
        
        questions = agent.run(product)
        
        # Count total questions
        total_questions = sum(len(q_list) for q_list in questions.values())
        assert total_questions >= 15, f"Expected at least 15 questions, got {total_questions}"
        
        # Verify categories
        expected_categories = ["informational", "safety", "usage", "purchase", "comparison"]
        for category in expected_categories:
            assert category in questions, f"Missing category: {category}"
            assert len(questions[category]) > 0, f"Empty category: {category}"

class TestValidationAgent:
    def test_valid_data_passes(self):
        """Test that valid data passes validation"""
        agent = ValidationAgent()
        
        valid_data = {
            "product_name": "Test",
            "concentration": "10%",
            "skin_type": ["Oily"],
            "key_ingredients": ["Vit C"],
            "benefits": ["Brightening"],
            "how_to_use": "Apply",
            "side_effects": "None",
            "price": 100
        }
        
        result = agent.process({"data": valid_data})
        assert result["valid"] == True
        
    def test_invalid_data_fails(self):
        """Test that invalid data fails validation"""
        agent = ValidationAgent()
        
        invalid_data = {
            "product_name": "Test",
            # Missing required fields
            "price": -100  # Invalid price
        }
        
        result = agent.process({"data": invalid_data})
        assert result["valid"] == False