from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_webhooks_response_default_type_0 import (
    GetWebhooksResponseDefaultType0,
)
from ...models.get_webhooks_response_default_type_1 import (
    GetWebhooksResponseDefaultType1,
)
from ...models.webhooks_schema import WebhooksSchema
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/webhooks/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetWebhooksResponseDefaultType0
    | GetWebhooksResponseDefaultType1
    | WebhooksSchema
):
    if response.status_code == 200:
        response_200 = WebhooksSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> GetWebhooksResponseDefaultType0 | GetWebhooksResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetWebhooksResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetWebhooksResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetWebhooksResponseDefaultType0
    | GetWebhooksResponseDefaultType1
    | WebhooksSchema
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
    Any
    | GetWebhooksResponseDefaultType0
    | GetWebhooksResponseDefaultType1
    | WebhooksSchema
]:
    """Get all webhooks


    Required roles:
     - can_read_webhooks

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetWebhooksResponseDefaultType0 | GetWebhooksResponseDefaultType1 | WebhooksSchema]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetWebhooksResponseDefaultType0
    | GetWebhooksResponseDefaultType1
    | WebhooksSchema
    | None
):
    """Get all webhooks


    Required roles:
     - can_read_webhooks

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetWebhooksResponseDefaultType0 | GetWebhooksResponseDefaultType1 | WebhooksSchema
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetWebhooksResponseDefaultType0
    | GetWebhooksResponseDefaultType1
    | WebhooksSchema
]:
    """Get all webhooks


    Required roles:
     - can_read_webhooks

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetWebhooksResponseDefaultType0 | GetWebhooksResponseDefaultType1 | WebhooksSchema]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetWebhooksResponseDefaultType0
    | GetWebhooksResponseDefaultType1
    | WebhooksSchema
    | None
):
    """Get all webhooks


    Required roles:
     - can_read_webhooks

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetWebhooksResponseDefaultType0 | GetWebhooksResponseDefaultType1 | WebhooksSchema
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
