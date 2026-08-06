from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_search_view_by_view_id_group_ids_response_default import (
    DeleteSearchViewByViewIdGroupIdsResponseDefault,
)
from ...models.group_settings_id_schema import GroupSettingsIDSchema
from ...types import Response


def _get_kwargs(
    view_id: str,
    *,
    body: GroupSettingsIDSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/search_view/{view_id}/group_ids/".format(
            view_id=quote(str(view_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteSearchViewByViewIdGroupIdsResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = DeleteSearchViewByViewIdGroupIdsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteSearchViewByViewIdGroupIdsResponseDefault]:
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
    body: GroupSettingsIDSchema,
) -> Response[Any | DeleteSearchViewByViewIdGroupIdsResponseDefault]:
    """Remove the Search View ID from any Group ID in the list.

    Args:
        view_id (str):
        body (GroupSettingsIDSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSearchViewByViewIdGroupIdsResponseDefault]
    """

    kwargs = _get_kwargs(
        view_id=view_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GroupSettingsIDSchema,
) -> Any | DeleteSearchViewByViewIdGroupIdsResponseDefault | None:
    """Remove the Search View ID from any Group ID in the list.

    Args:
        view_id (str):
        body (GroupSettingsIDSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSearchViewByViewIdGroupIdsResponseDefault
    """

    return sync_detailed(
        view_id=view_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GroupSettingsIDSchema,
) -> Response[Any | DeleteSearchViewByViewIdGroupIdsResponseDefault]:
    """Remove the Search View ID from any Group ID in the list.

    Args:
        view_id (str):
        body (GroupSettingsIDSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSearchViewByViewIdGroupIdsResponseDefault]
    """

    kwargs = _get_kwargs(
        view_id=view_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GroupSettingsIDSchema,
) -> Any | DeleteSearchViewByViewIdGroupIdsResponseDefault | None:
    """Remove the Search View ID from any Group ID in the list.

    Args:
        view_id (str):
        body (GroupSettingsIDSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSearchViewByViewIdGroupIdsResponseDefault
    """

    return (
        await asyncio_detailed(
            view_id=view_id,
            client=client,
            body=body,
        )
    ).parsed
