from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_users_response_default_type_0 import GetUsersResponseDefaultType0
from ...models.get_users_response_default_type_1 import GetUsersResponseDefaultType1
from ...models.users_schema import UsersSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    sort: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    email: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    groups: str | Unset = UNSET,
    hide_email: str | Unset = UNSET,
    hide_phone: str | Unset = UNSET,
    is_admin: str | Unset = UNSET,
    password_changed: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    photo: str | Unset = UNSET,
    status: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["sort"] = sort

    params["date_created"] = date_created

    params["date_modified"] = date_modified

    params["email"] = email

    params["first_name"] = first_name

    params["last_name"] = last_name

    params["groups"] = groups

    params["hide_email"] = hide_email

    params["hide_phone"] = hide_phone

    params["is_admin"] = is_admin

    params["password_changed"] = password_changed

    params["phone"] = phone

    params["photo"] = photo

    params["status"] = status

    params["query"] = query

    params["ids"] = ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetUsersResponseDefaultType0 | GetUsersResponseDefaultType1 | UsersSchema:
    if response.status_code == 200:
        response_200 = UsersSchema.from_dict(response.json())

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
    ) -> GetUsersResponseDefaultType0 | GetUsersResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetUsersResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetUsersResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetUsersResponseDefaultType0 | GetUsersResponseDefaultType1 | UsersSchema
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
    sort: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    email: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    groups: str | Unset = UNSET,
    hide_email: str | Unset = UNSET,
    hide_phone: str | Unset = UNSET,
    is_admin: str | Unset = UNSET,
    password_changed: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    photo: str | Unset = UNSET,
    status: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> Response[
    Any | GetUsersResponseDefaultType0 | GetUsersResponseDefaultType1 | UsersSchema
]:
    """List of users with details


    Required roles:
     - can_read_users

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        sort (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        email (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        groups (str | Unset):
        hide_email (str | Unset):
        hide_phone (str | Unset):
        is_admin (str | Unset):
        password_changed (str | Unset):
        phone (str | Unset):
        photo (str | Unset):
        status (str | Unset):
        query (str | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUsersResponseDefaultType0 | GetUsersResponseDefaultType1 | UsersSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        sort=sort,
        date_created=date_created,
        date_modified=date_modified,
        email=email,
        first_name=first_name,
        last_name=last_name,
        groups=groups,
        hide_email=hide_email,
        hide_phone=hide_phone,
        is_admin=is_admin,
        password_changed=password_changed,
        phone=phone,
        photo=photo,
        status=status,
        query=query,
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
    sort: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    email: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    groups: str | Unset = UNSET,
    hide_email: str | Unset = UNSET,
    hide_phone: str | Unset = UNSET,
    is_admin: str | Unset = UNSET,
    password_changed: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    photo: str | Unset = UNSET,
    status: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> (
    Any
    | GetUsersResponseDefaultType0
    | GetUsersResponseDefaultType1
    | UsersSchema
    | None
):
    """List of users with details


    Required roles:
     - can_read_users

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        sort (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        email (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        groups (str | Unset):
        hide_email (str | Unset):
        hide_phone (str | Unset):
        is_admin (str | Unset):
        password_changed (str | Unset):
        phone (str | Unset):
        photo (str | Unset):
        status (str | Unset):
        query (str | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUsersResponseDefaultType0 | GetUsersResponseDefaultType1 | UsersSchema
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        sort=sort,
        date_created=date_created,
        date_modified=date_modified,
        email=email,
        first_name=first_name,
        last_name=last_name,
        groups=groups,
        hide_email=hide_email,
        hide_phone=hide_phone,
        is_admin=is_admin,
        password_changed=password_changed,
        phone=phone,
        photo=photo,
        status=status,
        query=query,
        ids=ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    sort: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    email: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    groups: str | Unset = UNSET,
    hide_email: str | Unset = UNSET,
    hide_phone: str | Unset = UNSET,
    is_admin: str | Unset = UNSET,
    password_changed: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    photo: str | Unset = UNSET,
    status: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> Response[
    Any | GetUsersResponseDefaultType0 | GetUsersResponseDefaultType1 | UsersSchema
]:
    """List of users with details


    Required roles:
     - can_read_users

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        sort (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        email (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        groups (str | Unset):
        hide_email (str | Unset):
        hide_phone (str | Unset):
        is_admin (str | Unset):
        password_changed (str | Unset):
        phone (str | Unset):
        photo (str | Unset):
        status (str | Unset):
        query (str | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUsersResponseDefaultType0 | GetUsersResponseDefaultType1 | UsersSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        sort=sort,
        date_created=date_created,
        date_modified=date_modified,
        email=email,
        first_name=first_name,
        last_name=last_name,
        groups=groups,
        hide_email=hide_email,
        hide_phone=hide_phone,
        is_admin=is_admin,
        password_changed=password_changed,
        phone=phone,
        photo=photo,
        status=status,
        query=query,
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    sort: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    email: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    groups: str | Unset = UNSET,
    hide_email: str | Unset = UNSET,
    hide_phone: str | Unset = UNSET,
    is_admin: str | Unset = UNSET,
    password_changed: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    photo: str | Unset = UNSET,
    status: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> (
    Any
    | GetUsersResponseDefaultType0
    | GetUsersResponseDefaultType1
    | UsersSchema
    | None
):
    """List of users with details


    Required roles:
     - can_read_users

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        sort (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        email (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        groups (str | Unset):
        hide_email (str | Unset):
        hide_phone (str | Unset):
        is_admin (str | Unset):
        password_changed (str | Unset):
        phone (str | Unset):
        photo (str | Unset):
        status (str | Unset):
        query (str | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUsersResponseDefaultType0 | GetUsersResponseDefaultType1 | UsersSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            sort=sort,
            date_created=date_created,
            date_modified=date_modified,
            email=email,
            first_name=first_name,
            last_name=last_name,
            groups=groups,
            hide_email=hide_email,
            hide_phone=hide_phone,
            is_admin=is_admin,
            password_changed=password_changed,
            phone=phone,
            photo=photo,
            status=status,
            query=query,
            ids=ids,
        )
    ).parsed
