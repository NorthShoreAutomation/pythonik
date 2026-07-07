from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_system_domains_search_response_default_type_0 import (
    GetSystemDomainsSearchResponseDefaultType0,
)
from ...models.get_system_domains_search_response_default_type_1 import (
    GetSystemDomainsSearchResponseDefaultType1,
)
from ...models.system_domains_schema import SystemDomainsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
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
) -> (
    Any
    | GetSystemDomainsSearchResponseDefaultType0
    | GetSystemDomainsSearchResponseDefaultType1
    | SystemDomainsSchema
):
    if response.status_code == 200:
        response_200 = SystemDomainsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        GetSystemDomainsSearchResponseDefaultType0
        | GetSystemDomainsSearchResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetSystemDomainsSearchResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetSystemDomainsSearchResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSystemDomainsSearchResponseDefaultType0
    | GetSystemDomainsSearchResponseDefaultType1
    | SystemDomainsSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
    types: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> Response[
    Any
    | GetSystemDomainsSearchResponseDefaultType0
    | GetSystemDomainsSearchResponseDefaultType1
    | SystemDomainsSchema
]:
    """List of system domains from Elasticsearch

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        sort (str | Unset):
        query (str | Unset):
        statuses (str | Unset):
        types (str | Unset):
        field_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSystemDomainsSearchResponseDefaultType0 | GetSystemDomainsSearchResponseDefaultType1 | SystemDomainsSchema]
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
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
    types: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> (
    Any
    | GetSystemDomainsSearchResponseDefaultType0
    | GetSystemDomainsSearchResponseDefaultType1
    | SystemDomainsSchema
    | None
):
    """List of system domains from Elasticsearch

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        sort (str | Unset):
        query (str | Unset):
        statuses (str | Unset):
        types (str | Unset):
        field_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSystemDomainsSearchResponseDefaultType0 | GetSystemDomainsSearchResponseDefaultType1 | SystemDomainsSchema
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
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
    types: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> Response[
    Any
    | GetSystemDomainsSearchResponseDefaultType0
    | GetSystemDomainsSearchResponseDefaultType1
    | SystemDomainsSchema
]:
    """List of system domains from Elasticsearch

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        sort (str | Unset):
        query (str | Unset):
        statuses (str | Unset):
        types (str | Unset):
        field_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSystemDomainsSearchResponseDefaultType0 | GetSystemDomainsSearchResponseDefaultType1 | SystemDomainsSchema]
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
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
    types: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> (
    Any
    | GetSystemDomainsSearchResponseDefaultType0
    | GetSystemDomainsSearchResponseDefaultType1
    | SystemDomainsSchema
    | None
):
    """List of system domains from Elasticsearch

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        sort (str | Unset):
        query (str | Unset):
        statuses (str | Unset):
        types (str | Unset):
        field_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSystemDomainsSearchResponseDefaultType0 | GetSystemDomainsSearchResponseDefaultType1 | SystemDomainsSchema
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
