# pythonik/tests/test_logger_integration.py
"""Tests for the integration of the logger in the Pythonik codebase."""

import importlib
import os
import tempfile
import unittest
from unittest.mock import (
    MagicMock,
    patch,
)

from pythonik._logger import logger
from pythonik.client import PythonikClient


class TestLoggerIntegration(unittest.TestCase):
    """Test suite for logger integration in Pythonik client classes."""

    def setUp(self):
        """Set up test fixtures."""
        self.app_id = "test_app_id"
        self.auth_token = "test_auth_token"
        self.client = PythonikClient(app_id=self.app_id,
                                     auth_token=self.auth_token,
                                     timeout=3)

    @patch("requests.Session.send")
    @patch("pythonik._logger.logger.debug")
    def test_logs_in_api_calls(self, mock_debug, mock_send):
        """Test that API calls log using the centralized logger."""
        # Setup mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.text = '{"id": "test-id"}'
        mock_response.json.return_value = {"id": "test-id"}
        mock_send.return_value = mock_response

        # Make API call
        self.client.assets().get(asset_id="test-id")

        # Verify debug logs
        self.assertGreaterEqual(mock_debug.call_count, 1)
        # Look for specific log messages we expect
        url_log_found = False
        response_log_found = False
        for call_args in mock_debug.call_args_list:
            args, _ = call_args
            if len(args) > 1 and args[0] == "Sending {} request to {}":
                url_log_found = True
            if args and '{"id": "test-id"}' in str(args):
                response_log_found = True

        self.assertTrue(url_log_found, "URL log message not found")
        self.assertTrue(response_log_found, "Response log message not found")

    @patch.dict(os.environ, {"LOGURU_LEVEL": "DEBUG"})
    def test_environment_var_affects_logger(self):
        """Test that LOGURU_LEVEL environment variable affects the logger."""
        # Reload _logger module to pick up env var change
        import pythonik._logger

        importlib.reload(pythonik._logger)

        # Setup a temp file for log output to verify level
        temp_log = tempfile.NamedTemporaryFile(delete=False)
        try:
            # Add a handler to write to our temp file
            log_id = logger.add(temp_log.name, level="DEBUG")

            # Log messages at different levels
            logger.debug("Debug message")
            logger.info("Info message")
            logger.warning("Warning message")

            # Remove our handler
            logger.remove(log_id)

            # Check log contents
            with open(temp_log.name, "r") as f:
                log_content = f.read()

            # Debug should be logged since LOGURU_LEVEL is set to DEBUG
            self.assertIn("Debug message", log_content)
            self.assertIn("Info message", log_content)
            self.assertIn("Warning message", log_content)
        finally:
            # Clean up
            os.unlink(temp_log.name)

    @patch("pythonik._logger.logger.debug")
    def test_request_payload_logging(self, mock_debug):
        """Test that request payloads are logged when making API calls."""
        with patch("requests.Session.send") as mock_send:
            # Setup mock response
            mock_response = MagicMock()
            mock_response.ok = True
            mock_response.json.return_value = {}
            mock_send.return_value = mock_response

            # Make API call with a payload
            from pythonik.models.assets.assets import AssetCreate

            asset = AssetCreate(title="Test Asset")
            self.client.assets().create(body=asset)

            # Verify we log the URL properly
            url_log_call = None
            for call_args in mock_debug.call_args_list:
                args, _ = call_args
                if len(args) > 1 and args[0] == "Sending {} request to {}":
                    url_log_call = call_args
                    break

            self.assertIsNotNone(url_log_call, "URL log not found")
            args, _ = url_log_call
            self.assertEqual(args[1], "POST")  # Should be a POST request
            self.assertIn("assets", args[2])  # URL should contain 'assets'


if __name__ == "__main__":
    unittest.main()
