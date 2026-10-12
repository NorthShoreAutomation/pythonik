from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.logo_create_schema import LogoCreateSchema
from ...models.post_logos_response_default import PostLogosResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    body: LogoCreateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/logos/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | LogoCreateSchema | PostLogosResponseDefault:
    if response.status_code == 201:
        response_201 = LogoCreateSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostLogosResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | LogoCreateSchema | PostLogosResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LogoCreateSchema,
) -> Response[Any | LogoCreateSchema | PostLogosResponseDefault]:
    """Create a new saved logo

     <br/>The image itself is uploaded by the client to the returned `upload_url`<br/>using the returned
    `upload_method` (PUT for S3, POST for GCS resumable).<br/>The image itself is uploaded by the client
    to the returned `upload_url`<br/>using the returned `upload_method` (PUT for S3, POST for GCS
    resumable).
    Required roles:
     - can_write_portals

    Args:
        body (LogoCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LogoCreateSchema | PostLogosResponseDefault]
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
    body: LogoCreateSchema,
) -> Any | LogoCreateSchema | PostLogosResponseDefault | None:
    """Create a new saved logo

     <br/>The image itself is uploaded by the client to the returned `upload_url`<br/>using the returned
    `upload_method` (PUT for S3, POST for GCS resumable).<br/>The image itself is uploaded by the client
    to the returned `upload_url`<br/>using the returned `upload_method` (PUT for S3, POST for GCS
    resumable).
    Required roles:
     - can_write_portals

    Args:
        body (LogoCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LogoCreateSchema | PostLogosResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LogoCreateSchema,
) -> Response[Any | LogoCreateSchema | PostLogosResponseDefault]:
    """Create a new saved logo

     <br/>The image itself is uploaded by the client to the returned `upload_url`<br/>using the returned
    `upload_method` (PUT for S3, POST for GCS resumable).<br/>The image itself is uploaded by the client
    to the returned `upload_url`<br/>using the returned `upload_method` (PUT for S3, POST for GCS
    resumable).
    Required roles:
     - can_write_portals

    Args:
        body (LogoCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LogoCreateSchema | PostLogosResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: LogoCreateSchema,
) -> Any | LogoCreateSchema | PostLogosResponseDefault | None:
    """Create a new saved logo

     <br/>The image itself is uploaded by the client to the returned `upload_url`<br/>using the returned
    `upload_method` (PUT for S3, POST for GCS resumable).<br/>The image itself is uploaded by the client
    to the returned `upload_url`<br/>using the returned `upload_method` (PUT for S3, POST for GCS
    resumable).
    Required roles:
     - can_write_portals

    Args:
        body (LogoCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LogoCreateSchema | PostLogosResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
