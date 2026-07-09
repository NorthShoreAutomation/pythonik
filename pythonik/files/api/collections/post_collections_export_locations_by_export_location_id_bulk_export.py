from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_export_collection_request_schema import (
    BulkExportCollectionRequestSchema,
)
from ...models.post_collections_export_locations_by_export_location_id_bulk_export_response_default import (
    PostCollectionsExportLocationsByExportLocationIdBulkExportResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    export_location_id: str,
    *,
    body: BulkExportCollectionRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["allow_host_transfer"] = allow_host_transfer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/collections/export_locations/{export_location_id}/bulk/export/".format(
            export_location_id=quote(str(export_location_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostCollectionsExportLocationsByExportLocationIdBulkExportResponseDefault:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    response_default = PostCollectionsExportLocationsByExportLocationIdBulkExportResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PostCollectionsExportLocationsByExportLocationIdBulkExportResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    export_location_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkExportCollectionRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[
    Any | PostCollectionsExportLocationsByExportLocationIdBulkExportResponseDefault
]:
    """Export multiple collections.


    Required roles:
     - can_write_exports

    Args:
        export_location_id (str):
        allow_host_transfer (bool | Unset):
        body (BulkExportCollectionRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostCollectionsExportLocationsByExportLocationIdBulkExportResponseDefault]
    """

    kwargs = _get_kwargs(
        export_location_id=export_location_id,
        body=body,
        allow_host_transfer=allow_host_transfer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    export_location_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkExportCollectionRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> (
    Any
    | PostCollectionsExportLocationsByExportLocationIdBulkExportResponseDefault
    | None
):
    """Export multiple collections.


    Required roles:
     - can_write_exports

    Args:
        export_location_id (str):
        allow_host_transfer (bool | Unset):
        body (BulkExportCollectionRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostCollectionsExportLocationsByExportLocationIdBulkExportResponseDefault
    """

    return sync_detailed(
        export_location_id=export_location_id,
        client=client,
        body=body,
        allow_host_transfer=allow_host_transfer,
    ).parsed


async def asyncio_detailed(
    export_location_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkExportCollectionRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[
    Any | PostCollectionsExportLocationsByExportLocationIdBulkExportResponseDefault
]:
    """Export multiple collections.


    Required roles:
     - can_write_exports

    Args:
        export_location_id (str):
        allow_host_transfer (bool | Unset):
        body (BulkExportCollectionRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostCollectionsExportLocationsByExportLocationIdBulkExportResponseDefault]
    """

    kwargs = _get_kwargs(
        export_location_id=export_location_id,
        body=body,
        allow_host_transfer=allow_host_transfer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    export_location_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkExportCollectionRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> (
    Any
    | PostCollectionsExportLocationsByExportLocationIdBulkExportResponseDefault
    | None
):
    """Export multiple collections.


    Required roles:
     - can_write_exports

    Args:
        export_location_id (str):
        allow_host_transfer (bool | Unset):
        body (BulkExportCollectionRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostCollectionsExportLocationsByExportLocationIdBulkExportResponseDefault
    """

    return (
        await asyncio_detailed(
            export_location_id=export_location_id,
            client=client,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )
    ).parsed
