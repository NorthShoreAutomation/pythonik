from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_subscriptions_response_default_type_0 import (
    GetSubscriptionsResponseDefaultType0,
)
from ...models.get_subscriptions_response_default_type_1 import (
    GetSubscriptionsResponseDefaultType1,
)
from ...models.subscriptions_schema import SubscriptionsSchema
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/subscriptions/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSubscriptionsResponseDefaultType0
    | GetSubscriptionsResponseDefaultType1
    | SubscriptionsSchema
):
    if response.status_code == 200:
        response_200 = SubscriptionsSchema.from_dict(response.json())

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

    def _parse_response_default(
        data: object,
    ) -> GetSubscriptionsResponseDefaultType0 | GetSubscriptionsResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetSubscriptionsResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetSubscriptionsResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSubscriptionsResponseDefaultType0
    | GetSubscriptionsResponseDefaultType1
    | SubscriptionsSchema
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
    | GetSubscriptionsResponseDefaultType0
    | GetSubscriptionsResponseDefaultType1
    | SubscriptionsSchema
]:
    """Returns all user subscriptions


    Required roles:
     - can_read_subscriptions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSubscriptionsResponseDefaultType0 | GetSubscriptionsResponseDefaultType1 | SubscriptionsSchema]
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
    | GetSubscriptionsResponseDefaultType0
    | GetSubscriptionsResponseDefaultType1
    | SubscriptionsSchema
    | None
):
    """Returns all user subscriptions


    Required roles:
     - can_read_subscriptions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSubscriptionsResponseDefaultType0 | GetSubscriptionsResponseDefaultType1 | SubscriptionsSchema
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetSubscriptionsResponseDefaultType0
    | GetSubscriptionsResponseDefaultType1
    | SubscriptionsSchema
]:
    """Returns all user subscriptions


    Required roles:
     - can_read_subscriptions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSubscriptionsResponseDefaultType0 | GetSubscriptionsResponseDefaultType1 | SubscriptionsSchema]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetSubscriptionsResponseDefaultType0
    | GetSubscriptionsResponseDefaultType1
    | SubscriptionsSchema
    | None
):
    """Returns all user subscriptions


    Required roles:
     - can_read_subscriptions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSubscriptionsResponseDefaultType0 | GetSubscriptionsResponseDefaultType1 | SubscriptionsSchema
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
