from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_export_locations_by_export_location_id_response_default import (
    DeleteExportLocationsByExportLocationIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    export_location_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/export_locations/{export_location_id}/".format(
            export_location_id=quote(str(export_location_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteExportLocationsByExportLocationIdResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = DeleteExportLocationsByExportLocationIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteExportLocationsByExportLocationIdResponseDefault]:
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
) -> Response[Any | DeleteExportLocationsByExportLocationIdResponseDefault]:
    """Delete a particular export_location by id


    Required roles:
     - can_delete_export_locations

    Args:
        export_location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteExportLocationsByExportLocationIdResponseDefault]
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
) -> Any | DeleteExportLocationsByExportLocationIdResponseDefault | None:
    """Delete a particular export_location by id


    Required roles:
     - can_delete_export_locations

    Args:
        export_location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteExportLocationsByExportLocationIdResponseDefault
    """

    return sync_detailed(
        export_location_id=export_location_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    export_location_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteExportLocationsByExportLocationIdResponseDefault]:
    """Delete a particular export_location by id


    Required roles:
     - can_delete_export_locations

    Args:
        export_location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteExportLocationsByExportLocationIdResponseDefault]
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
) -> Any | DeleteExportLocationsByExportLocationIdResponseDefault | None:
    """Delete a particular export_location by id


    Required roles:
     - can_delete_export_locations

    Args:
        export_location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteExportLocationsByExportLocationIdResponseDefault
    """

    return (
        await asyncio_detailed(
            export_location_id=export_location_id,
            client=client,
        )
    ).parsed
