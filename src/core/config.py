import yaml
from typing import Dict, Any
from pathlib import Path

class ConfigManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance
    
    def _load_config(self):
        config_path = Path("config/settings.yaml")
        if config_path.exists():
            with open(config_path, 'r') as f:
                self.config = yaml.safe_load(f)
        else:
            self.config = self._get_default_config()
    
    def _get_default_config(self):
        return {
            "system": {
                "log_level": "INFO",
                "max_execution_time": 30000,
                "enable_metrics": True
            },
            "agents": {
                "parser": {"enabled": True, "timeout": 5000},
                "questions": {"enabled": True, "max_questions": 20},
                "faq": {"enabled": True, "min_answers": 5},
                "product": {"enabled": True},
                "comparison": {"enabled": True}
            },
            "output": {
                "format": "json",
                "pretty_print": True,
                "validate_schema": True
            }
        }
    
    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k, {})
        return value if value != {} else default