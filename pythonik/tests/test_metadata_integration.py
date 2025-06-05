# pythonik/tests/test_metadata_integration.py
"""
Integration tests for metadata component changes in Pythonik SDK.

This module tests the integration between the ViewMetadata class changes
and the new metadata retrieval methods.
"""
import uuid
import requests_mock
import pytest
from pythonik.client import PythonikClient
from pythonik.models.metadata.views import ViewMetadata


def test_get_object_metadata_with_legacy_response():
    """
    Test retrieving metadata with legacy format in the response.

    This test verifies that when the API returns data in the legacy format
    (with 'values' instead of 'field_values'), the ViewMetadata initialization
    properly transforms it.
    """
    with requests_mock.Mocker() as m:
        # Arrange
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = str(uuid.uuid4())
        view_id = str(uuid.uuid4())
        object_type = "assets"

        # Legacy format API response
        response_data = {
            "object_id": object_id,
            "object_type": object_type,
            "date_created": "2023-01-01T12:00:00Z",
            "date_modified": "2023-01-01T12:00:00Z",
            "field1": {"values": [{"value": "value1"}]},
            "field2": {"values": [{"value": "value2"}]},
        }

        mock_address = f"https://app.iconik.io/API/metadata/v1/{object_type}/{object_id}/views/{view_id}/"
        m.get(mock_address, json=response_data)

        # Act
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().get_object_metadata(
            object_type=object_type, object_id=object_id, view_id=view_id
        )

        # Assert
        assert response.response.ok

        # The implementation preserves the original fields
        assert response.data.object_id == object_id
        assert response.data.object_type == object_type
        assert response.data.date_created == "2023-01-01T12:00:00Z"
        assert response.data.date_modified == "2023-01-01T12:00:00Z"

        # Verify the transformation happened correctly
        assert response.data.metadata_values is not None
        assert "field1" in response.data.metadata_values
        assert "field2" in response.data.metadata_values
        assert response.data.metadata_values["field1"].field_values[0].value == "value1"
        assert response.data.metadata_values["field2"].field_values[0].value == "value2"


def test_get_object_metadata_direct_with_legacy_response():
    """
    Test retrieving metadata directly with legacy format in the response.

    This test verifies that when the API returns data in the legacy format
    (with 'values' instead of 'field_values'), the ViewMetadata initialization
    properly transforms it when using get_object_metadata_direct.
    """
    with requests_mock.Mocker() as m:
        # Arrange
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = str(uuid.uuid4())
        object_type = "collections"

        # Legacy format API response
        response_data = {
            "object_id": object_id,
            "object_type": object_type,
            "date_created": "2023-01-01T12:00:00Z",
            "date_modified": "2023-01-01T12:00:00Z",
            "collection_field": {"values": [{"value": "collection_value"}]},
            "status_field": {"values": [{"value": "active"}]},
        }

        mock_address = (
            f"https://app.iconik.io/API/metadata/v1/{object_type}/{object_id}/"
        )
        m.get(mock_address, json=response_data)

        # Act
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().get_object_metadata_direct(
            object_type=object_type, object_id=object_id
        )

        # Assert
        assert response.response.ok

        # The implementation preserves the original fields
        assert response.data.object_id == object_id
        assert response.data.object_type == object_type
        assert response.data.date_created == "2023-01-01T12:00:00Z"
        assert response.data.date_modified == "2023-01-01T12:00:00Z"

        # Verify the transformation happened correctly
        assert response.data.metadata_values is not None
        assert "collection_field" in response.data.metadata_values
        assert "status_field" in response.data.metadata_values
        assert (
            response.data.metadata_values["collection_field"].field_values[0].value
            == "collection_value"
        )
        assert (
            response.data.metadata_values["status_field"].field_values[0].value
            == "active"
        )


def test_get_object_metadata_intercept_404_with_legacy_format():
    """
    Test 404 interception with legacy format in the default model.

    This test verifies that when a 404 response is intercepted with a default
    model in legacy format, the ViewMetadata initialization properly transforms it.
    """
    with requests_mock.Mocker() as m:
        # Arrange
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = str(uuid.uuid4())
        view_id = str(uuid.uuid4())
        object_type = "segments"

        # Legacy format default model
        default_model = ViewMetadata(
            field1={"values": [{"value": "default_value_1"}]},
            field2={"values": [{"value": "default_value_2"}]},
        )

        mock_address = f"https://app.iconik.io/API/metadata/v1/{object_type}/{object_id}/views/{view_id}/"
        m.get(mock_address, status_code=404, json={"error": "Not found"})

        # Act
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().get_object_metadata(
            object_type=object_type,
            object_id=object_id,
            view_id=view_id,
            intercept_404=default_model,
        )

        # Assert
        assert response.data is default_model
        # Verify the transformation happened during default_model creation
        assert response.data.metadata_values is not None
        assert "field1" in response.data.metadata_values
        assert "field2" in response.data.metadata_values
        assert (
            response.data.metadata_values["field1"].field_values[0].value
            == "default_value_1"
        )
        assert (
            response.data.metadata_values["field2"].field_values[0].value
            == "default_value_2"
        )


def test_end_to_end_integration_with_complex_data():
    """
    End-to-end test with complex data structures.

    This test simulates a complex real-world scenario with mixed data formats.
    """
    with requests_mock.Mocker() as m:
        # Arrange
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = str(uuid.uuid4())
        view_id = str(uuid.uuid4())
        object_type = "assets"

        # Complex mixed format API response
        response_data = {
            "object_id": object_id,
            "object_type": object_type,
            "date_created": "2023-01-01T12:00:00Z",
            "date_modified": "2023-01-01T12:00:00Z",
            "title": {"values": [{"value": "Asset Title"}]},
            "description": {"values": [{"value": "Line 1"}, {"value": "Line 2"}]},
            "tags": {
                "values": [{"value": "tag1"}, {"value": "tag2"}, {"value": "tag3"}]
            },
            "status": {"values": [{"value": "active"}]},
            "nested_data": {"sub_field": {"values": [{"value": "nested value"}]}},
            "empty_field": {"values": []},
            "normal_field": "not a transformable field",
        }

        mock_address = f"https://app.iconik.io/API/metadata/v1/{object_type}/{object_id}/views/{view_id}/"
        m.get(mock_address, json=response_data)

        # Act
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().get_object_metadata(
            object_type=object_type, object_id=object_id, view_id=view_id
        )

        # Assert
        assert response.response.ok

        # Note: In the current implementation, the standard fields are not
        # preserved when transforming the legacy format. The implementation
        # creates a new data dict with only metadata_values.

        # Verify the transformation happened correctly for all fields
        assert response.data.metadata_values is not None

        # Single value fields
        assert "title" in response.data.metadata_values
        assert (
            response.data.metadata_values["title"].field_values[0].value
            == "Asset Title"
        )

        # Multi-value fields
        assert "description" in response.data.metadata_values
        assert len(response.data.metadata_values["description"].field_values) == 2
        assert (
            response.data.metadata_values["description"].field_values[0].value
            == "Line 1"
        )
        assert (
            response.data.metadata_values["description"].field_values[1].value
            == "Line 2"
        )

        # Array fields
        assert "tags" in response.data.metadata_values
        assert len(response.data.metadata_values["tags"].field_values) == 3
        tag_values = [
            fv.value for fv in response.data.metadata_values["tags"].field_values
        ]
        assert sorted(tag_values) == ["tag1", "tag2", "tag3"]

        # Status field
        assert "status" in response.data.metadata_values
        assert response.data.metadata_values["status"].field_values[0].value == "active"

        # Empty fields
        assert "empty_field" in response.data.metadata_values
        assert response.data.metadata_values["empty_field"].field_values == []

        # Nested data flat "values" fields should be transformed
        assert "nested_data" not in response.data.metadata_values

        # Regular fields should not be in the metadata_values
        assert "normal_field" not in response.data.metadata_values
