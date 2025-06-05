# pythonik/tests/test_get_object_metadata.py
"""
Tests for the new object metadata retrieval methods in Pythonik SDK.

This module tests the get_object_metadata and get_object_metadata_direct
methods added to the MetadataSpec class.
"""
import uuid
import requests_mock
import pytest
from loguru import logger

from pythonik.client import PythonikClient
from pythonik.models.metadata.views import ViewMetadata, MetadataValues
from pythonik.models.metadata.views import FieldValue, FieldValues
from pythonik.specs.metadata import MetadataSpec


def test_get_object_metadata_assets():
    """Test retrieving metadata for an asset object type."""
    with requests_mock.Mocker() as m:
        # Arrange
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = str(uuid.uuid4())
        view_id = str(uuid.uuid4())
        object_type = "assets"

        mv = MetadataValues(
            {"test_field": FieldValues(field_values=[FieldValue(value="test_value")])}
        )

        model = ViewMetadata(
            metadata_values=mv,
            object_id=object_id,
            object_type=object_type,
            date_created="2023-01-01T12:00:00Z",
            date_modified="2023-01-01T12:00:00Z",
        )

        data = model.model_dump()
        mock_address = MetadataSpec.gen_url(
            f"{object_type}/{object_id}/views/{view_id}/"
        )

        m.get(mock_address, json=data)

        # Act
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().get_object_metadata(
            object_type=object_type, object_id=object_id, view_id=view_id
        )

        # Assert
        assert response.response.ok
        assert response.data.object_id == object_id
        assert response.data.object_type == object_type
        assert response.data.metadata_values is not None
        assert "test_field" in response.data.metadata_values
        assert (
            response.data.metadata_values["test_field"].field_values[0].value
            == "test_value"
        )


def test_get_object_metadata_collections():
    """Test retrieving metadata for a collection object type."""
    with requests_mock.Mocker() as m:
        # Arrange
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = str(uuid.uuid4())
        view_id = str(uuid.uuid4())
        object_type = "collections"

        model = ViewMetadata(
            metadata_values=MetadataValues(
                {
                    "collection_field": FieldValues(
                        field_values=[FieldValue(value="collection_value")]
                    )
                }
            ),
            object_id=object_id,
            object_type=object_type,
        )

        data = model.model_dump()
        mock_address = MetadataSpec.gen_url(
            f"{object_type}/{object_id}/views/{view_id}/"
        )

        m.get(mock_address, json=data)

        # Act
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().get_object_metadata(
            object_type=object_type, object_id=object_id, view_id=view_id
        )

        # Assert
        assert response.response.ok
        assert response.data.object_id == object_id
        assert response.data.object_type == object_type
        assert response.data.metadata_values is not None
        assert "collection_field" in response.data.metadata_values
        assert (
            response.data.metadata_values["collection_field"].field_values[0].value
            == "collection_value"
        )


def test_get_object_metadata_segments():
    """Test retrieving metadata for a segment object type."""
    with requests_mock.Mocker() as m:
        # Arrange
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = str(uuid.uuid4())
        view_id = str(uuid.uuid4())
        object_type = "segments"

        model = ViewMetadata(
            metadata_values=MetadataValues(
                {
                    "segment_field": FieldValues(
                        field_values=[FieldValue(value="segment_value")]
                    )
                }
            ),
            object_id=object_id,
            object_type=object_type,
        )

        data = model.model_dump()
        mock_address = MetadataSpec.gen_url(
            f"{object_type}/{object_id}/views/{view_id}/"
        )

        m.get(mock_address, json=data)

        # Act
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().get_object_metadata(
            object_type=object_type, object_id=object_id, view_id=view_id
        )

        # Assert
        assert response.response.ok
        assert response.data.object_id == object_id
        assert response.data.object_type == object_type
        assert response.data.metadata_values is not None
        assert "segment_field" in response.data.metadata_values
        assert (
            response.data.metadata_values["segment_field"].field_values[0].value
            == "segment_value"
        )


def test_get_object_metadata_invalid_type():
    """Test get_object_metadata with an invalid object type."""
    # Arrange
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    object_id = str(uuid.uuid4())
    view_id = str(uuid.uuid4())
    object_type = "invalid_type"

    # Act & Assert
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
    with pytest.raises(ValueError) as excinfo:
        client.metadata().get_object_metadata(
            object_type=object_type, object_id=object_id, view_id=view_id
        )

    # Check error message
    assert "object_type must be one of" in str(excinfo.value)


def test_get_object_metadata_not_found():
    """Test get_object_metadata when object is not found."""
    with requests_mock.Mocker() as m:
        # Arrange
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = "non_existent_id"
        view_id = str(uuid.uuid4())
        object_type = "assets"

        mock_address = MetadataSpec.gen_url(
            f"{object_type}/{object_id}/views/{view_id}/"
        )
        m.get(mock_address, status_code=404, json={"error": "Not found"})

        # Act
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().get_object_metadata(
            object_type=object_type, object_id=object_id, view_id=view_id
        )

        # Assert
        assert not response.response.ok
        assert response.response.status_code == 404
        assert response.data is None


def test_get_object_metadata_intercept_404():
    """Test get_object_metadata with 404 interception."""
    with requests_mock.Mocker() as m:
        # Arrange
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = str(uuid.uuid4())
        view_id = str(uuid.uuid4())
        object_type = "assets"

        mv = MetadataValues(
            {
                "default_field": FieldValues(
                    field_values=[FieldValue(value="default_value")]
                )
            }
        )

        default_model = ViewMetadata(metadata_values=mv)

        mock_address = MetadataSpec.gen_url(
            f"{object_type}/{object_id}/views/{view_id}/"
        )
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
        assert response.data == default_model
        assert "default_field" in response.data.metadata_values

        # Test that raise_for_status is disabled
        response.response.raise_for_status()  # Should not raise exception

        # Test that we can still access the original raise_for_status_404
        with pytest.raises(Exception):
            response.response.raise_for_status_404()


def test_get_object_metadata_direct():
    """Test retrieving metadata directly for an object."""
    with requests_mock.Mocker() as m:
        # Arrange
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = str(uuid.uuid4())
        object_type = "assets"

        mv = MetadataValues(
            {
                "direct_field": FieldValues(
                    field_values=[FieldValue(value="direct_value")]
                )
            }
        )

        model = ViewMetadata(
            metadata_values=mv, object_id=object_id, object_type=object_type
        )

        data = model.model_dump()
        mock_address = MetadataSpec.gen_url(f"{object_type}/{object_id}/")

        m.get(mock_address, json=data)

        # Act
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().get_object_metadata_direct(
            object_type=object_type, object_id=object_id
        )

        # Assert
        assert response.response.ok
        assert response.data.object_id == object_id
        assert response.data.object_type == object_type
        assert response.data.metadata_values is not None
        assert "direct_field" in response.data.metadata_values
        assert (
            response.data.metadata_values["direct_field"].field_values[0].value
            == "direct_value"
        )


def test_get_object_metadata_direct_invalid_type():
    """Test get_object_metadata_direct with an invalid object type."""
    # Arrange
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    object_id = str(uuid.uuid4())
    object_type = "invalid_type"

    # Act & Assert
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
    with pytest.raises(ValueError) as excinfo:
        client.metadata().get_object_metadata_direct(
            object_type=object_type, object_id=object_id
        )

    # Check error message
    assert "object_type must be one of" in str(excinfo.value)


def test_get_object_metadata_direct_not_found():
    """Test get_object_metadata_direct when object is not found."""
    with requests_mock.Mocker() as m:
        # Arrange
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = "non_existent_id"
        object_type = "assets"

        mock_address = MetadataSpec.gen_url(f"{object_type}/{object_id}/")
        m.get(mock_address, status_code=404, json={"error": "Not found"})

        # Act
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().get_object_metadata_direct(
            object_type=object_type, object_id=object_id
        )

        # Assert
        assert not response.response.ok
        assert response.response.status_code == 404
        assert response.data is None


def test_get_object_metadata_direct_intercept_404():
    """Test get_object_metadata_direct with 404 interception."""
    with requests_mock.Mocker() as m:
        # Arrange
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = str(uuid.uuid4())
        object_type = "assets"

        mv = MetadataValues(
            {
                "default_direct_field": FieldValues(
                    field_values=[FieldValue(value="default_direct_value")]
                )
            }
        )

        default_model = ViewMetadata(metadata_values=mv)

        mock_address = MetadataSpec.gen_url(f"{object_type}/{object_id}/")
        m.get(mock_address, status_code=404, json={"error": "Not found"})

        # Act
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().get_object_metadata_direct(
            object_type=object_type, object_id=object_id, intercept_404=default_model
        )

        # Assert
        assert response.data == default_model
        assert "default_direct_field" in response.data.metadata_values

        # Test that raise_for_status is disabled
        response.response.raise_for_status()  # Should not raise exception

        # Test that we can still access the original raise_for_status_404
        with pytest.raises(Exception):
            response.response.raise_for_status_404()


def test_get_object_metadata_collections_direct():
    """Test retrieving metadata directly for a collection object."""
    with requests_mock.Mocker() as m:
        # Arrange
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = str(uuid.uuid4())
        object_type = "collections"

        model = ViewMetadata(
            metadata_values=MetadataValues(
                {
                    "collection_direct_field": FieldValues(
                        field_values=[FieldValue(value="collection_direct_value")]
                    )
                }
            ),
            object_id=object_id,
            object_type=object_type,
        )

        data = model.model_dump()
        mock_address = MetadataSpec.gen_url(f"{object_type}/{object_id}/")

        m.get(mock_address, json=data)

        # Act
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().get_object_metadata_direct(
            object_type=object_type, object_id=object_id
        )

        # Assert
        assert response.response.ok
        assert response.data.object_id == object_id
        assert response.data.object_type == object_type
        assert response.data.metadata_values is not None
        assert "collection_direct_field" in response.data.metadata_values
        assert (
            response.data.metadata_values["collection_direct_field"]
            .field_values[0]
            .value
            == "collection_direct_value"
        )


def test_get_object_metadata_segments_direct():
    """Test retrieving metadata directly for a segment object."""
    with requests_mock.Mocker() as m:
        # Arrange
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = str(uuid.uuid4())
        object_type = "segments"

        model = ViewMetadata(
            metadata_values=MetadataValues(
                {
                    "segment_direct_field": FieldValues(
                        field_values=[FieldValue(value="segment_direct_value")]
                    )
                }
            ),
            object_id=object_id,
            object_type=object_type,
        )

        data = model.model_dump()
        mock_address = MetadataSpec.gen_url(f"{object_type}/{object_id}/")

        m.get(mock_address, json=data)

        # Act
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().get_object_metadata_direct(
            object_type=object_type, object_id=object_id
        )

        # Assert
        assert response.response.ok
        assert response.data.object_id == object_id
        assert response.data.object_type == object_type
        assert response.data.metadata_values is not None
        assert "segment_direct_field" in response.data.metadata_values
        assert (
            response.data.metadata_values["segment_direct_field"].field_values[0].value
            == "segment_direct_value"
        )
