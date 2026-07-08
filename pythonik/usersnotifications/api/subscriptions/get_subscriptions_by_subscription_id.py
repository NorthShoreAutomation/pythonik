from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_subscriptions_by_subscription_id_response_default import (
    GetSubscriptionsBySubscriptionIdResponseDefault,
)
from ...models.subscription_schema import SubscriptionSchema
from ...types import Response


def _get_kwargs(
    subscription_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/subscriptions/{subscription_id}/".format(
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSubscriptionsBySubscriptionIdResponseDefault | SubscriptionSchema:
    if response.status_code == 200:
        response_200 = SubscriptionSchema.from_dict(response.json())

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

    response_default = GetSubscriptionsBySubscriptionIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetSubscriptionsBySubscriptionIdResponseDefault | SubscriptionSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | GetSubscriptionsBySubscriptionIdResponseDefault | SubscriptionSchema
]:
    """Returns a particular subscription by id


    Required roles:
     - can_read_subscriptions

    Args:
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSubscriptionsBySubscriptionIdResponseDefault | SubscriptionSchema]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetSubscriptionsBySubscriptionIdResponseDefault | SubscriptionSchema | None:
    """Returns a particular subscription by id


    Required roles:
     - can_read_subscriptions

    Args:
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSubscriptionsBySubscriptionIdResponseDefault | SubscriptionSchema
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | GetSubscriptionsBySubscriptionIdResponseDefault | SubscriptionSchema
]:
    """Returns a particular subscription by id


    Required roles:
     - can_read_subscriptions

    Args:
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSubscriptionsBySubscriptionIdResponseDefault | SubscriptionSchema]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetSubscriptionsBySubscriptionIdResponseDefault | SubscriptionSchema | None:
    """Returns a particular subscription by id


    Required roles:
     - can_read_subscriptions

    Args:
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSubscriptionsBySubscriptionIdResponseDefault | SubscriptionSchema
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
        )
    ).parsed
