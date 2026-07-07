from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_search_saved_group_response_default_type_0 import (
    PostSearchSavedGroupResponseDefaultType0,
)
from ...models.post_search_saved_group_response_default_type_1 import (
    PostSearchSavedGroupResponseDefaultType1,
)
from ...models.saved_search_group_schema import SavedSearchGroupSchema
from ...types import Response


def _get_kwargs(
    *,
    body: SavedSearchGroupSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/search/saved/group/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostSearchSavedGroupResponseDefaultType0
    | PostSearchSavedGroupResponseDefaultType1
    | SavedSearchGroupSchema
):
    if response.status_code == 201:
        response_201 = SavedSearchGroupSchema.from_dict(response.json())

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
        PostSearchSavedGroupResponseDefaultType0
        | PostSearchSavedGroupResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostSearchSavedGroupResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostSearchSavedGroupResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSearchSavedGroupResponseDefaultType0
    | PostSearchSavedGroupResponseDefaultType1
    | SavedSearchGroupSchema
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
    body: SavedSearchGroupSchema,
) -> Response[
    Any
    | PostSearchSavedGroupResponseDefaultType0
    | PostSearchSavedGroupResponseDefaultType1
    | SavedSearchGroupSchema
]:
    """Create and return saved search group data


    Required roles:
     - can_write_saved_search_groups

    Args:
        body (SavedSearchGroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSearchSavedGroupResponseDefaultType0 | PostSearchSavedGroupResponseDefaultType1 | SavedSearchGroupSchema]
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
    body: SavedSearchGroupSchema,
) -> (
    Any
    | PostSearchSavedGroupResponseDefaultType0
    | PostSearchSavedGroupResponseDefaultType1
    | SavedSearchGroupSchema
    | None
):
    """Create and return saved search group data


    Required roles:
     - can_write_saved_search_groups

    Args:
        body (SavedSearchGroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSearchSavedGroupResponseDefaultType0 | PostSearchSavedGroupResponseDefaultType1 | SavedSearchGroupSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SavedSearchGroupSchema,
) -> Response[
    Any
    | PostSearchSavedGroupResponseDefaultType0
    | PostSearchSavedGroupResponseDefaultType1
    | SavedSearchGroupSchema
]:
    """Create and return saved search group data


    Required roles:
     - can_write_saved_search_groups

    Args:
        body (SavedSearchGroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSearchSavedGroupResponseDefaultType0 | PostSearchSavedGroupResponseDefaultType1 | SavedSearchGroupSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SavedSearchGroupSchema,
) -> (
    Any
    | PostSearchSavedGroupResponseDefaultType0
    | PostSearchSavedGroupResponseDefaultType1
    | SavedSearchGroupSchema
    | None
):
    """Create and return saved search group data


    Required roles:
     - can_write_saved_search_groups

    Args:
        body (SavedSearchGroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSearchSavedGroupResponseDefaultType0 | PostSearchSavedGroupResponseDefaultType1 | SavedSearchGroupSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
