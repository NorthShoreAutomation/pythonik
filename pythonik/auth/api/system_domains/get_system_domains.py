from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_system_domains_response_default import (
    GetSystemDomainsResponseDefault,
)
from ...models.system_domains_schema import SystemDomainsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["query"] = query

    params["statuses"] = statuses

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/system_domains/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSystemDomainsResponseDefault | SystemDomainsSchema:
    if response.status_code == 200:
        response_200 = SystemDomainsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetSystemDomainsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetSystemDomainsResponseDefault | SystemDomainsSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
) -> Response[Any | GetSystemDomainsResponseDefault | SystemDomainsSchema]:
    """List of system domains

    Args:
        query (str | Unset):
        statuses (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSystemDomainsResponseDefault | SystemDomainsSchema]
    """

    kwargs = _get_kwargs(
        query=query,
        statuses=statuses,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
) -> Any | GetSystemDomainsResponseDefault | SystemDomainsSchema | None:
    """List of system domains

    Args:
        query (str | Unset):
        statuses (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSystemDomainsResponseDefault | SystemDomainsSchema
    """

    return sync_detailed(
        client=client,
        query=query,
        statuses=statuses,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
) -> Response[Any | GetSystemDomainsResponseDefault | SystemDomainsSchema]:
    """List of system domains

    Args:
        query (str | Unset):
        statuses (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSystemDomainsResponseDefault | SystemDomainsSchema]
    """

    kwargs = _get_kwargs(
        query=query,
        statuses=statuses,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
) -> Any | GetSystemDomainsResponseDefault | SystemDomainsSchema | None:
    """List of system domains

    Args:
        query (str | Unset):
        statuses (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSystemDomainsResponseDefault | SystemDomainsSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            statuses=statuses,
        )
    ).parsed
