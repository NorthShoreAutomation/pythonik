from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_merged_by_user_id_response_default import (
    GetMergedByUserIdResponseDefault,
)
from ...models.merged_settings_schema import MergedSettingsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    ignore_logo_url: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ignore_logo_url"] = ignore_logo_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/merged/{user_id}/".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetMergedByUserIdResponseDefault | MergedSettingsSchema:
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

    response_default = GetMergedByUserIdResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetMergedByUserIdResponseDefault | MergedSettingsSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    ignore_logo_url: bool | Unset = UNSET,
) -> Response[Any | GetMergedByUserIdResponseDefault | MergedSettingsSchema]:
    """Get merged settings for a specific user

    Args:
        user_id (str):
        ignore_logo_url (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMergedByUserIdResponseDefault | MergedSettingsSchema]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        ignore_logo_url=ignore_logo_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    ignore_logo_url: bool | Unset = UNSET,
) -> Any | GetMergedByUserIdResponseDefault | MergedSettingsSchema | None:
    """Get merged settings for a specific user

    Args:
        user_id (str):
        ignore_logo_url (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMergedByUserIdResponseDefault | MergedSettingsSchema
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        ignore_logo_url=ignore_logo_url,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    ignore_logo_url: bool | Unset = UNSET,
) -> Response[Any | GetMergedByUserIdResponseDefault | MergedSettingsSchema]:
    """Get merged settings for a specific user

    Args:
        user_id (str):
        ignore_logo_url (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMergedByUserIdResponseDefault | MergedSettingsSchema]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        ignore_logo_url=ignore_logo_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    ignore_logo_url: bool | Unset = UNSET,
) -> Any | GetMergedByUserIdResponseDefault | MergedSettingsSchema | None:
    """Get merged settings for a specific user

    Args:
        user_id (str):
        ignore_logo_url (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMergedByUserIdResponseDefault | MergedSettingsSchema
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            ignore_logo_url=ignore_logo_url,
        )
    ).parsed
