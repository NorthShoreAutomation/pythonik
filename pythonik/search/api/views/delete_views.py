from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_views_response_default_type_0 import (
    DeleteViewsResponseDefaultType0,
)
from ...models.delete_views_response_default_type_1 import (
    DeleteViewsResponseDefaultType1,
)
from ...models.search_views_id_schema import SearchViewsIDSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchViewsIDSchema | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/views/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteViewsResponseDefaultType0 | DeleteViewsResponseDefaultType1:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
    ) -> DeleteViewsResponseDefaultType0 | DeleteViewsResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteViewsResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = DeleteViewsResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteViewsResponseDefaultType0 | DeleteViewsResponseDefaultType1]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchViewsIDSchema | Unset = UNSET,
) -> Response[Any | DeleteViewsResponseDefaultType0 | DeleteViewsResponseDefaultType1]:
    """Delete Views for the system domain.


    Required roles:
     - can_delete_search_views

    Args:
        body (SearchViewsIDSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteViewsResponseDefaultType0 | DeleteViewsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchViewsIDSchema | Unset = UNSET,
) -> Any | DeleteViewsResponseDefaultType0 | DeleteViewsResponseDefaultType1 | None:
    """Delete Views for the system domain.


    Required roles:
     - can_delete_search_views

    Args:
        body (SearchViewsIDSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteViewsResponseDefaultType0 | DeleteViewsResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchViewsIDSchema | Unset = UNSET,
) -> Response[Any | DeleteViewsResponseDefaultType0 | DeleteViewsResponseDefaultType1]:
    """Delete Views for the system domain.


    Required roles:
     - can_delete_search_views

    Args:
        body (SearchViewsIDSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteViewsResponseDefaultType0 | DeleteViewsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchViewsIDSchema | Unset = UNSET,
) -> Any | DeleteViewsResponseDefaultType0 | DeleteViewsResponseDefaultType1 | None:
    """Delete Views for the system domain.


    Required roles:
     - can_delete_search_views

    Args:
        body (SearchViewsIDSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteViewsResponseDefaultType0 | DeleteViewsResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
