from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_groups_all_basic_response_default_type_0 import (
    GetGroupsAllBasicResponseDefaultType0,
)
from ...models.get_groups_all_basic_response_default_type_1 import (
    GetGroupsAllBasicResponseDefaultType1,
)
from ...models.groups_schema import GroupsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
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
) -> (
    Any
    | GetGroupsAllBasicResponseDefaultType0
    | GetGroupsAllBasicResponseDefaultType1
    | GroupsSchema
):
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

    def _parse_response_default(
        data: object,
    ) -> GetGroupsAllBasicResponseDefaultType0 | GetGroupsAllBasicResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetGroupsAllBasicResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetGroupsAllBasicResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetGroupsAllBasicResponseDefaultType0
    | GetGroupsAllBasicResponseDefaultType1
    | GroupsSchema
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
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    ids: str | Unset = UNSET,
) -> Response[
    Any
    | GetGroupsAllBasicResponseDefaultType0
    | GetGroupsAllBasicResponseDefaultType1
    | GroupsSchema
]:
    """List all groups without details

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetGroupsAllBasicResponseDefaultType0 | GetGroupsAllBasicResponseDefaultType1 | GroupsSchema]
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
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    ids: str | Unset = UNSET,
) -> (
    Any
    | GetGroupsAllBasicResponseDefaultType0
    | GetGroupsAllBasicResponseDefaultType1
    | GroupsSchema
    | None
):
    """List all groups without details

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetGroupsAllBasicResponseDefaultType0 | GetGroupsAllBasicResponseDefaultType1 | GroupsSchema
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
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    ids: str | Unset = UNSET,
) -> Response[
    Any
    | GetGroupsAllBasicResponseDefaultType0
    | GetGroupsAllBasicResponseDefaultType1
    | GroupsSchema
]:
    """List all groups without details

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetGroupsAllBasicResponseDefaultType0 | GetGroupsAllBasicResponseDefaultType1 | GroupsSchema]
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
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    ids: str | Unset = UNSET,
) -> (
    Any
    | GetGroupsAllBasicResponseDefaultType0
    | GetGroupsAllBasicResponseDefaultType1
    | GroupsSchema
    | None
):
    """List all groups without details

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetGroupsAllBasicResponseDefaultType0 | GetGroupsAllBasicResponseDefaultType1 | GroupsSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            ids=ids,
        )
    ).parsed
