# pythonik/tests/test_base_spec_logging.py
"""Tests for logging functionality in Spec base class."""

import unittest
from unittest.mock import (
    MagicMock,
    call,
    patch,
)

from pythonik.specs.base import Spec


class TestBaseSpecLogging(unittest.TestCase):
    """Test suite for the logging functionality in the Spec base class."""

    def setUp(self):
        """Set up test fixtures."""
        self.session = MagicMock()
        self.spec = Spec(self.session,
                         timeout=5,
                         base_url="https://test.iconik.io")

    @patch("pythonik._logger.logger.debug")
    def test_send_request_logs_url(self, mock_debug):
        """Test that send_request logs the URL being requested."""
        # Mock the prepare_request and send methods
        self.session.prepare_request.return_value = MagicMock()
        self.session.send.return_value = MagicMock()

        # Call send_request
        self.spec.send_request("GET", "test/path")

        # Verify debug was called with URL info
        expected_call = call(
            "Sending {} request to {}",
            "GET",
            "https://test.iconik.io/v1/test/path",
        )
        self.assertEqual(mock_debug.call_args, expected_call)

    @patch("pythonik._logger.logger.debug")
    def test_parse_response_logs_response_text(self, mock_debug):
        """Test that parse_response logs the response text for successful responses."""
        # Create a mock response with ok=True
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.text = '{"key": "value"}'
        mock_response.json.return_value = {"key": "value"}

        # Call parse_response with a mock model
        mock_model = MagicMock()
        mock_model.model_validate.return_value = "model_instance"
        self.spec.parse_response(mock_response, mock_model)

        # Verify debug was called with response text
        mock_debug.assert_called_once_with(mock_response.text)

    @patch("pythonik._logger.logger.debug")
    def test_parse_response_no_logging_for_failed_responses(self, mock_debug):
        """Test that parse_response doesn't log for failed responses."""
        # Create a mock response with ok=False
        mock_response = MagicMock()
        mock_response.ok = False

        # Call parse_response
        self.spec.parse_response(mock_response, MagicMock())

        # Verify debug was not called
        mock_debug.assert_not_called()


if __name__ == "__main__":
    unittest.main()
