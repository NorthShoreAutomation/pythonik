from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.collection_usages_schema import CollectionUsagesSchema
from ...models.get_collections_by_by_period_response_default import (
    GetCollectionsByByPeriodResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    period: str,
    *,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from_date"] = from_date

    params["to_date"] = to_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/collections/by/{period}/".format(
            period=quote(str(period), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CollectionUsagesSchema | GetCollectionsByByPeriodResponseDefault:
    if response.status_code == 200:
        response_200 = CollectionUsagesSchema.from_dict(response.json())

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

    response_default = GetCollectionsByByPeriodResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CollectionUsagesSchema | GetCollectionsByByPeriodResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    period: str,
    *,
    client: AuthenticatedClient | Client,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
) -> Response[Any | CollectionUsagesSchema | GetCollectionsByByPeriodResponseDefault]:
    """Returns all collection usage


    Required roles:
     - can_read_stats

    Args:
        period (str):
        from_date (str | Unset):
        to_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionUsagesSchema | GetCollectionsByByPeriodResponseDefault]
    """

    kwargs = _get_kwargs(
        period=period,
        from_date=from_date,
        to_date=to_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    period: str,
    *,
    client: AuthenticatedClient | Client,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
) -> Any | CollectionUsagesSchema | GetCollectionsByByPeriodResponseDefault | None:
    """Returns all collection usage


    Required roles:
     - can_read_stats

    Args:
        period (str):
        from_date (str | Unset):
        to_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionUsagesSchema | GetCollectionsByByPeriodResponseDefault
    """

    return sync_detailed(
        period=period,
        client=client,
        from_date=from_date,
        to_date=to_date,
    ).parsed


async def asyncio_detailed(
    period: str,
    *,
    client: AuthenticatedClient | Client,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
) -> Response[Any | CollectionUsagesSchema | GetCollectionsByByPeriodResponseDefault]:
    """Returns all collection usage


    Required roles:
     - can_read_stats

    Args:
        period (str):
        from_date (str | Unset):
        to_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionUsagesSchema | GetCollectionsByByPeriodResponseDefault]
    """

    kwargs = _get_kwargs(
        period=period,
        from_date=from_date,
        to_date=to_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    period: str,
    *,
    client: AuthenticatedClient | Client,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
) -> Any | CollectionUsagesSchema | GetCollectionsByByPeriodResponseDefault | None:
    """Returns all collection usage


    Required roles:
     - can_read_stats

    Args:
        period (str):
        from_date (str | Unset):
        to_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionUsagesSchema | GetCollectionsByByPeriodResponseDefault
    """

    return (
        await asyncio_detailed(
            period=period,
            client=client,
            from_date=from_date,
            to_date=to_date,
        )
    ).parsed
