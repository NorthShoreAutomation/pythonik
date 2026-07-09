from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_cors_hosts_by_cors_host_id_response_default import (
    DeleteCorsHostsByCorsHostIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    cors_host_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/cors_hosts/{cors_host_id}/".format(
            cors_host_id=quote(str(cors_host_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteCorsHostsByCorsHostIdResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = DeleteCorsHostsByCorsHostIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteCorsHostsByCorsHostIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cors_host_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteCorsHostsByCorsHostIdResponseDefault]:
    """Delete a particular CORS host by id


    Required roles:
     - can_delete_cors_hosts

    Args:
        cors_host_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteCorsHostsByCorsHostIdResponseDefault]
    """

    kwargs = _get_kwargs(
        cors_host_id=cors_host_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cors_host_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteCorsHostsByCorsHostIdResponseDefault | None:
    """Delete a particular CORS host by id


    Required roles:
     - can_delete_cors_hosts

    Args:
        cors_host_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteCorsHostsByCorsHostIdResponseDefault
    """

    return sync_detailed(
        cors_host_id=cors_host_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cors_host_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteCorsHostsByCorsHostIdResponseDefault]:
    """Delete a particular CORS host by id


    Required roles:
     - can_delete_cors_hosts

    Args:
        cors_host_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteCorsHostsByCorsHostIdResponseDefault]
    """

    kwargs = _get_kwargs(
        cors_host_id=cors_host_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cors_host_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteCorsHostsByCorsHostIdResponseDefault | None:
    """Delete a particular CORS host by id


    Required roles:
     - can_delete_cors_hosts

    Args:
        cors_host_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteCorsHostsByCorsHostIdResponseDefault
    """

    return (
        await asyncio_detailed(
            cors_host_id=cors_host_id,
            client=client,
        )
    ).parsed
