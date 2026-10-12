from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.ai_consent_decline_request_schema import AIConsentDeclineRequestSchema
from ...models.ai_consents_schema import AIConsentsSchema
from ...models.post_ai_consents_decline_response_default import (
    PostAiConsentsDeclineResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    body: AIConsentDeclineRequestSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/ai/consents/decline/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AIConsentsSchema | Any | PostAiConsentsDeclineResponseDefault:
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

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    response_default = PostAiConsentsDeclineResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AIConsentsSchema | Any | PostAiConsentsDeclineResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AIConsentDeclineRequestSchema,
) -> Response[AIConsentsSchema | Any | PostAiConsentsDeclineResponseDefault]:
    """Refuse consent documents, so they cannot take effect by non-objection

    Args:
        body (AIConsentDeclineRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AIConsentsSchema | Any | PostAiConsentsDeclineResponseDefault]
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
    body: AIConsentDeclineRequestSchema,
) -> AIConsentsSchema | Any | PostAiConsentsDeclineResponseDefault | None:
    """Refuse consent documents, so they cannot take effect by non-objection

    Args:
        body (AIConsentDeclineRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AIConsentsSchema | Any | PostAiConsentsDeclineResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AIConsentDeclineRequestSchema,
) -> Response[AIConsentsSchema | Any | PostAiConsentsDeclineResponseDefault]:
    """Refuse consent documents, so they cannot take effect by non-objection

    Args:
        body (AIConsentDeclineRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AIConsentsSchema | Any | PostAiConsentsDeclineResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AIConsentDeclineRequestSchema,
) -> AIConsentsSchema | Any | PostAiConsentsDeclineResponseDefault | None:
    """Refuse consent documents, so they cannot take effect by non-objection

    Args:
        body (AIConsentDeclineRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AIConsentsSchema | Any | PostAiConsentsDeclineResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
