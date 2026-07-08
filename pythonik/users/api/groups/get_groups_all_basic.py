from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_groups_all_basic_response_default import (
    GetGroupsAllBasicResponseDefault,
)
from ...models.groups_schema import GroupsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["ids"] = ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/groups/all/basic/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetGroupsAllBasicResponseDefault | GroupsSchema:
    if response.status_code == 200:
        response_200 = GroupsSchema.from_dict(response.json())

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

    response_default = GetGroupsAllBasicResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetGroupsAllBasicResponseDefault | GroupsSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> Response[Any | GetGroupsAllBasicResponseDefault | GroupsSchema]:
    """List all groups without details

    Args:
        page (int | Unset):
        per_page (int | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetGroupsAllBasicResponseDefault | GroupsSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        ids=ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> Any | GetGroupsAllBasicResponseDefault | GroupsSchema | None:
    """List all groups without details

    Args:
        page (int | Unset):
        per_page (int | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetGroupsAllBasicResponseDefault | GroupsSchema
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        ids=ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> Response[Any | GetGroupsAllBasicResponseDefault | GroupsSchema]:
    """List all groups without details

    Args:
        page (int | Unset):
        per_page (int | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetGroupsAllBasicResponseDefault | GroupsSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> Any | GetGroupsAllBasicResponseDefault | GroupsSchema | None:
    """List all groups without details

    Args:
        page (int | Unset):
        per_page (int | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetGroupsAllBasicResponseDefault | GroupsSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            ids=ids,
        )
    ).parsed
