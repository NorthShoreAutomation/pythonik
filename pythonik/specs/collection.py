from typing import Union, Dict, Any

from pythonik.specs.base import Spec
from pythonik.models.base import Response
from pythonik.models.assets.collections import (
    Collection,
    CollectionContents,
    CollectionContentInfo,
    Content,
    AddContentResponse
)

BASE = "collections"
GET_URL = BASE + "/{}/"
GET_INFO = GET_URL + "content/info"
GET_CONTENTS = GET_URL + "contents"
POST_CONTENT = GET_CONTENTS


class CollectionSpec(Spec):
    server = "API/assets/"

    def delete(self, collection_id: str, **kwargs) -> Response:
        """
        Delete a collection

        Args:
            collection_id: The ID of the collection to delete
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response with no data model (202 status code)

        Required roles:
            - can_delete_collections

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Collection does not exist
        """
        resp = self._delete(GET_URL.format(collection_id), **kwargs)
        return self.parse_response(resp, None)

    def get(self, collection_id: str, **kwargs) -> Response:
        """
        Retrieve a specific collection by ID

        Args:
            collection_id: The ID of the collection to retrieve
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=Collection)

        Required roles:
            - can_read_collections

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Collection does not exist
        """
        resp = self._get(GET_URL.format(collection_id), **kwargs)
        return self.parse_response(resp, Collection)

    def get_info(self, collection_id: str, **kwargs) -> Response:
        """
        Returns all sub-collections and assets count for a specific collection

        Args:
            collection_id: The ID of the collection to retrieve
            **kwargs: Additional kwargs to pass to the request

        Response:
            Response(model=CollectionContentInfo)

        Required roles:
            - can_read_collections

        Raise:
            - 400 Bad request
            - 401 Token is invalid
        """
        resp = self._get(GET_INFO.format(collection_id), **kwargs)
        return self.parse_response(resp, CollectionContentInfo)

    def get_contents(self, collection_id: str, **kwargs) -> Response:
        """
        Retrieve the contents of a specific collection

        Args:
            collection_id: The ID of the collection
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=CollectionContents)

        Required roles:
            - can_read_collections

        Raises:
            - 400 Bad request
            - 401 Token is invalid
            - 404 Collection does not exist
        """
        resp = self._get(GET_CONTENTS.format(collection_id), **kwargs)
        return self.parse_response(resp, CollectionContents)

    def create(
        self,
        body: Union[Collection, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs
    ) -> Response:
        """
        Create a new collection

        Args:
            body: Collection creation parameters, either as Collection model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response(model=Collection)

        Required roles:
            - can_create_collections

        Raises:
            - 400 Bad request
            - 401 Token is invalid
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._post(BASE, json=json_data, **kwargs)
        return self.parse_response(response, Collection)

    def add_content(
        self,
        collection_id: str,
        body: Union[Content, Dict[str, Any]],
        exclude_defaults: bool = True,
        **kwargs
    ) -> Response:
        """Add an object to a collection.

        Args:
            collection_id: The ID of the collection to add content to
            body: The content object containing object_id and object_type, either as Content model or dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            **kwargs: Additional kwargs to pass to the request

        Returns:
            Response[Collection]: The updated collection object

        Response Codes:
            201: Content added successfully
            400: Bad request
            401: Token is invalid
            404: Collection not found
        """
        json_data = self._prepare_model_data(body, exclude_defaults=exclude_defaults)
        response = self._post(
            POST_CONTENT.format(collection_id),
            json=json_data,
            **kwargs,
        )
        return self.parse_response(response, AddContentResponse)
