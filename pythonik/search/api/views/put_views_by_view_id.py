from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_views_by_view_id_response_default_type_0 import (
    PutViewsByViewIdResponseDefaultType0,
)
from ...models.put_views_by_view_id_response_default_type_1 import (
    PutViewsByViewIdResponseDefaultType1,
)
from ...models.search_view_schema import SearchViewSchema
from ...types import Response


def _get_kwargs(
    view_id: str,
    *,
    body: SearchViewSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/views/{view_id}/".format(
            view_id=quote(str(view_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PutViewsByViewIdResponseDefaultType0
    | PutViewsByViewIdResponseDefaultType1
    | SearchViewSchema
):
    if response.status_code == 200:
        response_200 = SearchViewSchema.from_dict(response.json())

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
    ) -> PutViewsByViewIdResponseDefaultType0 | PutViewsByViewIdResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PutViewsByViewIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PutViewsByViewIdResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PutViewsByViewIdResponseDefaultType0
    | PutViewsByViewIdResponseDefaultType1
    | SearchViewSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SearchViewSchema,
) -> Response[
    Any
    | PutViewsByViewIdResponseDefaultType0
    | PutViewsByViewIdResponseDefaultType1
    | SearchViewSchema
]:
    """Replace a View for the system domain.


    Required roles:
     - can_write_search_views

    Args:
        view_id (str):
        body (SearchViewSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutViewsByViewIdResponseDefaultType0 | PutViewsByViewIdResponseDefaultType1 | SearchViewSchema]
    """

    kwargs = _get_kwargs(
        view_id=view_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SearchViewSchema,
) -> (
    Any
    | PutViewsByViewIdResponseDefaultType0
    | PutViewsByViewIdResponseDefaultType1
    | SearchViewSchema
    | None
):
    """Replace a View for the system domain.


    Required roles:
     - can_write_search_views

    Args:
        view_id (str):
        body (SearchViewSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutViewsByViewIdResponseDefaultType0 | PutViewsByViewIdResponseDefaultType1 | SearchViewSchema
    """

    return sync_detailed(
        view_id=view_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SearchViewSchema,
) -> Response[
    Any
    | PutViewsByViewIdResponseDefaultType0
    | PutViewsByViewIdResponseDefaultType1
    | SearchViewSchema
]:
    """Replace a View for the system domain.


    Required roles:
     - can_write_search_views

    Args:
        view_id (str):
        body (SearchViewSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutViewsByViewIdResponseDefaultType0 | PutViewsByViewIdResponseDefaultType1 | SearchViewSchema]
    """

    kwargs = _get_kwargs(
        view_id=view_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SearchViewSchema,
) -> (
    Any
    | PutViewsByViewIdResponseDefaultType0
    | PutViewsByViewIdResponseDefaultType1
    | SearchViewSchema
    | None
):
    """Replace a View for the system domain.


    Required roles:
     - can_write_search_views

    Args:
        view_id (str):
        body (SearchViewSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutViewsByViewIdResponseDefaultType0 | PutViewsByViewIdResponseDefaultType1 | SearchViewSchema
    """

    return (
        await asyncio_detailed(
            view_id=view_id,
            client=client,
            body=body,
        )
    ).parsed
