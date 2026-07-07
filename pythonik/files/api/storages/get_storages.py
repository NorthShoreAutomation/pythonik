from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storages_response_default_type_0 import (
    GetStoragesResponseDefaultType0,
)
from ...models.get_storages_response_default_type_1 import (
    GetStoragesResponseDefaultType1,
)
from ...models.storages_read_schema import StoragesReadSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    sort: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    method: str | Unset = UNSET,
    status: str | Unset = UNSET,
    purpose: str | Unset = UNSET,
    last_scanned: str | Unset = UNSET,
    scanner_status: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["sort"] = sort

    params["id"] = id

    params["name"] = name

    params["method"] = method

    params["status"] = status

    params["purpose"] = purpose

    params["last_scanned"] = last_scanned

    params["scanner_status"] = scanner_status

    params["query"] = query

    params["ids"] = ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storages/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetStoragesResponseDefaultType0
    | GetStoragesResponseDefaultType1
    | StoragesReadSchema
):
    if response.status_code == 200:
        response_200 = StoragesReadSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> GetStoragesResponseDefaultType0 | GetStoragesResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetStoragesResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetStoragesResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetStoragesResponseDefaultType0
    | GetStoragesResponseDefaultType1
    | StoragesReadSchema
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
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    method: str | Unset = UNSET,
    status: str | Unset = UNSET,
    purpose: str | Unset = UNSET,
    last_scanned: str | Unset = UNSET,
    scanner_status: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> Response[
    Any
    | GetStoragesResponseDefaultType0
    | GetStoragesResponseDefaultType1
    | StoragesReadSchema
]:
    """Get all storages


    Required roles:
     - can_read_storages

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        sort (str | Unset):
        id (str | Unset):
        name (str | Unset):
        method (str | Unset):
        status (str | Unset):
        purpose (str | Unset):
        last_scanned (str | Unset):
        scanner_status (str | Unset):
        query (str | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesResponseDefaultType0 | GetStoragesResponseDefaultType1 | StoragesReadSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        sort=sort,
        id=id,
        name=name,
        method=method,
        status=status,
        purpose=purpose,
        last_scanned=last_scanned,
        scanner_status=scanner_status,
        query=query,
        ids=ids,
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
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    method: str | Unset = UNSET,
    status: str | Unset = UNSET,
    purpose: str | Unset = UNSET,
    last_scanned: str | Unset = UNSET,
    scanner_status: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> (
    Any
    | GetStoragesResponseDefaultType0
    | GetStoragesResponseDefaultType1
    | StoragesReadSchema
    | None
):
    """Get all storages


    Required roles:
     - can_read_storages

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        sort (str | Unset):
        id (str | Unset):
        name (str | Unset):
        method (str | Unset):
        status (str | Unset):
        purpose (str | Unset):
        last_scanned (str | Unset):
        scanner_status (str | Unset):
        query (str | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesResponseDefaultType0 | GetStoragesResponseDefaultType1 | StoragesReadSchema
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        sort=sort,
        id=id,
        name=name,
        method=method,
        status=status,
        purpose=purpose,
        last_scanned=last_scanned,
        scanner_status=scanner_status,
        query=query,
        ids=ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    sort: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    method: str | Unset = UNSET,
    status: str | Unset = UNSET,
    purpose: str | Unset = UNSET,
    last_scanned: str | Unset = UNSET,
    scanner_status: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> Response[
    Any
    | GetStoragesResponseDefaultType0
    | GetStoragesResponseDefaultType1
    | StoragesReadSchema
]:
    """Get all storages


    Required roles:
     - can_read_storages

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        sort (str | Unset):
        id (str | Unset):
        name (str | Unset):
        method (str | Unset):
        status (str | Unset):
        purpose (str | Unset):
        last_scanned (str | Unset):
        scanner_status (str | Unset):
        query (str | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesResponseDefaultType0 | GetStoragesResponseDefaultType1 | StoragesReadSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        sort=sort,
        id=id,
        name=name,
        method=method,
        status=status,
        purpose=purpose,
        last_scanned=last_scanned,
        scanner_status=scanner_status,
        query=query,
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    sort: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    method: str | Unset = UNSET,
    status: str | Unset = UNSET,
    purpose: str | Unset = UNSET,
    last_scanned: str | Unset = UNSET,
    scanner_status: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> (
    Any
    | GetStoragesResponseDefaultType0
    | GetStoragesResponseDefaultType1
    | StoragesReadSchema
    | None
):
    """Get all storages


    Required roles:
     - can_read_storages

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        sort (str | Unset):
        id (str | Unset):
        name (str | Unset):
        method (str | Unset):
        status (str | Unset):
        purpose (str | Unset):
        last_scanned (str | Unset):
        scanner_status (str | Unset):
        query (str | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesResponseDefaultType0 | GetStoragesResponseDefaultType1 | StoragesReadSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            sort=sort,
            id=id,
            name=name,
            method=method,
            status=status,
            purpose=purpose,
            last_scanned=last_scanned,
            scanner_status=scanner_status,
            query=query,
            ids=ids,
        )
    ).parsed
