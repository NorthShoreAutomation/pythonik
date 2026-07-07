from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.collection_metadata_values_batch_schema import (
    CollectionMetadataValuesBatchSchema,
)
from ...models.put_by_object_type_content_views_by_view_id_response_default_type_0 import (
    PutByObjectTypeContentViewsByViewIdResponseDefaultType0,
)
from ...models.put_by_object_type_content_views_by_view_id_response_default_type_1 import (
    PutByObjectTypeContentViewsByViewIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    object_type: str,
    view_id: str,
    *,
    body: CollectionMetadataValuesBatchSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/{object_type}/content/views/{view_id}/".format(
            object_type=quote(str(object_type), safe=""),
            view_id=quote(str(view_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PutByObjectTypeContentViewsByViewIdResponseDefaultType0
    | PutByObjectTypeContentViewsByViewIdResponseDefaultType1
):
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        PutByObjectTypeContentViewsByViewIdResponseDefaultType0
        | PutByObjectTypeContentViewsByViewIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PutByObjectTypeContentViewsByViewIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PutByObjectTypeContentViewsByViewIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PutByObjectTypeContentViewsByViewIdResponseDefaultType0
    | PutByObjectTypeContentViewsByViewIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_type: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CollectionMetadataValuesBatchSchema,
) -> Response[
    Any
    | PutByObjectTypeContentViewsByViewIdResponseDefaultType0
    | PutByObjectTypeContentViewsByViewIdResponseDefaultType1
]:
    """Edit view metadata values for collection or saved search content.


    Required roles:
     - can_write_metadata_values

    Args:
        object_type (str):
        view_id (str):
        body (CollectionMetadataValuesBatchSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutByObjectTypeContentViewsByViewIdResponseDefaultType0 | PutByObjectTypeContentViewsByViewIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        view_id=view_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CollectionMetadataValuesBatchSchema,
) -> (
    Any
    | PutByObjectTypeContentViewsByViewIdResponseDefaultType0
    | PutByObjectTypeContentViewsByViewIdResponseDefaultType1
    | None
):
    """Edit view metadata values for collection or saved search content.


    Required roles:
     - can_write_metadata_values

    Args:
        object_type (str):
        view_id (str):
        body (CollectionMetadataValuesBatchSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutByObjectTypeContentViewsByViewIdResponseDefaultType0 | PutByObjectTypeContentViewsByViewIdResponseDefaultType1
    """

    return sync_detailed(
        object_type=object_type,
        view_id=view_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CollectionMetadataValuesBatchSchema,
) -> Response[
    Any
    | PutByObjectTypeContentViewsByViewIdResponseDefaultType0
    | PutByObjectTypeContentViewsByViewIdResponseDefaultType1
]:
    """Edit view metadata values for collection or saved search content.


    Required roles:
     - can_write_metadata_values

    Args:
        object_type (str):
        view_id (str):
        body (CollectionMetadataValuesBatchSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutByObjectTypeContentViewsByViewIdResponseDefaultType0 | PutByObjectTypeContentViewsByViewIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        view_id=view_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CollectionMetadataValuesBatchSchema,
) -> (
    Any
    | PutByObjectTypeContentViewsByViewIdResponseDefaultType0
    | PutByObjectTypeContentViewsByViewIdResponseDefaultType1
    | None
):
    """Edit view metadata values for collection or saved search content.


    Required roles:
     - can_write_metadata_values

    Args:
        object_type (str):
        view_id (str):
        body (CollectionMetadataValuesBatchSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutByObjectTypeContentViewsByViewIdResponseDefaultType0 | PutByObjectTypeContentViewsByViewIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            view_id=view_id,
            client=client,
            body=body,
        )
    ).parsed
