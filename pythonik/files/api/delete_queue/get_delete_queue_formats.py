from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.formats_elastic_schema import FormatsElasticSchema
from ...models.get_delete_queue_formats_response_default import (
    GetDeleteQueueFormatsResponseDefault,
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
        "url": "/v1/delete_queue/formats/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FormatsElasticSchema | GetDeleteQueueFormatsResponseDefault:
    if response.status_code == 200:
        response_200 = FormatsElasticSchema.from_dict(response.json())

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

    response_default = GetDeleteQueueFormatsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | FormatsElasticSchema | GetDeleteQueueFormatsResponseDefault]:
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
) -> Response[Any | FormatsElasticSchema | GetDeleteQueueFormatsResponseDefault]:
    """Get deleted formats


    Required roles:
     - can_read_formats

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
        Response[Any | FormatsElasticSchema | GetDeleteQueueFormatsResponseDefault]
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
) -> Any | FormatsElasticSchema | GetDeleteQueueFormatsResponseDefault | None:
    """Get deleted formats


    Required roles:
     - can_read_formats

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
        Any | FormatsElasticSchema | GetDeleteQueueFormatsResponseDefault
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
) -> Response[Any | FormatsElasticSchema | GetDeleteQueueFormatsResponseDefault]:
    """Get deleted formats


    Required roles:
     - can_read_formats

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
        Response[Any | FormatsElasticSchema | GetDeleteQueueFormatsResponseDefault]
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
) -> Any | FormatsElasticSchema | GetDeleteQueueFormatsResponseDefault | None:
    """Get deleted formats


    Required roles:
     - can_read_formats

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
        Any | FormatsElasticSchema | GetDeleteQueueFormatsResponseDefault
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
