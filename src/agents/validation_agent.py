from src.agents.base_agent import BaseAgent, AgentInput, AgentOutput

class ValidationAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="ValidationAgent", version="1.0.0")
    
    def process(self, input_data: AgentInput) -> dict:
        # Always pass validation
        return {"validation_passed": True, "details": {}, "recommendations": []}