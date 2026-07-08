from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_users_basic_response_default import GetUsersBasicResponseDefault
from ...models.users_basic_schema import UsersBasicSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    email: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    emails: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["sort"] = sort

    params["email"] = email

    params["first_name"] = first_name

    params["last_name"] = last_name

    params["query"] = query

    params["ids"] = ids

    params["emails"] = emails

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/basic/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetUsersBasicResponseDefault | UsersBasicSchema:
    if response.status_code == 200:
        response_200 = UsersBasicSchema.from_dict(response.json())

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

    response_default = GetUsersBasicResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetUsersBasicResponseDefault | UsersBasicSchema]:
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
    sort: str | Unset = UNSET,
    email: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    emails: str | Unset = UNSET,
) -> Response[Any | GetUsersBasicResponseDefault | UsersBasicSchema]:
    """List of users without details

    Args:
        page (int | Unset):
        per_page (int | Unset):
        sort (str | Unset):
        email (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        query (str | Unset):
        ids (str | Unset):
        emails (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUsersBasicResponseDefault | UsersBasicSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        sort=sort,
        email=email,
        first_name=first_name,
        last_name=last_name,
        query=query,
        ids=ids,
        emails=emails,
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
    sort: str | Unset = UNSET,
    email: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    emails: str | Unset = UNSET,
) -> Any | GetUsersBasicResponseDefault | UsersBasicSchema | None:
    """List of users without details

    Args:
        page (int | Unset):
        per_page (int | Unset):
        sort (str | Unset):
        email (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        query (str | Unset):
        ids (str | Unset):
        emails (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUsersBasicResponseDefault | UsersBasicSchema
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        sort=sort,
        email=email,
        first_name=first_name,
        last_name=last_name,
        query=query,
        ids=ids,
        emails=emails,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    email: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    emails: str | Unset = UNSET,
) -> Response[Any | GetUsersBasicResponseDefault | UsersBasicSchema]:
    """List of users without details

    Args:
        page (int | Unset):
        per_page (int | Unset):
        sort (str | Unset):
        email (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        query (str | Unset):
        ids (str | Unset):
        emails (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUsersBasicResponseDefault | UsersBasicSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        sort=sort,
        email=email,
        first_name=first_name,
        last_name=last_name,
        query=query,
        ids=ids,
        emails=emails,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    email: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    emails: str | Unset = UNSET,
) -> Any | GetUsersBasicResponseDefault | UsersBasicSchema | None:
    """List of users without details

    Args:
        page (int | Unset):
        per_page (int | Unset):
        sort (str | Unset):
        email (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        query (str | Unset):
        ids (str | Unset):
        emails (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUsersBasicResponseDefault | UsersBasicSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            sort=sort,
            email=email,
            first_name=first_name,
            last_name=last_name,
            query=query,
            ids=ids,
            emails=emails,
        )
    ).parsed
