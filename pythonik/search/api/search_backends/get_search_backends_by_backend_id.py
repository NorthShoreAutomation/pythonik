from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.search_backend_read_schema import SearchBackendReadSchema
from ...types import Response


def _get_kwargs(
    backend_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/search_backends/{backend_id}/".format(
            backend_id=quote(str(backend_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | SearchBackendReadSchema | None:
    if response.status_code == 200:
        response_200 = SearchBackendReadSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | HTTPValidationError | SearchBackendReadSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backend_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | HTTPValidationError | SearchBackendReadSchema]:
    """Get one configured search backend

     Required roles:
    - can_read_search_backends

    Args:
        backend_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | SearchBackendReadSchema]
    """

    kwargs = _get_kwargs(
        backend_id=backend_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backend_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | HTTPValidationError | SearchBackendReadSchema | None:
    """Get one configured search backend

     Required roles:
    - can_read_search_backends

    Args:
        backend_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | SearchBackendReadSchema
    """

    return sync_detailed(
        backend_id=backend_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    backend_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | HTTPValidationError | SearchBackendReadSchema]:
    """Get one configured search backend

     Required roles:
    - can_read_search_backends

    Args:
        backend_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | SearchBackendReadSchema]
    """

    kwargs = _get_kwargs(
        backend_id=backend_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backend_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | HTTPValidationError | SearchBackendReadSchema | None:
    """Get one configured search backend

     Required roles:
    - can_read_search_backends

    Args:
        backend_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | SearchBackendReadSchema
    """

    return (
        await asyncio_detailed(
            backend_id=backend_id,
            client=client,
        )
    ).parsed
