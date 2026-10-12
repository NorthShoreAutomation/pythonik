from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.ai_consent_revoke_schema import AIConsentRevokeSchema
from ...models.ai_consents_schema import AIConsentsSchema
from ...models.post_ai_consents_revoke_response_default import (
    PostAiConsentsRevokeResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    body: AIConsentRevokeSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/ai/consents/revoke/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AIConsentsSchema | Any | PostAiConsentsRevokeResponseDefault:
    if response.status_code == 200:
        response_200 = AIConsentsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    response_default = PostAiConsentsRevokeResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AIConsentsSchema | Any | PostAiConsentsRevokeResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AIConsentRevokeSchema,
) -> Response[AIConsentsSchema | Any | PostAiConsentsRevokeResponseDefault]:
    """Withdraw the acceptance of consent documents

    Args:
        body (AIConsentRevokeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AIConsentsSchema | Any | PostAiConsentsRevokeResponseDefault]
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
    body: AIConsentRevokeSchema,
) -> AIConsentsSchema | Any | PostAiConsentsRevokeResponseDefault | None:
    """Withdraw the acceptance of consent documents

    Args:
        body (AIConsentRevokeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AIConsentsSchema | Any | PostAiConsentsRevokeResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AIConsentRevokeSchema,
) -> Response[AIConsentsSchema | Any | PostAiConsentsRevokeResponseDefault]:
    """Withdraw the acceptance of consent documents

    Args:
        body (AIConsentRevokeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AIConsentsSchema | Any | PostAiConsentsRevokeResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AIConsentRevokeSchema,
) -> AIConsentsSchema | Any | PostAiConsentsRevokeResponseDefault | None:
    """Withdraw the acceptance of consent documents

    Args:
        body (AIConsentRevokeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AIConsentsSchema | Any | PostAiConsentsRevokeResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
