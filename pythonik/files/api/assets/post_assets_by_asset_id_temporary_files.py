from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_assets_by_asset_id_temporary_files_response_default_type_0 import (
    PostAssetsByAssetIdTemporaryFilesResponseDefaultType0,
)
from ...models.post_assets_by_asset_id_temporary_files_response_default_type_1 import (
    PostAssetsByAssetIdTemporaryFilesResponseDefaultType1,
)
from ...models.temporary_file_create_schema import TemporaryFileCreateSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    *,
    body: TemporaryFileCreateSchema,
    store: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["store"] = store

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/temporary_files/".format(
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
    | PostAssetsByAssetIdTemporaryFilesResponseDefaultType0
    | PostAssetsByAssetIdTemporaryFilesResponseDefaultType1
    | TemporaryFileCreateSchema
):
    if response.status_code == 201:
        response_201 = TemporaryFileCreateSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PostAssetsByAssetIdTemporaryFilesResponseDefaultType0
        | PostAssetsByAssetIdTemporaryFilesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostAssetsByAssetIdTemporaryFilesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostAssetsByAssetIdTemporaryFilesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAssetsByAssetIdTemporaryFilesResponseDefaultType0
    | PostAssetsByAssetIdTemporaryFilesResponseDefaultType1
    | TemporaryFileCreateSchema
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
    body: TemporaryFileCreateSchema,
    store: bool | Unset = UNSET,
) -> Response[
    Any
    | PostAssetsByAssetIdTemporaryFilesResponseDefaultType0
    | PostAssetsByAssetIdTemporaryFilesResponseDefaultType1
    | TemporaryFileCreateSchema
]:
    """Create temporary transfer file for FILE storage transfers


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        store (bool | Unset):
        body (TemporaryFileCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdTemporaryFilesResponseDefaultType0 | PostAssetsByAssetIdTemporaryFilesResponseDefaultType1 | TemporaryFileCreateSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        store=store,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TemporaryFileCreateSchema,
    store: bool | Unset = UNSET,
) -> (
    Any
    | PostAssetsByAssetIdTemporaryFilesResponseDefaultType0
    | PostAssetsByAssetIdTemporaryFilesResponseDefaultType1
    | TemporaryFileCreateSchema
    | None
):
    """Create temporary transfer file for FILE storage transfers


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        store (bool | Unset):
        body (TemporaryFileCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdTemporaryFilesResponseDefaultType0 | PostAssetsByAssetIdTemporaryFilesResponseDefaultType1 | TemporaryFileCreateSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        body=body,
        store=store,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TemporaryFileCreateSchema,
    store: bool | Unset = UNSET,
) -> Response[
    Any
    | PostAssetsByAssetIdTemporaryFilesResponseDefaultType0
    | PostAssetsByAssetIdTemporaryFilesResponseDefaultType1
    | TemporaryFileCreateSchema
]:
    """Create temporary transfer file for FILE storage transfers


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        store (bool | Unset):
        body (TemporaryFileCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdTemporaryFilesResponseDefaultType0 | PostAssetsByAssetIdTemporaryFilesResponseDefaultType1 | TemporaryFileCreateSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        store=store,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TemporaryFileCreateSchema,
    store: bool | Unset = UNSET,
) -> (
    Any
    | PostAssetsByAssetIdTemporaryFilesResponseDefaultType0
    | PostAssetsByAssetIdTemporaryFilesResponseDefaultType1
    | TemporaryFileCreateSchema
    | None
):
    """Create temporary transfer file for FILE storage transfers


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        store (bool | Unset):
        body (TemporaryFileCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdTemporaryFilesResponseDefaultType0 | PostAssetsByAssetIdTemporaryFilesResponseDefaultType1 | TemporaryFileCreateSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
            store=store,
        )
    ).parsed
