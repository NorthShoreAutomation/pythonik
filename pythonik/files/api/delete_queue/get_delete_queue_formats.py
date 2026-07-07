from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.formats_elastic_schema import FormatsElasticSchema
from ...models.get_delete_queue_formats_response_default_type_0 import (
    GetDeleteQueueFormatsResponseDefaultType0,
)
from ...models.get_delete_queue_formats_response_default_type_1 import (
    GetDeleteQueueFormatsResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
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
) -> (
    Any
    | FormatsElasticSchema
    | GetDeleteQueueFormatsResponseDefaultType0
    | GetDeleteQueueFormatsResponseDefaultType1
):
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

    def _parse_response_default(
        data: object,
    ) -> (
        GetDeleteQueueFormatsResponseDefaultType0
        | GetDeleteQueueFormatsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetDeleteQueueFormatsResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetDeleteQueueFormatsResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | FormatsElasticSchema
    | GetDeleteQueueFormatsResponseDefaultType0
    | GetDeleteQueueFormatsResponseDefaultType1
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
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> Response[
    Any
    | FormatsElasticSchema
    | GetDeleteQueueFormatsResponseDefaultType0
    | GetDeleteQueueFormatsResponseDefaultType1
]:
    """Get deleted formats


    Required roles:
     - can_read_formats

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):
        query (str | Unset):
        field_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FormatsElasticSchema | GetDeleteQueueFormatsResponseDefaultType0 | GetDeleteQueueFormatsResponseDefaultType1]
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
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> (
    Any
    | FormatsElasticSchema
    | GetDeleteQueueFormatsResponseDefaultType0
    | GetDeleteQueueFormatsResponseDefaultType1
    | None
):
    """Get deleted formats


    Required roles:
     - can_read_formats

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):
        query (str | Unset):
        field_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FormatsElasticSchema | GetDeleteQueueFormatsResponseDefaultType0 | GetDeleteQueueFormatsResponseDefaultType1
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
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> Response[
    Any
    | FormatsElasticSchema
    | GetDeleteQueueFormatsResponseDefaultType0
    | GetDeleteQueueFormatsResponseDefaultType1
]:
    """Get deleted formats


    Required roles:
     - can_read_formats

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):
        query (str | Unset):
        field_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FormatsElasticSchema | GetDeleteQueueFormatsResponseDefaultType0 | GetDeleteQueueFormatsResponseDefaultType1]
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
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_name: str | Unset = UNSET,
) -> (
    Any
    | FormatsElasticSchema
    | GetDeleteQueueFormatsResponseDefaultType0
    | GetDeleteQueueFormatsResponseDefaultType1
    | None
):
    """Get deleted formats


    Required roles:
     - can_read_formats

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):
        query (str | Unset):
        field_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FormatsElasticSchema | GetDeleteQueueFormatsResponseDefaultType0 | GetDeleteQueueFormatsResponseDefaultType1
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
