from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_search_view_by_view_id_group_ids_response_default_type_0 import (
    GetSearchViewByViewIdGroupIdsResponseDefaultType0,
)
from ...models.get_search_view_by_view_id_group_ids_response_default_type_1 import (
    GetSearchViewByViewIdGroupIdsResponseDefaultType1,
)
from ...models.group_settings_id_schema import GroupSettingsIDSchema
from ...types import Response


def _get_kwargs(
    view_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/search_view/{view_id}/group_ids/".format(
            view_id=quote(str(view_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSearchViewByViewIdGroupIdsResponseDefaultType0
    | GetSearchViewByViewIdGroupIdsResponseDefaultType1
    | GroupSettingsIDSchema
):
    if response.status_code == 200:
        response_200 = GroupSettingsIDSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        GetSearchViewByViewIdGroupIdsResponseDefaultType0
        | GetSearchViewByViewIdGroupIdsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetSearchViewByViewIdGroupIdsResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetSearchViewByViewIdGroupIdsResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSearchViewByViewIdGroupIdsResponseDefaultType0
    | GetSearchViewByViewIdGroupIdsResponseDefaultType1
    | GroupSettingsIDSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetSearchViewByViewIdGroupIdsResponseDefaultType0
    | GetSearchViewByViewIdGroupIdsResponseDefaultType1
    | GroupSettingsIDSchema
]:
    """Get a list of Group IDs that use the given Search View ID

    Args:
        view_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchViewByViewIdGroupIdsResponseDefaultType0 | GetSearchViewByViewIdGroupIdsResponseDefaultType1 | GroupSettingsIDSchema]
    """

    kwargs = _get_kwargs(
        view_id=view_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetSearchViewByViewIdGroupIdsResponseDefaultType0
    | GetSearchViewByViewIdGroupIdsResponseDefaultType1
    | GroupSettingsIDSchema
    | None
):
    """Get a list of Group IDs that use the given Search View ID

    Args:
        view_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchViewByViewIdGroupIdsResponseDefaultType0 | GetSearchViewByViewIdGroupIdsResponseDefaultType1 | GroupSettingsIDSchema
    """

    return sync_detailed(
        view_id=view_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetSearchViewByViewIdGroupIdsResponseDefaultType0
    | GetSearchViewByViewIdGroupIdsResponseDefaultType1
    | GroupSettingsIDSchema
]:
    """Get a list of Group IDs that use the given Search View ID

    Args:
        view_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchViewByViewIdGroupIdsResponseDefaultType0 | GetSearchViewByViewIdGroupIdsResponseDefaultType1 | GroupSettingsIDSchema]
    """

    kwargs = _get_kwargs(
        view_id=view_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetSearchViewByViewIdGroupIdsResponseDefaultType0
    | GetSearchViewByViewIdGroupIdsResponseDefaultType1
    | GroupSettingsIDSchema
    | None
):
    """Get a list of Group IDs that use the given Search View ID

    Args:
        view_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchViewByViewIdGroupIdsResponseDefaultType0 | GetSearchViewByViewIdGroupIdsResponseDefaultType1 | GroupSettingsIDSchema
    """

    return (
        await asyncio_detailed(
            view_id=view_id,
            client=client,
        )
    ).parsed
