from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_shares_response_default import GetSharesResponseDefault
from ...models.shares_elastic_schema import SharesElasticSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    title: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    expires: str | Unset = UNSET,
    include_created_by_me: bool | Unset = UNSET,
    include_member_of: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["title"] = title

    params["object_type"] = object_type

    params["object_id"] = object_id

    params["ids"] = ids

    params["query"] = query

    params["_exists_"] = field_exists

    params["date_created"] = date_created

    params["date_modified"] = date_modified

    params["expires"] = expires

    params["include_created_by_me"] = include_created_by_me

    params["include_member_of"] = include_member_of

    params["page"] = page

    params["per_page"] = per_page

    params["scroll"] = scroll

    params["scroll_id"] = scroll_id

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/shares/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSharesResponseDefault | SharesElasticSchema:
    if response.status_code == 200:
        response_200 = SharesElasticSchema.from_dict(response.json())

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

    response_default = GetSharesResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetSharesResponseDefault | SharesElasticSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    title: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    expires: str | Unset = UNSET,
    include_created_by_me: bool | Unset = UNSET,
    include_member_of: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[Any | GetSharesResponseDefault | SharesElasticSchema]:
    """Get a list of user's shares


    Required roles:
     - can_read_shares

    Args:
        title (str | Unset):
        object_type (str | Unset):
        object_id (str | Unset):
        ids (str | Unset):
        query (str | Unset):
        field_exists (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        expires (str | Unset):
        include_created_by_me (bool | Unset):
        include_member_of (bool | Unset):
        page (int | Unset):
        per_page (int | Unset):
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesResponseDefault | SharesElasticSchema]
    """

    kwargs = _get_kwargs(
        title=title,
        object_type=object_type,
        object_id=object_id,
        ids=ids,
        query=query,
        field_exists=field_exists,
        date_created=date_created,
        date_modified=date_modified,
        expires=expires,
        include_created_by_me=include_created_by_me,
        include_member_of=include_member_of,
        page=page,
        per_page=per_page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    title: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    expires: str | Unset = UNSET,
    include_created_by_me: bool | Unset = UNSET,
    include_member_of: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Any | GetSharesResponseDefault | SharesElasticSchema | None:
    """Get a list of user's shares


    Required roles:
     - can_read_shares

    Args:
        title (str | Unset):
        object_type (str | Unset):
        object_id (str | Unset):
        ids (str | Unset):
        query (str | Unset):
        field_exists (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        expires (str | Unset):
        include_created_by_me (bool | Unset):
        include_member_of (bool | Unset):
        page (int | Unset):
        per_page (int | Unset):
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesResponseDefault | SharesElasticSchema
    """

    return sync_detailed(
        client=client,
        title=title,
        object_type=object_type,
        object_id=object_id,
        ids=ids,
        query=query,
        field_exists=field_exists,
        date_created=date_created,
        date_modified=date_modified,
        expires=expires,
        include_created_by_me=include_created_by_me,
        include_member_of=include_member_of,
        page=page,
        per_page=per_page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    title: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    expires: str | Unset = UNSET,
    include_created_by_me: bool | Unset = UNSET,
    include_member_of: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[Any | GetSharesResponseDefault | SharesElasticSchema]:
    """Get a list of user's shares


    Required roles:
     - can_read_shares

    Args:
        title (str | Unset):
        object_type (str | Unset):
        object_id (str | Unset):
        ids (str | Unset):
        query (str | Unset):
        field_exists (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        expires (str | Unset):
        include_created_by_me (bool | Unset):
        include_member_of (bool | Unset):
        page (int | Unset):
        per_page (int | Unset):
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesResponseDefault | SharesElasticSchema]
    """

    kwargs = _get_kwargs(
        title=title,
        object_type=object_type,
        object_id=object_id,
        ids=ids,
        query=query,
        field_exists=field_exists,
        date_created=date_created,
        date_modified=date_modified,
        expires=expires,
        include_created_by_me=include_created_by_me,
        include_member_of=include_member_of,
        page=page,
        per_page=per_page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    title: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    expires: str | Unset = UNSET,
    include_created_by_me: bool | Unset = UNSET,
    include_member_of: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Any | GetSharesResponseDefault | SharesElasticSchema | None:
    """Get a list of user's shares


    Required roles:
     - can_read_shares

    Args:
        title (str | Unset):
        object_type (str | Unset):
        object_id (str | Unset):
        ids (str | Unset):
        query (str | Unset):
        field_exists (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        expires (str | Unset):
        include_created_by_me (bool | Unset):
        include_member_of (bool | Unset):
        page (int | Unset):
        per_page (int | Unset):
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesResponseDefault | SharesElasticSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            title=title,
            object_type=object_type,
            object_id=object_id,
            ids=ids,
            query=query,
            field_exists=field_exists,
            date_created=date_created,
            date_modified=date_modified,
            expires=expires,
            include_created_by_me=include_created_by_me,
            include_member_of=include_member_of,
            page=page,
            per_page=per_page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
        )
    ).parsed
