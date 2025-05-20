from typing import (
    Any,
    Dict,
    Literal,
    Optional,
    Union,
)

from pythonik.models.base import Response
from pythonik.specs._internal_utils import is_pydantic_model
from pythonik.specs.base import Spec

from ..models.transcode import (
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
    TranscodeESQueueRecordsSchema,
    TranscodeQueueSchema,
    TranscribeSchema,
)


class TranscodeSpec(Spec):
    server = "API/transcode/"

    def analyze_asset(
        self,
        asset_id: str,
        analyze_schema: Union[AnalyzeSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Start a job that sends an asset for analysis

        Args:
            asset_id: ID of the asset
            analyze_schema: Analysis parameters (either as AnalyzeSchema
                or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (analyze_schema.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(analyze_schema) else analyze_schema)
        url = self.gen_url(f"analyze/assets/{asset_id}/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def analyze_asset_default_profile(
        self,
        asset_id: str,
        analyze_schema: Union[AnalyzeSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Start a job that sends an asset for analysis with a default
        analysis profile

        Args:
            asset_id: ID of the asset
            analyze_schema: Analysis parameters (either as AnalyzeSchema
                or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (analyze_schema.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(analyze_schema) else analyze_schema)
        url = self.gen_url(f"analyze/assets/{asset_id}/profiles/default/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def analyze_asset_default_profile_media_type(
        self,
        asset_id: str,
        media_type: str,
        analyze_schema: Union[AnalyzeSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Start a job that sends an asset for analysis with a default
        analysis profile of specified media type

        Args:
            asset_id: ID of the asset
            media_type: Type of media
            analyze_schema: Analysis parameters (either as AnalyzeSchema
                or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (analyze_schema.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(analyze_schema) else analyze_schema)
        url = self.gen_url(
            f"analyze/assets/{asset_id}/profiles/default/{media_type}/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def analyze_asset_custom_profile(
        self,
        asset_id: str,
        profile_id: str,
        analyze_schema: Union[AnalyzeSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Start a job that sends an asset for analysis with a custom
        analysis profile

        Args:
            asset_id: ID of the asset
            profile_id: ID of the analysis profile
            analyze_schema: Analysis parameters (either as AnalyzeSchema
                or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (analyze_schema.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(analyze_schema) else analyze_schema)
        url = self.gen_url(f"analyze/assets/{asset_id}/profiles/{profile_id}/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def analyze_bulk(
        self,
        bulk_analyze_schema: Union[BulkAnalyzeSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Start a job that sends objects for analysis using a custom
        analysis profile

        Args:
            bulk_analyze_schema: Bulk analysis parameters (either as
                BulkAnalyzeSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Analysis account/profile was not found
        """
        body = (
            bulk_analyze_schema.model_dump(exclude_defaults=exclude_defaults)
            if is_pydantic_model(bulk_analyze_schema) else bulk_analyze_schema)
        url = self.gen_url("analyze/bulk/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def get_asset_link_metadata(
        self,
        asset_link_url_schema: Union[AssetLinkURLSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Gets metadata info from the link

        Args:
            asset_link_url_schema: URL parameters (either as
                AssetLinkURLSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=AssetLinkData)

        Raises:
            - 400 Bad URL
            - 401 Token is invalid
            - 404 Could not extract data
        """
        body = (asset_link_url_schema.model_dump(
            exclude_defaults=exclude_defaults)
                if is_pydantic_model(asset_link_url_schema) else
                asset_link_url_schema)
        url = self.gen_url("assets/link/metadata/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, AssetLinkData)

    def acknowledge_edge_transcode_job(
        self,
        job_id: str,
        **kwargs,
    ) -> Response:
        """
        Acknowledge an edge transcode job

        Args:
            job_id: ID of the edge transcode job
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Edge transcode job doesn't exist
        """
        url = self.gen_url(f"edge_transcode/jobs/{job_id}/acknowledge/")
        resp = self._post(url, **kwargs)
        return self.parse_response(resp, None)

    def list_edge_transcode_workers(
        self,
        **kwargs,
    ) -> Response:
        """
        Get edge transcode workers

        Args:
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=EdgeTranscodeWorkersSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url("edge_transcode/workers/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, EdgeTranscodeWorkersSchema)

    def create_edge_transcode_worker(
        self,
        worker_schema: Union[EdgeTranscodeWorkerSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new edge transcode worker

        Args:
            worker_schema: Edge transcode worker parameters (either as
                EdgeTranscodeWorkerSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=EdgeTranscodeWorkerSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (worker_schema.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(worker_schema) else worker_schema)
        url = self.gen_url("edge_transcode/workers/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, EdgeTranscodeWorkerSchema)

    def get_edge_transcode_worker(
        self,
        worker_id: str,
        **kwargs,
    ) -> Response:
        """
        Get an edge transcode worker

        Args:
            worker_id: ID of the edge transcode worker
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=EdgeTranscodeWorkerSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Edge transcode worker doesn't exist
        """
        url = self.gen_url(f"edge_transcode/workers/{worker_id}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, EdgeTranscodeWorkerSchema)

    def delete_edge_transcode_worker(
        self,
        worker_id: str,
        **kwargs,
    ) -> Response:
        """
        Delete a edge transcode worker

        Args:
            worker_id: ID of the edge transcode worker
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Edge transcode worker doesn't exist
        """
        url = self.gen_url(f"edge_transcode/workers/{worker_id}/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def update_edge_transcode_worker(
        self,
        worker_id: str,
        worker_schema: Union[EdgeTranscodeWorkerSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Update an edge transcode worker

        Args:
            worker_id: ID of the edge transcode worker
            worker_schema: Edge transcode worker parameters (either as
                EdgeTranscodeWorkerSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=EdgeTranscodeWorkerSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Edge transcode worker doesn't exist
        """
        body = (worker_schema.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(worker_schema) else worker_schema)
        url = self.gen_url(f"edge_transcode/workers/{worker_id}/")
        resp = self._put(url, json=body, **kwargs)
        return self.parse_response(resp, EdgeTranscodeWorkerSchema)

    def partial_update_edge_transcode_worker(
        self,
        worker_id: str,
        worker_schema: Union[EdgeTranscodeWorkerSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Update an edge transcode worker partially

        Args:
            worker_id: ID of the edge transcode worker
            worker_schema: Edge transcode worker parameters to update
                (either as EdgeTranscodeWorkerSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=EdgeTranscodeWorkerSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Edge transcode worker doesn't exist
        """
        body = (worker_schema.model_dump(exclude_defaults=exclude_defaults,
                                         exclude_unset=True)
                if is_pydantic_model(worker_schema) else worker_schema)
        url = self.gen_url(f"edge_transcode/workers/{worker_id}/")
        resp = self._patch(url, json=body, **kwargs)
        return self.parse_response(resp, EdgeTranscodeWorkerSchema)

    def generate_collection_keyframe(
        self,
        collection_id: str,
        keyframe_schema: Union[GenerateCollectionKeyframeSchema, Dict[str,
                                                                      Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Start a job that creates a collection keyframe

        Args:
            collection_id: ID of the collection
            keyframe_schema: Keyframe generation parameters (either as
                GenerateCollectionKeyframeSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (keyframe_schema.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(keyframe_schema) else keyframe_schema)
        url = self.gen_url(f"keyframes/collections/{collection_id}/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def abort_storage_transcode_jobs(
        self,
        storage_id: str,
        abort_schema: Union[AbortStorageTranscodeJobsSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Cancel all transcode jobs linked to the storage

        Args:
            storage_id: ID of the storage
            abort_schema: Abort parameters (either as
                AbortStorageTranscodeJobsSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 User does not exist
        """
        body = (abort_schema.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(abort_schema) else abort_schema)
        url = self.gen_url(f"storages/{storage_id}/")
        resp = self._delete(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def list_storage_edge_transcode_jobs(
        self,
        storage_id: str,
        limit: int = 10,
        **kwargs,
    ) -> Response:
        """
        Get edge transcode jobs from the job queue

        Args:
            storage_id: ID of the storage
            limit: The max number of items to fetch
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=EdgeTranscodeJobsSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        params = {"limit": limit}
        url = self.gen_url(f"storages/{storage_id}/edge_transcode/jobs/")
        resp = self._get(url, params=params, **kwargs)
        return self.parse_response(resp, EdgeTranscodeJobsSchema)

    def delete_storage_file_transcode(
        self,
        storage_id: str,
        file_id: str,
        **kwargs,
    ) -> Response:
        """
        Delete local storage transcode job.

        Args:
            storage_id: ID of the storage
            file_id: ID of the file
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 404 Transcode job does not exist
        """
        url = self.gen_url(f"storages/{storage_id}/files/{file_id}/transcode/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def list_storage_transcode_jobs(
        self,
        storage_id: str,
        per_page: int = 10,
        last_id: Optional[str] = None,
        **kwargs,
    ) -> Response:
        """
        Get pending local storage transcode jobs.

        Args:
            storage_id: ID of the storage
            per_page: The number of items for each page
            last_id: ID of a last transcode job entity on previous page
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=LocalStorageFileTranscodeJobsSchema)
        """
        params: Dict[str, Any] = {"per_page": per_page}
        if last_id is not None:
            params["last_id"] = last_id
        url = self.gen_url(f"storages/{storage_id}/transcode/")
        resp = self._get(url, params=params, **kwargs)
        return self.parse_response(resp, LocalStorageFileTranscodeJobsSchema)

    def get_storage_transcode_job(
        self,
        storage_id: str,
        record_id: str,
        **kwargs,
    ) -> Response:
        """
        Get local storage transcode job.

        Args:
            storage_id: ID of the storage
            record_id: ID of the transcode record
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=LocalStorageFileTranscodeJobSchema)

        Raises:
            - 404 Transcode job does not exist
        """
        url = self.gen_url(f"storages/{storage_id}/transcode/{record_id}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, LocalStorageFileTranscodeJobSchema)

    def delete_storage_transcode_job(
        self,
        storage_id: str,
        record_id: str,
        **kwargs,
    ) -> Response:
        """
        Delete local storage transcode job.

        Args:
            storage_id: ID of the storage
            record_id: ID of the transcode record
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 404 Transcode job does not exist
        """
        url = self.gen_url(f"storages/{storage_id}/transcode/{record_id}/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def create_transcode(
        self,
        job_schema: Union[JobSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Starts a new transcode.

        Args:
            job_schema: Job parameters (either as JobSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=JobSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (job_schema.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(job_schema) else job_schema)
        url = self.gen_url("transcode/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, JobSchema)

    def list_transcode_queue(
        self,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        **kwargs,
    ) -> Response:
        """
        Get all the statuses of the queued transcode jobs

        Args:
            per_page: The number of items for each page
            page: Which page number to fetch
            sort: A comma separated list of fieldnames without spaces.
                object_type,user_id,retry_count,priority,type,status
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=TranscodeQueueSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        params = {}
        if per_page is not None:
            params["per_page"] = per_page
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        url = self.gen_url("transcode/queue/")
        resp = self._get(url, params=params, **kwargs)
        return self.parse_response(resp, TranscodeQueueSchema)

    def list_transcode_queue_system(
        self,
        per_domain_id: Optional[bool] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        sort: Optional[str] = None,
        **kwargs,
    ) -> Response:
        """
        Get the status of the transcode job queues

        Args:
            per_domain_id: Whether to group by domain ID
            per_page: The number of items for each page
            page: Which page number to fetch
            sort: Sort order
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=TranscodeQueueSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        params = {}
        if per_domain_id is not None:
            params["per_domain_id"] = per_domain_id
        if per_page is not None:
            params["per_page"] = per_page
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        url = self.gen_url("transcode/queue/system/")
        resp = self._get(url, params=params, **kwargs)
        return self.parse_response(resp, TranscodeQueueSchema)

    def list_transcode_object_queue_records(
        self,
        object_type: str,
        object_id: str,
        **kwargs,
    ) -> Response:
        """
        Returns list of transcode queue records by object_id

        Args:
            object_type: Type of object
            object_id: ID of the object
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=TranscodeESQueueRecordsSchema)

        Raises:
            - 400 Bad request - malformed parameters
        """
        url = self.gen_url(f"transcode/{object_type}/{object_id}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, TranscodeESQueueRecordsSchema)

    def list_transcode_version_queue_records(
        self,
        object_type: str,
        object_id: str,
        version_id: str,
        **kwargs,
    ) -> Response:
        """
        Returns list of transcode queue records by version_id

        Args:
            object_type: Type of object
            object_id: ID of the object
            version_id: ID of the version
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=TranscodeESQueueRecordsSchema)

        Raises:
            - 400 Bad request - malformed parameters
        """
        url = self.gen_url(
            f"transcode/{object_type}/{object_id}/versions/{version_id}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, TranscodeESQueueRecordsSchema)

    def get_transcode_job(
        self,
        transcode_job_id: str,
        **kwargs,
    ) -> Response:
        """
        Get transcode job

        Args:
            transcode_job_id: ID of the transcode job
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=JobSchema)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        url = self.gen_url(f"transcode/{transcode_job_id}/")
        resp = self._get(url, **kwargs)
        return self.parse_response(resp, JobSchema)

    def delete_transcode_job(
        self,
        transcode_job_id: str,
        **kwargs,
    ) -> Response:
        """
        Cancel a particular transcode job by id

        Args:
            transcode_job_id: ID of the transcode job
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Transcode does not exist
        """
        url = self.gen_url(f"transcode/{transcode_job_id}/")
        resp = self._delete(url, **kwargs)
        return self.parse_response(resp, None)

    def move_transcode_job_position(
        self,
        transcode_job_id: str,
        position: Literal["top", "bottom"],
        **kwargs,
    ) -> Response:
        """
        Move transcode job to top or bottom of the queue

        Args:
            transcode_job_id: ID of the transcode job
            position: Position in the queue ("top" or "bottom")
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Transcode does not exist
        """
        url = self.gen_url(
            f"transcode/{transcode_job_id}/position/{position}/")
        resp = self._post(url, **kwargs)
        return self.parse_response(resp, None)

    def update_transcode_job_priority(
        self,
        transcode_job_id: str,
        priority: int,
        **kwargs,
    ) -> Response:
        """
        Change transcode job priority

        Args:
            transcode_job_id: ID of the transcode job
            priority: Priority level
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Transcode does not exist
        """
        url = self.gen_url(
            f"transcode/{transcode_job_id}/priority/{priority}/")
        resp = self._put(url, **kwargs)
        return self.parse_response(resp, None)

    def transcribe_asset_default_profile(
        self,
        asset_id: str,
        transcribe_schema: Union[TranscribeSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Start a job that sends an asset to default transcription service

        Args:
            asset_id: ID of the asset
            transcribe_schema: Transcribe parameters (either as
                TranscribeSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (transcribe_schema.model_dump(exclude_defaults=exclude_defaults)
                if is_pydantic_model(transcribe_schema) else transcribe_schema)
        url = self.gen_url(f"transcribe/assets/{asset_id}/profiles/default/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, None)

    def transcribe_bulk(
        self,
        bulk_transcribe_schema: Union[BulkTranscribeSchema, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Start a job that sends multiple objects to transcription service

        Args:
            bulk_transcribe_schema: Bulk transcribe parameters (either as
                BulkTranscribeSchema or dict)
            exclude_defaults: Whether to exclude default values when dumping
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=None)

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        body = (bulk_transcribe_schema.model_dump(
            exclude_defaults=exclude_defaults)
                if is_pydantic_model(bulk_transcribe_schema) else
                bulk_transcribe_schema)
        url = self.gen_url("transcribe/bulk/")
        resp = self._post(url, json=body, **kwargs)
        return self.parse_response(resp, None)
