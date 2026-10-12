from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.natural_search_request import NaturalSearchRequest
from ...models.natural_search_response import NaturalSearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: NaturalSearchRequest,
    generate_signed_url: bool | Unset = UNSET,
    generate_signed_download_url: bool | Unset = UNSET,
    generate_signed_proxy_url: bool | Unset = UNSET,
    include_users: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["generate_signed_url"] = generate_signed_url

    params["generate_signed_download_url"] = generate_signed_download_url

    params["generate_signed_proxy_url"] = generate_signed_proxy_url

    params["include_users"] = include_users

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/search/natural/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | NaturalSearchResponse | None:
    if response.status_code == 200:
        response_200 = NaturalSearchResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 504:
        response_504 = ErrorResponse.from_dict(response.json())

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | HTTPValidationError | NaturalSearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NaturalSearchRequest,
    generate_signed_url: bool | Unset = UNSET,
    generate_signed_download_url: bool | Unset = UNSET,
    generate_signed_proxy_url: bool | Unset = UNSET,
    include_users: bool | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | NaturalSearchResponse]:
    """Natural language search

     Required roles:
    - can_search

    Args:
        generate_signed_url (bool | Unset):
        generate_signed_download_url (bool | Unset):
        generate_signed_proxy_url (bool | Unset):
        include_users (bool | Unset):
        body (NaturalSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | NaturalSearchResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        generate_signed_url=generate_signed_url,
        generate_signed_download_url=generate_signed_download_url,
        generate_signed_proxy_url=generate_signed_proxy_url,
        include_users=include_users,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: NaturalSearchRequest,
    generate_signed_url: bool | Unset = UNSET,
    generate_signed_download_url: bool | Unset = UNSET,
    generate_signed_proxy_url: bool | Unset = UNSET,
    include_users: bool | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | NaturalSearchResponse | None:
    """Natural language search

     Required roles:
    - can_search

    Args:
        generate_signed_url (bool | Unset):
        generate_signed_download_url (bool | Unset):
        generate_signed_proxy_url (bool | Unset):
        include_users (bool | Unset):
        body (NaturalSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | NaturalSearchResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        generate_signed_url=generate_signed_url,
        generate_signed_download_url=generate_signed_download_url,
        generate_signed_proxy_url=generate_signed_proxy_url,
        include_users=include_users,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NaturalSearchRequest,
    generate_signed_url: bool | Unset = UNSET,
    generate_signed_download_url: bool | Unset = UNSET,
    generate_signed_proxy_url: bool | Unset = UNSET,
    include_users: bool | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | NaturalSearchResponse]:
    """Natural language search

     Required roles:
    - can_search

    Args:
        generate_signed_url (bool | Unset):
        generate_signed_download_url (bool | Unset):
        generate_signed_proxy_url (bool | Unset):
        include_users (bool | Unset):
        body (NaturalSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | NaturalSearchResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        generate_signed_url=generate_signed_url,
        generate_signed_download_url=generate_signed_download_url,
        generate_signed_proxy_url=generate_signed_proxy_url,
        include_users=include_users,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NaturalSearchRequest,
    generate_signed_url: bool | Unset = UNSET,
    generate_signed_download_url: bool | Unset = UNSET,
    generate_signed_proxy_url: bool | Unset = UNSET,
    include_users: bool | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | NaturalSearchResponse | None:
    """Natural language search

     Required roles:
    - can_search

    Args:
        generate_signed_url (bool | Unset):
        generate_signed_download_url (bool | Unset):
        generate_signed_proxy_url (bool | Unset):
        include_users (bool | Unset):
        body (NaturalSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | NaturalSearchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            generate_signed_url=generate_signed_url,
            generate_signed_download_url=generate_signed_download_url,
            generate_signed_proxy_url=generate_signed_proxy_url,
            include_users=include_users,
        )
    ).parsed
