from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_sets_schema import FileSetsSchema
from ...models.get_assets_by_asset_id_file_sets_response_default_type_0 import (
    GetAssetsByAssetIdFileSetsResponseDefaultType0,
)
from ...models.get_assets_by_asset_id_file_sets_response_default_type_1 import (
    GetAssetsByAssetIdFileSetsResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    *,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
    file_count: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["last_id"] = last_id

    params["file_count"] = file_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/file_sets/".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | FileSetsSchema
    | GetAssetsByAssetIdFileSetsResponseDefaultType0
    | GetAssetsByAssetIdFileSetsResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = FileSetsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetAssetsByAssetIdFileSetsResponseDefaultType0
        | GetAssetsByAssetIdFileSetsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAssetsByAssetIdFileSetsResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetAssetsByAssetIdFileSetsResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | FileSetsSchema
    | GetAssetsByAssetIdFileSetsResponseDefaultType0
    | GetAssetsByAssetIdFileSetsResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
    file_count: bool | Unset = False,
) -> Response[
    Any
    | FileSetsSchema
    | GetAssetsByAssetIdFileSetsResponseDefaultType0
    | GetAssetsByAssetIdFileSetsResponseDefaultType1
]:
    """Get all asset's file sets


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):
        file_count (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileSetsSchema | GetAssetsByAssetIdFileSetsResponseDefaultType0 | GetAssetsByAssetIdFileSetsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        per_page=per_page,
        last_id=last_id,
        file_count=file_count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
    file_count: bool | Unset = False,
) -> (
    Any
    | FileSetsSchema
    | GetAssetsByAssetIdFileSetsResponseDefaultType0
    | GetAssetsByAssetIdFileSetsResponseDefaultType1
    | None
):
    """Get all asset's file sets


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):
        file_count (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileSetsSchema | GetAssetsByAssetIdFileSetsResponseDefaultType0 | GetAssetsByAssetIdFileSetsResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        per_page=per_page,
        last_id=last_id,
        file_count=file_count,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
    file_count: bool | Unset = False,
) -> Response[
    Any
    | FileSetsSchema
    | GetAssetsByAssetIdFileSetsResponseDefaultType0
    | GetAssetsByAssetIdFileSetsResponseDefaultType1
]:
    """Get all asset's file sets


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):
        file_count (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileSetsSchema | GetAssetsByAssetIdFileSetsResponseDefaultType0 | GetAssetsByAssetIdFileSetsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        per_page=per_page,
        last_id=last_id,
        file_count=file_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
    file_count: bool | Unset = False,
) -> (
    Any
    | FileSetsSchema
    | GetAssetsByAssetIdFileSetsResponseDefaultType0
    | GetAssetsByAssetIdFileSetsResponseDefaultType1
    | None
):
    """Get all asset's file sets


    Required roles:
     - can_read_files

    Args:
        asset_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):
        file_count (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileSetsSchema | GetAssetsByAssetIdFileSetsResponseDefaultType0 | GetAssetsByAssetIdFileSetsResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            per_page=per_page,
            last_id=last_id,
            file_count=file_count,
        )
    ).parsed
