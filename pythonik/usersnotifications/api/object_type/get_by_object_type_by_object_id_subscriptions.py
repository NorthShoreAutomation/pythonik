from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_by_object_type_by_object_id_subscriptions_response_default import (
    GetByObjectTypeByObjectIdSubscriptionsResponseDefault,
)
from ...models.subscriptions_schema import SubscriptionsSchema
from ...types import Response


def _get_kwargs(
    object_type: str,
    object_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{object_type}/{object_id}/subscriptions/".format(
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetByObjectTypeByObjectIdSubscriptionsResponseDefault | SubscriptionsSchema:
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

    response_default = GetByObjectTypeByObjectIdSubscriptionsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetByObjectTypeByObjectIdSubscriptionsResponseDefault | SubscriptionsSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | GetByObjectTypeByObjectIdSubscriptionsResponseDefault | SubscriptionsSchema
]:
    """Returns user subscriptions for a specific object_type and object_id


    Required roles:
     - can_read_subscriptions

    Args:
        object_type (str):
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetByObjectTypeByObjectIdSubscriptionsResponseDefault | SubscriptionsSchema]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetByObjectTypeByObjectIdSubscriptionsResponseDefault
    | SubscriptionsSchema
    | None
):
    """Returns user subscriptions for a specific object_type and object_id


    Required roles:
     - can_read_subscriptions

    Args:
        object_type (str):
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetByObjectTypeByObjectIdSubscriptionsResponseDefault | SubscriptionsSchema
    """

    return sync_detailed(
        object_type=object_type,
        object_id=object_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | GetByObjectTypeByObjectIdSubscriptionsResponseDefault | SubscriptionsSchema
]:
    """Returns user subscriptions for a specific object_type and object_id


    Required roles:
     - can_read_subscriptions

    Args:
        object_type (str):
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetByObjectTypeByObjectIdSubscriptionsResponseDefault | SubscriptionsSchema]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetByObjectTypeByObjectIdSubscriptionsResponseDefault
    | SubscriptionsSchema
    | None
):
    """Returns user subscriptions for a specific object_type and object_id


    Required roles:
     - can_read_subscriptions

    Args:
        object_type (str):
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetByObjectTypeByObjectIdSubscriptionsResponseDefault | SubscriptionsSchema
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            object_id=object_id,
            client=client,
        )
    ).parsed
