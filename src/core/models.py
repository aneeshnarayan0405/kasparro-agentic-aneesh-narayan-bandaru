from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional
from datetime import datetime


@dataclass
class Product:
    """
    Product data model representing skincare product information.
    
    Attributes:
        name: Product name
        concentration: Active ingredient concentration
        skin_type: List of suitable skin types
        ingredients: List of key ingredients
        benefits: List of product benefits
        usage: Usage instructions
        side_effects: Potential side effects
        price: Price in local currency
    """
    
    name: str
    concentration: str
    skin_type: List[str]
    ingredients: List[str]
    benefits: List[str]
    usage: str
    side_effects: str
    price: int
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert Product object to dictionary."""
        return asdict(self)
    
    def get_ingredients_count(self) -> int:
        """Get count of ingredients."""
        return len(self.ingredients)
    
    def get_benefits_count(self) -> int:
        """Get count of benefits."""
        return len(self.benefits)
    
    def get_skin_type_string(self) -> str:
        """Get skin types as comma-separated string."""
        return ", ".join(self.skin_type)
    
    def get_price_formatted(self) -> str:
        """Get formatted price string."""
        return f"₹{self.price}"
    
    def get_summary(self) -> str:
        """Get one-line product summary."""
        return f"{self.name} - {self.concentration} for {self.get_skin_type_string()} skin"


@dataclass
class PageOutput:
    """
    Standard output model for generated content pages.
    
    Attributes:
        page_type: Type of page (FAQ, ProductPage, ComparisonPage)
        content: The generated content
        metadata: Additional metadata about generation
    """
    
    page_type: str
    content: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = None
    
    def __post_init__(self):
        """Initialize metadata if not provided."""
        if self.metadata is None:
            self.metadata = {
                "generated_at": datetime.utcnow().isoformat(),
                "version": "1.0.0"
            }
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert PageOutput to dictionary."""
        return {
            "page_type": self.page_type,
            "content": self.content,
            "metadata": self.metadata
        }
    
    def validate(self) -> bool:
        """Basic validation of page output."""
        required_fields = ["page_type", "content"]
        for field in required_fields:
            if not getattr(self, field):
                return False
        return True


@dataclass
class ValidationResult:
    """
    Model for validation results.
    
    Attributes:
        is_valid: Whether validation passed
        errors: List of validation errors
        warnings: List of validation warnings
        score: Validation score (0-100)
    """
    
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    score: float
    
    def __post_init__(self):
        """Ensure lists are initialized."""
        if self.errors is None:
            self.errors = []
        if self.warnings is None:
            self.warnings = []
    
    def add_error(self, error: str):
        """Add validation error."""
        self.errors.append(error)
        self.is_valid = False
    
    def add_warning(self, warning: str):
        """Add validation warning."""
        self.warnings.append(warning)
    
    def get_summary(self) -> str:
        """Get validation summary."""
        if self.is_valid and not self.warnings:
            return "✅ Validation passed"
        elif self.is_valid and self.warnings:
            return f"⚠️ Validation passed with {len(self.warnings)} warnings"
        else:
            return f"❌ Validation failed with {len(self.errors)} errors"


@dataclass
class AgentMetrics:
    """
    Metrics for agent performance tracking.
    
    Attributes:
        agent_name: Name of the agent
        executions: Total number of executions
        successes: Number of successful executions
        failures: Number of failed executions
        avg_execution_time_ms: Average execution time in milliseconds
        total_execution_time_ms: Total execution time in milliseconds
    """
    
    agent_name: str
    executions: int = 0
    successes: int = 0
    failures: int = 0
    avg_execution_time_ms: float = 0.0
    total_execution_time_ms: float = 0.0
    
    def record_execution(self, success: bool, execution_time_ms: float):
        """Record an agent execution."""
        self.executions += 1
        
        if success:
            self.successes += 1
        else:
            self.failures += 1
        
        self.total_execution_time_ms += execution_time_ms
        self.avg_execution_time_ms = self.total_execution_time_ms / self.executions
    
    def get_success_rate(self) -> float:
        """Calculate success rate."""
        if self.executions == 0:
            return 0.0
        return (self.successes / self.executions) * 100
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert metrics to dictionary."""
        return {
            "agent_name": self.agent_name,
            "executions": self.executions,
            "successes": self.successes,
            "failures": self.failures,
            "success_rate": self.get_success_rate(),
            "avg_execution_time_ms": self.avg_execution_time_ms,
            "total_execution_time_ms": self.total_execution_time_ms
        }


@dataclass
class SystemMetrics:
    """
    System-wide performance metrics.
    
    Attributes:
        total_executions: Total agent executions
        system_uptime_ms: System uptime in milliseconds
        pipeline_successes: Successful pipeline executions
        pipeline_failures: Failed pipeline executions
        agent_metrics: Dictionary of individual agent metrics
    """
    
    total_executions: int = 0
    system_uptime_ms: float = 0.0
    pipeline_successes: int = 0
    pipeline_failures: int = 0
    agent_metrics: Dict[str, AgentMetrics] = None
    
    def __post_init__(self):
        """Initialize agent_metrics dictionary."""
        if self.agent_metrics is None:
            self.agent_metrics = {}
    
    def record_pipeline_execution(self, success: bool):
        """Record a pipeline execution."""
        if success:
            self.pipeline_successes += 1
        else:
            self.pipeline_failures += 1
    
    def get_agent_metrics(self, agent_name: str) -> AgentMetrics:
        """Get or create metrics for an agent."""
        if agent_name not in self.agent_metrics:
            self.agent_metrics[agent_name] = AgentMetrics(agent_name=agent_name)
        return self.agent_metrics[agent_name]
    
    def get_pipeline_success_rate(self) -> float:
        """Calculate pipeline success rate."""
        total_pipelines = self.pipeline_successes + self.pipeline_failures
        if total_pipelines == 0:
            return 0.0
        return (self.pipeline_successes / total_pipelines) * 100
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert system metrics to dictionary."""
        return {
            "total_executions": self.total_executions,
            "system_uptime_ms": self.system_uptime_ms,
            "pipeline_successes": self.pipeline_successes,
            "pipeline_failures": self.pipeline_failures,
            "pipeline_success_rate": self.get_pipeline_success_rate(),
            "agents": {
                name: metrics.to_dict()
                for name, metrics in self.agent_metrics.items()
            }
        }