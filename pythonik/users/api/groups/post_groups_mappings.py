from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.group_mapping_schema import GroupMappingSchema
from ...models.post_groups_mappings_response_default_type_0 import (
    PostGroupsMappingsResponseDefaultType0,
)
from ...models.post_groups_mappings_response_default_type_1 import (
    PostGroupsMappingsResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    *,
    body: GroupMappingSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/groups/mappings/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GroupMappingSchema
    | PostGroupsMappingsResponseDefaultType0
    | PostGroupsMappingsResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = GroupMappingSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    def _parse_response_default(
        data: object,
    ) -> (
        PostGroupsMappingsResponseDefaultType0 | PostGroupsMappingsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostGroupsMappingsResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostGroupsMappingsResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GroupMappingSchema
    | PostGroupsMappingsResponseDefaultType0
    | PostGroupsMappingsResponseDefaultType1
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
    body: GroupMappingSchema,
) -> Response[
    Any
    | GroupMappingSchema
    | PostGroupsMappingsResponseDefaultType0
    | PostGroupsMappingsResponseDefaultType1
]:
    """Create a new group mapping


    Required roles:
     - can_write_group_mappings

    Args:
        body (GroupMappingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GroupMappingSchema | PostGroupsMappingsResponseDefaultType0 | PostGroupsMappingsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: GroupMappingSchema,
) -> (
    Any
    | GroupMappingSchema
    | PostGroupsMappingsResponseDefaultType0
    | PostGroupsMappingsResponseDefaultType1
    | None
):
    """Create a new group mapping


    Required roles:
     - can_write_group_mappings

    Args:
        body (GroupMappingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GroupMappingSchema | PostGroupsMappingsResponseDefaultType0 | PostGroupsMappingsResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GroupMappingSchema,
) -> Response[
    Any
    | GroupMappingSchema
    | PostGroupsMappingsResponseDefaultType0
    | PostGroupsMappingsResponseDefaultType1
]:
    """Create a new group mapping


    Required roles:
     - can_write_group_mappings

    Args:
        body (GroupMappingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GroupMappingSchema | PostGroupsMappingsResponseDefaultType0 | PostGroupsMappingsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GroupMappingSchema,
) -> (
    Any
    | GroupMappingSchema
    | PostGroupsMappingsResponseDefaultType0
    | PostGroupsMappingsResponseDefaultType1
    | None
):
    """Create a new group mapping


    Required roles:
     - can_write_group_mappings

    Args:
        body (GroupMappingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GroupMappingSchema | PostGroupsMappingsResponseDefaultType0 | PostGroupsMappingsResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
