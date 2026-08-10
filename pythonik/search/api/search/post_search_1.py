from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.search_criteria import SearchCriteria
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchCriteria,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: None | str | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    generate_signed_download_url: bool | Unset = UNSET,
    generate_signed_proxy_url: bool | Unset = UNSET,
    save_search_history: bool | Unset = UNSET,
    types: None | str | Unset = UNSET,
    include_users: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params["scroll"] = scroll

    json_scroll_id: None | str | Unset
    if isinstance(scroll_id, Unset):
        json_scroll_id = UNSET
    else:
        json_scroll_id = scroll_id
    params["scroll_id"] = json_scroll_id

    params["generate_signed_url"] = generate_signed_url

    params["generate_signed_download_url"] = generate_signed_download_url

    params["generate_signed_proxy_url"] = generate_signed_proxy_url

    params["save_search_history"] = save_search_history

    json_types: None | str | Unset
    if isinstance(types, Unset):
        json_types = UNSET
    else:
        json_types = types
    params["types"] = json_types

    params["include_users"] = include_users

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/search/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCriteria,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: None | str | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    generate_signed_download_url: bool | Unset = UNSET,
    generate_signed_proxy_url: bool | Unset = UNSET,
    save_search_history: bool | Unset = UNSET,
    types: None | str | Unset = UNSET,
    include_users: bool | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Search

     Required roles:
    - can_search

    Args:
        per_page (int | Unset):
        page (int | Unset):
        scroll (bool | Unset):
        scroll_id (None | str | Unset):
        generate_signed_url (bool | Unset):
        generate_signed_download_url (bool | Unset):
        generate_signed_proxy_url (bool | Unset):
        save_search_history (bool | Unset):
        types (None | str | Unset):
        include_users (bool | Unset):
        body (SearchCriteria):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        generate_signed_url=generate_signed_url,
        generate_signed_download_url=generate_signed_download_url,
        generate_signed_proxy_url=generate_signed_proxy_url,
        save_search_history=save_search_history,
        types=types,
        include_users=include_users,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCriteria,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: None | str | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    generate_signed_download_url: bool | Unset = UNSET,
    generate_signed_proxy_url: bool | Unset = UNSET,
    save_search_history: bool | Unset = UNSET,
    types: None | str | Unset = UNSET,
    include_users: bool | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Search

     Required roles:
    - can_search

    Args:
        per_page (int | Unset):
        page (int | Unset):
        scroll (bool | Unset):
        scroll_id (None | str | Unset):
        generate_signed_url (bool | Unset):
        generate_signed_download_url (bool | Unset):
        generate_signed_proxy_url (bool | Unset):
        save_search_history (bool | Unset):
        types (None | str | Unset):
        include_users (bool | Unset):
        body (SearchCriteria):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        generate_signed_url=generate_signed_url,
        generate_signed_download_url=generate_signed_download_url,
        generate_signed_proxy_url=generate_signed_proxy_url,
        save_search_history=save_search_history,
        types=types,
        include_users=include_users,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCriteria,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: None | str | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    generate_signed_download_url: bool | Unset = UNSET,
    generate_signed_proxy_url: bool | Unset = UNSET,
    save_search_history: bool | Unset = UNSET,
    types: None | str | Unset = UNSET,
    include_users: bool | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Search

     Required roles:
    - can_search

    Args:
        per_page (int | Unset):
        page (int | Unset):
        scroll (bool | Unset):
        scroll_id (None | str | Unset):
        generate_signed_url (bool | Unset):
        generate_signed_download_url (bool | Unset):
        generate_signed_proxy_url (bool | Unset):
        save_search_history (bool | Unset):
        types (None | str | Unset):
        include_users (bool | Unset):
        body (SearchCriteria):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        generate_signed_url=generate_signed_url,
        generate_signed_download_url=generate_signed_download_url,
        generate_signed_proxy_url=generate_signed_proxy_url,
        save_search_history=save_search_history,
        types=types,
        include_users=include_users,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCriteria,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: None | str | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    generate_signed_download_url: bool | Unset = UNSET,
    generate_signed_proxy_url: bool | Unset = UNSET,
    save_search_history: bool | Unset = UNSET,
    types: None | str | Unset = UNSET,
    include_users: bool | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Search

     Required roles:
    - can_search

    Args:
        per_page (int | Unset):
        page (int | Unset):
        scroll (bool | Unset):
        scroll_id (None | str | Unset):
        generate_signed_url (bool | Unset):
        generate_signed_download_url (bool | Unset):
        generate_signed_proxy_url (bool | Unset):
        save_search_history (bool | Unset):
        types (None | str | Unset):
        include_users (bool | Unset):
        body (SearchCriteria):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            generate_signed_url=generate_signed_url,
            generate_signed_download_url=generate_signed_download_url,
            generate_signed_proxy_url=generate_signed_proxy_url,
            save_search_history=save_search_history,
            types=types,
            include_users=include_users,
        )
    ).parsed
