from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_delete_from_favorites_schema import BulkDeleteFromFavoritesSchema
from ...models.delete_favorites_response_default import DeleteFavoritesResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    body: BulkDeleteFromFavoritesSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/favorites/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BulkDeleteFromFavoritesSchema | DeleteFavoritesResponseDefault:
    if response.status_code == 200:
        response_200 = BulkDeleteFromFavoritesSchema.from_dict(response.json())

        return response_200

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

    response_default = DeleteFavoritesResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BulkDeleteFromFavoritesSchema | DeleteFavoritesResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkDeleteFromFavoritesSchema,
) -> Response[Any | BulkDeleteFromFavoritesSchema | DeleteFavoritesResponseDefault]:
    """Deletes objects items from a list of favorites


    Required roles:
     - can_delete_favorites

    Args:
        body (BulkDeleteFromFavoritesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BulkDeleteFromFavoritesSchema | DeleteFavoritesResponseDefault]
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
    body: BulkDeleteFromFavoritesSchema,
) -> Any | BulkDeleteFromFavoritesSchema | DeleteFavoritesResponseDefault | None:
    """Deletes objects items from a list of favorites


    Required roles:
     - can_delete_favorites

    Args:
        body (BulkDeleteFromFavoritesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BulkDeleteFromFavoritesSchema | DeleteFavoritesResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkDeleteFromFavoritesSchema,
) -> Response[Any | BulkDeleteFromFavoritesSchema | DeleteFavoritesResponseDefault]:
    """Deletes objects items from a list of favorites


    Required roles:
     - can_delete_favorites

    Args:
        body (BulkDeleteFromFavoritesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BulkDeleteFromFavoritesSchema | DeleteFavoritesResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BulkDeleteFromFavoritesSchema,
) -> Any | BulkDeleteFromFavoritesSchema | DeleteFavoritesResponseDefault | None:
    """Deletes objects items from a list of favorites


    Required roles:
     - can_delete_favorites

    Args:
        body (BulkDeleteFromFavoritesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BulkDeleteFromFavoritesSchema | DeleteFavoritesResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
