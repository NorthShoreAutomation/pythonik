from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_schema import FileSchema
from ...models.patch_assets_by_asset_id_files_by_file_id_response_default_type_0 import (
    PatchAssetsByAssetIdFilesByFileIdResponseDefaultType0,
)
from ...models.patch_assets_by_asset_id_files_by_file_id_response_default_type_1 import (
    PatchAssetsByAssetIdFilesByFileIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    file_id: str,
    *,
    body: FileSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/assets/{asset_id}/files/{file_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | FileSchema
    | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType0
    | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = FileSchema.from_dict(response.json())

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
        PatchAssetsByAssetIdFilesByFileIdResponseDefaultType0
        | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PatchAssetsByAssetIdFilesByFileIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PatchAssetsByAssetIdFilesByFileIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | FileSchema
    | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType0
    | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileSchema,
) -> Response[
    Any
    | FileSchema
    | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType0
    | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType1
]:
    """Update file information


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        body (FileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileSchema | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType0 | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_id=file_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileSchema,
) -> (
    Any
    | FileSchema
    | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType0
    | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType1
    | None
):
    """Update file information


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        body (FileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileSchema | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType0 | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        file_id=file_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileSchema,
) -> Response[
    Any
    | FileSchema
    | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType0
    | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType1
]:
    """Update file information


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        body (FileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileSchema | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType0 | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        file_id=file_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileSchema,
) -> (
    Any
    | FileSchema
    | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType0
    | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType1
    | None
):
    """Update file information


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        file_id (str):
        body (FileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileSchema | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType0 | PatchAssetsByAssetIdFilesByFileIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            file_id=file_id,
            client=client,
            body=body,
        )
    ).parsed
