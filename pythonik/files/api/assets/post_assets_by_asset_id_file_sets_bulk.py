from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_fileset_schema import BulkFilesetSchema
from ...models.post_assets_by_asset_id_file_sets_bulk_response_default_type_0 import (
    PostAssetsByAssetIdFileSetsBulkResponseDefaultType0,
)
from ...models.post_assets_by_asset_id_file_sets_bulk_response_default_type_1 import (
    PostAssetsByAssetIdFileSetsBulkResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    *,
    body: BulkFilesetSchema,
    keep_source: bool | Unset = False,
    immediately: bool | Unset = False,
    do_not_delete_last_copy: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["keep_source"] = keep_source

    params["immediately"] = immediately

    params["do_not_delete_last_copy"] = do_not_delete_last_copy

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/file_sets/bulk/".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostAssetsByAssetIdFileSetsBulkResponseDefaultType0
    | PostAssetsByAssetIdFileSetsBulkResponseDefaultType1
):
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        PostAssetsByAssetIdFileSetsBulkResponseDefaultType0
        | PostAssetsByAssetIdFileSetsBulkResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostAssetsByAssetIdFileSetsBulkResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostAssetsByAssetIdFileSetsBulkResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAssetsByAssetIdFileSetsBulkResponseDefaultType0
    | PostAssetsByAssetIdFileSetsBulkResponseDefaultType1
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
    body: BulkFilesetSchema,
    keep_source: bool | Unset = False,
    immediately: bool | Unset = False,
    do_not_delete_last_copy: bool | Unset = False,
) -> Response[
    Any
    | PostAssetsByAssetIdFileSetsBulkResponseDefaultType0
    | PostAssetsByAssetIdFileSetsBulkResponseDefaultType1
]:
    """Delete asset's file set, file entries, and actual files in bulk


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        keep_source (bool | Unset):  Default: False.
        immediately (bool | Unset):  Default: False.
        do_not_delete_last_copy (bool | Unset):  Default: False.
        body (BulkFilesetSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdFileSetsBulkResponseDefaultType0 | PostAssetsByAssetIdFileSetsBulkResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        keep_source=keep_source,
        immediately=immediately,
        do_not_delete_last_copy=do_not_delete_last_copy,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkFilesetSchema,
    keep_source: bool | Unset = False,
    immediately: bool | Unset = False,
    do_not_delete_last_copy: bool | Unset = False,
) -> (
    Any
    | PostAssetsByAssetIdFileSetsBulkResponseDefaultType0
    | PostAssetsByAssetIdFileSetsBulkResponseDefaultType1
    | None
):
    """Delete asset's file set, file entries, and actual files in bulk


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        keep_source (bool | Unset):  Default: False.
        immediately (bool | Unset):  Default: False.
        do_not_delete_last_copy (bool | Unset):  Default: False.
        body (BulkFilesetSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdFileSetsBulkResponseDefaultType0 | PostAssetsByAssetIdFileSetsBulkResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        body=body,
        keep_source=keep_source,
        immediately=immediately,
        do_not_delete_last_copy=do_not_delete_last_copy,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkFilesetSchema,
    keep_source: bool | Unset = False,
    immediately: bool | Unset = False,
    do_not_delete_last_copy: bool | Unset = False,
) -> Response[
    Any
    | PostAssetsByAssetIdFileSetsBulkResponseDefaultType0
    | PostAssetsByAssetIdFileSetsBulkResponseDefaultType1
]:
    """Delete asset's file set, file entries, and actual files in bulk


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        keep_source (bool | Unset):  Default: False.
        immediately (bool | Unset):  Default: False.
        do_not_delete_last_copy (bool | Unset):  Default: False.
        body (BulkFilesetSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdFileSetsBulkResponseDefaultType0 | PostAssetsByAssetIdFileSetsBulkResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        keep_source=keep_source,
        immediately=immediately,
        do_not_delete_last_copy=do_not_delete_last_copy,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkFilesetSchema,
    keep_source: bool | Unset = False,
    immediately: bool | Unset = False,
    do_not_delete_last_copy: bool | Unset = False,
) -> (
    Any
    | PostAssetsByAssetIdFileSetsBulkResponseDefaultType0
    | PostAssetsByAssetIdFileSetsBulkResponseDefaultType1
    | None
):
    """Delete asset's file set, file entries, and actual files in bulk


    Required roles:
     - can_delete_files

    Args:
        asset_id (str):
        keep_source (bool | Unset):  Default: False.
        immediately (bool | Unset):  Default: False.
        do_not_delete_last_copy (bool | Unset):  Default: False.
        body (BulkFilesetSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdFileSetsBulkResponseDefaultType0 | PostAssetsByAssetIdFileSetsBulkResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
            keep_source=keep_source,
            immediately=immediately,
            do_not_delete_last_copy=do_not_delete_last_copy,
        )
    ).parsed
