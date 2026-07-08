from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.collection_input_schema import CollectionInputSchema
from ...models.collection_schema import CollectionSchema
from ...models.post_collections_response_default import PostCollectionsResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CollectionInputSchema,
    apply_default_acls: bool | Unset = UNSET,
    apply_collection_acls: bool | Unset = UNSET,
    restrict_collection_acls: bool | Unset = UNSET,
    apply_acl_template_id: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["apply_default_acls"] = apply_default_acls

    params["apply_collection_acls"] = apply_collection_acls

    params["restrict_collection_acls"] = restrict_collection_acls

    json_apply_acl_template_id: str | Unset = UNSET
    if not isinstance(apply_acl_template_id, Unset):
        json_apply_acl_template_id = str(apply_acl_template_id)
    params["apply_acl_template_id"] = json_apply_acl_template_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/collections/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CollectionSchema | PostCollectionsResponseDefault:
    if response.status_code == 201:
        response_201 = CollectionSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostCollectionsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CollectionSchema | PostCollectionsResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CollectionInputSchema,
    apply_default_acls: bool | Unset = UNSET,
    apply_collection_acls: bool | Unset = UNSET,
    restrict_collection_acls: bool | Unset = UNSET,
    apply_acl_template_id: UUID | Unset = UNSET,
) -> Response[Any | CollectionSchema | PostCollectionsResponseDefault]:
    """Create a new collection


    Required roles:
     - can_create_collections

    Args:
        apply_default_acls (bool | Unset):
        apply_collection_acls (bool | Unset):
        restrict_collection_acls (bool | Unset):
        apply_acl_template_id (UUID | Unset):
        body (CollectionInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionSchema | PostCollectionsResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
        apply_default_acls=apply_default_acls,
        apply_collection_acls=apply_collection_acls,
        restrict_collection_acls=restrict_collection_acls,
        apply_acl_template_id=apply_acl_template_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CollectionInputSchema,
    apply_default_acls: bool | Unset = UNSET,
    apply_collection_acls: bool | Unset = UNSET,
    restrict_collection_acls: bool | Unset = UNSET,
    apply_acl_template_id: UUID | Unset = UNSET,
) -> Any | CollectionSchema | PostCollectionsResponseDefault | None:
    """Create a new collection


    Required roles:
     - can_create_collections

    Args:
        apply_default_acls (bool | Unset):
        apply_collection_acls (bool | Unset):
        restrict_collection_acls (bool | Unset):
        apply_acl_template_id (UUID | Unset):
        body (CollectionInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionSchema | PostCollectionsResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
        apply_default_acls=apply_default_acls,
        apply_collection_acls=apply_collection_acls,
        restrict_collection_acls=restrict_collection_acls,
        apply_acl_template_id=apply_acl_template_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CollectionInputSchema,
    apply_default_acls: bool | Unset = UNSET,
    apply_collection_acls: bool | Unset = UNSET,
    restrict_collection_acls: bool | Unset = UNSET,
    apply_acl_template_id: UUID | Unset = UNSET,
) -> Response[Any | CollectionSchema | PostCollectionsResponseDefault]:
    """Create a new collection


    Required roles:
     - can_create_collections

    Args:
        apply_default_acls (bool | Unset):
        apply_collection_acls (bool | Unset):
        restrict_collection_acls (bool | Unset):
        apply_acl_template_id (UUID | Unset):
        body (CollectionInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionSchema | PostCollectionsResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
        apply_default_acls=apply_default_acls,
        apply_collection_acls=apply_collection_acls,
        restrict_collection_acls=restrict_collection_acls,
        apply_acl_template_id=apply_acl_template_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CollectionInputSchema,
    apply_default_acls: bool | Unset = UNSET,
    apply_collection_acls: bool | Unset = UNSET,
    restrict_collection_acls: bool | Unset = UNSET,
    apply_acl_template_id: UUID | Unset = UNSET,
) -> Any | CollectionSchema | PostCollectionsResponseDefault | None:
    """Create a new collection


    Required roles:
     - can_create_collections

    Args:
        apply_default_acls (bool | Unset):
        apply_collection_acls (bool | Unset):
        restrict_collection_acls (bool | Unset):
        apply_acl_template_id (UUID | Unset):
        body (CollectionInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionSchema | PostCollectionsResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            apply_default_acls=apply_default_acls,
            apply_collection_acls=apply_collection_acls,
            restrict_collection_acls=restrict_collection_acls,
            apply_acl_template_id=apply_acl_template_id,
        )
    ).parsed
