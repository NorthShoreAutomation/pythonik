from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.current_usage_schema import CurrentUsageSchema
from ...models.get_current_usage_response_default import GetCurrentUsageResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/current_usage/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CurrentUsageSchema | GetCurrentUsageResponseDefault:
    if response.status_code == 200:
        response_200 = CurrentUsageSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = GetCurrentUsageResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CurrentUsageSchema | GetCurrentUsageResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
) -> Response[Any | CurrentUsageSchema | GetCurrentUsageResponseDefault]:
    """Returns current usage for system domains


    Required roles:
     - can_read_stats

    Args:
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CurrentUsageSchema | GetCurrentUsageResponseDefault]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
) -> Any | CurrentUsageSchema | GetCurrentUsageResponseDefault | None:
    """Returns current usage for system domains


    Required roles:
     - can_read_stats

    Args:
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CurrentUsageSchema | GetCurrentUsageResponseDefault
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
) -> Response[Any | CurrentUsageSchema | GetCurrentUsageResponseDefault]:
    """Returns current usage for system domains


    Required roles:
     - can_read_stats

    Args:
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CurrentUsageSchema | GetCurrentUsageResponseDefault]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
) -> Any | CurrentUsageSchema | GetCurrentUsageResponseDefault | None:
    """Returns current usage for system domains


    Required roles:
     - can_read_stats

    Args:
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CurrentUsageSchema | GetCurrentUsageResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
        )
    ).parsed
