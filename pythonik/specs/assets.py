from typing import Union, Dict, Any

from pythonik.models.assets.assets import Asset, AssetCreate, BulkDelete
from pythonik.models.assets.segments import (
    SegmentBody,
    SegmentResponse,
    BulkDeleteSegmentsBody,
)
from pythonik.models.assets.versions import (
    AssetVersionCreate,
    AssetVersionResponse,
    AssetVersionFromAssetCreate,
    AssetVersion,
)
from pythonik.models.base import Response
from pythonik.specs.base import Spec
from pythonik.specs.collection import CollectionSpec

BASE = "assets"
DELETE_QUEUE = "delete_queue"
GET_URL = BASE + "/{}/"
SEGMENT_URL = BASE + "/{}/segments/"
SEGMENT_URL_UPDATE = SEGMENT_URL + "{}/"
VERSIONS_URL = BASE + "/{}/versions/"
VERSION_URL = VERSIONS_URL + "{}/"
VERSION_PROMOTE_URL = VERSION_URL + "promote/"
VERSION_OLD_URL = VERSIONS_URL + "old/"
VERSIONS_FROM_ASSET_URL = BASE + "/{}/versions/from/assets/{}/"
BULK_DELETE_URL = DELETE_QUEUE + "/bulk/"
PURGE_ALL_URL = DELETE_QUEUE + "/purge/all/"
BULK_DELETE_SEGMENTS_URL = SEGMENT_URL + "bulk/"


class AssetSpec(Spec):
    server = "API/assets/"

    def __init__(self, session, timeout=3, base_url: str = "https://app.iconik.io"):
        self._collection_spec = CollectionSpec(session=session, timeout=timeout)
        return super().__init__(session, timeout, base_url)

    @property
    def collections(self) -> CollectionSpec:
        """
        Access the collections API

        Returns:
            CollectionSpec: An instance of CollectionSpec for working with collections
        """
        return self._collection_spec

    def permanently_delete(self, **kwargs) -> Response:
        """
        Purge all assets and collections from the delete queue (Permanently delete)

        Args:
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response with no data model (202 status code)

        Required roles:
            - can_purge_assets
            - can_purge_collections

        Raises:
            401 Invalid token
            403 User does not have permission
        """
        response = self._post(PURGE_ALL_URL, **kwargs)
        return self.parse_response(response, model=None)

    def bulk_delete(
        self,
        body: Union[BulkDelete, Dict[str, Any]],
        permanently_delete=False,
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Bulk delete objects. If `permanently_delete` is True, the objects are
        first added to the delete queue then the queue is purged,
        permanently deleting.

        Args:
            body: Bulk delete parameters, either as BulkDelete model or dict
            permanently_delete: If True, Purge all assets and collections from
                delete queue (Permanently delete)
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response with no data model (202 status code)

        Required roles:
            - To bulk delete objects:
                - can_delete_assets
            - To permanently delete objects:
                - can_purge_assets
                - can_purge_collections

        Raises:
            400 Bad request
            401 Invalid token
            403 User does not have permission
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._post(BULK_DELETE_URL, json=json_data, **kwargs)
        if permanently_delete:
            response = self.permanently_delete().response
        return self.parse_response(response, model=None)

    def partial_update_asset(
        self,
        asset_id: str,
        body: Union[Asset, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """Partially update an asset using PATCH

        Args:
            asset_id: The asset ID to update
            body: Asset data to update, either as Asset model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._patch(GET_URL.format(asset_id), json=json_data, **kwargs)
        return self.parse_response(response, Asset)

    def get(self, asset_id: str, **kwargs) -> Response:
        """
        Get an iconik asset by id

        Args:
            asset_id: The asset ID to get
            **kwargs: Additional kwargs to pass to the request

        Returns: Response(model=Asset)
        """
        resp = self._get(GET_URL.format(asset_id), **kwargs)
        return self.parse_response(resp, Asset)

    def create(
        self,
        body: Union[AssetCreate, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new asset

        Args:
            body: Asset creation parameters, either as AssetCreate model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request

        Returns: Response(model=Asset)
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._post(BASE, json=json_data, **kwargs)
        return self.parse_response(response, Asset)

    def create_segment(
        self,
        asset_id: str,
        body: Union[SegmentBody, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a segment on an asset, such as a comment

        Args:
            asset_id: The asset ID to create segment for
            body: Segment data, either as SegmentBody model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        resp = self._post(SEGMENT_URL.format(asset_id), json=json_data, **kwargs)

        return self.parse_response(resp, SegmentResponse)

    def update_segment(
        self,
        asset_id: str,
        segment_id: str,
        body: Union[SegmentBody, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Update a segment on an asset

        Args:
            asset_id: The asset ID to update segment for
            segment_id: The segment ID to update
            body: Segment data, either as SegmentBody model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request

        Note:
            Full Representation: A PUT request requires a complete representation of the segment.
            If you want to update only specific fields, use partial_update_segment instead.
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        resp = self._put(
            SEGMENT_URL_UPDATE.format(asset_id, segment_id), json=json_data, **kwargs
        )

        return self.parse_response(resp, SegmentResponse)

    def partial_update_segment(
        self,
        asset_id: str,
        segment_id: str,
        body: Union[SegmentBody, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Partially update a segment on an asset

        Args:
            asset_id: The asset ID to update segment for
            segment_id: The segment ID to update
            body: Segment data, either as SegmentBody model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request

        Note:
            Sparse Representation: A PATCH request typically contains only the fields that need to be modified.
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        resp = self._patch(
            SEGMENT_URL_UPDATE.format(asset_id, segment_id), json=json_data, **kwargs
        )

        return self.parse_response(resp, SegmentResponse)

    def bulk_delete_segments(
        self,
        asset_id: str,
        body: Union[BulkDeleteSegmentsBody, Dict[str, Any]],
        immediately: bool = True,
        ignore_reindexing: bool = False,
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Delete segments with either ids or by type.

        Args:
            asset_id: The ID of the asset containing the segments.
            body: Request body containing segment_ids or segment_type, and optionally version_id.
                  Can be BulkDeleteSegmentsBody model or dict.
            immediately: If True, delete segments synchronously. If False, delete asynchronously.
            ignore_reindexing: If True, skip reindexing after deletion.
            exclude_defaults: Whether to exclude default values when dumping Pydantic models.
            **kwargs: Additional kwargs to pass to the request.

        Returns:
            Response with no data model (204 status code).

        Required roles:
            - can_delete_segments

        Raises:
            400 Segment ids or segment type not provided correctly
            401 Token is invalid
            403 User does not have permission (Implicit from required roles)
            404 No segments found
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        params = {"immediately": immediately, "ignore_reindexing": ignore_reindexing}
        response = self._delete(
            BULK_DELETE_SEGMENTS_URL.format(asset_id),
            json=json_data,
            params=params,
            **kwargs,
        )
        # Expects 204 No Content on success
        return self.parse_response(response, model=None)

    def delete_segment(
        self, asset_id: str, segment_id: str, soft_delete: bool = True, **kwargs
    ) -> Response:
        """
        Delete a particular segment from an asset by id.

        Args:
            asset_id: The ID of the asset containing the segment.
            segment_id: The ID of the segment to delete.
            soft_delete: Query parameter to control soft/hard delete.
            **kwargs: Additional kwargs to pass to the request.

        Returns:
            Response with no data model (204 status code).

        Required roles:
            - can_delete_segments

        Raises:
            401 Token is invalid
            403 User does not have permission (Implicit from required roles)
            404 Segment not found
        """
        params = {"soft_delete": soft_delete}
        response = self._delete(
            SEGMENT_URL_UPDATE.format(asset_id, segment_id), params=params, **kwargs
        )
        # Expects 204 No Content on success
        return self.parse_response(response, model=None)

    def create_version(
        self,
        asset_id: str,
        body: Union[AssetVersionCreate, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new version of an asset

        Args:
            asset_id: The ID of the asset to create a version for
            body: Version creation parameters, either as AssetVersionCreate model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response[AssetVersionResponse]

        Required roles:
            - can_write_versions
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._post(VERSIONS_URL.format(asset_id), json=json_data, **kwargs)
        return self.parse_response(response, AssetVersionResponse)

    def create_version_from_asset(
        self,
        asset_id: str,
        source_asset_id: str,
        body: Union[AssetVersionFromAssetCreate, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:
        """
        Create a new version of an asset from another asset

        Args:
            asset_id: The ID of the asset to create a version for
            source_asset_id: The ID of the source asset to create version from
            body: Version creation parameters, either as AssetVersionFromAssetCreate model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response with no data model (202 status code)

        Required roles:
            - can_write_versions

        Raises:
            - 400: Bad request
            - 401: Invalid token
            - 403: User does not have permission
            - 404: Source or destination asset does not exist
            - 409: The asset is being transcoded and cannot be set as a new version
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._post(
            VERSIONS_FROM_ASSET_URL.format(asset_id, source_asset_id),
            json=json_data,
            **kwargs,
        )
        # Since this returns 202 with no content, we don't need a response model
        return self.parse_response(response, None)

    def delete(self, asset_id: str, **kwargs) -> Response:
        """
        Delete a particular asset by id

        Args:
            asset_id: ID of the asset to delete
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response with no data model (204 status code)

        Required roles:
            - can_delete_assets

        Raises:
            400 Bad request
            401 Token is invalid
            403 Forbidden
            404 Asset does not exist
        """
        response = self._delete(GET_URL.format(asset_id), **kwargs)
        return self.parse_response(response, model=None)

    def partial_update_version(
        self, asset_id: str, version_id: str, body: AssetVersion, **kwargs
    ) -> Response:
        """
        Partially update an asset version.

        Args:
            asset_id: The ID of the asset
            version_id: The ID of the version
            body: The version data to update
        """
        response = self._patch(
            VERSION_URL.format(asset_id, version_id),
            json=self._prepare_model_data(body),
        )
        return self.parse_response(response, AssetVersionResponse)

    def update_version(
        self, asset_id: str, version_id: str, body: AssetVersion, **kwargs
    ) -> Response:
        """
        Update an asset version.

        Args:
            asset_id: The ID of the asset
            version_id: The ID of the version
            body: The version data to update
        """
        response = self._put(
            VERSION_URL.format(asset_id, version_id),
            json=self._prepare_model_data(body),
        )
        return self.parse_response(response, AssetVersionResponse)

    def promote_version(self, asset_id: str, version_id: str, **kwargs) -> Response:
        """
        Promote a particular asset version to latest version

        Args:
            asset_id: The asset ID to promote version for
            version_id: The version ID to promote
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response with no data model (204 status code)

        Required roles:
            - can_write_versions

        Raises:
            400 Bad request
            401 Token is invalid
            404 Asset does not exist
        """
        response = self._put(VERSION_PROMOTE_URL.format(asset_id, version_id), **kwargs)
        return self.parse_response(response, None)

    def delete_old_versions(self, asset_id: str, **kwargs) -> Response:
        """
        Delete all asset versions except the latest one

        Args:
            asset_id: The asset ID to delete old versions for
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response with no data model (204 status code)

        Required roles:
            - can_delete_versions

        Raises:
            400 Bad request
            401 Token is invalid
            403 Forbidden
            404 Asset does not exist
        """
        response = self._delete(VERSION_OLD_URL.format(asset_id), **kwargs)
        return self.parse_response(response, None)

    def delete_version(
        self, asset_id: str, version_id: str, hard_delete: bool = False, **kwargs
    ) -> Response:
        """
        Delete a particular asset version by id

        Args:
            asset_id: The asset ID to delete version from
            version_id: The version ID to delete
            hard_delete: If True, completely remove the version
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response with no data model (204 status code)

        Required roles:
            - can_delete_versions

        Raises:
            400 Bad request
            401 Token is invalid
            403 Forbidden
            404 Asset does not exist
        """
        params = {"hard_delete": hard_delete} if hard_delete else None
        response = self._delete(
            VERSION_URL.format(asset_id, version_id), params=params, **kwargs
        )
        return self.parse_response(response, None)
