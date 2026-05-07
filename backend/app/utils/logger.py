import logging
import sys
from typing import Any

# Configure logging format
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - [ID: %(correlation_id)s] - %(message)s"

class CorrelationIdFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, "correlation_id") or record.correlation_id is None:
            record.correlation_id = "N/A"
        return True

def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Console handler
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(LOG_FORMAT)
    handler.setFormatter(formatter)
    
    # Add filter for correlation ID
    logger.addFilter(CorrelationIdFilter())
    
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger

# Global logger instance example
logger = setup_logger("AI-LeadPilot")
