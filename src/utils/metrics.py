from typing import Dict, List
import time
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class AgentMetrics:
    total_executions: int = 0
    successful_executions: int = 0
    failed_executions: int = 0
    total_duration_ms: float = 0
    avg_duration_ms: float = 0

class MetricsCollector:
    def __init__(self):
        self.metrics = defaultdict(AgentMetrics)
        self.start_time = time.time()
        
    def record_agent_execution(self, agent_name: str, success: bool, duration_ms: float):
        metrics = self.metrics[agent_name]
        metrics.total_executions += 1
        
        if success:
            metrics.successful_executions += 1
        else:
            metrics.failed_executions += 1
            
        metrics.total_duration_ms += duration_ms
        metrics.avg_duration_ms = metrics.total_duration_ms / metrics.total_executions
        
    def get_summary(self) -> Dict:
        total_executions = sum(m.total_executions for m in self.metrics.values())
        total_duration = sum(m.total_duration_ms for m in self.metrics.values())
        
        return {
            "agents": {
                name: {
                    "total_executions": m.total_executions,
                    "success_rate": m.successful_executions / m.total_executions if m.total_executions > 0 else 0,
                    "avg_duration_ms": m.avg_duration_ms
                }
                for name, m in self.metrics.items()
            },
            "system": {
                "total_executions": total_executions,
                "total_duration_ms": total_duration,
                "uptime_seconds": time.time() - self.start_time
            }
        }