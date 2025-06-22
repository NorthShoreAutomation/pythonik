# pythonik/tests/test_imports.py
"""Tests to verify the correct logger imports in different modules."""

import unittest


class TestLoggerImports(unittest.TestCase):
    """Test suite for verifying logger imports in various modules."""

    def test_specs_base_imports_logger(self):
        """Test that specs/base.py imports logger from the central module."""
        # First ensure our module is imported
        import pythonik.specs.base

        # Check if the specs.base module imports from _logger
        source = inspect_imports(pythonik.specs.base)
        self.assertIn("from pythonik._logger import logger", source)

    def test_specs_metadata_imports_logger(self):
        """Test that specs/metadata.py imports logger from the central module."""
        # First ensure our module is imported
        import pythonik.specs.metadata

        # Check if the specs.metadata module imports from _logger
        source = inspect_imports(pythonik.specs.metadata)
        self.assertIn("from pythonik._logger import logger", source)
        self.assertNotIn("from loguru import logger", source)

    def test_tests_metadata_imports_logger(self):
        """Test that tests/test_metadata.py imports logger from the central module."""
        # First ensure our module is imported
        import pythonik.tests.test_metadata

        # Check if the test_metadata module imports from _logger
        source = inspect_imports(pythonik.tests.test_metadata)
        self.assertIn("from pythonik._logger import logger", source)
        self.assertNotIn("from loguru import logger", source)


def inspect_imports(module):
    """
    Helper function to extract import statements from a module's source code.

    Args:
        module: The module to inspect

    Returns:
        str: The source code of the module
    """
    try:
        # Get the source of the module
        import inspect

        return inspect.getsource(module)
    except (TypeError, IOError):
        return ""


if __name__ == "__main__":
    unittest.main()
