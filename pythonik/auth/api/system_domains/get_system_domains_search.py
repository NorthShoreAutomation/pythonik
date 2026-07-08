from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_system_domains_search_response_default import (
    GetSystemDomainsSearchResponseDefault,
)
from ...models.system_domains_schema import SystemDomainsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
    types: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["sort"] = sort

    params["query"] = query

    params["statuses"] = statuses

    params["types"] = types

    params["field_name"] = field_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/system_domains/search/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSystemDomainsSearchResponseDefault | SystemDomainsSchema:
    if response.status_code == 200:
        response_200 = SystemDomainsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetSystemDomainsSearchResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetSystemDomainsSearchResponseDefault | SystemDomainsSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
    types: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> Response[Any | GetSystemDomainsSearchResponseDefault | SystemDomainsSchema]:
    """List of system domains from Elasticsearch

    Args:
        page (int | Unset):
        per_page (int | Unset):
        sort (str | Unset):
        query (str | Unset):
        statuses (str | Unset):
        types (str | Unset):
        field_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSystemDomainsSearchResponseDefault | SystemDomainsSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        sort=sort,
        query=query,
        statuses=statuses,
        types=types,
        field_name=field_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
    types: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> Any | GetSystemDomainsSearchResponseDefault | SystemDomainsSchema | None:
    """List of system domains from Elasticsearch

    Args:
        page (int | Unset):
        per_page (int | Unset):
        sort (str | Unset):
        query (str | Unset):
        statuses (str | Unset):
        types (str | Unset):
        field_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSystemDomainsSearchResponseDefault | SystemDomainsSchema
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        sort=sort,
        query=query,
        statuses=statuses,
        types=types,
        field_name=field_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
    types: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> Response[Any | GetSystemDomainsSearchResponseDefault | SystemDomainsSchema]:
    """List of system domains from Elasticsearch

    Args:
        page (int | Unset):
        per_page (int | Unset):
        sort (str | Unset):
        query (str | Unset):
        statuses (str | Unset):
        types (str | Unset):
        field_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSystemDomainsSearchResponseDefault | SystemDomainsSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        sort=sort,
        query=query,
        statuses=statuses,
        types=types,
        field_name=field_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
    types: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> Any | GetSystemDomainsSearchResponseDefault | SystemDomainsSchema | None:
    """List of system domains from Elasticsearch

    Args:
        page (int | Unset):
        per_page (int | Unset):
        sort (str | Unset):
        query (str | Unset):
        statuses (str | Unset):
        types (str | Unset):
        field_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSystemDomainsSearchResponseDefault | SystemDomainsSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            sort=sort,
            query=query,
            statuses=statuses,
            types=types,
            field_name=field_name,
        )
    ).parsed
