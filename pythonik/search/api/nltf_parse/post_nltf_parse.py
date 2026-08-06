from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.nltf_parse_request_schema import NltfParseRequestSchema
from ...models.nltf_parse_response_schema import NltfParseResponseSchema
from ...models.post_nltf_parse_response_default import PostNltfParseResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    body: NltfParseRequestSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/nltf_parse/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | NltfParseResponseSchema | PostNltfParseResponseDefault:
    if response.status_code == 200:
        response_200 = NltfParseResponseSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if response.status_code == 502:
        response_502 = cast(Any, None)
        return response_502

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    response_default = PostNltfParseResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | NltfParseResponseSchema | PostNltfParseResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NltfParseRequestSchema,
) -> Response[Any | NltfParseResponseSchema | PostNltfParseResponseDefault]:
    """Parse a natural language query into structured search filters


    Required roles:
     - can_search

    Args:
        body (NltfParseRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | NltfParseResponseSchema | PostNltfParseResponseDefault]
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
    body: NltfParseRequestSchema,
) -> Any | NltfParseResponseSchema | PostNltfParseResponseDefault | None:
    """Parse a natural language query into structured search filters


    Required roles:
     - can_search

    Args:
        body (NltfParseRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | NltfParseResponseSchema | PostNltfParseResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NltfParseRequestSchema,
) -> Response[Any | NltfParseResponseSchema | PostNltfParseResponseDefault]:
    """Parse a natural language query into structured search filters


    Required roles:
     - can_search

    Args:
        body (NltfParseRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | NltfParseResponseSchema | PostNltfParseResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NltfParseRequestSchema,
) -> Any | NltfParseResponseSchema | PostNltfParseResponseDefault | None:
    """Parse a natural language query into structured search filters


    Required roles:
     - can_search

    Args:
        body (NltfParseRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | NltfParseResponseSchema | PostNltfParseResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
