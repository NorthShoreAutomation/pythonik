from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_publications_by_publication_id_cancel_response_default import (
    PostPublicationsByPublicationIdCancelResponseDefault,
)
from ...types import Response


def _get_kwargs(
    publication_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/publications/{publication_id}/cancel/".format(
            publication_id=quote(str(publication_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostPublicationsByPublicationIdCancelResponseDefault:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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

    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422

    response_default = PostPublicationsByPublicationIdCancelResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostPublicationsByPublicationIdCancelResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    publication_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PostPublicationsByPublicationIdCancelResponseDefault]:
    """⚠️ Beta: Cancels the scheduled publication of a post asset


    Required roles:
     - can_publish

    Args:
        publication_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostPublicationsByPublicationIdCancelResponseDefault]
    """

    kwargs = _get_kwargs(
        publication_id=publication_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    publication_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PostPublicationsByPublicationIdCancelResponseDefault | None:
    """⚠️ Beta: Cancels the scheduled publication of a post asset


    Required roles:
     - can_publish

    Args:
        publication_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostPublicationsByPublicationIdCancelResponseDefault
    """

    return sync_detailed(
        publication_id=publication_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    publication_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PostPublicationsByPublicationIdCancelResponseDefault]:
    """⚠️ Beta: Cancels the scheduled publication of a post asset


    Required roles:
     - can_publish

    Args:
        publication_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostPublicationsByPublicationIdCancelResponseDefault]
    """

    kwargs = _get_kwargs(
        publication_id=publication_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    publication_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PostPublicationsByPublicationIdCancelResponseDefault | None:
    """⚠️ Beta: Cancels the scheduled publication of a post asset


    Required roles:
     - can_publish

    Args:
        publication_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostPublicationsByPublicationIdCancelResponseDefault
    """

    return (
        await asyncio_detailed(
            publication_id=publication_id,
            client=client,
        )
    ).parsed
