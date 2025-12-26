from abc import ABC, abstractmethod
from typing import Any, Dict
from dataclasses import dataclass

@dataclass
class BlockConfig:
    enabled: bool = True
    priority: int = 1
    cacheable: bool = True

class BaseLogicBlock(ABC):
    def __init__(self, name: str, config: BlockConfig = None):
        self.name = name
        self.config = config or BlockConfig()
        
    @abstractmethod
    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        pass
    
    def get_metadata(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "config": self.config.__dict__,
            "version": "1.0.0"
        }