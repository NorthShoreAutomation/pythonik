import uuid

import requests_mock

from pythonik.client import PythonikClient
from pythonik.models.assets.assets import (
    Asset,
    AssetCreate,
    BulkDelete,
    BulkDeleteObjectType,
)
from pythonik.models.assets.versions import (
    AssetVersionCreate,
    AssetVersionResponse,
    AssetVersionFromAssetCreate,
)
from pythonik.models.assets.segments import SegmentBody, SegmentResponse
from pythonik.specs.assets import (
    BASE,
    GET_URL,
    AssetSpec,
    SEGMENT_URL,
    VERSIONS_URL,
    PURGE_ALL_URL,
    BULK_DELETE_URL,
    SEGMENT_URL_UPDATE,
    VERSIONS_FROM_ASSET_URL,
)


def test_partial_update_asset():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())

        model = Asset()
        data = model.model_dump()
        mock_address = AssetSpec.gen_url(GET_URL.format(asset_id))

        m.patch(mock_address, json=data)
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

        client.assets().partial_update_asset(asset_id=asset_id, body=model)


def test_bulk_delete():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())

        model = BulkDelete(
            object_ids=[str(uuid.uuid4()), str(uuid.uuid4())],
            object_type=BulkDeleteObjectType.ASSETS,
        )
        mock_address = AssetSpec.gen_url(BULK_DELETE_URL)

        m.post(mock_address)
        m.post(AssetSpec.gen_url(PURGE_ALL_URL))
        
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        client.assets().bulk_delete(body=model, permanently_delete=True)


def test_permanently_delete():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())

        mock_address = AssetSpec.gen_url(PURGE_ALL_URL)

        m.post(mock_address)
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

        client.assets().permanently_delete()


def test_get_asset():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())

        model = Asset()
        data = model.model_dump()
        mock_address = AssetSpec.gen_url(GET_URL.format(asset_id))

        m.get(mock_address, json=data)
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

        client.assets().get(asset_id=asset_id)


def test_create_asset():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_title = str(uuid.uuid4())

        model = AssetCreate(title=asset_title)
        data = model.model_dump()
        mock_address = AssetSpec.gen_url(BASE)

        m.post(mock_address, json=data)
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

        client.assets().create(body=model)


def test_create_segment():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())

        model = SegmentBody()
        response = SegmentResponse()
        data = response.model_dump()
        mock_address = AssetSpec.gen_url(SEGMENT_URL.format(asset_id))

        m.post(mock_address, json=data)
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

        client.assets().create_segment(asset_id=asset_id, body=model)


def test_update_segment():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        segment_id = str(uuid.uuid4())

        model = SegmentBody()
        response = SegmentResponse()
        data = response.model_dump()
        mock_address = AssetSpec.gen_url(
            SEGMENT_URL_UPDATE.format(asset_id, segment_id)
        )

        m.put(mock_address, json=data)
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

        client.assets().update_segment(
            asset_id=asset_id, segment_id=segment_id, body=model
        )


def test_partial_update_segment():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        segment_id = str(uuid.uuid4())

        model = SegmentBody()
        response = SegmentResponse()
        data = response.model_dump()
        mock_address = AssetSpec.gen_url(
            SEGMENT_URL_UPDATE.format(asset_id, segment_id)
        )

        m.patch(mock_address, json=data)
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

        client.assets().partial_update_segment(
            asset_id=asset_id, segment_id=segment_id, body=model
        )


def test_create_version():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())

        model = AssetVersionCreate(
            copy_metadata=True, copy_segments=True, include_segment_types=["MARKER"]
        )
        response = AssetVersionResponse(
            asset_id=asset_id, system_domain_id=str(uuid.uuid4()), versions=[]
        )
        data = response.model_dump()
        mock_address = AssetSpec.gen_url(VERSIONS_URL.format(asset_id))

        m.post(mock_address, json=data)
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

        client.assets().create_version(asset_id=asset_id, body=model)


def test_create_version_from_asset():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        source_asset_id = str(uuid.uuid4())

        model = AssetVersionFromAssetCreate(
            copy_previous_version_segments=True, include_segment_types=["MARKER"]
        )
        # No response data needed as it returns 202 with no content
        mock_address = AssetSpec.gen_url(
            VERSIONS_FROM_ASSET_URL.format(asset_id, source_asset_id)
        )

        m.post(mock_address, status_code=202)
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

        client.assets().create_version_from_asset(
            asset_id=asset_id, source_asset_id=source_asset_id, body=model
        )
