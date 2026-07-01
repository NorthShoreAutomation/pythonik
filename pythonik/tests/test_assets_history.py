# pythonik/tests/test_assets_history.py
import uuid
import requests_mock

from pythonik.client import PythonikClient
from pythonik.models.base import PaginatedResponse, HistoryOperationType
from pythonik.specs.assets import AssetSpec


def test_list_all():
    """Test fetching a list of assets."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())

        # Mock response data structure
        response_data = {
            "objects": [
                {"id": str(uuid.uuid4()), "title": "Test Asset 1", "status": "ACTIVE"},
                {"id": str(uuid.uuid4()), "title": "Test Asset 2", "status": "ACTIVE"},
            ],
            "page": 1,
            "pages": 1,
            "per_page": 2,
            "total": 2,
        }

        # Setup mock endpoint
        mock_address = AssetSpec.gen_url("assets/")
        m.get(mock_address, json=response_data)

        # Create client and call the method
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.assets().list_all()

        # Verify response
        assert result.response.ok
        assert isinstance(result.data, PaginatedResponse)
        assert len(result.data.objects) == 2
        assert result.data.page == 1
        assert result.data.pages == 1
        assert result.data.total == 2


def test_list_all_with_params():
    """Test fetching a list of assets with query parameters."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())

        # Mock response data
        response_data = {
            "objects": [
                {"id": str(uuid.uuid4()), "title": "Test Asset 1", "status": "ACTIVE"}
            ],
            "page": 1,
            "pages": 1,
            "per_page": 1,
            "total": 1,
        }

        # Setup mock endpoint with params matcher
        mock_address = AssetSpec.gen_url("assets/")
        m.get(
            mock_address,
            json=response_data,
            # Add request matcher to ensure params are passed correctly
            additional_matcher=lambda req: req.qs == {"page": ["1"], "per_page": ["1"]},
        )

        # Create client and call method with params
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        params = {"page": 1, "per_page": 1}
        result = client.assets().list_all(params=params)

        # Verify response
        assert result.response.ok
        assert isinstance(result.data, PaginatedResponse)
        assert len(result.data.objects) == 1


def test_list_asset_history_entities():
    """Test fetching history entities for an asset."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())

        # Mock response data
        response_data = {
            "objects": [
                {
                    "id": str(uuid.uuid4()),
                    "operation_type": "METADATA",
                    "operation_description": "Updated metadata",
                    "date_created": "2025-05-13T10:00:00Z",
                    "created_by_user": "user123",
                },
                {
                    "id": str(uuid.uuid4()),
                    "operation_type": "VERSION_CREATE",
                    "operation_description": "Created new version",
                    "date_created": "2025-05-12T15:30:00Z",
                    "created_by_user": "user123",
                },
            ],
            "page": 1,
            "pages": 1,
            "per_page": 10,
            "total": 2,
        }

        # Setup mock endpoint
        mock_address = AssetSpec.gen_url(f"assets/{asset_id}/history/")
        m.get(mock_address, json=response_data)

        # Create client and call the method
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.assets().list_asset_history_entities(asset_id)

        # Verify response
        assert result.response.ok
        assert isinstance(result.data, PaginatedResponse)
        assert len(result.data.objects) == 2
        assert result.data.objects[0]["operation_type"] == "METADATA"
        assert result.data.objects[1]["operation_type"] == "VERSION_CREATE"


def test_create_history_entity():
    """Test creating a history entity for an asset."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        operation_description = "Test history entry"
        operation_type = "CUSTOM"

        # Setup mock endpoint
        mock_address = AssetSpec.gen_url(f"assets/{asset_id}/history/")
        m.post(mock_address, status_code=201)

        # Create client and call the method
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.assets().create_history_entity(
            asset_id=asset_id,
            operation_description=operation_description,
            operation_type=operation_type,
        )

        # Verify response
        assert result.response.ok
        assert result.response.status_code == 201

        # Verify the correct request body was sent
        assert m.last_request.json() == {
            "operation_description": operation_description,
            "operation_type": operation_type,
        }


def test_create_history_entity_accepts_enum():
    """Passing a HistoryOperationType enum sends its string value."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        operation_description = "Created new version"

        mock_address = AssetSpec.gen_url(f"assets/{asset_id}/history/")
        m.post(mock_address, status_code=201)

        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.assets().create_history_entity(
            asset_id=asset_id,
            operation_description=operation_description,
            operation_type=HistoryOperationType.VERSION_CREATE,
        )

        assert result.response.ok
        # Enum is serialized to its plain string value in the request body.
        assert m.last_request.json() == {
            "operation_description": operation_description,
            "operation_type": "VERSION_CREATE",
        }


def test_create_history_entity_accepts_arbitrary_string():
    """Unknown operation types are accepted (API may add new ones)."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        operation_description = "Some brand new operation"
        operation_type = "SOME_FUTURE_OPERATION"

        mock_address = AssetSpec.gen_url(f"assets/{asset_id}/history/")
        m.post(mock_address, status_code=201)

        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.assets().create_history_entity(
            asset_id=asset_id,
            operation_description=operation_description,
            operation_type=operation_type,
        )

        assert result.response.ok
        assert m.last_request.json() == {
            "operation_description": operation_description,
            "operation_type": operation_type,
        }
