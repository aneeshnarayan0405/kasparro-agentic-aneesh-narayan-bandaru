#!/usr/bin/env python3
"""
Script for running the pipeline with different configurations
"""
import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.config import ConfigManager
from src.utils.logger import setup_logging
from main import run_pipeline, load_input_data

def run_with_config(config_name: str):
    """Run pipeline with specific configuration"""
    print(f"🚀 Running pipeline with config: {config_name}")
    
    # Setup logging
    setup_logging(log_level="INFO")
    
    # Load config
    config = ConfigManager()
    
    # Load input data
    input_data = load_input_data(config.get("paths.input_data"))
    
    # Run pipeline
    run_pipeline(config, input_data)
    
    print("✅ Pipeline completed successfully")

def main():
    parser = argparse.ArgumentParser(description="Run pipeline with different configurations")
    parser.add_argument(
        "--config", 
        choices=["default", "test", "production"],
        default="default",
        help="Configuration profile to use"
    )
    
    args = parser.parse_args()
    
    # Map config names to settings files
    config_files = {
        "default": "config/settings.yaml",
        "test": "config/test_settings.yaml",  # You can create this
        "production": "config/production_settings.yaml"  # You can create this
    }
    
    # For now, use default
    run_with_config(args.config)

if __name__ == "__main__":
    main()