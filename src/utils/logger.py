import logging
import sys
from pathlib import Path
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_object = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        if hasattr(record, 'custom_fields'):
            log_object.update(record.custom_fields)
        return json.dumps(log_object)

def setup_logging(log_level="INFO", log_file="logs/system.log"):
    """Setup structured logging"""
    Path("logs").mkdir(exist_ok=True)
    
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, log_level))
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(JSONFormatter())
    
    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(JSONFormatter())
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

def get_logger(name):
    return logging.getLogger(name)