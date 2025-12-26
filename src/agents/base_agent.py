from abc import ABC, abstractmethod
from typing import Any, Dict
from dataclasses import dataclass
from src.utils.logger import get_logger

logger = get_logger(__name__)

@dataclass
class AgentInput:
    data: Dict[str, Any]
    metadata: Dict[str, Any] = None

@dataclass
class AgentOutput:
    success: bool
    data: Dict[str, Any]
    error: str = None
    execution_time_ms: float = 0

class BaseAgent(ABC):
    def __init__(self, name: str, version: str = "1.0.0"):
        self.name = name
        self.version = version
        self.logger = get_logger(f"agent.{name}")
        
    @abstractmethod
    def process(self, input_data: AgentInput) -> AgentOutput:
        pass
    
    def validate_input(self, input_data: AgentInput) -> bool:
        """Override for custom validation"""
        return True
        
    def execute(self, input_data: AgentInput) -> AgentOutput:
        import time
        start_time = time.time()
        
        try:
            self.logger.info(f"Starting {self.name} execution")
            
            if not self.validate_input(input_data):
                return AgentOutput(
                    success=False,
                    data={},
                    error="Input validation failed"
                )
            
            result = self.process(input_data)
            execution_time = (time.time() - start_time) * 1000
            
            self.logger.info(f"{self.name} completed in {execution_time:.2f}ms")
            
            return AgentOutput(
                success=True,
                data=result,
                execution_time_ms=execution_time
            )
            
        except Exception as e:
            self.logger.error(f"{self.name} failed: {str(e)}")
            return AgentOutput(
                success=False,
                data={},
                error=str(e)
            )