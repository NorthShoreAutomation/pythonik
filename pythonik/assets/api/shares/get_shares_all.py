from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_shares_all_response_default_type_0 import (
    GetSharesAllResponseDefaultType0,
)
from ...models.get_shares_all_response_default_type_1 import (
    GetSharesAllResponseDefaultType1,
)
from ...models.shares_elastic_schema import SharesElasticSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    title: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    owner_id: str | Unset = UNSET,
    member_id: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    expires: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["title"] = title

    params["object_type"] = object_type

    params["object_id"] = object_id

    params["owner_id"] = owner_id

    params["member_id"] = member_id

    params["ids"] = ids

    params["query"] = query

    params["_exists_"] = field_exists

    params["date_created"] = date_created

    params["date_modified"] = date_modified

    params["expires"] = expires

    params["page"] = page

    params["per_page"] = per_page

    params["scroll"] = scroll

    params["scroll_id"] = scroll_id

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/shares/all/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSharesAllResponseDefaultType0
    | GetSharesAllResponseDefaultType1
    | SharesElasticSchema
):
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

    def _parse_response_default(
        data: object,
    ) -> GetSharesAllResponseDefaultType0 | GetSharesAllResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetSharesAllResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetSharesAllResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSharesAllResponseDefaultType0
    | GetSharesAllResponseDefaultType1
    | SharesElasticSchema
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
    title: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    owner_id: str | Unset = UNSET,
    member_id: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    expires: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[
    Any
    | GetSharesAllResponseDefaultType0
    | GetSharesAllResponseDefaultType1
    | SharesElasticSchema
]:
    """Get a list of all domain shares


    Required roles:
     - can_manage_all_shares

    Args:
        title (str | Unset):
        object_type (str | Unset):
        object_id (str | Unset):
        owner_id (str | Unset):
        member_id (str | Unset):
        ids (str | Unset):
        query (str | Unset):
        field_exists (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        expires (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesAllResponseDefaultType0 | GetSharesAllResponseDefaultType1 | SharesElasticSchema]
    """

    kwargs = _get_kwargs(
        title=title,
        object_type=object_type,
        object_id=object_id,
        owner_id=owner_id,
        member_id=member_id,
        ids=ids,
        query=query,
        field_exists=field_exists,
        date_created=date_created,
        date_modified=date_modified,
        expires=expires,
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
    owner_id: str | Unset = UNSET,
    member_id: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    expires: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> (
    Any
    | GetSharesAllResponseDefaultType0
    | GetSharesAllResponseDefaultType1
    | SharesElasticSchema
    | None
):
    """Get a list of all domain shares


    Required roles:
     - can_manage_all_shares

    Args:
        title (str | Unset):
        object_type (str | Unset):
        object_id (str | Unset):
        owner_id (str | Unset):
        member_id (str | Unset):
        ids (str | Unset):
        query (str | Unset):
        field_exists (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        expires (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesAllResponseDefaultType0 | GetSharesAllResponseDefaultType1 | SharesElasticSchema
    """

    return sync_detailed(
        client=client,
        title=title,
        object_type=object_type,
        object_id=object_id,
        owner_id=owner_id,
        member_id=member_id,
        ids=ids,
        query=query,
        field_exists=field_exists,
        date_created=date_created,
        date_modified=date_modified,
        expires=expires,
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
    owner_id: str | Unset = UNSET,
    member_id: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    expires: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[
    Any
    | GetSharesAllResponseDefaultType0
    | GetSharesAllResponseDefaultType1
    | SharesElasticSchema
]:
    """Get a list of all domain shares


    Required roles:
     - can_manage_all_shares

    Args:
        title (str | Unset):
        object_type (str | Unset):
        object_id (str | Unset):
        owner_id (str | Unset):
        member_id (str | Unset):
        ids (str | Unset):
        query (str | Unset):
        field_exists (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        expires (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesAllResponseDefaultType0 | GetSharesAllResponseDefaultType1 | SharesElasticSchema]
    """

    kwargs = _get_kwargs(
        title=title,
        object_type=object_type,
        object_id=object_id,
        owner_id=owner_id,
        member_id=member_id,
        ids=ids,
        query=query,
        field_exists=field_exists,
        date_created=date_created,
        date_modified=date_modified,
        expires=expires,
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
    owner_id: str | Unset = UNSET,
    member_id: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    expires: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> (
    Any
    | GetSharesAllResponseDefaultType0
    | GetSharesAllResponseDefaultType1
    | SharesElasticSchema
    | None
):
    """Get a list of all domain shares


    Required roles:
     - can_manage_all_shares

    Args:
        title (str | Unset):
        object_type (str | Unset):
        object_id (str | Unset):
        owner_id (str | Unset):
        member_id (str | Unset):
        ids (str | Unset):
        query (str | Unset):
        field_exists (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        expires (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesAllResponseDefaultType0 | GetSharesAllResponseDefaultType1 | SharesElasticSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            title=title,
            object_type=object_type,
            object_id=object_id,
            owner_id=owner_id,
            member_id=member_id,
            ids=ids,
            query=query,
            field_exists=field_exists,
            date_created=date_created,
            date_modified=date_modified,
            expires=expires,
            page=page,
            per_page=per_page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
        )
    ).parsed
