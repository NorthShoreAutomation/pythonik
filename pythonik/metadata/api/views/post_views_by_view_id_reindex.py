from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_views_by_view_id_reindex_response_default_type_0 import (
    PostViewsByViewIdReindexResponseDefaultType0,
)
from ...models.post_views_by_view_id_reindex_response_default_type_1 import (
    PostViewsByViewIdReindexResponseDefaultType1,
)
from ...models.reindex_metadata_view_schema import ReindexMetadataViewSchema
from ...types import Response


def _get_kwargs(
    view_id: str,
    *,
    body: ReindexMetadataViewSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/views/{view_id}/reindex/".format(
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
    | PostViewsByViewIdReindexResponseDefaultType0
    | PostViewsByViewIdReindexResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        PostViewsByViewIdReindexResponseDefaultType0
        | PostViewsByViewIdReindexResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostViewsByViewIdReindexResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostViewsByViewIdReindexResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostViewsByViewIdReindexResponseDefaultType0
    | PostViewsByViewIdReindexResponseDefaultType1
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
    body: ReindexMetadataViewSchema,
) -> Response[
    Any
    | PostViewsByViewIdReindexResponseDefaultType0
    | PostViewsByViewIdReindexResponseDefaultType1
]:
    """Reindex metadata views


    Required roles:
     - can_reindex_metadata_views

    Args:
        view_id (str):
        body (ReindexMetadataViewSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostViewsByViewIdReindexResponseDefaultType0 | PostViewsByViewIdReindexResponseDefaultType1]
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
    body: ReindexMetadataViewSchema,
) -> (
    Any
    | PostViewsByViewIdReindexResponseDefaultType0
    | PostViewsByViewIdReindexResponseDefaultType1
    | None
):
    """Reindex metadata views


    Required roles:
     - can_reindex_metadata_views

    Args:
        view_id (str):
        body (ReindexMetadataViewSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostViewsByViewIdReindexResponseDefaultType0 | PostViewsByViewIdReindexResponseDefaultType1
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
    body: ReindexMetadataViewSchema,
) -> Response[
    Any
    | PostViewsByViewIdReindexResponseDefaultType0
    | PostViewsByViewIdReindexResponseDefaultType1
]:
    """Reindex metadata views


    Required roles:
     - can_reindex_metadata_views

    Args:
        view_id (str):
        body (ReindexMetadataViewSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostViewsByViewIdReindexResponseDefaultType0 | PostViewsByViewIdReindexResponseDefaultType1]
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
    body: ReindexMetadataViewSchema,
) -> (
    Any
    | PostViewsByViewIdReindexResponseDefaultType0
    | PostViewsByViewIdReindexResponseDefaultType1
    | None
):
    """Reindex metadata views


    Required roles:
     - can_reindex_metadata_views

    Args:
        view_id (str):
        body (ReindexMetadataViewSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostViewsByViewIdReindexResponseDefaultType0 | PostViewsByViewIdReindexResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            view_id=view_id,
            client=client,
            body=body,
        )
    ).parsed
