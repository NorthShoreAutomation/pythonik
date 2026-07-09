from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_assets_by_asset_id_keyframes_by_keyframe_id_response_default import (
    DeleteAssetsByAssetIdKeyframesByKeyframeIdResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    keyframe_id: str,
    *,
    keep_poster: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["keep_poster"] = keep_poster

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/assets/{asset_id}/keyframes/{keyframe_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            keyframe_id=quote(str(keyframe_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteAssetsByAssetIdKeyframesByKeyframeIdResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        DeleteAssetsByAssetIdKeyframesByKeyframeIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteAssetsByAssetIdKeyframesByKeyframeIdResponseDefault]:
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
    keep_poster: bool | Unset = UNSET,
) -> Response[Any | DeleteAssetsByAssetIdKeyframesByKeyframeIdResponseDefault]:
    """Delete asset's keyframe


    Required roles:
     - can_write_keyframes

    Args:
        asset_id (str):
        keyframe_id (str):
        keep_poster (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdKeyframesByKeyframeIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        keyframe_id=keyframe_id,
        keep_poster=keep_poster,
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
    keep_poster: bool | Unset = UNSET,
) -> Any | DeleteAssetsByAssetIdKeyframesByKeyframeIdResponseDefault | None:
    """Delete asset's keyframe


    Required roles:
     - can_write_keyframes

    Args:
        asset_id (str):
        keyframe_id (str):
        keep_poster (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdKeyframesByKeyframeIdResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        keyframe_id=keyframe_id,
        client=client,
        keep_poster=keep_poster,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
    keep_poster: bool | Unset = UNSET,
) -> Response[Any | DeleteAssetsByAssetIdKeyframesByKeyframeIdResponseDefault]:
    """Delete asset's keyframe


    Required roles:
     - can_write_keyframes

    Args:
        asset_id (str):
        keyframe_id (str):
        keep_poster (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAssetsByAssetIdKeyframesByKeyframeIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        keyframe_id=keyframe_id,
        keep_poster=keep_poster,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
    keep_poster: bool | Unset = UNSET,
) -> Any | DeleteAssetsByAssetIdKeyframesByKeyframeIdResponseDefault | None:
    """Delete asset's keyframe


    Required roles:
     - can_write_keyframes

    Args:
        asset_id (str):
        keyframe_id (str):
        keep_poster (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAssetsByAssetIdKeyframesByKeyframeIdResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            keyframe_id=keyframe_id,
            client=client,
            keep_poster=keep_poster,
        )
    ).parsed
