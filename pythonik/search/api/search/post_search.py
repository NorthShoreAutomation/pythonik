from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_search_response_default import PostSearchResponseDefault
from ...models.search_criteria_schema import SearchCriteriaSchema
from ...models.search_documents_schema import SearchDocumentsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchCriteriaSchema,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    generate_signed_download_url: bool | Unset = UNSET,
    generate_signed_proxy_url: bool | Unset = UNSET,
    save_search_history: bool | Unset = UNSET,
    types: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params["scroll"] = scroll

    params["scroll_id"] = scroll_id

    params["generate_signed_url"] = generate_signed_url

    params["generate_signed_download_url"] = generate_signed_download_url

    params["generate_signed_proxy_url"] = generate_signed_proxy_url

    params["save_search_history"] = save_search_history

    params["types"] = types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/search/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostSearchResponseDefault | SearchDocumentsSchema:
    if response.status_code == 200:
        response_200 = SearchDocumentsSchema.from_dict(response.json())

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

    response_default = PostSearchResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostSearchResponseDefault | SearchDocumentsSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCriteriaSchema,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    generate_signed_download_url: bool | Unset = UNSET,
    generate_signed_proxy_url: bool | Unset = UNSET,
    save_search_history: bool | Unset = UNSET,
    types: str | Unset = UNSET,
) -> Response[Any | PostSearchResponseDefault | SearchDocumentsSchema]:
    """Search


    Required roles:
     - can_search

    Args:
        per_page (int | Unset):
        page (int | Unset):
        scroll (bool | Unset):
        scroll_id (str | Unset):
        generate_signed_url (bool | Unset):
        generate_signed_download_url (bool | Unset):
        generate_signed_proxy_url (bool | Unset):
        save_search_history (bool | Unset):
        types (str | Unset):
        body (SearchCriteriaSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSearchResponseDefault | SearchDocumentsSchema]
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
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCriteriaSchema,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    generate_signed_download_url: bool | Unset = UNSET,
    generate_signed_proxy_url: bool | Unset = UNSET,
    save_search_history: bool | Unset = UNSET,
    types: str | Unset = UNSET,
) -> Any | PostSearchResponseDefault | SearchDocumentsSchema | None:
    """Search


    Required roles:
     - can_search

    Args:
        per_page (int | Unset):
        page (int | Unset):
        scroll (bool | Unset):
        scroll_id (str | Unset):
        generate_signed_url (bool | Unset):
        generate_signed_download_url (bool | Unset):
        generate_signed_proxy_url (bool | Unset):
        save_search_history (bool | Unset):
        types (str | Unset):
        body (SearchCriteriaSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSearchResponseDefault | SearchDocumentsSchema
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCriteriaSchema,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    generate_signed_download_url: bool | Unset = UNSET,
    generate_signed_proxy_url: bool | Unset = UNSET,
    save_search_history: bool | Unset = UNSET,
    types: str | Unset = UNSET,
) -> Response[Any | PostSearchResponseDefault | SearchDocumentsSchema]:
    """Search


    Required roles:
     - can_search

    Args:
        per_page (int | Unset):
        page (int | Unset):
        scroll (bool | Unset):
        scroll_id (str | Unset):
        generate_signed_url (bool | Unset):
        generate_signed_download_url (bool | Unset):
        generate_signed_proxy_url (bool | Unset):
        save_search_history (bool | Unset):
        types (str | Unset):
        body (SearchCriteriaSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSearchResponseDefault | SearchDocumentsSchema]
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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCriteriaSchema,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    generate_signed_url: bool | Unset = UNSET,
    generate_signed_download_url: bool | Unset = UNSET,
    generate_signed_proxy_url: bool | Unset = UNSET,
    save_search_history: bool | Unset = UNSET,
    types: str | Unset = UNSET,
) -> Any | PostSearchResponseDefault | SearchDocumentsSchema | None:
    """Search


    Required roles:
     - can_search

    Args:
        per_page (int | Unset):
        page (int | Unset):
        scroll (bool | Unset):
        scroll_id (str | Unset):
        generate_signed_url (bool | Unset):
        generate_signed_download_url (bool | Unset):
        generate_signed_proxy_url (bool | Unset):
        save_search_history (bool | Unset):
        types (str | Unset):
        body (SearchCriteriaSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSearchResponseDefault | SearchDocumentsSchema
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
        )
    ).parsed
