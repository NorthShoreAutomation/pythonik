from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_sets_elastic_schema import FileSetsElasticSchema
from ...models.get_delete_queue_file_sets_response_default import (
    GetDeleteQueueFileSetsResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params["sort"] = sort

    params["query"] = query

    params["field_name"] = field_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/delete_queue/file_sets/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FileSetsElasticSchema | GetDeleteQueueFileSetsResponseDefault:
    if response.status_code == 200:
        response_200 = FileSetsElasticSchema.from_dict(response.json())

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

    response_default = GetDeleteQueueFileSetsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | FileSetsElasticSchema | GetDeleteQueueFileSetsResponseDefault]:
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
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> Response[Any | FileSetsElasticSchema | GetDeleteQueueFileSetsResponseDefault]:
    """Get deleted file sets


    Required roles:
     - can_read_files

    Args:
        per_page (int | Unset):
        page (int | Unset):
        sort (str | Unset):
        query (str | Unset):
        field_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileSetsElasticSchema | GetDeleteQueueFileSetsResponseDefault]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        sort=sort,
        query=query,
        field_name=field_name,
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
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> Any | FileSetsElasticSchema | GetDeleteQueueFileSetsResponseDefault | None:
    """Get deleted file sets


    Required roles:
     - can_read_files

    Args:
        per_page (int | Unset):
        page (int | Unset):
        sort (str | Unset):
        query (str | Unset):
        field_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileSetsElasticSchema | GetDeleteQueueFileSetsResponseDefault
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        page=page,
        sort=sort,
        query=query,
        field_name=field_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> Response[Any | FileSetsElasticSchema | GetDeleteQueueFileSetsResponseDefault]:
    """Get deleted file sets


    Required roles:
     - can_read_files

    Args:
        per_page (int | Unset):
        page (int | Unset):
        sort (str | Unset):
        query (str | Unset):
        field_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileSetsElasticSchema | GetDeleteQueueFileSetsResponseDefault]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        sort=sort,
        query=query,
        field_name=field_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> Any | FileSetsElasticSchema | GetDeleteQueueFileSetsResponseDefault | None:
    """Get deleted file sets


    Required roles:
     - can_read_files

    Args:
        per_page (int | Unset):
        page (int | Unset):
        sort (str | Unset):
        query (str | Unset):
        field_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileSetsElasticSchema | GetDeleteQueueFileSetsResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            page=page,
            sort=sort,
            query=query,
            field_name=field_name,
        )
    ).parsed
