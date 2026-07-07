from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.keyframe_create_schema import KeyframeCreateSchema
from ...models.post_assets_by_asset_id_keyframes_response_default_type_0 import (
    PostAssetsByAssetIdKeyframesResponseDefaultType0,
)
from ...models.post_assets_by_asset_id_keyframes_response_default_type_1 import (
    PostAssetsByAssetIdKeyframesResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    *,
    body: KeyframeCreateSchema,
    use_google_resumable_upload: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["use_google_resumable_upload"] = use_google_resumable_upload

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/keyframes/".format(
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
    | KeyframeCreateSchema
    | PostAssetsByAssetIdKeyframesResponseDefaultType0
    | PostAssetsByAssetIdKeyframesResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = KeyframeCreateSchema.from_dict(response.json())

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
        PostAssetsByAssetIdKeyframesResponseDefaultType0
        | PostAssetsByAssetIdKeyframesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostAssetsByAssetIdKeyframesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostAssetsByAssetIdKeyframesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | KeyframeCreateSchema
    | PostAssetsByAssetIdKeyframesResponseDefaultType0
    | PostAssetsByAssetIdKeyframesResponseDefaultType1
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
    body: KeyframeCreateSchema,
    use_google_resumable_upload: bool | Unset = False,
) -> Response[
    Any
    | KeyframeCreateSchema
    | PostAssetsByAssetIdKeyframesResponseDefaultType0
    | PostAssetsByAssetIdKeyframesResponseDefaultType1
]:
    """Create keyframe and associate to asset


    Required roles:
     - can_write_keyframes

    Args:
        asset_id (str):
        use_google_resumable_upload (bool | Unset):  Default: False.
        body (KeyframeCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | KeyframeCreateSchema | PostAssetsByAssetIdKeyframesResponseDefaultType0 | PostAssetsByAssetIdKeyframesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        use_google_resumable_upload=use_google_resumable_upload,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KeyframeCreateSchema,
    use_google_resumable_upload: bool | Unset = False,
) -> (
    Any
    | KeyframeCreateSchema
    | PostAssetsByAssetIdKeyframesResponseDefaultType0
    | PostAssetsByAssetIdKeyframesResponseDefaultType1
    | None
):
    """Create keyframe and associate to asset


    Required roles:
     - can_write_keyframes

    Args:
        asset_id (str):
        use_google_resumable_upload (bool | Unset):  Default: False.
        body (KeyframeCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | KeyframeCreateSchema | PostAssetsByAssetIdKeyframesResponseDefaultType0 | PostAssetsByAssetIdKeyframesResponseDefaultType1
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        body=body,
        use_google_resumable_upload=use_google_resumable_upload,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KeyframeCreateSchema,
    use_google_resumable_upload: bool | Unset = False,
) -> Response[
    Any
    | KeyframeCreateSchema
    | PostAssetsByAssetIdKeyframesResponseDefaultType0
    | PostAssetsByAssetIdKeyframesResponseDefaultType1
]:
    """Create keyframe and associate to asset


    Required roles:
     - can_write_keyframes

    Args:
        asset_id (str):
        use_google_resumable_upload (bool | Unset):  Default: False.
        body (KeyframeCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | KeyframeCreateSchema | PostAssetsByAssetIdKeyframesResponseDefaultType0 | PostAssetsByAssetIdKeyframesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        use_google_resumable_upload=use_google_resumable_upload,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: KeyframeCreateSchema,
    use_google_resumable_upload: bool | Unset = False,
) -> (
    Any
    | KeyframeCreateSchema
    | PostAssetsByAssetIdKeyframesResponseDefaultType0
    | PostAssetsByAssetIdKeyframesResponseDefaultType1
    | None
):
    """Create keyframe and associate to asset


    Required roles:
     - can_write_keyframes

    Args:
        asset_id (str):
        use_google_resumable_upload (bool | Unset):  Default: False.
        body (KeyframeCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | KeyframeCreateSchema | PostAssetsByAssetIdKeyframesResponseDefaultType0 | PostAssetsByAssetIdKeyframesResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
            use_google_resumable_upload=use_google_resumable_upload,
        )
    ).parsed
