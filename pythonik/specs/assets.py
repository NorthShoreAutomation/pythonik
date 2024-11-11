from pythonik.models.assets.assets import Asset, AssetCreate, BulkDelete
from pythonik.models.assets.segments import SegmentBody, SegmentResponse
from pythonik.models.assets.versions import (
    AssetVersionCreate,
    AssetVersionResponse,
    AssetVersionFromAssetCreate,
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
VERSIONS_FROM_ASSET_URL = BASE + "/{}/versions/from/assets/{}/"
BULK_DELETE_URL = DELETE_QUEUE + "/bulk/"
PURGE_ALL_URL = DELETE_QUEUE + "/purge/all/"


class AssetSpec(Spec):
    server = "API/assets/"

    def __init__(self, session, timeout=3):
        super().__init__(session, timeout)
        self._collection_spec = CollectionSpec(session=session, timeout=timeout)

    @property
    def collections(self) -> CollectionSpec:
        """
        Access the collections API

        Returns:
            CollectionSpec: An instance of CollectionSpec for working with collections
        """
        return self._collection_spec

    def permanently_delete(self):
        """
        Purge all assets and collections from the delete queue (Permanently delete)

        Returns:
            Response with no data model (202 status code)

        Required roles:
            - can_purge_assets
            - can_purge_collections

        Raises:
            401 Invalid token
            403 User does not have permission
        """
        response = self._post(PURGE_ALL_URL)
        return self.parse_response(response, model=None)

    def bulk_delete(
        self,
        body: BulkDelete,
        permanently_delete=False,
        exclude_defaults=True,
        **kwargs
    ) -> Response:
        """
        Bulk delete objects. If `permanently_delete` is True, the objects are
        first added to the delete queue then the queue is purged,
        permanently deleting.

        Args:
            body: bulk delete parameters
            permanently_delete: If True, Purge all assets and collections from
            delete queue (Permanently delete)
            exclude_defaults: If True, exclude default values from request
            kwargs: additional kwargs passed to the request

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
        response = self._post(
            BULK_DELETE_URL,
            json=body.model_dump(exclude_defaults=exclude_defaults),
            **kwargs
        )
        if permanently_delete:
            response  = self.permanently_delete().response
        return self.parse_response(response, model=None)

    def partial_update_asset(
        self, asset_id: str, body: Asset, exclude_defaults=True, **kwargs
    ) -> Response:
        """Partially update an asset using PATCH"""
        response = self._patch(
            GET_URL.format(asset_id),
            json=body.model_dump(exclude_defaults=exclude_defaults),
            **kwargs
        )
        return self.parse_response(response, Asset)

    def get(self, asset_id: str) -> Response:
        """
        Get an iconik asset by id
        Returns: Response(model=Asset)
        """

        resp = self._get(GET_URL.format(asset_id))

        return self.parse_response(resp, Asset)

    def create(self, body: AssetCreate, exclude_defaults=True, **kwargs) -> Response:
        """
        Create a new asset
        Returns: Response(model=Asset)
        """
        response = self._post(
            BASE, json=body.model_dump(exclude_defaults=exclude_defaults), **kwargs
        )
        return self.parse_response(response, Asset)

    def create_segment(
        self, asset_id: str, body: SegmentBody, exclude_defaults=True, **kwargs
    ) -> Response:
        """
        Create a segment on an asset, such as a comment
        Returns: Response(model=SegmentResponse)
        """

        resp = self._post(
            SEGMENT_URL.format(asset_id),
            json=body.model_dump(exclude_defaults=exclude_defaults),
            **kwargs
        )

        return self.parse_response(resp, SegmentResponse)

    def update_segment(
        self,
        asset_id: str,
        segment_id: str,
        body: SegmentBody,
        exclude_defaults=True,
        **kwargs
    ) -> Response:
        """
        Update a segment on an asset, such as a comment, using PUT
        Returns: Response(model=SegmentResponse)

        PUT

        Full Update: PUT is used to update a resource by replacing it with the new data provided in the request.
        It usually requires sending the complete representation of the resource.

        Idempotent: If you perform the same PUT request multiple times,
        the result will be the same. It will replace the resource with the same data every time.

        Complete Resource: Typically, a PUT request contains the entire resource.
        If any fields are omitted in the request, those fields are typically reset to their default values or removed.


        """

        resp = self._put(
            SEGMENT_URL_UPDATE.format(asset_id, segment_id),
            json=body.model_dump(exclude_defaults=exclude_defaults),
            **kwargs
        )

        return self.parse_response(resp, SegmentResponse)

    def partial_update_segment(
        self,
        asset_id: str,
        segment_id: str,
        body: SegmentBody,
        exclude_defaults=True,
        **kwargs
    ) -> Response:
        """
        Partially Update a segment on an asset, such as a comment, using PATCH
        Returns: Response(model=SegmentResponse)

        PATCH
            Partial Update: PATCH is used for partial updates. It allows you to send only the fields that need to be updated,
            leaving the rest of the resource unchanged.

            Not Necessarily Idempotent: While PATCH can be idempotent, it's not guaranteed to be. Multiple identical PATCH requests could result in different states
            if the updates depend on the current state of the resource.

            Sparse Representation: A PATCH request typically contains only the fields that need to be modified.
        """

        resp = self._patch(
            SEGMENT_URL_UPDATE.format(asset_id, segment_id),
            json=body.model_dump(exclude_defaults=exclude_defaults),
            **kwargs
        )

        return self.parse_response(resp, SegmentResponse)

    def create_version(
        self, asset_id: str, body: AssetVersionCreate, exclude_defaults=True, **kwargs
    ) -> Response:
        """
        Create a new version of an asset

        Args:
            asset_id: The ID of the asset to create a version for
            body: Version creation parameters
            exclude_defaults: If True, exclude default values from request
            **kwargs: Additional arguments to pass to the request

        Returns:
            Response(model=AssetVersionResponse)

        Required roles:
            - can_write_versions
        """
        response = self._post(
            VERSIONS_URL.format(asset_id),
            json=body.model_dump(exclude_defaults=exclude_defaults),
            **kwargs
        )
        return self.parse_response(response, AssetVersionResponse)

    def create_version_from_asset(
        self,
        asset_id: str,
        source_asset_id: str,
        body: AssetVersionFromAssetCreate,
        exclude_defaults=True,
        **kwargs
    ) -> Response:
        """
        Create a new version of an asset from another asset

        Args:
            asset_id: The ID of the asset to create a version for
            source_asset_id: The ID of the source asset to create version from
            body: Version creation parameters
            exclude_defaults: If True, exclude default values from request
            **kwargs: Additional arguments to pass to the request

        Returns:
            Response with no data model (202 status code)

        Required roles:
            - can_write_versions

        Raises:
            - 400: Bad request
            - 401: Token is invalid
            - 404: Source or destination asset does not exist
            - 409: The asset is being transcoded and cannot be set as a new version
        """
        response = self._post(
            VERSIONS_FROM_ASSET_URL.format(asset_id, source_asset_id),
            json=body.model_dump(exclude_defaults=exclude_defaults),
            **kwargs
        )
        # Since this returns 202 with no content, we don't need a response model
        return self.parse_response(response, model=None)
