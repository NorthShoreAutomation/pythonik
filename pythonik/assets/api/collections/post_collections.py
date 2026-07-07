from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.collection_input_schema import CollectionInputSchema
from ...models.collection_schema import CollectionSchema
from ...models.post_collections_response_default_type_0 import (
    PostCollectionsResponseDefaultType0,
)
from ...models.post_collections_response_default_type_1 import (
    PostCollectionsResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CollectionInputSchema,
    apply_default_acls: bool | Unset = True,
    apply_collection_acls: bool | Unset = False,
    restrict_collection_acls: bool | Unset = False,
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
) -> (
    Any
    | CollectionSchema
    | PostCollectionsResponseDefaultType0
    | PostCollectionsResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = CollectionSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> PostCollectionsResponseDefaultType0 | PostCollectionsResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostCollectionsResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostCollectionsResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | CollectionSchema
    | PostCollectionsResponseDefaultType0
    | PostCollectionsResponseDefaultType1
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
    body: CollectionInputSchema,
    apply_default_acls: bool | Unset = True,
    apply_collection_acls: bool | Unset = False,
    restrict_collection_acls: bool | Unset = False,
    apply_acl_template_id: UUID | Unset = UNSET,
) -> Response[
    Any
    | CollectionSchema
    | PostCollectionsResponseDefaultType0
    | PostCollectionsResponseDefaultType1
]:
    """Create a new collection


    Required roles:
     - can_create_collections

    Args:
        apply_default_acls (bool | Unset):  Default: True.
        apply_collection_acls (bool | Unset):  Default: False.
        restrict_collection_acls (bool | Unset):  Default: False.
        apply_acl_template_id (UUID | Unset):
        body (CollectionInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionSchema | PostCollectionsResponseDefaultType0 | PostCollectionsResponseDefaultType1]
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
    apply_default_acls: bool | Unset = True,
    apply_collection_acls: bool | Unset = False,
    restrict_collection_acls: bool | Unset = False,
    apply_acl_template_id: UUID | Unset = UNSET,
) -> (
    Any
    | CollectionSchema
    | PostCollectionsResponseDefaultType0
    | PostCollectionsResponseDefaultType1
    | None
):
    """Create a new collection


    Required roles:
     - can_create_collections

    Args:
        apply_default_acls (bool | Unset):  Default: True.
        apply_collection_acls (bool | Unset):  Default: False.
        restrict_collection_acls (bool | Unset):  Default: False.
        apply_acl_template_id (UUID | Unset):
        body (CollectionInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionSchema | PostCollectionsResponseDefaultType0 | PostCollectionsResponseDefaultType1
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
    apply_default_acls: bool | Unset = True,
    apply_collection_acls: bool | Unset = False,
    restrict_collection_acls: bool | Unset = False,
    apply_acl_template_id: UUID | Unset = UNSET,
) -> Response[
    Any
    | CollectionSchema
    | PostCollectionsResponseDefaultType0
    | PostCollectionsResponseDefaultType1
]:
    """Create a new collection


    Required roles:
     - can_create_collections

    Args:
        apply_default_acls (bool | Unset):  Default: True.
        apply_collection_acls (bool | Unset):  Default: False.
        restrict_collection_acls (bool | Unset):  Default: False.
        apply_acl_template_id (UUID | Unset):
        body (CollectionInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionSchema | PostCollectionsResponseDefaultType0 | PostCollectionsResponseDefaultType1]
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
    apply_default_acls: bool | Unset = True,
    apply_collection_acls: bool | Unset = False,
    restrict_collection_acls: bool | Unset = False,
    apply_acl_template_id: UUID | Unset = UNSET,
) -> (
    Any
    | CollectionSchema
    | PostCollectionsResponseDefaultType0
    | PostCollectionsResponseDefaultType1
    | None
):
    """Create a new collection


    Required roles:
     - can_create_collections

    Args:
        apply_default_acls (bool | Unset):  Default: True.
        apply_collection_acls (bool | Unset):  Default: False.
        restrict_collection_acls (bool | Unset):  Default: False.
        apply_acl_template_id (UUID | Unset):
        body (CollectionInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionSchema | PostCollectionsResponseDefaultType0 | PostCollectionsResponseDefaultType1
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
