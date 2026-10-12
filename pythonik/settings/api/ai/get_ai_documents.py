from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.ai_consent_documents_schema import AIConsentDocumentsSchema
from ...models.get_ai_documents_response_default import GetAiDocumentsResponseDefault
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/ai/documents/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AIConsentDocumentsSchema | Any | GetAiDocumentsResponseDefault:
    if response.status_code == 200:
        response_200 = AIConsentDocumentsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetAiDocumentsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AIConsentDocumentsSchema | Any | GetAiDocumentsResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[AIConsentDocumentsSchema | Any | GetAiDocumentsResponseDefault]:
    """List the consent documents a customer may be asked to accept

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AIConsentDocumentsSchema | Any | GetAiDocumentsResponseDefault]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> AIConsentDocumentsSchema | Any | GetAiDocumentsResponseDefault | None:
    """List the consent documents a customer may be asked to accept

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AIConsentDocumentsSchema | Any | GetAiDocumentsResponseDefault
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[AIConsentDocumentsSchema | Any | GetAiDocumentsResponseDefault]:
    """List the consent documents a customer may be asked to accept

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AIConsentDocumentsSchema | Any | GetAiDocumentsResponseDefault]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> AIConsentDocumentsSchema | Any | GetAiDocumentsResponseDefault | None:
    """List the consent documents a customer may be asked to accept

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AIConsentDocumentsSchema | Any | GetAiDocumentsResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
