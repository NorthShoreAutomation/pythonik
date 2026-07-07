from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_assets_by_asset_id_temporary_file_sets_response_default_type_0 import (
    PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType0,
)
from ...models.post_assets_by_asset_id_temporary_file_sets_response_default_type_1 import (
    PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType1,
)
from ...models.temporary_file_set_schema import TemporaryFileSetSchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    *,
    body: TemporaryFileSetSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/temporary_file_sets/".format(
            asset_id=quote(str(asset_id), safe=""),
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
    | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType0
    | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType1
    | TemporaryFileSetSchema
):
    if response.status_code == 201:
        response_201 = TemporaryFileSetSchema.from_dict(response.json())

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
        PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType0
        | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType0
    | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType1
    | TemporaryFileSetSchema
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
    body: TemporaryFileSetSchema,
) -> Response[
    Any
    | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType0
    | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType1
    | TemporaryFileSetSchema
]:
    """Create temporary file set and associate to asset


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        body (TemporaryFileSetSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType0 | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType1 | TemporaryFileSetSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TemporaryFileSetSchema,
) -> (
    Any
    | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType0
    | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType1
    | TemporaryFileSetSchema
    | None
):
    """Create temporary file set and associate to asset


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        body (TemporaryFileSetSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType0 | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType1 | TemporaryFileSetSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TemporaryFileSetSchema,
) -> Response[
    Any
    | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType0
    | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType1
    | TemporaryFileSetSchema
]:
    """Create temporary file set and associate to asset


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        body (TemporaryFileSetSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType0 | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType1 | TemporaryFileSetSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TemporaryFileSetSchema,
) -> (
    Any
    | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType0
    | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType1
    | TemporaryFileSetSchema
    | None
):
    """Create temporary file set and associate to asset


    Required roles:
     - can_write_files

    Args:
        asset_id (str):
        body (TemporaryFileSetSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType0 | PostAssetsByAssetIdTemporaryFileSetsResponseDefaultType1 | TemporaryFileSetSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
        )
    ).parsed
