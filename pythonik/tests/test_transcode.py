# pythonik/tests/test_transcode.py
import uuid
from datetime import datetime
from typing import (
    Any,
    Dict,
)

import requests_mock

from pythonik.client import PythonikClient
from pythonik.models.transcode import (
    AbortStorageTranscodeJobsSchema,
    AnalyzeSchema,
    AssetLinkData,
    AssetLinkURLSchema,
    BulkAnalyzeSchema,
    BulkTranscribeSchema,
    EdgeTranscodeJobsSchema,
    EdgeTranscodeWorkerSchema,
    EdgeTranscodeWorkersSchema,
    GenerateCollectionKeyframeSchema,
    JobSchema,
    LocalStorageFileTranscodeJobSchema,
    LocalStorageFileTranscodeJobsSchema,
    SpecifiedKeyframes,
    TranscodeESQueueRecordsSchema,
    TranscodeQueueSchema,
    TranscribeSchema,
)
from pythonik.specs.transcode import TranscodeSpec


def test_analyze_asset():
    """Test analyze_asset method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())

        analyze_schema = AnalyzeSchema(force=True)
        mock_address = TranscodeSpec.gen_url(f"analyze/assets/{asset_id}/")
        m.post(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)

        response = client.transcode().analyze_asset(asset_id, analyze_schema)

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address
        assert m.last_request.json() == {"force": True}


def test_analyze_asset_with_dict():
    """Test analyze_asset method with a dictionary input."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())

        analyze_schema = {"force": True, "force_type": "OVERWRITE"}
        mock_address = TranscodeSpec.gen_url(f"analyze/assets/{asset_id}/")
        m.post(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)

        response = client.transcode().analyze_asset(asset_id, analyze_schema)

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address
        assert m.last_request.json() == analyze_schema


def test_analyze_asset_default_profile():
    """Test analyze_asset_default_profile method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())

        analyze_schema = AnalyzeSchema(force=True)
        mock_address = TranscodeSpec.gen_url(
            f"analyze/assets/{asset_id}/profiles/default/")
        m.post(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)

        response = client.transcode().analyze_asset_default_profile(
            asset_id, analyze_schema)

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address
        assert m.last_request.json() == {"force": True}


def test_analyze_asset_default_profile_media_type():
    """Test analyze_asset_default_profile_media_type method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        media_type = "video"

        analyze_schema = AnalyzeSchema(force=True)
        mock_address = TranscodeSpec.gen_url(
            f"analyze/assets/{asset_id}/profiles/default/{media_type}/")
        m.post(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)

        response = client.transcode().analyze_asset_default_profile_media_type(
            asset_id, media_type, analyze_schema)

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address
        assert m.last_request.json() == {"force": True}


def test_analyze_asset_custom_profile():
    """Test analyze_asset_custom_profile method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        profile_id = str(uuid.uuid4())

        analyze_schema = AnalyzeSchema(force=True)
        mock_address = TranscodeSpec.gen_url(
            f"analyze/assets/{asset_id}/profiles/{profile_id}/")
        m.post(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)

        response = client.transcode().analyze_asset_custom_profile(
            asset_id, profile_id, analyze_schema)

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address
        assert m.last_request.json() == {"force": True}


def test_analyze_bulk():
    """Test analyze_bulk method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = str(uuid.uuid4())

        analyze_schema = BulkAnalyzeSchema(force=True,
                                           object_ids=[object_id],
                                           object_type="assets")
        mock_address = TranscodeSpec.gen_url("analyze/bulk/")
        m.post(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)

        response = client.transcode().analyze_bulk(analyze_schema)

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address
        assert m.last_request.json()["force"] is True
        assert m.last_request.json()["object_type"] == "assets"
        assert m.last_request.json()["object_ids"] == [object_id]


def test_get_asset_link_metadata():
    """Test get_asset_link_metadata method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())

        url_schema = AssetLinkURLSchema(url="https://example.com/video.mp4")
        response_data = {"site_name": "Example Site", "title": "Sample Video"}
        mock_address = TranscodeSpec.gen_url("assets/link/metadata/")
        m.post(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)

        response = client.transcode().get_asset_link_metadata(url_schema)

        assert response.response.ok
        assert m.last_request.url == mock_address
        assert m.last_request.json()["url"] == "https://example.com/video.mp4"
        assert isinstance(response.data, AssetLinkData)
        assert response.data.site_name == "Example Site"
        assert response.data.title == "Sample Video"


def test_acknowledge_edge_transcode_job():
    """Test acknowledge_edge_transcode_job method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        job_id = str(uuid.uuid4())

        mock_address = TranscodeSpec.gen_url(
            f"edge_transcode/jobs/{job_id}/acknowledge/")
        m.post(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().acknowledge_edge_transcode_job(job_id)

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address


def test_fetch_edge_transcode_workers():
    """Test fetch_edge_transcode_workers method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        worker_id = str(uuid.uuid4())
        storage_id = str(uuid.uuid4())

        response_data = {
            "objects": [{
                "id": worker_id,
                "status": "ACTIVE",
                "storage_id": storage_id,
                "last_update_date": datetime.now().isoformat(),
            }]
        }
        mock_address = TranscodeSpec.gen_url("edge_transcode/workers/")
        m.get(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().list_edge_transcode_workers()

        assert response.response.ok
        assert m.last_request.url == mock_address
        assert isinstance(response.data, EdgeTranscodeWorkersSchema)
        assert len(response.data.objects) == 1
        assert str(response.data.objects[0].id) == worker_id
        assert response.data.objects[0].status == "ACTIVE"
        assert str(response.data.objects[0].storage_id) == storage_id


def test_create_edge_transcode_worker():
    """Test create_edge_transcode_worker method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        worker_id = str(uuid.uuid4())
        storage_id = str(uuid.uuid4())

        worker_schema = EdgeTranscodeWorkerSchema(status="ACTIVE",
                                                  storage_id=storage_id)
        response_data = {
            "id": worker_id,
            "status": "ACTIVE",
            "storage_id": storage_id,
            "last_update_date": datetime.now().isoformat(),
        }
        mock_address = TranscodeSpec.gen_url("edge_transcode/workers/")
        m.post(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)

        response = client.transcode().create_edge_transcode_worker(
            worker_schema)

        assert response.response.ok
        assert m.last_request.url == mock_address
        assert m.last_request.json()["status"] == "ACTIVE"
        assert m.last_request.json()["storage_id"] == storage_id
        assert isinstance(response.data, EdgeTranscodeWorkerSchema)
        assert str(response.data.id) == worker_id
        assert response.data.status == "ACTIVE"
        assert str(response.data.storage_id) == storage_id


def test_get_edge_transcode_worker():
    """Test get_edge_transcode_worker method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        worker_id = str(uuid.uuid4())
        storage_id = str(uuid.uuid4())

        response_data = {
            "id": worker_id,
            "status": "ACTIVE",
            "storage_id": storage_id,
            "last_update_date": datetime.now().isoformat(),
        }
        mock_address = TranscodeSpec.gen_url(
            f"edge_transcode/workers/{worker_id}/")
        m.get(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().get_edge_transcode_worker(worker_id)

        assert response.response.ok
        assert m.last_request.url == mock_address
        assert isinstance(response.data, EdgeTranscodeWorkerSchema)
        assert str(response.data.id) == worker_id
        assert response.data.status == "ACTIVE"
        assert str(response.data.storage_id) == storage_id


def test_delete_edge_transcode_worker():
    """Test delete_edge_transcode_worker method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        worker_id = str(uuid.uuid4())

        mock_address = TranscodeSpec.gen_url(
            f"edge_transcode/workers/{worker_id}/")
        m.delete(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().delete_edge_transcode_worker(worker_id)

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address


def test_update_edge_transcode_worker():
    """Test update_edge_transcode_worker method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        worker_id = str(uuid.uuid4())
        storage_id = str(uuid.uuid4())

        worker_schema = EdgeTranscodeWorkerSchema(status="ACTIVE",
                                                  storage_id=storage_id)
        response_data = {
            "id": worker_id,
            "status": "ACTIVE",
            "storage_id": storage_id,
            "last_update_date": datetime.now().isoformat(),
        }
        mock_address = TranscodeSpec.gen_url(
            f"edge_transcode/workers/{worker_id}/")
        m.put(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)

        response = client.transcode().update_edge_transcode_worker(
            worker_id, worker_schema)

        assert response.response.ok
        assert m.last_request.url == mock_address
        assert m.last_request.json()["status"] == "ACTIVE"
        assert m.last_request.json()["storage_id"] == storage_id
        assert isinstance(response.data, EdgeTranscodeWorkerSchema)
        assert str(response.data.id) == worker_id
        assert response.data.status == "ACTIVE"
        assert str(response.data.storage_id) == storage_id


def test_partial_update_edge_transcode_worker():
    """Test partial_update_edge_transcode_worker method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        worker_id = str(uuid.uuid4())
        storage_id = str(uuid.uuid4())

        worker_schema = {"status": "INACTIVE"}
        response_data = {
            "id": worker_id,
            "status": "INACTIVE",
            "storage_id": storage_id,
            "last_update_date": datetime.now().isoformat(),
        }
        mock_address = TranscodeSpec.gen_url(
            f"edge_transcode/workers/{worker_id}/")
        m.patch(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)

        response = client.transcode().partial_update_edge_transcode_worker(
            worker_id, worker_schema)

        assert response.response.ok
        assert m.last_request.url == mock_address
        assert m.last_request.json()["status"] == "INACTIVE"
        assert isinstance(response.data, EdgeTranscodeWorkerSchema)
        assert str(response.data.id) == worker_id
        assert response.data.status == "INACTIVE"
        assert str(response.data.storage_id) == storage_id


def test_generate_collection_keyframe():
    """Test generate_collection_keyframe method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        collection_id = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())

        keyframe_schema = GenerateCollectionKeyframeSchema(
            force=True,
            specified_asset_ids=[asset_id],
            specified_keyframes=[
                SpecifiedKeyframes(url="https://example.com/image.jpg")
            ],
        )
        mock_address = TranscodeSpec.gen_url(
            f"keyframes/collections/{collection_id}/")
        m.post(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)

        response = client.transcode().generate_collection_keyframe(
            collection_id, keyframe_schema)

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address
        request_json = m.last_request.json()
        assert request_json["force"] is True
        assert request_json["specified_asset_ids"] == [asset_id]
        assert (request_json["specified_keyframes"][0]["url"] ==
                "https://example.com/image.jpg")


def test_abort_storage_transcode_jobs():
    """Test abort_storage_transcode_jobs method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        storage_id = str(uuid.uuid4())

        abort_schema = AbortStorageTranscodeJobsSchema(
            error_message="Test abort all jobs")
        mock_address = TranscodeSpec.gen_url(f"storages/{storage_id}/")
        m.delete(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)

        response = client.transcode().abort_storage_transcode_jobs(
            storage_id, abort_schema)

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address
        assert m.last_request.json()["error_message"] == "Test abort all jobs"


def test_fetch_storage_edge_transcode_jobs():
    """Test fetch_storage_edge_transcode_jobs method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        storage_id = str(uuid.uuid4())
        job_id = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        collection_id = str(uuid.uuid4())

        # Create a complete response that meets EdgeTranscodeJobSchema requirements
        response_data = {
            "objects": [{
                "job_id": job_id,
                "asset_id": asset_id,
                "collection_id": collection_id,
                "input": {
                    "asset_id": asset_id,
                    "endpoint": {
                        "url": "https://example.com/file.mp4",
                        "type": "http",
                    },
                },
                # Add any other required fields
                "job_steps": [],
            }]
        }
        mock_address = TranscodeSpec.gen_url(
            f"storages/{storage_id}/edge_transcode/jobs/")
        m.get(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().list_storage_edge_transcode_jobs(
            storage_id, limit=5)

        assert response.response.ok
        assert m.last_request.url.startswith(mock_address)
        assert "limit=5" in m.last_request.url
        assert isinstance(response.data, EdgeTranscodeJobsSchema)
        assert len(response.data.objects) == 1
        assert response.data.objects[0].job_id == job_id


def test_delete_storage_file_transcode():
    """Test delete_storage_file_transcode method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        storage_id = str(uuid.uuid4())
        file_id = str(uuid.uuid4())

        mock_address = TranscodeSpec.gen_url(
            f"storages/{storage_id}/files/{file_id}/transcode/")
        m.delete(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().delete_storage_file_transcode(
            storage_id, file_id)

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address


def test_fetch_storage_transcode_jobs():
    """Test fetch_storage_transcode_jobs method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        storage_id = str(uuid.uuid4())
        job_id = str(uuid.uuid4())

        response_data = {
            "objects": [{
                "id": str(uuid.uuid4()),
                "job_id": job_id,
                "asset_id": str(uuid.uuid4()),
                "file_id": str(uuid.uuid4()),
                "file_set_id": str(uuid.uuid4()),
                "format_id": str(uuid.uuid4()),
                "version_id": str(uuid.uuid4()),
                "filename": "test.mp4",
                "directory_path": "/path/to/file",
                "size": 1024,
            }],
            "per_page":
            10,
            "page":
            1,
            "total":
            1,
        }
        mock_address = TranscodeSpec.gen_url(
            f"storages/{storage_id}/transcode/")
        m.get(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().list_storage_transcode_jobs(
            storage_id, per_page=10, last_id="last-job-id")

        assert response.response.ok
        assert m.last_request.url.startswith(mock_address)
        assert "per_page=10" in m.last_request.url
        assert "last_id=last-job-id" in m.last_request.url
        assert isinstance(response.data, LocalStorageFileTranscodeJobsSchema)
        assert len(response.data.objects) == 1
        assert response.data.objects[0].job_id == job_id


def test_get_storage_transcode_job():
    """Test get_storage_transcode_job method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        storage_id = str(uuid.uuid4())
        record_id = str(uuid.uuid4())
        job_id = str(uuid.uuid4())

        response_data = {
            "id": record_id,
            "job_id": job_id,
            "asset_id": str(uuid.uuid4()),
            "file_id": str(uuid.uuid4()),
            "file_set_id": str(uuid.uuid4()),
            "format_id": str(uuid.uuid4()),
            "version_id": str(uuid.uuid4()),
            "filename": "test.mp4",
            "directory_path": "/path/to/file",
            "size": 1024,
        }
        mock_address = TranscodeSpec.gen_url(
            f"storages/{storage_id}/transcode/{record_id}/")
        m.get(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().get_storage_transcode_job(
            storage_id, record_id)

        assert response.response.ok
        assert m.last_request.url == mock_address
        assert isinstance(response.data, LocalStorageFileTranscodeJobSchema)
        assert response.data.id == record_id
        assert response.data.job_id == job_id


def test_delete_storage_transcode_job():
    """Test delete_storage_transcode_job method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        storage_id = str(uuid.uuid4())
        record_id = str(uuid.uuid4())

        mock_address = TranscodeSpec.gen_url(
            f"storages/{storage_id}/transcode/{record_id}/")
        m.delete(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().delete_storage_transcode_job(
            storage_id, record_id)

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address


def test_create_transcode():
    """Test create_transcode method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        job_id = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())

        # Creating a simplified job schema - a real one would be more complex
        job_schema: Dict[str, Any] = {
            "asset_id": asset_id,
            "priority": 5,
            "input": {
                "file_id": str(uuid.uuid4()),
                "endpoint": {
                    "url": "https://example.com/file.mp4",
                    "type": "http",
                },
            },
        }

        response_data = {"job_id": job_id, "asset_id": asset_id, "priority": 5}
        mock_address = TranscodeSpec.gen_url("transcode/")
        m.post(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)

        response = client.transcode().create_transcode(job_schema)

        assert response.response.ok
        assert m.last_request.url == mock_address
        assert m.last_request.json()["asset_id"] == asset_id
        assert m.last_request.json()["priority"] == 5
        assert isinstance(response.data, JobSchema)
        assert response.data.asset_id == asset_id
        assert response.data.priority == 5


def test_fetch_transcode_queue():
    """Test fetch_transcode_queue method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())

        response_data = {
            "objects": [{
                "id": str(uuid.uuid4()),
                "status": "READY",
                "priority": 5,
                "type": "TRANSCODE",
            }],
            "per_page":
            10,
            "page":
            1,
            "total":
            1,
        }
        mock_address = TranscodeSpec.gen_url("transcode/queue/")
        m.get(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().list_transcode_queue(per_page=10,
                                                           page=1,
                                                           sort="priority")

        assert response.response.ok
        assert m.last_request.url.startswith(mock_address)
        assert "per_page=10" in m.last_request.url
        assert "page=1" in m.last_request.url
        assert "sort=priority" in m.last_request.url
        assert isinstance(response.data, TranscodeQueueSchema)
        assert len(response.data.objects) == 1
        assert response.data.objects[0].status == "READY"
        assert response.data.objects[0].priority == 5


def test_fetch_transcode_queue_system():
    """Test fetch_transcode_queue_system method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())

        response_data = {
            "objects": [{
                "id": str(uuid.uuid4()),
                "status": "READY",
                "priority": 5,
                "type": "TRANSCODE",
                "system_domain": "default",
            }],
            "per_page":
            10,
            "page":
            1,
            "total":
            1,
        }
        mock_address = TranscodeSpec.gen_url("transcode/queue/system/")
        m.get(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().list_transcode_queue_system(
            per_domain_id=True, per_page=10, page=1, sort="priority")

        assert response.response.ok
        assert m.last_request.url.startswith(mock_address)
        assert "per_domain_id=true" in m.last_request.url.lower()
        assert "per_page=10" in m.last_request.url
        assert "page=1" in m.last_request.url
        assert "sort=priority" in m.last_request.url
        assert isinstance(response.data, TranscodeQueueSchema)
        assert len(response.data.objects) == 1
        assert response.data.objects[0].status == "READY"
        assert response.data.objects[0].priority == 5
        assert response.data.objects[0].system_domain == "default"


def test_fetch_transcode_object_queue_records():
    """Test fetch_transcode_object_queue_records method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = str(uuid.uuid4())
        object_type = "assets"

        response_data = {
            "objects": [{
                "id": str(uuid.uuid4()),
                "object_id": object_id,
                "object_type": object_type,
                "status": "READY",
            }]
        }
        mock_address = TranscodeSpec.gen_url(
            f"transcode/{object_type}/{object_id}/")
        m.get(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().list_transcode_object_queue_records(
            object_type, object_id)

        assert response.response.ok
        assert m.last_request.url == mock_address
        assert isinstance(response.data, TranscodeESQueueRecordsSchema)
        assert len(response.data.objects) == 1
        assert response.data.objects[0].object_id == object_id
        assert response.data.objects[0].object_type == object_type
        assert response.data.objects[0].status == "READY"


def test_fetch_transcode_version_queue_records():
    """Test fetch_transcode_version_queue_records method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = str(uuid.uuid4())
        object_type = "assets"
        version_id = str(uuid.uuid4())

        response_data = {
            "objects": [{
                "id": str(uuid.uuid4()),
                "object_id": object_id,
                "object_type": object_type,
                "version_id": version_id,
                "status": "READY",
            }]
        }
        mock_address = TranscodeSpec.gen_url(
            f"transcode/{object_type}/{object_id}/versions/{version_id}/")
        m.get(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().list_transcode_version_queue_records(
            object_type, object_id, version_id)

        assert response.response.ok
        assert m.last_request.url == mock_address
        assert isinstance(response.data, TranscodeESQueueRecordsSchema)
        assert len(response.data.objects) == 1
        assert response.data.objects[0].object_id == object_id
        assert response.data.objects[0].object_type == object_type
        assert response.data.objects[0].version_id == version_id
        assert response.data.objects[0].status == "READY"


def test_get_transcode_job():
    """Test get_transcode_job method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        job_id = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())

        response_data = {
            "job_id": job_id,
            "asset_id": asset_id,
            "priority": 5,
            "status": "READY",
        }
        mock_address = TranscodeSpec.gen_url(f"transcode/{job_id}/")
        m.get(mock_address, json=response_data)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().get_transcode_job(job_id)

        assert response.response.ok
        assert m.last_request.url == mock_address
        assert isinstance(response.data, JobSchema)
        assert response.data.job_id == job_id
        assert response.data.asset_id == asset_id
        assert response.data.priority == 5


def test_delete_transcode_job():
    """Test delete_transcode_job method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        job_id = str(uuid.uuid4())

        mock_address = TranscodeSpec.gen_url(f"transcode/{job_id}/")
        m.delete(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().delete_transcode_job(job_id)

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address


def test_move_transcode_job_position():
    """Test move_transcode_job_position method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        job_id = str(uuid.uuid4())

        mock_address = TranscodeSpec.gen_url(
            f"transcode/{job_id}/position/top/")
        m.post(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().move_transcode_job_position(
            job_id, "top")

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address


def test_update_transcode_job_priority():
    """Test update_transcode_job_priority method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        job_id = str(uuid.uuid4())
        priority = 8

        mock_address = TranscodeSpec.gen_url(
            f"transcode/{job_id}/priority/{priority}/")
        m.put(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)
        response = client.transcode().update_transcode_job_priority(
            job_id, priority)

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address


def test_transcribe_asset_default_profile():
    """Test transcribe_asset_default_profile method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())

        transcribe_schema = TranscribeSchema(language="en",
                                             speakers=2,
                                             force=True)
        mock_address = TranscodeSpec.gen_url(
            f"transcribe/assets/{asset_id}/profiles/default/")
        m.post(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)

        response = client.transcode().transcribe_asset_default_profile(
            asset_id, transcribe_schema)

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address
        request_json = m.last_request.json()
        assert request_json["language"] == "en"
        assert request_json["speakers"] == 2
        assert request_json["force"] is True


def test_transcribe_bulk():
    """Test transcribe_bulk method."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        object_id = str(uuid.uuid4())

        transcribe_schema = BulkTranscribeSchema(
            object_ids=[object_id],
            object_type="assets",
            language="en",
            speakers=2,
            force=True,
        )
        mock_address = TranscodeSpec.gen_url("transcribe/bulk/")
        m.post(mock_address, status_code=204)

        client = PythonikClient(app_id=app_id,
                                auth_token=auth_token,
                                timeout=3)

        response = client.transcode().transcribe_bulk(transcribe_schema)

        assert response.response.ok
        assert response.response.status_code == 204
        assert m.last_request.url == mock_address
        request_json = m.last_request.json()
        assert request_json["object_type"] == "assets"
        assert request_json["object_ids"] == [object_id]
        assert request_json["language"] == "en"
        assert request_json["speakers"] == 2
        assert request_json["force"] is True
