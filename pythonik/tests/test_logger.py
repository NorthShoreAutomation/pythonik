# pythonik/tests/test_logger.py
"""Tests for the centralized logger configuration."""

import os
import sys
import unittest
from unittest.mock import patch

from pythonik._logger import logger


class TestLogger(unittest.TestCase):
    """Test suite for the logger configuration."""

    def test_logger_initialization(self):
        """Test that the logger is correctly initialized."""
        # Check that the logger is a Loguru instance
        self.assertEqual(str(type(logger).__module__), "loguru._logger")

    @patch.dict(os.environ, {}, clear=True)
    @patch("loguru._defaults.env")
    def test_default_log_level(self, mock_env):
        """Test that the default log level is INFO when not specified."""
        # Mock the env function to simulate no environment variable
        mock_env.return_value = "INFO"

        # Re-import to trigger logger configuration
        import importlib

        importlib.reload(sys.modules["pythonik._logger"])

        # Verify that env was called with the correct arguments
        mock_env.assert_called_with("LOGURU_LEVEL", str, "INFO")

    @patch.dict(os.environ, {"LOGURU_LEVEL": "DEBUG"})
    @patch("loguru.logger.add")
    def test_custom_log_level(self, mock_add):
        """Test that the logger respects LOGURU_LEVEL environment variable."""
        # Re-import to trigger logger configuration with patched env
        import importlib

        importlib.reload(sys.modules["pythonik._logger"])

        # Verify that add was called with correct level
        mock_add.assert_called_once()
        _, kwargs = mock_add.call_args
        self.assertEqual(kwargs.get("level"), "DEBUG")

    @patch("loguru.logger.debug")
    def test_logger_output(self, mock_debug):
        """Test that the logger outputs messages correctly."""
        # Log a message
        logger.debug("Test message")

        # Verify that the debug method was called with the right message
        mock_debug.assert_called_once_with("Test message")


if __name__ == "__main__":
    unittest.main()
