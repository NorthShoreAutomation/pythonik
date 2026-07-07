from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.asset_create_schema import AssetCreateSchema
from ...models.asset_post_create import AssetPostCreate
from ...models.asset_post_schema import AssetPostSchema
from ...models.asset_schema import AssetSchema
from ...models.post_assets_response_default_type_0 import PostAssetsResponseDefaultType0
from ...models.post_assets_response_default_type_1 import PostAssetsResponseDefaultType1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AssetCreateSchema | AssetPostCreate,
    apply_default_acls: bool | Unset = True,
    apply_collection_acls: bool | Unset = False,
    assign_to_collection: bool | Unset = False,
    generate_subclip_keyframes: bool | Unset = True,
    apply_acl_template_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["apply_default_acls"] = apply_default_acls

    params["apply_collection_acls"] = apply_collection_acls

    params["assign_to_collection"] = assign_to_collection

    params["generate_subclip_keyframes"] = generate_subclip_keyframes

    json_apply_acl_template_id: str | Unset = UNSET
    if not isinstance(apply_acl_template_id, Unset):
        json_apply_acl_template_id = str(apply_acl_template_id)
    params["apply_acl_template_id"] = json_apply_acl_template_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/",
        "params": params,
    }

    if isinstance(body, AssetCreateSchema):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | AssetPostSchema
    | AssetSchema
    | PostAssetsResponseDefaultType0
    | PostAssetsResponseDefaultType1
):
    if response.status_code == 201:

        def _parse_response_201(data: object) -> AssetPostSchema | AssetSchema:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_asset_schema_typed_type_0 = AssetSchema.from_dict(
                    data
                )

                return componentsschemas_asset_schema_typed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_asset_schema_typed_type_1 = AssetPostSchema.from_dict(
                data
            )

            return componentsschemas_asset_schema_typed_type_1

        response_201 = _parse_response_201(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    def _parse_response_default(
        data: object,
    ) -> PostAssetsResponseDefaultType0 | PostAssetsResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostAssetsResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostAssetsResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AssetPostSchema
    | AssetSchema
    | PostAssetsResponseDefaultType0
    | PostAssetsResponseDefaultType1
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
    body: AssetCreateSchema | AssetPostCreate,
    apply_default_acls: bool | Unset = True,
    apply_collection_acls: bool | Unset = False,
    assign_to_collection: bool | Unset = False,
    generate_subclip_keyframes: bool | Unset = True,
    apply_acl_template_id: UUID | Unset = UNSET,
) -> Response[
    Any
    | AssetPostSchema
    | AssetSchema
    | PostAssetsResponseDefaultType0
    | PostAssetsResponseDefaultType1
]:
    """Create a new asset


    Required roles:
     - can_create_assets

    Args:
        apply_default_acls (bool | Unset):  Default: True.
        apply_collection_acls (bool | Unset):  Default: False.
        assign_to_collection (bool | Unset):  Default: False.
        generate_subclip_keyframes (bool | Unset):  Default: True.
        apply_acl_template_id (UUID | Unset):
        body (AssetCreateSchema | AssetPostCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetPostSchema | AssetSchema | PostAssetsResponseDefaultType0 | PostAssetsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
        apply_default_acls=apply_default_acls,
        apply_collection_acls=apply_collection_acls,
        assign_to_collection=assign_to_collection,
        generate_subclip_keyframes=generate_subclip_keyframes,
        apply_acl_template_id=apply_acl_template_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: AssetCreateSchema | AssetPostCreate,
    apply_default_acls: bool | Unset = True,
    apply_collection_acls: bool | Unset = False,
    assign_to_collection: bool | Unset = False,
    generate_subclip_keyframes: bool | Unset = True,
    apply_acl_template_id: UUID | Unset = UNSET,
) -> (
    Any
    | AssetPostSchema
    | AssetSchema
    | PostAssetsResponseDefaultType0
    | PostAssetsResponseDefaultType1
    | None
):
    """Create a new asset


    Required roles:
     - can_create_assets

    Args:
        apply_default_acls (bool | Unset):  Default: True.
        apply_collection_acls (bool | Unset):  Default: False.
        assign_to_collection (bool | Unset):  Default: False.
        generate_subclip_keyframes (bool | Unset):  Default: True.
        apply_acl_template_id (UUID | Unset):
        body (AssetCreateSchema | AssetPostCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetPostSchema | AssetSchema | PostAssetsResponseDefaultType0 | PostAssetsResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        body=body,
        apply_default_acls=apply_default_acls,
        apply_collection_acls=apply_collection_acls,
        assign_to_collection=assign_to_collection,
        generate_subclip_keyframes=generate_subclip_keyframes,
        apply_acl_template_id=apply_acl_template_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AssetCreateSchema | AssetPostCreate,
    apply_default_acls: bool | Unset = True,
    apply_collection_acls: bool | Unset = False,
    assign_to_collection: bool | Unset = False,
    generate_subclip_keyframes: bool | Unset = True,
    apply_acl_template_id: UUID | Unset = UNSET,
) -> Response[
    Any
    | AssetPostSchema
    | AssetSchema
    | PostAssetsResponseDefaultType0
    | PostAssetsResponseDefaultType1
]:
    """Create a new asset


    Required roles:
     - can_create_assets

    Args:
        apply_default_acls (bool | Unset):  Default: True.
        apply_collection_acls (bool | Unset):  Default: False.
        assign_to_collection (bool | Unset):  Default: False.
        generate_subclip_keyframes (bool | Unset):  Default: True.
        apply_acl_template_id (UUID | Unset):
        body (AssetCreateSchema | AssetPostCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetPostSchema | AssetSchema | PostAssetsResponseDefaultType0 | PostAssetsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
        apply_default_acls=apply_default_acls,
        apply_collection_acls=apply_collection_acls,
        assign_to_collection=assign_to_collection,
        generate_subclip_keyframes=generate_subclip_keyframes,
        apply_acl_template_id=apply_acl_template_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AssetCreateSchema | AssetPostCreate,
    apply_default_acls: bool | Unset = True,
    apply_collection_acls: bool | Unset = False,
    assign_to_collection: bool | Unset = False,
    generate_subclip_keyframes: bool | Unset = True,
    apply_acl_template_id: UUID | Unset = UNSET,
) -> (
    Any
    | AssetPostSchema
    | AssetSchema
    | PostAssetsResponseDefaultType0
    | PostAssetsResponseDefaultType1
    | None
):
    """Create a new asset


    Required roles:
     - can_create_assets

    Args:
        apply_default_acls (bool | Unset):  Default: True.
        apply_collection_acls (bool | Unset):  Default: False.
        assign_to_collection (bool | Unset):  Default: False.
        generate_subclip_keyframes (bool | Unset):  Default: True.
        apply_acl_template_id (UUID | Unset):
        body (AssetCreateSchema | AssetPostCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetPostSchema | AssetSchema | PostAssetsResponseDefaultType0 | PostAssetsResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            apply_default_acls=apply_default_acls,
            apply_collection_acls=apply_collection_acls,
            assign_to_collection=assign_to_collection,
            generate_subclip_keyframes=generate_subclip_keyframes,
            apply_acl_template_id=apply_acl_template_id,
        )
    ).parsed
