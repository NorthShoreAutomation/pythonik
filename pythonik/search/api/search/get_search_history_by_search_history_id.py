from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_search_history_by_search_history_id_response_default_type_0 import (
    GetSearchHistoryBySearchHistoryIdResponseDefaultType0,
)
from ...models.get_search_history_by_search_history_id_response_default_type_1 import (
    GetSearchHistoryBySearchHistoryIdResponseDefaultType1,
)
from ...models.search_documents_schema import SearchDocumentsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    search_history_id: str,
    *,
    generate_signed_download_url: bool | Unset = False,
    generate_signed_proxy_url: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["generate_signed_download_url"] = generate_signed_download_url

    params["generate_signed_proxy_url"] = generate_signed_proxy_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/search/history/{search_history_id}/".format(
            search_history_id=quote(str(search_history_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSearchHistoryBySearchHistoryIdResponseDefaultType0
    | GetSearchHistoryBySearchHistoryIdResponseDefaultType1
    | SearchDocumentsSchema
):
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

    def _parse_response_default(
        data: object,
    ) -> (
        GetSearchHistoryBySearchHistoryIdResponseDefaultType0
        | GetSearchHistoryBySearchHistoryIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetSearchHistoryBySearchHistoryIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetSearchHistoryBySearchHistoryIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSearchHistoryBySearchHistoryIdResponseDefaultType0
    | GetSearchHistoryBySearchHistoryIdResponseDefaultType1
    | SearchDocumentsSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    search_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    generate_signed_download_url: bool | Unset = False,
    generate_signed_proxy_url: bool | Unset = False,
) -> Response[
    Any
    | GetSearchHistoryBySearchHistoryIdResponseDefaultType0
    | GetSearchHistoryBySearchHistoryIdResponseDefaultType1
    | SearchDocumentsSchema
]:
    """Returns results of search history


    Required roles:
     - can_read_search_history

    Args:
        search_history_id (str):
        generate_signed_download_url (bool | Unset):  Default: False.
        generate_signed_proxy_url (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchHistoryBySearchHistoryIdResponseDefaultType0 | GetSearchHistoryBySearchHistoryIdResponseDefaultType1 | SearchDocumentsSchema]
    """

    kwargs = _get_kwargs(
        search_history_id=search_history_id,
        generate_signed_download_url=generate_signed_download_url,
        generate_signed_proxy_url=generate_signed_proxy_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    search_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    generate_signed_download_url: bool | Unset = False,
    generate_signed_proxy_url: bool | Unset = False,
) -> (
    Any
    | GetSearchHistoryBySearchHistoryIdResponseDefaultType0
    | GetSearchHistoryBySearchHistoryIdResponseDefaultType1
    | SearchDocumentsSchema
    | None
):
    """Returns results of search history


    Required roles:
     - can_read_search_history

    Args:
        search_history_id (str):
        generate_signed_download_url (bool | Unset):  Default: False.
        generate_signed_proxy_url (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchHistoryBySearchHistoryIdResponseDefaultType0 | GetSearchHistoryBySearchHistoryIdResponseDefaultType1 | SearchDocumentsSchema
    """

    return sync_detailed(
        search_history_id=search_history_id,
        client=client,
        generate_signed_download_url=generate_signed_download_url,
        generate_signed_proxy_url=generate_signed_proxy_url,
    ).parsed


async def asyncio_detailed(
    search_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    generate_signed_download_url: bool | Unset = False,
    generate_signed_proxy_url: bool | Unset = False,
) -> Response[
    Any
    | GetSearchHistoryBySearchHistoryIdResponseDefaultType0
    | GetSearchHistoryBySearchHistoryIdResponseDefaultType1
    | SearchDocumentsSchema
]:
    """Returns results of search history


    Required roles:
     - can_read_search_history

    Args:
        search_history_id (str):
        generate_signed_download_url (bool | Unset):  Default: False.
        generate_signed_proxy_url (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchHistoryBySearchHistoryIdResponseDefaultType0 | GetSearchHistoryBySearchHistoryIdResponseDefaultType1 | SearchDocumentsSchema]
    """

    kwargs = _get_kwargs(
        search_history_id=search_history_id,
        generate_signed_download_url=generate_signed_download_url,
        generate_signed_proxy_url=generate_signed_proxy_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    search_history_id: str,
    *,
    client: AuthenticatedClient | Client,
    generate_signed_download_url: bool | Unset = False,
    generate_signed_proxy_url: bool | Unset = False,
) -> (
    Any
    | GetSearchHistoryBySearchHistoryIdResponseDefaultType0
    | GetSearchHistoryBySearchHistoryIdResponseDefaultType1
    | SearchDocumentsSchema
    | None
):
    """Returns results of search history


    Required roles:
     - can_read_search_history

    Args:
        search_history_id (str):
        generate_signed_download_url (bool | Unset):  Default: False.
        generate_signed_proxy_url (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchHistoryBySearchHistoryIdResponseDefaultType0 | GetSearchHistoryBySearchHistoryIdResponseDefaultType1 | SearchDocumentsSchema
    """

    return (
        await asyncio_detailed(
            search_history_id=search_history_id,
            client=client,
            generate_signed_download_url=generate_signed_download_url,
            generate_signed_proxy_url=generate_signed_proxy_url,
        )
    ).parsed
