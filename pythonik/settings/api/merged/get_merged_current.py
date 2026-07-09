from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_merged_current_response_default import (
    GetMergedCurrentResponseDefault,
)
from ...models.merged_settings_schema import MergedSettingsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ignore_logo_url: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ignore_logo_url"] = ignore_logo_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/merged/current/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetMergedCurrentResponseDefault | MergedSettingsSchema:
    if response.status_code == 200:
        response_200 = MergedSettingsSchema.from_dict(response.json())

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

    response_default = GetMergedCurrentResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetMergedCurrentResponseDefault | MergedSettingsSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    ignore_logo_url: bool | Unset = UNSET,
) -> Response[Any | GetMergedCurrentResponseDefault | MergedSettingsSchema]:
    """Get merged settings for current user

    Args:
        ignore_logo_url (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMergedCurrentResponseDefault | MergedSettingsSchema]
    """

    kwargs = _get_kwargs(
        ignore_logo_url=ignore_logo_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    ignore_logo_url: bool | Unset = UNSET,
) -> Any | GetMergedCurrentResponseDefault | MergedSettingsSchema | None:
    """Get merged settings for current user

    Args:
        ignore_logo_url (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMergedCurrentResponseDefault | MergedSettingsSchema
    """

    return sync_detailed(
        client=client,
        ignore_logo_url=ignore_logo_url,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    ignore_logo_url: bool | Unset = UNSET,
) -> Response[Any | GetMergedCurrentResponseDefault | MergedSettingsSchema]:
    """Get merged settings for current user

    Args:
        ignore_logo_url (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMergedCurrentResponseDefault | MergedSettingsSchema]
    """

    kwargs = _get_kwargs(
        ignore_logo_url=ignore_logo_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    ignore_logo_url: bool | Unset = UNSET,
) -> Any | GetMergedCurrentResponseDefault | MergedSettingsSchema | None:
    """Get merged settings for current user

    Args:
        ignore_logo_url (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMergedCurrentResponseDefault | MergedSettingsSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            ignore_logo_url=ignore_logo_url,
        )
    ).parsed
