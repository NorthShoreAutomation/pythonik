from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_add_to_favorites_schema import BulkAddToFavoritesSchema
from ...models.post_favorites_response_default import PostFavoritesResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    body: BulkAddToFavoritesSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/favorites/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BulkAddToFavoritesSchema | PostFavoritesResponseDefault:
    if response.status_code == 200:
        response_200 = BulkAddToFavoritesSchema.from_dict(response.json())

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

    response_default = PostFavoritesResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BulkAddToFavoritesSchema | PostFavoritesResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkAddToFavoritesSchema,
) -> Response[Any | BulkAddToFavoritesSchema | PostFavoritesResponseDefault]:
    """Adds multiple objects to a list of favorites


    Required roles:
     - can_write_favorites

    Args:
        body (BulkAddToFavoritesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BulkAddToFavoritesSchema | PostFavoritesResponseDefault]
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
    body: BulkAddToFavoritesSchema,
) -> Any | BulkAddToFavoritesSchema | PostFavoritesResponseDefault | None:
    """Adds multiple objects to a list of favorites


    Required roles:
     - can_write_favorites

    Args:
        body (BulkAddToFavoritesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BulkAddToFavoritesSchema | PostFavoritesResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkAddToFavoritesSchema,
) -> Response[Any | BulkAddToFavoritesSchema | PostFavoritesResponseDefault]:
    """Adds multiple objects to a list of favorites


    Required roles:
     - can_write_favorites

    Args:
        body (BulkAddToFavoritesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BulkAddToFavoritesSchema | PostFavoritesResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BulkAddToFavoritesSchema,
) -> Any | BulkAddToFavoritesSchema | PostFavoritesResponseDefault | None:
    """Adds multiple objects to a list of favorites


    Required roles:
     - can_write_favorites

    Args:
        body (BulkAddToFavoritesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BulkAddToFavoritesSchema | PostFavoritesResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
