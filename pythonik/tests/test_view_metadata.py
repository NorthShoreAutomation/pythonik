# pythonik/tests/test_view_metadata_init.py
"""
Tests for the ViewMetadata initialization functionality in the Pythonik SDK.

This module contains tests for the custom initialization of the ViewMetadata
class, which handles legacy data formats.
"""
import pytest
from pythonik.models.metadata.views import ViewMetadata, MetadataValues


def test_view_metadata_init_empty():
    """Test initialization of ViewMetadata with empty data."""
    # Arrange & Act
    view_metadata = ViewMetadata()

    # Assert
    assert view_metadata.date_created == ""
    assert view_metadata.date_modified == ""
    assert view_metadata.object_id == ""
    assert view_metadata.object_type == ""
    assert view_metadata.version_id == ""
    assert view_metadata.metadata_values is None


def test_view_metadata_init_with_metadata_values():
    """Test initialization of ViewMetadata with metadata_values dict."""
    # Arrange
    metadata_values = {"field1": {"field_values": [{"value": "value1"}]}}

    # Act
    view_metadata = ViewMetadata(metadata_values=MetadataValues(root=metadata_values))

    # Assert
    assert view_metadata.metadata_values is not None
    assert view_metadata.metadata_values["field1"].field_values[0].value == "value1"


def test_view_metadata_init_with_legacy_format():
    """Test initialization of ViewMetadata with legacy 'values' format."""
    # Arrange
    data = {
        "field1": {"values": [{"value": "value1"}]},
        "field2": {"values": [{"value": "value2"}]},
        "date_created": "2023-01-01",
        "object_id": "123",
    }

    # Act
    view_metadata = ViewMetadata(**data)

    # Assert
    # Note: Based on the implementation, non-metadata fields are NOT preserved
    # when transforming legacy format. Only metadata_values are set.
    assert view_metadata.metadata_values is not None

    # Verify the transformation happened correctly
    assert "field1" in view_metadata.metadata_values
    assert "field2" in view_metadata.metadata_values
    assert view_metadata.metadata_values["field1"].field_values[0].value == "value1"
    assert view_metadata.metadata_values["field2"].field_values[0].value == "value2"


def test_view_metadata_init_with_mixed_format():
    """Test initialization with both standard fields and legacy format."""
    # Arrange
    data = {
        "field1": {"values": [{"value": "value1"}]},
        "date_created": "2023-01-01",
        "object_id": "123",
        "metadata_values": {"field2": {"field_values": [{"value": "value2"}]}},
    }

    # Act
    view_metadata = ViewMetadata(**data)

    # Assert
    assert view_metadata.date_created == "2023-01-01"
    assert view_metadata.object_id == "123"
    assert view_metadata.metadata_values is not None
    assert "field2" in view_metadata.metadata_values
    assert view_metadata.metadata_values["field2"].field_values[0].value == "value2"

    # The legacy format fields should not be transformed since metadata_values was provided
    assert "field1" not in view_metadata.metadata_values


def test_view_metadata_init_with_non_transformable_data():
    """Test initialization with data that should not be transformed."""
    # Arrange
    data = {
        "field1": "string_value",
        "field2": 123,
        "date_created": "2023-01-01",
        "object_id": "123",
    }

    # Act
    view_metadata = ViewMetadata(**data)

    # Assert
    assert view_metadata.date_created == "2023-01-01"
    assert view_metadata.object_id == "123"
    assert view_metadata.metadata_values is None


def test_view_metadata_init_with_empty_values():
    """Test initialization with empty 'values' lists."""
    # Arrange
    data = {
        "field1": {"values": []},
        "field2": {"values": None},
        "date_created": "2023-01-01",
    }

    # Act
    view_metadata = ViewMetadata(**data)

    # Assert
    assert view_metadata.metadata_values is not None
    assert "field1" in view_metadata.metadata_values
    assert "field2" in view_metadata.metadata_values
    assert view_metadata.metadata_values["field1"].field_values == []
    # The None value is preserved as None (not converted to empty list)
    assert view_metadata.metadata_values["field2"].field_values is None
