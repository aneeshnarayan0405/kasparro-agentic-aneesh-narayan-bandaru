"""
Custom exceptions for the multi-agent system
"""

class AgenticSystemError(Exception):
    """Base exception for all system errors"""
    pass

class ValidationError(AgenticSystemError):
    """Raised when input validation fails"""
    pass

class AgentExecutionError(AgenticSystemError):
    """Raised when an agent fails during execution"""
    pass

class OrchestrationError(AgenticSystemError):
    """Raised when orchestration pipeline fails"""
    pass

class ConfigurationError(AgenticSystemError):
    """Raised when configuration is invalid"""
    pass

class TemplateError(AgenticSystemError):
    """Raised when template processing fails"""
    pass