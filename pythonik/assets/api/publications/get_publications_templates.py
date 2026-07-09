from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_publications_templates_response_default import (
    GetPublicationsTemplatesResponseDefault,
)
from ...models.publication_templates_schema import PublicationTemplatesSchema
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/publications/templates/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetPublicationsTemplatesResponseDefault | PublicationTemplatesSchema:
    if response.status_code == 200:
        response_200 = PublicationTemplatesSchema.from_dict(response.json())

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

    response_default = GetPublicationsTemplatesResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetPublicationsTemplatesResponseDefault | PublicationTemplatesSchema
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
) -> Response[
    Any | GetPublicationsTemplatesResponseDefault | PublicationTemplatesSchema
]:
    """Returns publication templates that can be used for publishing


    Required roles:
     - can_publish

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPublicationsTemplatesResponseDefault | PublicationTemplatesSchema]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetPublicationsTemplatesResponseDefault | PublicationTemplatesSchema | None:
    """Returns publication templates that can be used for publishing


    Required roles:
     - can_publish

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPublicationsTemplatesResponseDefault | PublicationTemplatesSchema
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | GetPublicationsTemplatesResponseDefault | PublicationTemplatesSchema
]:
    """Returns publication templates that can be used for publishing


    Required roles:
     - can_publish

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPublicationsTemplatesResponseDefault | PublicationTemplatesSchema]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetPublicationsTemplatesResponseDefault | PublicationTemplatesSchema | None:
    """Returns publication templates that can be used for publishing


    Required roles:
     - can_publish

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPublicationsTemplatesResponseDefault | PublicationTemplatesSchema
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
