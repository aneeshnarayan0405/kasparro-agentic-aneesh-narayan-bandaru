from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import time
from src.agents.base_agent import BaseAgent, AgentInput, AgentOutput
from src.utils.logger import get_logger
from src.utils.metrics import MetricsCollector
from src.core.exceptions import OrchestrationError

@dataclass
class PipelineResult:
    success: bool
    outputs: Dict[str, Any]
    metrics: Dict[str, Any]
    errors: List[str]
    execution_time_ms: float

class Orchestrator:
    def __init__(self, agents: Dict[str, BaseAgent]):
        self.agents = agents
        self.logger = get_logger("orchestrator")
        self.metrics = MetricsCollector()
        self.execution_graph = []
        
    def build_execution_plan(self) -> List[List[str]]:
        """DAG-based execution plan"""
        return [
            ["parser", "validation"],
            ["questions"],
            ["faq", "product", "comparison"]
        ]
    
    def execute_phase(self, phase_agents: List[str], context: Dict) -> Dict:
        phase_results = {}
        
        for agent_name in phase_agents:
            if agent_name not in self.agents:
                continue
                
            agent = self.agents[agent_name]
            self.logger.info(f"Executing {agent_name}...")
            
            # Prepare agent input
            agent_input = AgentInput(
                data=context,
                metadata={"phase": "generation"}
            )
            
            # Execute with timing
            result = agent.execute(agent_input)
            
            # Collect metrics
            self.metrics.record_agent_execution(
                agent_name=agent_name,
                success=result.success,
                duration_ms=result.execution_time_ms
            )
            
            if result.success:
                phase_results[agent_name] = result.data
                context.update(result.data)
            else:
                self.logger.error(f"Agent {agent_name} failed: {result.error}")
                raise OrchestrationError(f"Agent {agent_name} failed")
        
        return phase_results
    
    def run(self, input_data: Dict) -> PipelineResult:
        """Main orchestration pipeline"""
        start_time = time.time()
        all_outputs = {}
        errors = []
        
        try:
            # Build and execute phases
            execution_plan = self.build_execution_plan()
            context = {"input": input_data}
            
            for phase_idx, phase_agents in enumerate(execution_plan):
                self.logger.info(f"Starting phase {phase_idx + 1}: {phase_agents}")
                
                try:
                    phase_results = self.execute_phase(phase_agents, context)
                    all_outputs.update(phase_results)
                    
                except Exception as e:
                    errors.append(str(e))
                    self.logger.error(f"Phase {phase_idx + 1} failed: {e}")
                    raise
            
            # Generate final outputs
            final_outputs = {
                "faq": all_outputs.get("faq", {}),
                "product_page": all_outputs.get("product", {}),
                "comparison": all_outputs.get("comparison", {})
            }
            
            # Calculate execution time
            execution_time = (time.time() - start_time) * 1000
            
            # Get metrics
            metrics_summary = self.metrics.get_summary()
            
            return PipelineResult(
                success=True,
                outputs=final_outputs,
                metrics=metrics_summary,
                errors=errors,
                execution_time_ms=execution_time
            )
            
        except Exception as e:
            self.logger.error(f"Orchestration failed: {e}")
            return PipelineResult(
                success=False,
                outputs={},
                metrics=self.metrics.get_summary(),
                errors=[str(e)],
                execution_time_ms=(time.time() - start_time) * 1000
            )