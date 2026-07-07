from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_group_by_group_id_response_default_type_0 import (
    GetGroupByGroupIdResponseDefaultType0,
)
from ...models.get_group_by_group_id_response_default_type_1 import (
    GetGroupByGroupIdResponseDefaultType1,
)
from ...models.group_setting_public_schema import GroupSettingPublicSchema
from ...types import Response


def _get_kwargs(
    group_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/group/{group_id}/".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetGroupByGroupIdResponseDefaultType0
    | GetGroupByGroupIdResponseDefaultType1
    | GroupSettingPublicSchema
):
    if response.status_code == 200:
        response_200 = GroupSettingPublicSchema.from_dict(response.json())

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
    ) -> GetGroupByGroupIdResponseDefaultType0 | GetGroupByGroupIdResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetGroupByGroupIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetGroupByGroupIdResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetGroupByGroupIdResponseDefaultType0
    | GetGroupByGroupIdResponseDefaultType1
    | GroupSettingPublicSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetGroupByGroupIdResponseDefaultType0
    | GetGroupByGroupIdResponseDefaultType1
    | GroupSettingPublicSchema
]:
    """Group settings

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetGroupByGroupIdResponseDefaultType0 | GetGroupByGroupIdResponseDefaultType1 | GroupSettingPublicSchema]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetGroupByGroupIdResponseDefaultType0
    | GetGroupByGroupIdResponseDefaultType1
    | GroupSettingPublicSchema
    | None
):
    """Group settings

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetGroupByGroupIdResponseDefaultType0 | GetGroupByGroupIdResponseDefaultType1 | GroupSettingPublicSchema
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetGroupByGroupIdResponseDefaultType0
    | GetGroupByGroupIdResponseDefaultType1
    | GroupSettingPublicSchema
]:
    """Group settings

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetGroupByGroupIdResponseDefaultType0 | GetGroupByGroupIdResponseDefaultType1 | GroupSettingPublicSchema]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetGroupByGroupIdResponseDefaultType0
    | GetGroupByGroupIdResponseDefaultType1
    | GroupSettingPublicSchema
    | None
):
    """Group settings

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetGroupByGroupIdResponseDefaultType0 | GetGroupByGroupIdResponseDefaultType1 | GroupSettingPublicSchema
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
