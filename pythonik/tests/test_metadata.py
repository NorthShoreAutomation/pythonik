import uuid
import requests_mock
from pythonik.client import PythonikClient
from requests import HTTPError
from pythonik.models.base import ObjectType
from loguru import logger
import json

from pythonik.models.metadata.views import (
    FieldValue,
    FieldValues,
    MetadataValues,
    ViewMetadata,
    CreateViewRequest,
    ViewField,
    ViewOption,
    UpdateViewRequest,
)
from pythonik.models.mutation.metadata.mutate import (
    UpdateMetadata,
    UpdateMetadataResponse,
)
from pythonik.models.metadata.view_responses import ViewResponse, ViewListResponse
from pythonik.specs.metadata import (
    ASSET_METADATA_FROM_VIEW_PATH,
    UPDATE_ASSET_METADATA,
    MetadataSpec,
    ASSET_OBJECT_VIEW_PATH,
    PUT_METADATA_DIRECT_PATH,
    CREATE_VIEW_PATH,
    VIEWS_BASE,
    UPDATE_VIEW_PATH,
    DELETE_VIEW_PATH,
    GET_VIEW_PATH,
    FIELDS_BASE_PATH,
    FIELD_BY_NAME_PATH,
)

from pythonik.models.metadata.fields import (
    FieldCreate,
    FieldUpdate,
    FieldOption,
    FieldResponse,
)
import pytest
from pythonik.models.metadata.fields import IconikFieldType
from pydantic import ValidationError


def test_get_asset_metadata():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        model = ViewMetadata()
        data = model.model_dump()

        # OLD - Using the constant:
        # mock_address = MetadataSpec.gen_url(
        #     ASSET_METADATA_FROM_VIEW_PATH.format(asset_id, view_id)
        # )

        # NEW - Using the same format as the implementation:
        mock_address = f"{MetadataSpec.base_url}/API/metadata/v1/assets/{asset_id}/views/{view_id}/"

        m.get(mock_address, json=data)
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        client.metadata().get_asset_metadata(asset_id, view_id)


def test_get_asset_intercept_404():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        mv = MetadataValues(
            {
                "this_worked_right?": FieldValues(
                    field_values=[FieldValue(value="lets hope")]
                )
            }
        )

        model = ViewMetadata()
        model.metadata_values = mv
        data = model.model_dump()

        # OLD - Using the constant:
        # mock_address = MetadataSpec.gen_url(
        #     ASSET_METADATA_FROM_VIEW_PATH.format(asset_id, view_id)
        # )

        # NEW - Using the same format as the implementation:
        mock_address = f"{MetadataSpec.base_url}/API/metadata/v1/assets/{asset_id}/views/{view_id}/"

        m.get(mock_address, json=data, status_code=404)
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        resp = client.metadata().get_asset_metadata(
            asset_id, view_id, intercept_404=model
        )
        assert resp.data == model


def test_get_asset_intercept_404_raise_for_status():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        mv = MetadataValues(
            {
                "this_worked_right?": FieldValues(
                    field_values=[FieldValue(value="lets hope")]
                )
            }
        )

        model = ViewMetadata()
        model.metadata_values = mv
        data = model.model_dump()

        # OLD - Using the constant:
        # mock_address = MetadataSpec.gen_url(
        #     ASSET_METADATA_FROM_VIEW_PATH.format(asset_id, view_id)
        # )

        # NEW - Using the same format as the implementation:
        mock_address = f"{MetadataSpec.base_url}/API/metadata/v1/assets/{asset_id}/views/{view_id}/"

        m.get(mock_address, json=data, status_code=404)
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        resp = client.metadata().get_asset_metadata(
            asset_id, view_id, intercept_404=model
        )
        # should not raise for status
        try:
            resp.response.raise_for_status()
            # this line should run and the above should not raise for status
            assert True is True
        except Exception as e:
            pass


def test_get_asset_intercept_404_raise_for_status_404():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        mv = MetadataValues(
            {
                "this_worked_right?": FieldValues(
                    field_values=[FieldValue(value="lets hope")]
                )
            }
        )

        model = ViewMetadata()
        model.metadata_values = mv
        data = model.model_dump()

        # OLD - Using the constant:
        # mock_address = MetadataSpec.gen_url(
        #     ASSET_METADATA_FROM_VIEW_PATH.format(asset_id, view_id)
        # )

        # NEW - Using the same format as the implementation:
        mock_address = f"{MetadataSpec.base_url}/API/metadata/v1/assets/{asset_id}/views/{view_id}/"

        m.get(mock_address, json=data, status_code=404)
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        resp = client.metadata().get_asset_metadata(
            asset_id, view_id, intercept_404=model
        )
        # should not raise for status
        exception = None
        try:
            resp.response.raise_for_status_404()
            # this line should run and the above should not raise for status
        except HTTPError as e:
            exception = e

        # assert exception still raised with 404
        assert exception.response.status_code == 404


def test_update_asset_metadata():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        view_id = str(uuid.uuid4())
        payload = {"metadata_values": {"field1": {"field_values": [{"value": "123"}]}}}

        mutate_model = UpdateMetadata.model_validate(payload)
        response_model = UpdateMetadataResponse(
            metadata_values=mutate_model.metadata_values.model_dump()
        )

        mock_address = MetadataSpec.gen_url(
            UPDATE_ASSET_METADATA.format(asset_id, view_id)
        )
        m.put(mock_address, json=response_model.model_dump())
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        client.metadata().update_asset_metadata(asset_id, view_id, mutate_model)


def test_put_segment_view_metadata():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        segment_id = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        # Create test payload
        payload = {"metadata_values": {"field1": {"field_values": [{"value": "123"}]}}}

        mutate_model = UpdateMetadata.model_validate(payload)
        response_model = UpdateMetadataResponse(
            metadata_values=mutate_model.metadata_values.model_dump()
        )

        # Mock the endpoint using the ASSET_OBJECT_VIEW_PATH
        mock_address = MetadataSpec.gen_url(
            ASSET_OBJECT_VIEW_PATH.format(asset_id, "segments", segment_id, view_id)
        )
        m.put(mock_address, json=response_model.model_dump())

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        client.metadata().put_segment_view_metadata(
            asset_id, segment_id, view_id, mutate_model
        )


def test_put_metadata_direct():
    """Test direct metadata update without a view."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_type = ObjectType.ASSETS.value
        object_id = str(uuid.uuid4())

        # Create test metadata
        metadata_values = {
            "metadata_values": {
                "test_field": {"field_values": [{"value": "test_value"}]}
            }
        }
        metadata = UpdateMetadata.model_validate(metadata_values)

        # Expected response
        response_data = {
            "date_created": "2024-12-10T19:58:25Z",
            "date_modified": "2024-12-10T19:58:25Z",
            "metadata_values": metadata_values["metadata_values"],
            "object_id": object_id,
            "object_type": object_type,
            "version_id": str(uuid.uuid4()),
        }

        # Mock the PUT request
        mock_address = MetadataSpec.gen_url(
            PUT_METADATA_DIRECT_PATH.format(object_type, object_id)
        )
        m.put(mock_address, json=response_data)

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().put_metadata_direct(
            object_type, object_id, metadata
        )

        # Verify response
        assert response.response.ok
        assert response.data.object_id == object_id
        assert response.data.object_type == object_type
        assert response.data.metadata_values == metadata_values["metadata_values"]


def test_put_metadata_direct_unauthorized():
    """Test direct metadata update with invalid token."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = "invalid_token"
        object_type = ObjectType.ASSETS.value
        object_id = str(uuid.uuid4())

        # Create empty metadata
        metadata = UpdateMetadata.model_validate({"metadata_values": {}})

        # Mock the PUT request to return 401
        mock_address = MetadataSpec.gen_url(
            PUT_METADATA_DIRECT_PATH.format(object_type, object_id)
        )
        m.put(mock_address, status_code=401)

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().put_metadata_direct(
            object_type, object_id, metadata
        )

        # Verify response
        assert not response.response.ok
        assert response.response.status_code == 401


def test_put_metadata_direct_404():
    """Test direct metadata update with non-existent object."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_type = ObjectType.ASSETS.value
        object_id = str(uuid.uuid4())

        # Create test metadata
        metadata = UpdateMetadata.model_validate({"metadata_values": {}})

        # Mock the PUT request to return 404
        mock_address = MetadataSpec.gen_url(
            PUT_METADATA_DIRECT_PATH.format(object_type, object_id)
        )
        m.put(
            mock_address,
            status_code=404,
            json={
                "error": "Object not found",
                "message": f"Object {object_id} of type {object_type} not found",
            },
        )

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().put_metadata_direct(
            object_type, object_id, metadata
        )

        # Verify response
        assert not response.response.ok
        assert response.response.status_code == 404


def test_put_metadata_direct_invalid_format():
    """Test direct metadata update with invalid metadata format."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_type = ObjectType.ASSETS.value
        object_id = str(uuid.uuid4())

        # Create test metadata with invalid format
        metadata_values = {
            "metadata_values": {
                "test_field": {
                    # Missing required field_values array
                    "value": "test_value"
                }
            }
        }
        metadata = UpdateMetadata.model_validate({"metadata_values": {}})

        # Mock the PUT request to return 400
        mock_address = MetadataSpec.gen_url(
            PUT_METADATA_DIRECT_PATH.format(object_type, object_id)
        )
        m.put(
            mock_address,
            status_code=400,
            json={
                "error": "Invalid metadata format",
                "message": "Metadata values must contain field_values array",
            },
        )

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().put_metadata_direct(
            object_type, object_id, metadata
        )

        # Verify response
        assert not response.response.ok
        assert response.response.status_code == 400


def test_put_metadata_direct_malformed():
    """Test direct metadata update with malformed request."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_type = "invalid_type"  # Invalid object type
        object_id = str(uuid.uuid4())

        # Create test metadata
        metadata = UpdateMetadata.model_validate({"metadata_values": {}})

        # Mock the PUT request to return 400
        mock_address = MetadataSpec.gen_url(
            PUT_METADATA_DIRECT_PATH.format(object_type, object_id)
        )
        m.put(
            mock_address,
            status_code=400,
            json={
                "error": "Invalid request",
                "message": "Invalid object type: must be one of [assets, segments, collections]",
            },
        )

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().put_metadata_direct(
            object_type, object_id, metadata
        )

        # Verify response
        assert not response.response.ok
        assert response.response.status_code == 400


def test_put_metadata_direct_forbidden():
    """Test direct metadata update with non-admin user."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())  # Valid token but non-admin user
        object_type = ObjectType.ASSETS.value
        object_id = str(uuid.uuid4())

        # Create test metadata
        metadata = UpdateMetadata.model_validate({"metadata_values": {}})

        # Mock the PUT request to return 403
        mock_address = MetadataSpec.gen_url(
            PUT_METADATA_DIRECT_PATH.format(object_type, object_id)
        )
        m.put(
            mock_address,
            status_code=403,
            json={
                "error": "Forbidden",
                "message": "Admin access required for direct metadata updates",
            },
        )

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        response = client.metadata().put_metadata_direct(
            object_type, object_id, metadata
        )

        # Verify response
        assert not response.response.ok
        assert response.response.status_code == 403


def test_create_view():
    """Test creating a new view."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        # Create request data
        view = CreateViewRequest(
            name="Test View",
            description="A test view",
            view_fields=[
                ViewField(
                    name="field1",
                    label="Field 1",
                    required=True,
                    field_type="string",
                    options=[
                        ViewOption(label="Option 1", value="opt1"),
                        ViewOption(label="Option 2", value="opt2"),
                    ],
                )
            ],
        )

        # Create expected response
        response = ViewResponse(
            id=view_id,
            name=view.name,
            description=view.description,
            date_created="2024-12-20T18:40:03.279Z",
            date_modified="2024-12-20T18:40:03.279Z",
            view_fields=view.view_fields,
        )

        # Mock the API call
        mock_address = MetadataSpec.gen_url(CREATE_VIEW_PATH)
        m.post(mock_address, json=response.model_dump())

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().create_view(view)

        # Verify response
        assert result.response.ok
        assert result.data.id == view_id
        assert result.data.name == view.name
        assert result.data.description == view.description
        assert len(result.data.view_fields) == len(view.view_fields)
        assert result.data.view_fields[0].name == view.view_fields[0].name


def test_create_view_with_dict():
    """Test creating a new view using a dictionary."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        # Create request data as dict
        view = {
            "name": "Test View",
            "description": "A test view",
            "view_fields": [
                {
                    "name": "field1",
                    "label": "Field 1",
                    "required": True,
                    "field_type": "string",
                    "options": [
                        {"label": "Option 1", "value": "opt1"},
                        {"label": "Option 2", "value": "opt2"},
                    ],
                }
            ],
        }

        # Create expected response
        response = ViewResponse(
            id=view_id,
            name=view["name"],
            description=view["description"],
            date_created="2024-12-20T18:40:03.279Z",
            date_modified="2024-12-20T18:40:03.279Z",
            view_fields=[ViewField(**field) for field in view["view_fields"]],
        )

        # Mock the API call
        mock_address = MetadataSpec.gen_url(CREATE_VIEW_PATH)
        m.post(mock_address, json=response.model_dump())

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().create_view(view)

        # Verify response
        assert result.response.ok
        assert result.data.id == view_id
        assert result.data.name == view["name"]
        assert result.data.description == view["description"]
        assert len(result.data.view_fields) == len(view["view_fields"])
        assert result.data.view_fields[0].name == view["view_fields"][0]["name"]


def test_create_view_bad_request():
    """Test creating a view with invalid data."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())

        # Create invalid request (missing required fields)
        view = CreateViewRequest(
            name="Test View",
            view_fields=[],  # Invalid: view_fields cannot be empty
        )

        # Mock the API call with 400 response
        mock_address = MetadataSpec.gen_url(CREATE_VIEW_PATH)
        m.post(mock_address, status_code=400, json={"error": "Invalid view_fields"})

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().create_view(view)

        # Verify response
        assert not result.response.ok
        assert result.response.status_code == 400
        assert result.data is None


def test_create_view_unauthorized():
    """Test creating a view with invalid token."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = "invalid_token"

        view = CreateViewRequest(
            name="Test View",
            description="A test view",
            view_fields=[ViewField(name="field1", label="Field 1", required=True)],
        )

        # Mock the API call with 401 response
        mock_address = MetadataSpec.gen_url(CREATE_VIEW_PATH)
        m.post(mock_address, status_code=401, json={"error": "Invalid token"})

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().create_view(view)

        # Verify response
        assert not result.response.ok
        assert result.response.status_code == 401
        assert result.data is None


def test_get_views():
    """Test getting list of views."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        # Create expected response
        view = ViewResponse(
            id=view_id,
            name="Test View",
            description="A test view",
            date_created="2024-12-20T18:40:03.279Z",
            date_modified="2024-12-20T18:40:03.279Z",
            view_fields=[
                ViewField(
                    name="field1",
                    label="Field 1",
                    required=True,
                    field_type="string",
                    options=[
                        ViewOption(label="Option 1", value="opt1"),
                        ViewOption(label="Option 2", value="opt2"),
                    ],
                )
            ],
        )
        response = ViewListResponse(objects=[view], page=1, pages=1, per_page=10)

        # Mock the API call
        mock_address = MetadataSpec.gen_url(VIEWS_BASE)
        m.get(mock_address, json=response.model_dump())

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().get_views()

        # Verify response
        assert result.response.ok
        assert len(result.data.objects) == 1
        assert result.data.objects[0].id == view_id
        assert result.data.objects[0].name == view.name
        assert result.data.objects[0].description == view.description
        assert len(result.data.objects[0].view_fields) == len(view.view_fields)
        assert result.data.objects[0].view_fields[0].name == view.view_fields[0].name
        assert result.data.page == 1
        assert result.data.pages == 1
        assert result.data.per_page == 10


def test_get_views_unauthorized():
    """Test getting views with invalid token."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = "invalid_token"

        # Mock the API call with 401 response
        mock_address = MetadataSpec.gen_url(VIEWS_BASE)
        m.get(mock_address, status_code=401, json={"error": "Invalid token"})

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().get_views()

        # Verify response
        assert not result.response.ok
        assert result.response.status_code == 401
        assert result.data is None


def test_get_views_empty():
    """Test getting empty list of views."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())

        # Create expected response with empty list
        response = ViewListResponse(objects=[], page=1, pages=1, per_page=10)

        # Mock the API call
        mock_address = MetadataSpec.gen_url(VIEWS_BASE)
        m.get(mock_address, json=response.model_dump())

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().get_views()

        # Verify response
        assert result.response.ok
        assert len(result.data.objects) == 0
        assert result.data.page == 1
        assert result.data.pages == 1
        assert result.data.per_page == 10


def test_get_views_with_missing_labels():
    """Test getting views where some ViewFields have no labels."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        # Create expected response with a mix of labeled and unlabeled fields
        view = ViewResponse(
            id=view_id,
            name="Test View",
            description="A test view with mixed label fields",
            date_created="2024-12-20T18:40:03.279Z",
            date_modified="2024-12-20T18:40:03.279Z",
            view_fields=[
                # Field with a label
                ViewField(
                    name="field1",
                    label="Field 1",
                    required=True,
                    field_type="string",
                ),
                # Field without a label
                ViewField(
                    name="field2",
                    required=False,
                    field_type="string",
                ),
                # Another field without a label but with options
                ViewField(
                    name="field3",
                    field_type="select",
                    options=[
                        ViewOption(label="Option 1", value="opt1"),
                        ViewOption(label="Option 2", value="opt2"),
                    ],
                ),
            ],
        )
        response = ViewListResponse(objects=[view], page=1, pages=1, per_page=10)

        # Mock the API call
        mock_address = MetadataSpec.gen_url(VIEWS_BASE)
        m.get(mock_address, json=response.model_dump())

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().get_views()

        # Verify response
        assert result.response.ok
        assert len(result.data.objects) == 1
        assert result.data.objects[0].id == view_id
        assert result.data.objects[0].name == view.name

        # Verify the fields were processed correctly
        view_fields = result.data.objects[0].view_fields
        assert len(view_fields) == 3

        # Field with label
        assert view_fields[0].name == "field1"
        assert view_fields[0].label == "Field 1"

        # Field without label should have None as the label value
        assert view_fields[1].name == "field2"
        assert view_fields[1].label is None

        # Another field without label but with options
        assert view_fields[2].name == "field3"
        assert view_fields[2].label is None
        assert len(view_fields[2].options) == 2


def test_update_view():
    """Test updating a view."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        # Create update request
        view = UpdateViewRequest(
            name="Updated View",
            description="An updated test view",
            view_fields=[
                ViewField(
                    name="field1",
                    label="Updated Field 1",
                    required=True,
                    field_type="string",
                    options=[
                        ViewOption(label="New Option 1", value="new1"),
                        ViewOption(label="New Option 2", value="new2"),
                    ],
                )
            ],
        )

        # Create expected response
        response = ViewResponse(
            id=view_id,
            name=view.name,
            description=view.description,
            date_created="2024-12-20T18:40:03.279Z",
            date_modified="2024-12-20T19:22:58.522Z",  # Note: modified time updated
            view_fields=view.view_fields,
        )

        # Mock the API call
        mock_address = MetadataSpec.gen_url(UPDATE_VIEW_PATH.format(view_id=view_id))
        m.patch(mock_address, json=response.model_dump())

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().update_view(view_id, view)

        # Verify response
        assert result.response.ok
        assert result.data.id == view_id
        assert result.data.name == view.name
        assert result.data.description == view.description
        assert len(result.data.view_fields) == len(view.view_fields)
        assert result.data.view_fields[0].name == view.view_fields[0].name
        assert result.data.view_fields[0].label == view.view_fields[0].label


def test_update_view_with_dict():
    """Test updating a view using a dictionary."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        # Create update request as dict
        view = {
            "name": "Updated View",
            "description": "An updated test view",
            "view_fields": [
                {
                    "name": "field1",
                    "label": "Updated Field 1",
                    "required": True,
                    "field_type": "string",
                    "options": [
                        {"label": "New Option 1", "value": "new1"},
                        {"label": "New Option 2", "value": "new2"},
                    ],
                }
            ],
        }

        # Create expected response
        response = ViewResponse(
            id=view_id,
            name=view["name"],
            description=view["description"],
            date_created="2024-12-20T18:40:03.279Z",
            date_modified="2024-12-20T19:22:58.522Z",  # Note: modified time updated
            view_fields=[ViewField(**field) for field in view["view_fields"]],
        )

        # Mock the API call
        mock_address = MetadataSpec.gen_url(UPDATE_VIEW_PATH.format(view_id=view_id))
        m.patch(mock_address, json=response.model_dump())

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().update_view(view_id, view)

        # Verify response
        assert result.response.ok
        assert result.data.id == view_id
        assert result.data.name == view["name"]
        assert result.data.description == view["description"]
        assert len(result.data.view_fields) == len(view["view_fields"])
        assert result.data.view_fields[0].name == view["view_fields"][0]["name"]
        assert result.data.view_fields[0].label == view["view_fields"][0]["label"]


def test_update_view_not_found():
    """Test updating a non-existent view."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = "non_existent_id"

        view = UpdateViewRequest(
            name="Updated View", description="An updated test view"
        )

        # Mock the API call with 404 response
        mock_address = MetadataSpec.gen_url(UPDATE_VIEW_PATH.format(view_id=view_id))
        m.patch(mock_address, status_code=404, json={"error": "View not found"})

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().update_view(view_id, view)

        # Verify response
        assert not result.response.ok
        assert result.response.status_code == 404
        assert result.data is None


def test_update_view_unauthorized():
    """Test updating a view with invalid token."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = "invalid_token"
        view_id = str(uuid.uuid4())

        view = UpdateViewRequest(
            name="Updated View", description="An updated test view"
        )

        # Mock the API call with 401 response
        mock_address = MetadataSpec.gen_url(UPDATE_VIEW_PATH.format(view_id=view_id))
        m.patch(mock_address, status_code=401, json={"error": "Invalid token"})

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().update_view(view_id, view)

        # Verify response
        assert not result.response.ok
        assert result.response.status_code == 401
        assert result.data is None


def test_update_view_partial():
    """Test partial update of a view."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        # Create partial update request (only updating name)
        view = UpdateViewRequest(name="Updated View")

        # Create expected response (other fields unchanged)
        response = ViewResponse(
            id=view_id,
            name=view.name,
            description="Original description",  # Unchanged
            date_created="2024-12-20T18:40:03.279Z",
            date_modified="2024-12-20T19:22:58.522Z",  # Note: modified time updated
            view_fields=[  # Original fields unchanged
                ViewField(
                    name="field1", label="Field 1", required=True, field_type="string"
                )
            ],
        )

        # Mock the API call
        mock_address = MetadataSpec.gen_url(UPDATE_VIEW_PATH.format(view_id=view_id))
        m.patch(mock_address, json=response.model_dump())

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().update_view(view_id, view)

        # Verify response
        assert result.response.ok
        assert result.data.id == view_id
        assert result.data.name == view.name
        assert result.data.description == "Original description"  # Unchanged
        assert len(result.data.view_fields) == 1  # Original fields unchanged


def test_replace_view():
    """Test replacing a view."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        # Create replacement view data
        view = CreateViewRequest(
            name="Replaced View",
            description="A completely new view",
            view_fields=[
                ViewField(
                    name="new_field",
                    label="New Field",
                    required=True,
                    field_type="string",
                    options=[
                        ViewOption(label="New Option 1", value="new1"),
                        ViewOption(label="New Option 2", value="new2"),
                    ],
                )
            ],
        )

        # Create expected response
        response = ViewResponse(
            id=view_id,
            name=view.name,
            description=view.description,
            date_created="2024-12-20T18:40:03.279Z",
            date_modified="2024-12-20T19:28:42.213Z",  # Note: modified time updated
            view_fields=view.view_fields,
        )

        # Mock the API call
        mock_address = MetadataSpec.gen_url(UPDATE_VIEW_PATH.format(view_id=view_id))
        m.put(mock_address, json=response.model_dump())

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().replace_view(view_id, view)

        # Verify response
        assert result.response.ok
        assert result.data.id == view_id
        assert result.data.name == view.name
        assert result.data.description == view.description
        assert len(result.data.view_fields) == len(view.view_fields)
        assert result.data.view_fields[0].name == view.view_fields[0].name
        assert result.data.view_fields[0].label == view.view_fields[0].label


def test_replace_view_with_dict():
    """Test replacing a view using a dictionary."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        # Create replacement view data as dict
        view = {
            "name": "Replaced View",
            "description": "A completely new view",
            "view_fields": [
                {
                    "name": "new_field",
                    "label": "New Field",
                    "required": True,
                    "field_type": "string",
                    "options": [
                        {"label": "New Option 1", "value": "new1"},
                        {"label": "New Option 2", "value": "new2"},
                    ],
                }
            ],
        }

        # Create expected response
        response = ViewResponse(
            id=view_id,
            name=view["name"],
            description=view["description"],
            date_created="2024-12-20T18:40:03.279Z",
            date_modified="2024-12-20T19:28:42.213Z",  # Note: modified time updated
            view_fields=[ViewField(**field) for field in view["view_fields"]],
        )

        # Mock the API call
        mock_address = MetadataSpec.gen_url(UPDATE_VIEW_PATH.format(view_id=view_id))
        m.put(mock_address, json=response.model_dump())

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().replace_view(view_id, view)

        # Verify response
        assert result.response.ok
        assert result.data.id == view_id
        assert result.data.name == view["name"]
        assert result.data.description == view["description"]
        assert len(result.data.view_fields) == len(view["view_fields"])
        assert result.data.view_fields[0].name == view["view_fields"][0]["name"]
        assert result.data.view_fields[0].label == view["view_fields"][0]["label"]


def test_replace_view_not_found():
    """Test replacing a non-existent view."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = "non_existent_id"

        view = CreateViewRequest(
            name="Replaced View",
            description="A completely new view",
            view_fields=[ViewField(name="new_field", label="New Field", required=True)],
        )

        # Mock the API call with 404 response
        mock_address = MetadataSpec.gen_url(UPDATE_VIEW_PATH.format(view_id=view_id))
        m.put(mock_address, status_code=404, json={"error": "View not found"})

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().replace_view(view_id, view)

        # Verify response
        assert not result.response.ok
        assert result.response.status_code == 404
        assert result.data is None


def test_replace_view_unauthorized():
    """Test replacing a view with invalid token."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = "invalid_token"
        view_id = str(uuid.uuid4())

        view = CreateViewRequest(
            name="Replaced View",
            description="A completely new view",
            view_fields=[ViewField(name="new_field", label="New Field", required=True)],
        )

        # Mock the API call with 401 response
        mock_address = MetadataSpec.gen_url(UPDATE_VIEW_PATH.format(view_id=view_id))
        m.put(mock_address, status_code=401, json={"error": "Invalid token"})

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().replace_view(view_id, view)

        # Verify response
        assert not result.response.ok
        assert result.response.status_code == 401
        assert result.data is None


def test_replace_view_bad_request():
    """Test replacing a view with invalid data."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        # Create invalid request (missing required fields) as dict
        view = {
            "name": "Replaced View"  # Missing required view_fields
        }

        # Mock the API call with 400 response
        mock_address = MetadataSpec.gen_url(UPDATE_VIEW_PATH.format(view_id=view_id))
        m.put(mock_address, status_code=400, json={"error": "Missing required fields"})

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().replace_view(view_id, view)

        # Verify response
        assert not result.response.ok
        assert result.response.status_code == 400
        assert result.data is None


def test_delete_view():
    """Test deleting a view."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        # Mock the API call
        mock_address = MetadataSpec.gen_url(DELETE_VIEW_PATH.format(view_id=view_id))
        m.delete(mock_address, status_code=204)

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().delete_view(view_id)

        # Verify response
        assert result.response.ok
        assert result.response.status_code == 204
        assert result.data is None


def test_delete_view_not_found():
    """Test deleting a non-existent view."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = "non_existent_id"

        # Mock the API call with 404 response
        mock_address = MetadataSpec.gen_url(DELETE_VIEW_PATH.format(view_id=view_id))
        m.delete(mock_address, status_code=404, json={"error": "View not found"})

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().delete_view(view_id)

        # Verify response
        assert not result.response.ok
        assert result.response.status_code == 404
        assert result.data is None


def test_delete_view_unauthorized():
    """Test deleting a view with invalid token."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = "invalid_token"
        view_id = str(uuid.uuid4())

        # Mock the API call with 401 response
        mock_address = MetadataSpec.gen_url(DELETE_VIEW_PATH.format(view_id=view_id))
        m.delete(mock_address, status_code=401, json={"error": "Invalid token"})

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().delete_view(view_id)

        # Verify response
        assert not result.response.ok
        assert result.response.status_code == 401
        assert result.data is None


def test_delete_view_bad_request():
    """Test deleting a view with invalid request."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = "invalid!id@#$"  # Invalid ID format

        # Mock the API call with 400 response
        mock_address = MetadataSpec.gen_url(DELETE_VIEW_PATH.format(view_id=view_id))
        m.delete(
            mock_address, status_code=400, json={"error": "Invalid view ID format"}
        )

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().delete_view(view_id)

        # Verify response
        assert not result.response.ok
        assert result.response.status_code == 400
        assert result.data is None


def test_get_view():
    """Test getting a specific view."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        # Create expected response
        view = ViewResponse(
            id=view_id,
            name="Test View",
            description="A test view",
            date_created="2024-12-20T18:40:03.279Z",
            date_modified="2024-12-20T18:40:03.279Z",
            view_fields=[
                ViewField(
                    name="field1",
                    label="Field 1",
                    required=True,
                    field_type="string",
                    options=[
                        ViewOption(label="Option 1", value="opt1"),
                        ViewOption(label="Option 2", value="opt2"),
                    ],
                )
            ],
        )

        # Mock the API call
        mock_address = MetadataSpec.gen_url(GET_VIEW_PATH.format(view_id=view_id))
        m.get(mock_address, json=view.model_dump())

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().get_view(view_id)

        # Verify response
        assert result.response.ok
        assert result.data.id == view_id
        assert result.data.name == view.name
        assert result.data.description == view.description
        assert len(result.data.view_fields) == len(view.view_fields)
        assert result.data.view_fields[0].name == view.view_fields[0].name
        assert len(result.data.view_fields[0].options) == len(
            view.view_fields[0].options
        )


def test_get_view_not_found():
    """Test getting a non-existent view."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = "non_existent_id"

        # Mock the API call
        mock_address = MetadataSpec.gen_url(GET_VIEW_PATH.format(view_id=view_id))
        m.get(mock_address, status_code=404, json={"error": "View not found"})

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().get_view(view_id)

        # Verify response
        assert not result.response.ok
        assert result.response.status_code == 404
        assert result.data is None


def test_get_view_unauthorized():
    """Test getting a view with invalid token."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = "invalid_token"
        view_id = str(uuid.uuid4())

        # Mock the API call
        mock_address = MetadataSpec.gen_url(GET_VIEW_PATH.format(view_id=view_id))
        m.get(mock_address, status_code=401, json={"error": "Unauthorized"})

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().get_view(view_id)

        # Verify response
        assert not result.response.ok
        assert result.response.status_code == 401
        assert result.data is None


def test_get_view_with_merge_fields():
    """Test getting a view with merge_fields parameter."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = str(uuid.uuid4())

        # Create expected response
        view = ViewResponse(
            id=view_id,
            name="Test View",
            description="A test view",
            date_created="2024-12-20T18:40:03.279Z",
            date_modified="2024-12-20T18:40:03.279Z",
            view_fields=[
                ViewField(
                    name="field1",
                    label="Field 1",
                    required=True,
                    field_type="string",
                    options=[
                        ViewOption(label="Option 1", value="opt1"),
                        ViewOption(label="Option 2", value="opt2"),
                    ],
                )
            ],
        )

        # Mock the API call with merge_fields parameter
        mock_address = MetadataSpec.gen_url(GET_VIEW_PATH.format(view_id=view_id))
        m.get(f"{mock_address}?merge_fields=true", json=view.model_dump())

        # Make the request
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        result = client.metadata().get_view(view_id, merge_fields=True)

        # Verify response
        assert result.response.ok
        assert result.data.id == view_id
        assert result.data.name == view.name
        assert result.data.description == view.description
        assert len(result.data.view_fields) == len(view.view_fields)
        assert result.data.view_fields[0].name == view.view_fields[0].name
        assert len(result.data.view_fields[0].options) == len(
            view.view_fields[0].options
        )


def test_get_view_alternate_base_url():
    """Test getting a view with an alternate base URL."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        view_id = str(uuid.uuid4())
        alternate_base = "https://custom.iconik.io"

        # Create test data
        field = ViewField(
            field_id="test_field",
            name="Test Field",
            label="Test Field Label",
            type="text",
            required=False,
            options=[ViewOption(value="option1", label="Option 1")],
        )
        model = ViewResponse(
            id=str(uuid.uuid4()),
            name="Test View",
            date_created="2025-01-29T12:00:00Z",
            date_modified="2025-01-29T12:00:00Z",
            view_fields=[field],
            fields=[field],
        )
        data = model.model_dump()

        # Mock the endpoint with the expected URL pattern from MetadataSpec
        mock_address = f"{alternate_base}/API/metadata/v1/views/{view_id}/"
        m.get(mock_address, json=data)

        client = PythonikClient(
            app_id=app_id, auth_token=auth_token, timeout=3, base_url=alternate_base
        )
        response = client.metadata().get_view(view_id)

        # Verify the response
        assert response.data == model
        # Verify the request was made to the correct URL
        logger.info(m.last_request.url)
        logger.info(mock_address)
        assert m.last_request.url == mock_address


def test_create_field(requests_mock):
    """Test creating a metadata field using MetadataSpec.create_field and expecting FieldResponse."""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    client = PythonikClient(
        app_id=app_id, auth_token=auth_token, timeout=3
    )  # Client instance
    spec_instance = client.metadata()  # MetadataSpec instance

    field_name = "new_test_field_create"
    field_create_payload = FieldCreate(
        name=field_name,
        label="New Test Field Create",
        field_type="string",
        options=[FieldOption(label="Option 1", value="opt1_val_create")],
    )
    expected_field_response = FieldResponse(
        name=field_name,
        label="New Test Field Create",
        field_type="string",
        options=[FieldOption(label="Option 1", value="opt1_val_create")],
        date_created="2025-01-01T00:00:00Z",
        date_modified="2025-01-01T00:00:00Z",
        required=False,
        auto_set=False,
        hide_if_not_set=False,
        is_block_field=False,
        is_warning_field=False,
        multi=False,
        read_only=False,
        representative=False,
        sortable=False,
        use_as_facet=False,
    )

    # mock_address = MetadataSpec.gen_url(FIELDS_BASE_PATH) # Old way (classmethod, relative URL)
    mock_address = spec_instance.gen_url(
        FIELDS_BASE_PATH
    )  # New way (instance method, absolute URL)
    requests_mock.post(
        mock_address,
        json=json.loads(expected_field_response.model_dump_json()),
        status_code=201,
    )

    # client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3) # Already created above
    result = spec_instance.create_field(
        field_create_payload
    )  # Use the same spec_instance

    assert result.response.ok
    assert result.response.status_code == 201
    assert isinstance(result.data, FieldResponse)
    assert result.data.name == expected_field_response.name
    assert result.data.label == expected_field_response.label
    assert len(result.data.options) == 1
    assert result.data.options[0].label == "Option 1"


def test_update_field(requests_mock):
    """Test updating a metadata field using MetadataSpec.update_field and expecting FieldResponse."""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    field_to_update_name = "existing_field_for_update_test"
    field_update_payload = FieldUpdate(
        label="Updated Label for Field Test",
        description="Updated description test.",
    )
    expected_field_response = FieldResponse(
        name=field_to_update_name,
        label="Updated Label for Field Test",
        description="Updated description test.",
        field_type="string",
        options=[],
        date_created="2024-01-01T00:00:00Z",
        date_modified="2025-01-01T00:00:00Z",
        required=False,
        auto_set=False,
        hide_if_not_set=False,
        is_block_field=False,
        is_warning_field=False,
        multi=False,
        read_only=False,
        representative=False,
        sortable=False,
        use_as_facet=False,
    )

    mock_address = MetadataSpec.gen_url(
        FIELD_BY_NAME_PATH.format(field_name=field_to_update_name)
    )
    requests_mock.put(
        mock_address,
        json=json.loads(expected_field_response.model_dump_json()),
        status_code=200,
    )

    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
    result = client.metadata().update_field(field_to_update_name, field_update_payload)

    assert result.response.ok
    assert result.response.status_code == 200
    assert isinstance(result.data, FieldResponse)
    assert result.data.name == field_to_update_name
    assert result.data.label == "Updated Label for Field Test"
    assert result.data.description == "Updated description test."


def test_delete_field(requests_mock):
    """Test deleting a metadata field using MetadataSpec.delete_field."""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    field_to_delete_name = "field_marked_for_deletion_test"

    mock_address = MetadataSpec.gen_url(
        FIELD_BY_NAME_PATH.format(field_name=field_to_delete_name)
    )
    requests_mock.delete(mock_address, status_code=204)

    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
    result = client.metadata().delete_field(field_to_delete_name)

    assert result.response.ok
    assert result.response.status_code == 204


def test_create_field_conflict_error(requests_mock):
    """Test creating a metadata field with a conflicting name using MetadataSpec.create_field."""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    field_create_payload = FieldCreate(
        name="existing_name", label="Fail Label", field_type="string"
    )
    mock_address = MetadataSpec.gen_url(FIELDS_BASE_PATH)
    requests_mock.post(mock_address, json={"error": "conflict"}, status_code=409)
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
    result = client.metadata().create_field(field_create_payload)
    assert not result.response.ok
    assert result.response.status_code == 409


def test_update_field_not_found_error(requests_mock):
    """Test updating a non-existent metadata field using MetadataSpec.update_field."""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    field_update_payload = FieldUpdate(label="NonExistent Update")
    non_existent_field = "non_existent_field_name"
    mock_address = MetadataSpec.gen_url(
        FIELD_BY_NAME_PATH.format(field_name=non_existent_field)
    )
    requests_mock.put(mock_address, json={"error": "not found"}, status_code=404)
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
    result = client.metadata().update_field(non_existent_field, field_update_payload)
    assert not result.response.ok
    assert result.response.status_code == 404


def test_delete_field_not_found_error(requests_mock):
    """Test deleting a non-existent metadata field using MetadataSpec.delete_field."""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    non_existent_field = "another_non_existent_field"
    mock_address = MetadataSpec.gen_url(
        FIELD_BY_NAME_PATH.format(field_name=non_existent_field)
    )
    requests_mock.delete(mock_address, json={"error": "not found"}, status_code=404)
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
    result = client.metadata().delete_field(non_existent_field)
    assert not result.response.ok
    assert result.response.status_code == 404


def test_get_field_success(requests_mock):
    """Test successful retrieval of a metadata field by its name."""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    field_name_to_get = "my_test_field_get"

    expected_field_response = FieldResponse(
        name=field_name_to_get,
        label="My Test Field Get Label",
        field_type="string",
        options=[],
        date_created="2025-02-01T00:00:00Z",
        date_modified="2025-02-01T00:00:00Z",
        required=False,
        auto_set=False,
        hide_if_not_set=False,
        is_block_field=False,
        is_warning_field=False,
        multi=False,
        read_only=False,
        representative=False,
        sortable=False,
        use_as_facet=False,
    )

    mock_address = MetadataSpec.gen_url(
        FIELD_BY_NAME_PATH.format(field_name=field_name_to_get)
    )
    requests_mock.get(
        mock_address,
        json=json.loads(expected_field_response.model_dump_json()),
        status_code=200,
    )

    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
    result = client.metadata().get_field(field_name_to_get)

    assert result.response.ok
    assert result.response.status_code == 200
    assert isinstance(result.data, FieldResponse)
    assert result.data.name == field_name_to_get
    assert result.data.label == "My Test Field Get Label"


def test_get_field_not_found(requests_mock):
    """Test retrieving a non-existent metadata field (404)."""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    non_existent_field_name = "i_do_not_exist_field"

    mock_address = MetadataSpec.gen_url(
        FIELD_BY_NAME_PATH.format(field_name=non_existent_field_name)
    )
    requests_mock.get(mock_address, json={"error": "not found"}, status_code=404)

    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
    result = client.metadata().get_field(non_existent_field_name)

    assert not result.response.ok
    assert result.response.status_code == 404


def test_get_field_unauthorized(requests_mock):
    """Test retrieving a metadata field with an unauthorized token (401)."""
    app_id = str(uuid.uuid4())
    auth_token = "invalid_token"
    field_name = "any_field_name"

    mock_address = MetadataSpec.gen_url(
        FIELD_BY_NAME_PATH.format(field_name=field_name)
    )
    requests_mock.get(mock_address, json={"error": "unauthorized"}, status_code=401)

    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
    result = client.metadata().get_field(field_name)

    assert not result.response.ok
    assert result.response.status_code == 401


@pytest.mark.parametrize("field_type_enum", list(IconikFieldType))
def test_create_field_for_all_types(requests_mock, field_type_enum: IconikFieldType):
    """Test creating a metadata field for each IconikFieldType using MetadataSpec.create_field."""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
    spec_instance = client.metadata()

    field_name = f"test_sdk_{field_type_enum.value.lower()}_{str(uuid.uuid4())[:8]}"
    field_label = f"Test SDK {field_type_enum.name.replace('_', ' ').title()} Field"

    field_create_payload = {
        "name": field_name,
        "label": field_label,
        "field_type": field_type_enum,  # Use the Enum member directly
    }

    if field_type_enum == IconikFieldType.DROPDOWN:
        field_create_payload["options"] = [FieldOption(label="Opt1", value="val1")]

    # Prepare Pydantic model for request
    field_data_model = FieldCreate(**field_create_payload)

    # Expected response from API (API returns string value for field_type)
    expected_response_json = {
        "name": field_name,
        "label": field_label,
        "field_type": field_type_enum.value,  # API returns the string value
        "date_created": "2023-01-01T12:00:00Z",
        "date_modified": "2023-01-01T12:00:00Z",
        "description": None,
        "options": field_create_payload.get("options", []),
        "required": False,
        "auto_set": False,
        "hide_if_not_set": False,
        "is_block_field": False,
        "is_warning_field": False,
        "multi": False,
        "read_only": False,
        "representative": False,
        "sortable": False,
        "use_as_facet": False,
        "min_value": None,
        "max_value": None,
        "external_id": None,
        "source_url": None,
        "mapped_field_name": None,
    }
    if field_type_enum == IconikFieldType.DROPDOWN:
        # Pydantic model for options will be list of FieldOption objects
        # API mock should return list of dicts
        expected_response_json["options"] = [{"label": "Opt1", "value": "val1"}]
    else:
        expected_response_json["options"] = []

    create_url = spec_instance.gen_url(FIELDS_BASE_PATH)
    requests_mock.post(create_url, json=expected_response_json, status_code=201)

    # Call the method under test
    response = spec_instance.create_field(field_data=field_data_model)

    assert response.response.ok
    assert response.response.status_code == 201
    assert response.data is not None
    assert isinstance(response.data, FieldResponse), (
        "Response data should be a FieldResponse instance"
    )
    assert response.data.name == field_name
    assert response.data.label == field_label
    assert (
        response.data.field_type == field_type_enum
    )  # Pydantic model converts back to Enum

    # Optional: Mock and test deletion for cleanup (good practice)
    delete_url = spec_instance.gen_url(FIELD_BY_NAME_PATH.format(field_name=field_name))
    requests_mock.delete(delete_url, status_code=204)
    delete_response = spec_instance.delete_field(field_name)
    assert delete_response.response.ok
    assert delete_response.response.status_code == 204


def test_create_field_with_unknown_type_raises_validation_error(requests_mock):
    """
    Test that fetching a field with an unknown field_type string
    from the API raises a Pydantic ValidationError during response parsing.
    """
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
    spec_instance = client.metadata()

    field_name = f"test_sdk_unknown_type_{str(uuid.uuid4())[:8]}"
    field_label = "Test SDK Unknown Type Field"
    unknown_type_string = "some_future_unrecognized_type"

    # Data for creating the field - this part uses a valid IconikFieldType for the request
    field_data_model = FieldCreate(
        name=field_name,
        label=field_label,
        field_type=IconikFieldType.STRING,  # A valid type for the request itself
    )

    # Mocked API response containing the unknown field_type in its body
    mock_api_response_json = {
        "name": field_name,
        "label": field_label,
        "field_type": unknown_type_string,  # This is the unexpected value from API
        "date_created": "2023-01-01T12:00:00Z",
        "date_modified": "2023-01-01T12:00:00Z",
        # Fill in other required fields for FieldResponse model based on its definition
        "description": None,
        "options": [],
        "required": False,
        "auto_set": False,
        "hide_if_not_set": False,
        "is_block_field": False,
        "is_warning_field": False,
        "multi": False,
        "read_only": False,
        "representative": False,
        "sortable": False,
        "use_as_facet": False,
        "min_value": None,
        "max_value": None,
        "external_id": None,
        "source_url": None,
        "mapped_field_name": None,
    }

    create_url = spec_instance.gen_url(FIELDS_BASE_PATH)
    # We mock a successful creation (201) but with a problematic field_type in the response body
    requests_mock.post(create_url, json=mock_api_response_json, status_code=201)

    # The ValidationError should be raised when parse_response (called by create_field)
    # tries to fit unknown_type_string into IconikFieldType.
    with pytest.raises(ValidationError) as excinfo:
        spec_instance.create_field(field_data=field_data_model)

    # Check that the error message mentions 'field_type' and the unknown value
    error_str = str(excinfo.value).lower()
    assert "field_type" in error_str
    assert f"'{unknown_type_string}'" in error_str or unknown_type_string in error_str


# Field listing tests
# -------------------


def test_get_fields(requests_mock):
    """Test listing all metadata fields using MetadataSpec.get_fields."""
    # Setup test data
    field1 = {
        "name": "test_field_1",
        "label": "Test Field 1",
        "field_type": "string",
        "description": "First test field",
        "required": True,
        "auto_set": False,
        "multi": False,
        "read_only": False,
        "representative": False,
        "sortable": True,
        "use_as_facet": False,
        "hide_if_not_set": False,
        "is_block_field": False,
        "is_warning_field": False,
        "date_created": "2023-01-01T00:00:00Z",
        "date_modified": "2023-01-01T00:00:00Z",
    }

    field2 = {
        "name": "test_field_2",
        "label": "Test Field 2",
        "field_type": "integer",
        "description": "Second test field",
        "required": False,
        "auto_set": True,
        "multi": False,
        "read_only": True,
        "representative": True,
        "sortable": False,
        "use_as_facet": True,
        "hide_if_not_set": True,
        "is_block_field": False,
        "is_warning_field": True,
        "date_created": "2023-01-02T00:00:00Z",
        "date_modified": "2023-01-02T00:00:00Z",
    }

    response_data = {
        "objects": [field1, field2],
        "total": 2,
        "page": 1,
        "pages": 1,
        "per_page": 50,
        "first_url": "https://app.iconik.io/API/metadata/v1/fields/?page=1&per_page=50",
        "last_url": "https://app.iconik.io/API/metadata/v1/fields/?page=1&per_page=50",
        "next_url": None,
        "prev_url": None,
    }

    # Mock the API response
    mock_url = f"{MetadataSpec.base_url}/API/metadata/v1/fields/"
    requests_mock.get(mock_url, json=response_data)

    # Call the method
    client = PythonikClient(
        app_id=str(uuid.uuid4()), auth_token=str(uuid.uuid4()), timeout=3
    )
    response = client.metadata().list_fields()

    # Verify the response
    assert response.response.status_code == 200
    assert len(response.data.objects) == 2
    assert response.data.objects[0].name == "test_field_1"
    assert response.data.objects[0].field_type == "string"
    assert response.data.objects[1].name == "test_field_2"
    assert response.data.objects[1].field_type == "integer"
    assert response.data.total == 2
    assert response.data.page == 1


def test_get_fields_with_pagination(requests_mock):
    """Test pagination parameters (per_page and last_field_name) for get_fields."""
    # Setup test data for the next page
    last_field_name_from_prev_page = "field_on_prev_page"
    current_per_page = 2

    field_data_page_2_item_1 = {
        "name": "paged_field_1",
        "label": "Paged Field 1",
        "field_type": "string",
        "date_created": "2023-01-01T00:00:00Z",
        "date_modified": "2023-01-01T00:00:00Z",
        "auto_set": False,
        "hide_if_not_set": False,
        "is_block_field": False,
        "is_warning_field": False,
        "multi": False,
        "read_only": False,
        "representative": False,
        "required": False,
        "sortable": True,
        "use_as_facet": False,
    }
    field_data_page_2_item_2 = {
        "name": "paged_field_2",
        "label": "Paged Field 2",
        "field_type": "integer",
        "date_created": "2023-01-02T00:00:00Z",
        "date_modified": "2023-01-02T00:00:00Z",
        "auto_set": True,
        "hide_if_not_set": True,
        "is_block_field": True,
        "is_warning_field": True,
        "multi": True,
        "read_only": True,
        "representative": True,
        "required": True,
        "sortable": False,
        "use_as_facet": True,
    }

    response_data = {
        "objects": [field_data_page_2_item_1, field_data_page_2_item_2],
        "total": 10,  # Assuming 10 total fields for this example
        "page": 2,  # This is illustrative; API might not return page number with last_field_name
        "pages": 5,  # Illustrative
        "per_page": current_per_page,
        "first_url": f"{MetadataSpec.base_url}/API/metadata/v1/fields/?per_page={current_per_page}",
        "last_url": f"{MetadataSpec.base_url}/API/metadata/v1/fields/?last_field_name=some_last_field&per_page={current_per_page}",  # Illustrative
        "next_url": f"{MetadataSpec.base_url}/API/metadata/v1/fields/?last_field_name=paged_field_2&per_page={current_per_page}",
        "prev_url": f"{MetadataSpec.base_url}/API/metadata/v1/fields/?per_page={current_per_page}",  # Actual prev might need different handling
    }

    # Mock the API response with pagination parameters
    mock_url = f"{MetadataSpec.base_url}/API/metadata/v1/fields/?per_page={current_per_page}&last_field_name={last_field_name_from_prev_page}"
    requests_mock.get(mock_url, json=response_data)

    # Call the method with pagination
    client = PythonikClient(
        app_id=str(uuid.uuid4()), auth_token=str(uuid.uuid4()), timeout=3
    )
    response = client.metadata().list_fields(
        per_page=current_per_page, last_field_name=last_field_name_from_prev_page
    )

    # Verify the response
    assert response.response.status_code == 200
    assert len(response.data.objects) == 2
    assert response.data.objects[0].name == "paged_field_1"
    assert response.data.objects[1].name == "paged_field_2"
    assert response.data.per_page == current_per_page
    # Note: 'page', 'pages', 'total' might behave differently with cursor pagination
    # We're primarily testing that the SDK passes the params correctly and parses the response.


def test_get_fields_with_filter_param(requests_mock):
    """Test filtering fields by a comma-separated list of field names."""
    # Setup test data
    filter_names = "name_to_filter1,name_to_filter2"

    field_data1 = {
        "name": "name_to_filter1",
        "label": "Filtered Field 1",
        "field_type": "string",
        "date_created": "2023-01-01T00:00:00Z",
        "date_modified": "2023-01-01T00:00:00Z",
        "auto_set": False,
        "hide_if_not_set": False,
        "is_block_field": False,
        "is_warning_field": False,
        "multi": False,
        "read_only": False,
        "representative": False,
        "required": False,
        "sortable": True,
        "use_as_facet": False,
    }
    field_data2 = {
        "name": "name_to_filter2",
        "label": "Filtered Field 2",
        "field_type": "integer",
        "date_created": "2023-01-02T00:00:00Z",
        "date_modified": "2023-01-02T00:00:00Z",
        "auto_set": True,
        "hide_if_not_set": True,
        "is_block_field": True,
        "is_warning_field": True,
        "multi": True,
        "read_only": True,
        "representative": True,
        "required": True,
        "sortable": False,
        "use_as_facet": True,
    }

    response_data = {
        "objects": [field_data1, field_data2],
        "total": 2,
        "page": 1,  # May not be present or accurate with 'filter'
        "pages": 1,  # May not be present or accurate with 'filter'
        "per_page": 50,  # Default, or what was requested
    }

    # Mock the API response with filter parameter
    expected_url = (
        f"{MetadataSpec.base_url}/API/metadata/v1/fields/?filter={filter_names}"
    )
    requests_mock.get(expected_url, json=response_data)

    # Call the method with the filter
    client = PythonikClient(
        app_id=str(uuid.uuid4()), auth_token=str(uuid.uuid4()), timeout=3
    )
    response = client.metadata().list_fields(filter=filter_names)

    # Verify the response
    assert response.response.status_code == 200
    assert len(response.data.objects) == 2
    assert response.data.objects[0].name == "name_to_filter1"
    assert response.data.objects[1].name == "name_to_filter2"


def test_get_fields_unauthorized(requests_mock):
    """Test that get_fields handles unauthorized access."""
    # Mock unauthorized response
    mock_url = f"{MetadataSpec.base_url}/API/metadata/v1/fields/"
    requests_mock.get(mock_url, status_code=401, json={"message": "Unauthorized"})

    # Call the method and verify it raises an exception
    client = PythonikClient(
        app_id=str(uuid.uuid4()), auth_token="invalid-token", timeout=3
    )
    response = client.metadata().list_fields()

    # Verify the response
    assert response.response.status_code == 401
    assert response.data is None


def test_get_fields_empty(requests_mock):
    """Test get_fields with an empty result set."""
    # Mock empty response
    response_data = {"objects": [], "total": 0, "page": 1, "pages": 0, "per_page": 50}

    mock_url = f"{MetadataSpec.base_url}/API/metadata/v1/fields/"
    requests_mock.get(mock_url, json=response_data)

    # Call the method
    client = PythonikClient(
        app_id=str(uuid.uuid4()), auth_token=str(uuid.uuid4()), timeout=3
    )
    response = client.metadata().list_fields()

    # Verify the response
    assert response.response.status_code == 200
    assert len(response.data.objects) == 0
    assert response.data.total == 0


# Backward compatibility alias tests
# --------------------------------


def test_create_metadata_field_alias(requests_mock):
    """Test that the deprecated create_metadata_field method works as an alias for create_field."""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
    spec_instance = client.metadata()

    field_name = "test_alias_field"
    field_create_payload = FieldCreate(
        name=field_name,
        label="Test Alias Field",
        field_type="string",
    )

    # Mock the API response
    expected_response = FieldResponse(
        name=field_name,
        label="Test Alias Field",
        field_type="string",
        date_created="2025-01-01T00:00:00Z",
        date_modified="2025-01-01T00:00:00Z",
        required=False,
        auto_set=False,
        hide_if_not_set=False,
        is_block_field=False,
        is_warning_field=False,
        multi=False,
        read_only=False,
        representative=False,
        sortable=False,
        use_as_facet=False,
    )

    # Mock the API endpoint
    mock_address = spec_instance.gen_url(FIELDS_BASE_PATH)
    requests_mock.post(
        mock_address,
        json=json.loads(expected_response.model_dump_json()),
        status_code=201,
    )

    # Call the deprecated method
    result = spec_instance.create_metadata_field(field_create_payload)

    # Verify results
    assert result.response.ok
    assert result.response.status_code == 201
    assert isinstance(result.data, FieldResponse)
    assert result.data.name == field_name
    assert result.data.label == "Test Alias Field"
    assert result.data.field_type == "string"


def test_update_metadata_field_alias(requests_mock):
    """Test that the deprecated update_metadata_field method works as an alias for update_field."""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

    field_name = "test_alias_update_field"
    field_update_payload = FieldUpdate(
        label="Updated Alias Test Field", description="Updated via the alias method."
    )

    # Mock the API response
    expected_response = FieldResponse(
        name=field_name,
        label="Updated Alias Test Field",
        description="Updated via the alias method.",
        field_type="string",
        date_created="2024-01-01T00:00:00Z",
        date_modified="2025-01-01T00:00:00Z",
        required=False,
        auto_set=False,
        hide_if_not_set=False,
        is_block_field=False,
        is_warning_field=False,
        multi=False,
        read_only=False,
        representative=False,
        sortable=False,
        use_as_facet=False,
    )

    # Mock the API endpoint
    mock_address = MetadataSpec.gen_url(
        FIELD_BY_NAME_PATH.format(field_name=field_name)
    )
    requests_mock.put(
        mock_address,
        json=json.loads(expected_response.model_dump_json()),
        status_code=200,
    )

    # Call the deprecated method
    result = client.metadata().update_metadata_field(field_name, field_update_payload)

    # Verify results
    assert result.response.ok
    assert result.response.status_code == 200
    assert isinstance(result.data, FieldResponse)
    assert result.data.name == field_name
    assert result.data.label == "Updated Alias Test Field"
    assert result.data.description == "Updated via the alias method."


def test_delete_metadata_field_alias(requests_mock):
    """Test that the deprecated delete_metadata_field method works as an alias for delete_field."""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

    field_name = "field_to_delete_via_alias"

    # Mock the API endpoint
    mock_address = MetadataSpec.gen_url(
        FIELD_BY_NAME_PATH.format(field_name=field_name)
    )
    requests_mock.delete(mock_address, status_code=204)

    # Call the deprecated method
    result = client.metadata().delete_metadata_field(field_name)

    # Verify results
    assert result.response.ok
    assert result.response.status_code == 204
