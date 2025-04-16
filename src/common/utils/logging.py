"""
Logging utilities for standardized logging across notebooks and jobs.
"""

import logging
import datetime
from typing import Optional, Dict, Any


def _get_logger() -> logging.Logger:
    """
    Get or create a logger with standardized configuration.
    
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger("databricks")
    
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    
    return logger


def info(message: str, extra: Optional[Dict[str, Any]] = None) -> None:
    """
    Log an info-level message.
    
    Args:
        message: The log message
        extra: Optional dictionary of extra data to include in the log
    """
    logger = _get_logger()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # If running in Databricks, use notebook display
        # Check if we're in Databricks environment without using wildcard import
        import importlib.util
        if importlib.util.find_spec("databricks.sdk.runtime") is not None:
            print(f"{timestamp} - INFO - {message}")
            if extra:
                print(f"Extra context: {extra}")
        else:
            raise ImportError("Not in Databricks runtime")
    except ImportError:
        # If not running in Databricks, use standard logging
        logger.info(message, extra=extra or {})


def error(message: str, extra: Optional[Dict[str, Any]] = None) -> None:
    """
    Log an error-level message.
    
    Args:
        message: The error message
        extra: Optional dictionary of extra data to include in the log
    """
    logger = _get_logger()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # If running in Databricks, use notebook display
        # Check if we're in Databricks environment without using wildcard import
        import importlib.util
        if importlib.util.find_spec("databricks.sdk.runtime") is not None:
            print(f"{timestamp} - ERROR - {message}")
            if extra:
                print(f"Extra context: {extra}")
        else:
            raise ImportError("Not in Databricks runtime")
    except ImportError:
        # If not running in Databricks, use standard logging
        logger.error(message, extra=extra or {}) 