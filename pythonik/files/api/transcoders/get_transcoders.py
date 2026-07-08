from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_transcoders_response_default import GetTranscodersResponseDefault
from ...models.transcoders_schema import TranscodersSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    include_storages: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params["query"] = query

    params["ids"] = ids

    params["sort"] = sort

    params["include_storages"] = include_storages

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/transcoders/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetTranscodersResponseDefault | TranscodersSchema:
    if response.status_code == 200:
        response_200 = TranscodersSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetTranscodersResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetTranscodersResponseDefault | TranscodersSchema]:
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
    page: int | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    include_storages: bool | Unset = UNSET,
) -> Response[Any | GetTranscodersResponseDefault | TranscodersSchema]:
    """Get all transcoders


    Required roles:
     - can_read_transcoders

    Args:
        per_page (int | Unset):
        page (int | Unset):
        query (str | Unset):
        ids (str | Unset):
        sort (str | Unset):
        include_storages (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTranscodersResponseDefault | TranscodersSchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        query=query,
        ids=ids,
        sort=sort,
        include_storages=include_storages,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    include_storages: bool | Unset = UNSET,
) -> Any | GetTranscodersResponseDefault | TranscodersSchema | None:
    """Get all transcoders


    Required roles:
     - can_read_transcoders

    Args:
        per_page (int | Unset):
        page (int | Unset):
        query (str | Unset):
        ids (str | Unset):
        sort (str | Unset):
        include_storages (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTranscodersResponseDefault | TranscodersSchema
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        page=page,
        query=query,
        ids=ids,
        sort=sort,
        include_storages=include_storages,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    include_storages: bool | Unset = UNSET,
) -> Response[Any | GetTranscodersResponseDefault | TranscodersSchema]:
    """Get all transcoders


    Required roles:
     - can_read_transcoders

    Args:
        per_page (int | Unset):
        page (int | Unset):
        query (str | Unset):
        ids (str | Unset):
        sort (str | Unset):
        include_storages (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTranscodersResponseDefault | TranscodersSchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        query=query,
        ids=ids,
        sort=sort,
        include_storages=include_storages,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    include_storages: bool | Unset = UNSET,
) -> Any | GetTranscodersResponseDefault | TranscodersSchema | None:
    """Get all transcoders


    Required roles:
     - can_read_transcoders

    Args:
        per_page (int | Unset):
        page (int | Unset):
        query (str | Unset):
        ids (str | Unset):
        sort (str | Unset):
        include_storages (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTranscodersResponseDefault | TranscodersSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            page=page,
            query=query,
            ids=ids,
            sort=sort,
            include_storages=include_storages,
        )
    ).parsed
