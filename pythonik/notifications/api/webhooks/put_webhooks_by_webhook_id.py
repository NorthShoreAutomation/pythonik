from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_webhooks_by_webhook_id_response_default import (
    PutWebhooksByWebhookIdResponseDefault,
)
from ...models.webhook_create_schema import WebhookCreateSchema
from ...models.webhook_schema import WebhookSchema
from ...types import Response


def _get_kwargs(
    webhook_id: str,
    *,
    body: WebhookCreateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/webhooks/{webhook_id}/".format(
            webhook_id=quote(str(webhook_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutWebhooksByWebhookIdResponseDefault | WebhookSchema:
    if response.status_code == 200:
        response_200 = WebhookSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PutWebhooksByWebhookIdResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PutWebhooksByWebhookIdResponseDefault | WebhookSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: WebhookCreateSchema,
) -> Response[Any | PutWebhooksByWebhookIdResponseDefault | WebhookSchema]:
    """Update a webhook


    Required roles:
     - can_write_webhooks

    Args:
        webhook_id (str):
        body (WebhookCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutWebhooksByWebhookIdResponseDefault | WebhookSchema]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: WebhookCreateSchema,
) -> Any | PutWebhooksByWebhookIdResponseDefault | WebhookSchema | None:
    """Update a webhook


    Required roles:
     - can_write_webhooks

    Args:
        webhook_id (str):
        body (WebhookCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutWebhooksByWebhookIdResponseDefault | WebhookSchema
    """

    return sync_detailed(
        webhook_id=webhook_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: WebhookCreateSchema,
) -> Response[Any | PutWebhooksByWebhookIdResponseDefault | WebhookSchema]:
    """Update a webhook


    Required roles:
     - can_write_webhooks

    Args:
        webhook_id (str):
        body (WebhookCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutWebhooksByWebhookIdResponseDefault | WebhookSchema]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: WebhookCreateSchema,
) -> Any | PutWebhooksByWebhookIdResponseDefault | WebhookSchema | None:
    """Update a webhook


    Required roles:
     - can_write_webhooks

    Args:
        webhook_id (str):
        body (WebhookCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutWebhooksByWebhookIdResponseDefault | WebhookSchema
    """

    return (
        await asyncio_detailed(
            webhook_id=webhook_id,
            client=client,
            body=body,
        )
    ).parsed
