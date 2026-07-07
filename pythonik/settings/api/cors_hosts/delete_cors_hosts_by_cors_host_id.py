from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_cors_hosts_by_cors_host_id_response_default_type_0 import (
    DeleteCorsHostsByCorsHostIdResponseDefaultType0,
)
from ...models.delete_cors_hosts_by_cors_host_id_response_default_type_1 import (
    DeleteCorsHostsByCorsHostIdResponseDefaultType1,
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
) -> (
    Any
    | DeleteCorsHostsByCorsHostIdResponseDefaultType0
    | DeleteCorsHostsByCorsHostIdResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteCorsHostsByCorsHostIdResponseDefaultType0
        | DeleteCorsHostsByCorsHostIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteCorsHostsByCorsHostIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteCorsHostsByCorsHostIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteCorsHostsByCorsHostIdResponseDefaultType0
    | DeleteCorsHostsByCorsHostIdResponseDefaultType1
]:
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
) -> Response[
    Any
    | DeleteCorsHostsByCorsHostIdResponseDefaultType0
    | DeleteCorsHostsByCorsHostIdResponseDefaultType1
]:
    """Delete a particular CORS host by id


    Required roles:
     - can_delete_cors_hosts

    Args:
        cors_host_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteCorsHostsByCorsHostIdResponseDefaultType0 | DeleteCorsHostsByCorsHostIdResponseDefaultType1]
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
) -> (
    Any
    | DeleteCorsHostsByCorsHostIdResponseDefaultType0
    | DeleteCorsHostsByCorsHostIdResponseDefaultType1
    | None
):
    """Delete a particular CORS host by id


    Required roles:
     - can_delete_cors_hosts

    Args:
        cors_host_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteCorsHostsByCorsHostIdResponseDefaultType0 | DeleteCorsHostsByCorsHostIdResponseDefaultType1
    """

    return sync_detailed(
        cors_host_id=cors_host_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cors_host_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteCorsHostsByCorsHostIdResponseDefaultType0
    | DeleteCorsHostsByCorsHostIdResponseDefaultType1
]:
    """Delete a particular CORS host by id


    Required roles:
     - can_delete_cors_hosts

    Args:
        cors_host_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteCorsHostsByCorsHostIdResponseDefaultType0 | DeleteCorsHostsByCorsHostIdResponseDefaultType1]
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
) -> (
    Any
    | DeleteCorsHostsByCorsHostIdResponseDefaultType0
    | DeleteCorsHostsByCorsHostIdResponseDefaultType1
    | None
):
    """Delete a particular CORS host by id


    Required roles:
     - can_delete_cors_hosts

    Args:
        cors_host_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteCorsHostsByCorsHostIdResponseDefaultType0 | DeleteCorsHostsByCorsHostIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            cors_host_id=cors_host_id,
            client=client,
        )
    ).parsed
