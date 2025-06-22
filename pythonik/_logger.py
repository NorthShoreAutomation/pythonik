import sys

from loguru import (
    _defaults,
    logger,
)

__all__ = ["logger"]

# Default values
DEFAULT_LOGURU_LEVEL = "INFO"

# Safely remove the default handler
logger.remove()

# Configure handler with LOGURU_LEVEL from environment or fallback to default
logger.add(sys.stderr,
           level=_defaults.env("LOGURU_LEVEL", str, DEFAULT_LOGURU_LEVEL))
