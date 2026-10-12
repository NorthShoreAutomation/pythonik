from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_search_content_info_response_default import (
    PostSearchContentInfoResponseDefault,
)
from ...models.search_content_info_schema import SearchContentInfoSchema
from ...models.search_criteria_saved_schema import SearchCriteriaSavedSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchCriteriaSavedSchema,
    format_name: str | Unset = UNSET,
    by_storage_id: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["format_name"] = format_name

    params["by_storage_id"] = by_storage_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/search/content/info/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostSearchContentInfoResponseDefault | SearchContentInfoSchema:
    if response.status_code == 200:
        response_200 = SearchContentInfoSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostSearchContentInfoResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostSearchContentInfoResponseDefault | SearchContentInfoSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCriteriaSavedSchema,
    format_name: str | Unset = UNSET,
    by_storage_id: bool | Unset = UNSET,
) -> Response[Any | PostSearchContentInfoResponseDefault | SearchContentInfoSchema]:
    """Get aggregated information about search results

     <br/>The returned information includes count of assets and collections,<br/>total size of all assets
    (in bytes) and total duration of video and audio<br/>assets (in milliseconds).<br/>The returned
    information includes count of assets and collections,<br/>total size of all assets (in bytes) and
    total duration of video and audio<br/>assets (in milliseconds).
    Required roles:
     - can_search

    Args:
        format_name (str | Unset):
        by_storage_id (bool | Unset):
        body (SearchCriteriaSavedSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSearchContentInfoResponseDefault | SearchContentInfoSchema]
    """

    kwargs = _get_kwargs(
        body=body,
        format_name=format_name,
        by_storage_id=by_storage_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCriteriaSavedSchema,
    format_name: str | Unset = UNSET,
    by_storage_id: bool | Unset = UNSET,
) -> Any | PostSearchContentInfoResponseDefault | SearchContentInfoSchema | None:
    """Get aggregated information about search results

     <br/>The returned information includes count of assets and collections,<br/>total size of all assets
    (in bytes) and total duration of video and audio<br/>assets (in milliseconds).<br/>The returned
    information includes count of assets and collections,<br/>total size of all assets (in bytes) and
    total duration of video and audio<br/>assets (in milliseconds).
    Required roles:
     - can_search

    Args:
        format_name (str | Unset):
        by_storage_id (bool | Unset):
        body (SearchCriteriaSavedSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSearchContentInfoResponseDefault | SearchContentInfoSchema
    """

    return sync_detailed(
        client=client,
        body=body,
        format_name=format_name,
        by_storage_id=by_storage_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCriteriaSavedSchema,
    format_name: str | Unset = UNSET,
    by_storage_id: bool | Unset = UNSET,
) -> Response[Any | PostSearchContentInfoResponseDefault | SearchContentInfoSchema]:
    """Get aggregated information about search results

     <br/>The returned information includes count of assets and collections,<br/>total size of all assets
    (in bytes) and total duration of video and audio<br/>assets (in milliseconds).<br/>The returned
    information includes count of assets and collections,<br/>total size of all assets (in bytes) and
    total duration of video and audio<br/>assets (in milliseconds).
    Required roles:
     - can_search

    Args:
        format_name (str | Unset):
        by_storage_id (bool | Unset):
        body (SearchCriteriaSavedSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSearchContentInfoResponseDefault | SearchContentInfoSchema]
    """

    kwargs = _get_kwargs(
        body=body,
        format_name=format_name,
        by_storage_id=by_storage_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCriteriaSavedSchema,
    format_name: str | Unset = UNSET,
    by_storage_id: bool | Unset = UNSET,
) -> Any | PostSearchContentInfoResponseDefault | SearchContentInfoSchema | None:
    """Get aggregated information about search results

     <br/>The returned information includes count of assets and collections,<br/>total size of all assets
    (in bytes) and total duration of video and audio<br/>assets (in milliseconds).<br/>The returned
    information includes count of assets and collections,<br/>total size of all assets (in bytes) and
    total duration of video and audio<br/>assets (in milliseconds).
    Required roles:
     - can_search

    Args:
        format_name (str | Unset):
        by_storage_id (bool | Unset):
        body (SearchCriteriaSavedSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSearchContentInfoResponseDefault | SearchContentInfoSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            format_name=format_name,
            by_storage_id=by_storage_id,
        )
    ).parsed
