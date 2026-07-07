from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.export_locations_schema import ExportLocationsSchema
from ...models.get_export_locations_response_default_type_0 import (
    GetExportLocationsResponseDefaultType0,
)
from ...models.get_export_locations_response_default_type_1 import (
    GetExportLocationsResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["query"] = query

    params["ids"] = ids

    params["per_page"] = per_page

    params["last_id"] = last_id

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/export_locations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ExportLocationsSchema
    | GetExportLocationsResponseDefaultType0
    | GetExportLocationsResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = ExportLocationsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        GetExportLocationsResponseDefaultType0 | GetExportLocationsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetExportLocationsResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetExportLocationsResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | ExportLocationsSchema
    | GetExportLocationsResponseDefaultType0
    | GetExportLocationsResponseDefaultType1
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
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[
    Any
    | ExportLocationsSchema
    | GetExportLocationsResponseDefaultType0
    | GetExportLocationsResponseDefaultType1
]:
    """Get all export_locations


    Required roles:
     - can_read_export_locations

    Args:
        query (str | Unset):
        ids (str | Unset):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ExportLocationsSchema | GetExportLocationsResponseDefaultType0 | GetExportLocationsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        query=query,
        ids=ids,
        per_page=per_page,
        last_id=last_id,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> (
    Any
    | ExportLocationsSchema
    | GetExportLocationsResponseDefaultType0
    | GetExportLocationsResponseDefaultType1
    | None
):
    """Get all export_locations


    Required roles:
     - can_read_export_locations

    Args:
        query (str | Unset):
        ids (str | Unset):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ExportLocationsSchema | GetExportLocationsResponseDefaultType0 | GetExportLocationsResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        query=query,
        ids=ids,
        per_page=per_page,
        last_id=last_id,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[
    Any
    | ExportLocationsSchema
    | GetExportLocationsResponseDefaultType0
    | GetExportLocationsResponseDefaultType1
]:
    """Get all export_locations


    Required roles:
     - can_read_export_locations

    Args:
        query (str | Unset):
        ids (str | Unset):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ExportLocationsSchema | GetExportLocationsResponseDefaultType0 | GetExportLocationsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        query=query,
        ids=ids,
        per_page=per_page,
        last_id=last_id,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> (
    Any
    | ExportLocationsSchema
    | GetExportLocationsResponseDefaultType0
    | GetExportLocationsResponseDefaultType1
    | None
):
    """Get all export_locations


    Required roles:
     - can_read_export_locations

    Args:
        query (str | Unset):
        ids (str | Unset):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ExportLocationsSchema | GetExportLocationsResponseDefaultType0 | GetExportLocationsResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            ids=ids,
            per_page=per_page,
            last_id=last_id,
            sort=sort,
        )
    ).parsed
