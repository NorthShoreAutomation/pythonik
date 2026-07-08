from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_export_locations_by_export_location_id_reindex_response_default import (
    PostExportLocationsByExportLocationIdReindexResponseDefault,
)
from ...types import Response


def _get_kwargs(
    export_location_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/export_locations/{export_location_id}/reindex/".format(
            export_location_id=quote(str(export_location_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostExportLocationsByExportLocationIdReindexResponseDefault:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        PostExportLocationsByExportLocationIdReindexResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostExportLocationsByExportLocationIdReindexResponseDefault]:
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
) -> Response[Any | PostExportLocationsByExportLocationIdReindexResponseDefault]:
    """Trigger reindexing of a export location


    Required roles:
     - can_reindex_export_locations

    Args:
        export_location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostExportLocationsByExportLocationIdReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        export_location_id=export_location_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    export_location_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PostExportLocationsByExportLocationIdReindexResponseDefault | None:
    """Trigger reindexing of a export location


    Required roles:
     - can_reindex_export_locations

    Args:
        export_location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostExportLocationsByExportLocationIdReindexResponseDefault
    """

    return sync_detailed(
        export_location_id=export_location_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    export_location_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PostExportLocationsByExportLocationIdReindexResponseDefault]:
    """Trigger reindexing of a export location


    Required roles:
     - can_reindex_export_locations

    Args:
        export_location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostExportLocationsByExportLocationIdReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        export_location_id=export_location_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    export_location_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PostExportLocationsByExportLocationIdReindexResponseDefault | None:
    """Trigger reindexing of a export location


    Required roles:
     - can_reindex_export_locations

    Args:
        export_location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostExportLocationsByExportLocationIdReindexResponseDefault
    """

    return (
        await asyncio_detailed(
            export_location_id=export_location_id,
            client=client,
        )
    ).parsed
