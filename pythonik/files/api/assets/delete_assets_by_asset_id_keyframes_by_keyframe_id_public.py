from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_assets_by_asset_id_keyframes_by_keyframe_id_public_response_default_type_0 import (
    DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType0,
)
from ...models.delete_assets_by_asset_id_keyframes_by_keyframe_id_public_response_default_type_1 import (
    DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType1,
)
from ...models.keyframe_schema import KeyframeSchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    keyframe_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/assets/{asset_id}/keyframes/{keyframe_id}/public/".format(
            asset_id=quote(str(asset_id), safe=""),
            keyframe_id=quote(str(keyframe_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType0
    | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType1
    | KeyframeSchema
):
    if response.status_code == 201:
        response_201 = KeyframeSchema.from_dict(response.json())

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
        DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType0
        | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType0
    | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType1
    | KeyframeSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType0
    | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType1
    | KeyframeSchema
]:
    """Make the keyframe link private


    Required roles:
     - can_write_keyframes

    Args:
        asset_id (str):
        keyframe_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType0 | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType1 | KeyframeSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        keyframe_id=keyframe_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType0
    | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType1
    | KeyframeSchema
    | None
):
    """Make the keyframe link private


    Required roles:
     - can_write_keyframes

    Args:
        asset_id (str):
        keyframe_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType0 | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType1 | KeyframeSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        keyframe_id=keyframe_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType0
    | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType1
    | KeyframeSchema
]:
    """Make the keyframe link private


    Required roles:
     - can_write_keyframes

    Args:
        asset_id (str):
        keyframe_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType0 | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType1 | KeyframeSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        keyframe_id=keyframe_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType0
    | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType1
    | KeyframeSchema
    | None
):
    """Make the keyframe link private


    Required roles:
     - can_write_keyframes

    Args:
        asset_id (str):
        keyframe_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType0 | DeleteAssetsByAssetIdKeyframesByKeyframeIdPublicResponseDefaultType1 | KeyframeSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            keyframe_id=keyframe_id,
            client=client,
        )
    ).parsed
