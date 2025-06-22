import uuid
import requests_mock
import pytest
from typing import Literal

from pythonik.client import PythonikClient
from pythonik.models.base import PaginatedResponse
from pythonik.models.files.file import File, FileType, FileStatus


def test_create_storage_file():
    """Test creating a file directly on storage without associating it to an asset."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        storage_id = str(uuid.uuid4())
        file_name = f"test_file_{str(uuid.uuid4())[:8]}.mp4"

        # Prepare file model
        model = File(
            size=1024000,
            name=file_name,
            original_name=file_name,
            type=FileType.FILE,
            status=FileStatus.CLOSED,
        )

        # Mock response for paginated response
        response_data = {
            "objects": [model.model_dump()],
            "total": 1,
            "page": 1,
            "pages": 1,
            "per_page": 25,
        }

        mock_address = (
            f"https://app.iconik.io/API/files/v1/storages/{storage_id}/files/"
        )
        m.post(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.files().create_storage_file(storage_id, body=model)

        # Verify response
        assert m.called
        assert result.response.ok
        assert isinstance(result.data, PaginatedResponse)
        assert len(result.data.objects) == 1
        assert result.data.total == 1


def test_fetch_asset_format_components():
    """Test fetching components for a format in an asset."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        format_id = str(uuid.uuid4())

        # Mock response
        response_data = {
            "objects": [
                {
                    "id": str(uuid.uuid4()),
                    "name": "Component 1",
                    "type": "video",
                    "metadata": {"codec": "h264"},
                },
                {
                    "id": str(uuid.uuid4()),
                    "name": "Component 2",
                    "type": "audio",
                    "metadata": {"codec": "aac"},
                },
            ],
            "total": 2,
            "page": 1,
            "pages": 1,
            "per_page": 25,
        }

        mock_address = f"https://app.iconik.io/API/files/v1/assets/{asset_id}/formats/{format_id}/components/"
        m.get(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.files().list_asset_format_components(asset_id, format_id)

        # Verify response
        assert m.called
        assert result.response.ok
        assert isinstance(result.data, PaginatedResponse)
        assert len(result.data.objects) == 2
        assert result.data.total == 2


def test_fetch_storage_files():
    """Test fetching files from storage."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        storage_id = str(uuid.uuid4())

        # Mock response
        response_data = {
            "objects": [
                {
                    "id": str(uuid.uuid4()),
                    "name": "file1.mp4",
                    "size": 1024000,
                    "type": "FILE",
                    "status": "CLOSED",
                },
                {
                    "id": str(uuid.uuid4()),
                    "name": "file2.jpg",
                    "size": 256000,
                    "type": "FILE",
                    "status": "CLOSED",
                },
            ],
            "total": 2,
            "page": 1,
            "pages": 1,
            "per_page": 25,
        }

        mock_address = (
            f"https://app.iconik.io/API/files/v1/storages/{storage_id}/files/"
        )
        m.get(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.files().list_storage_files(storage_id)

        # Verify response
        assert m.called
        assert result.response.ok
        assert isinstance(result.data, PaginatedResponse)
        assert len(result.data.objects) == 2
        assert result.data.total == 2


def test_get_deleted_object_type_internal():
    """Test the internal _get_deleted_object_type method with invalid input."""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

    # Test with invalid object type
    with pytest.raises(ValueError) as excinfo:
        client.files()._get_deleted_object_type("invalid_type")

    assert "object_type must be one of file_sets or formats" in str(excinfo.value)


def test_get_deleted_file_sets():
    """Test fetching deleted file sets."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())

        # Mock response
        response_data = {
            "deleted_file_sets": [
                {
                    "id": str(uuid.uuid4()),
                    "asset_id": str(uuid.uuid4()),
                    "name": "Deleted File Set 1",
                    "date_deleted": "2023-01-01T12:00:00Z",
                },
                {
                    "id": str(uuid.uuid4()),
                    "asset_id": str(uuid.uuid4()),
                    "name": "Deleted File Set 2",
                    "date_deleted": "2023-01-02T12:00:00Z",
                },
            ]
        }

        mock_address = "https://app.iconik.io/API/files/v1/delete_queue/file_sets/"
        m.get(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

        # Test main method
        result = client.files().get_deleted_file_sets()
        assert m.called
        assert result.response.ok
        # Since the method uses parse_response(resp, None), the data field will be None
        # Instead, check the raw response json
        assert result.response.json() == response_data

        # Reset mock and test alias
        m.reset()
        m.get(mock_address, json=response_data)
        result_alias = client.files().get_deleted_filesets()
        assert m.called
        assert result_alias.response.ok
        assert result_alias.response.json() == response_data


def test_get_deleted_formats():
    """Test fetching deleted formats."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())

        # Mock response
        response_data = {
            "deleted_formats": [
                {
                    "id": str(uuid.uuid4()),
                    "asset_id": str(uuid.uuid4()),
                    "name": "Deleted Format 1",
                    "date_deleted": "2023-01-01T12:00:00Z",
                },
                {
                    "id": str(uuid.uuid4()),
                    "asset_id": str(uuid.uuid4()),
                    "name": "Deleted Format 2",
                    "date_deleted": "2023-01-02T12:00:00Z",
                },
            ]
        }

        mock_address = "https://app.iconik.io/API/files/v1/delete_queue/formats/"
        m.get(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.files().get_deleted_formats()

        # Verify response
        assert m.called
        assert result.response.ok
        # Since the method uses parse_response(resp, None), the data field will be None
        # Instead, check the raw response json
        assert result.response.json() == response_data


def test_create_mediainfo_job():
    """Test creating a mediainfo job."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        file_id = str(uuid.uuid4())

        # Mock response
        response_data = {
            "job_id": str(uuid.uuid4()),
            "status": "CREATED",
            "message": "Mediainfo job created successfully",
        }

        # Expected request body
        expected_body = {"priority": 7}

        mock_address = f"https://app.iconik.io/API/files/v1/assets/{asset_id}/files/{file_id}/mediainfo"
        m.post(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.files().create_mediainfo_job(asset_id, file_id, priority=7)

        # Verify response and request
        assert m.called
        assert result.response.ok
        # Since the method uses parse_response(resp, None), the data field will be None
        # Instead, check the raw response json
        assert result.response.json() == response_data
        assert m.last_request.json() == expected_body


def test_create_transcode_job():
    """Test creating a transcode job."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        file_id = str(uuid.uuid4())

        # Mock response
        response_data = {
            "job_id": str(uuid.uuid4()),
            "status": "CREATED",
            "message": "Transcode job created successfully",
        }

        # Expected request body with default priority
        expected_body = {"priority": 5}

        mock_address = f"https://app.iconik.io/API/files/v1/assets/{asset_id}/files/{file_id}/keyframes"
        m.post(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.files().create_transcode_job(asset_id, file_id)

        # Verify response and request
        assert m.called
        assert result.response.ok
        # Since the method uses parse_response(resp, None), the data field will be None
        # Instead, check the raw response json
        assert result.response.json() == response_data
        assert m.last_request.json() == expected_body


def test_alternate_base_url():
    """Test that all new methods respect the base_url parameter."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        alternate_base = "https://custom.iconik.io"

        # Test parameters
        storage_id = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        format_id = str(uuid.uuid4())
        file_id = str(uuid.uuid4())

        # Mock responses - simple empty responses are sufficient for this test
        storage_file_response = {
            "objects": [],
            "total": 0,
            "page": 1,
            "pages": 1,
            "per_page": 25,
        }
        format_components_response = {
            "objects": [],
            "total": 0,
            "page": 1,
            "pages": 1,
            "per_page": 25,
        }
        storage_files_response = {
            "objects": [],
            "total": 0,
            "page": 1,
            "pages": 1,
            "per_page": 25,
        }
        deleted_file_sets_response = {"deleted_file_sets": []}
        deleted_formats_response = {"deleted_formats": []}
        job_response = {"job_id": str(uuid.uuid4()), "status": "CREATED"}

        # Register mock responses with alternate base URL
        m.post(
            f"{alternate_base}/API/files/v1/storages/{storage_id}/files/",
            json=storage_file_response,
        )
        m.get(
            f"{alternate_base}/API/files/v1/assets/{asset_id}/formats/{format_id}/components/",
            json=format_components_response,
        )
        m.get(
            f"{alternate_base}/API/files/v1/storages/{storage_id}/files/",
            json=storage_files_response,
        )
        m.get(
            f"{alternate_base}/API/files/v1/delete_queue/file_sets/",
            json=deleted_file_sets_response,
        )
        m.get(
            f"{alternate_base}/API/files/v1/delete_queue/formats/",
            json=deleted_formats_response,
        )
        m.post(
            f"{alternate_base}/API/files/v1/assets/{asset_id}/files/{file_id}/mediainfo",
            json=job_response,
        )
        m.post(
            f"{alternate_base}/API/files/v1/assets/{asset_id}/files/{file_id}/keyframes",
            json=job_response,
        )

        # Initialize client with alternate base URL
        client = PythonikClient(
            app_id=app_id, auth_token=auth_token, timeout=3, base_url=alternate_base
        )
        files_spec = client.files()

        # Test all methods to ensure they use the alternate base URL
        file_model = File(
            name="test.mp4",
            original_name="test.mp4",
            size=1024,
            type=FileType.FILE,
            status=FileStatus.CLOSED,
        )
        files_spec.create_storage_file(storage_id, body=file_model)
        files_spec.list_asset_format_components(asset_id, format_id)
        files_spec.list_storage_files(storage_id)
        files_spec.get_deleted_file_sets()
        files_spec.get_deleted_formats()
        files_spec.create_mediainfo_job(asset_id, file_id)
        files_spec.create_transcode_job(asset_id, file_id)

        # Verify that all mocks were called
        assert m.call_count == 7, f"Expected 7 calls, got {m.call_count}"

        # Verify each mock individually to better diagnose which one failed
        assert (
            m.request_history[0].url
            == f"{alternate_base}/API/files/v1/storages/{storage_id}/files/"
        )
        assert (
            m.request_history[1].url
            == f"{alternate_base}/API/files/v1/assets/{asset_id}/formats/{format_id}/components/"
        )
        assert (
            m.request_history[2].url
            == f"{alternate_base}/API/files/v1/storages/{storage_id}/files/"
        )
        assert (
            m.request_history[3].url
            == f"{alternate_base}/API/files/v1/delete_queue/file_sets/"
        )
        assert (
            m.request_history[4].url
            == f"{alternate_base}/API/files/v1/delete_queue/formats/"
        )
        assert (
            m.request_history[5].url
            == f"{alternate_base}/API/files/v1/assets/{asset_id}/files/{file_id}/mediainfo"
        )
        assert (
            m.request_history[6].url
            == f"{alternate_base}/API/files/v1/assets/{asset_id}/files/{file_id}/keyframes"
        )
