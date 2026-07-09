from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_by_object_type_by_object_id_shares_url_response_default import (
    PostByObjectTypeByObjectIdSharesUrlResponseDefault,
)
from ...models.share_url_create_schema import ShareURLCreateSchema
from ...models.share_url_schema import ShareURLSchema
from ...types import Response


def _get_kwargs(
    object_type: str,
    object_id: str,
    *,
    body: ShareURLCreateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{object_type}/{object_id}/shares/url/".format(
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostByObjectTypeByObjectIdSharesUrlResponseDefault | ShareURLSchema:
    if response.status_code == 200:
        response_200 = ShareURLSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    response_default = PostByObjectTypeByObjectIdSharesUrlResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PostByObjectTypeByObjectIdSharesUrlResponseDefault | ShareURLSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ShareURLCreateSchema,
) -> Response[
    Any | PostByObjectTypeByObjectIdSharesUrlResponseDefault | ShareURLSchema
]:
    """Generates a URL for the shared object


    Required roles:
     - can_write_shares

    Args:
        object_type (str):
        object_id (str):
        body (ShareURLCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostByObjectTypeByObjectIdSharesUrlResponseDefault | ShareURLSchema]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ShareURLCreateSchema,
) -> Any | PostByObjectTypeByObjectIdSharesUrlResponseDefault | ShareURLSchema | None:
    """Generates a URL for the shared object


    Required roles:
     - can_write_shares

    Args:
        object_type (str):
        object_id (str):
        body (ShareURLCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostByObjectTypeByObjectIdSharesUrlResponseDefault | ShareURLSchema
    """

    return sync_detailed(
        object_type=object_type,
        object_id=object_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ShareURLCreateSchema,
) -> Response[
    Any | PostByObjectTypeByObjectIdSharesUrlResponseDefault | ShareURLSchema
]:
    """Generates a URL for the shared object


    Required roles:
     - can_write_shares

    Args:
        object_type (str):
        object_id (str):
        body (ShareURLCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostByObjectTypeByObjectIdSharesUrlResponseDefault | ShareURLSchema]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ShareURLCreateSchema,
) -> Any | PostByObjectTypeByObjectIdSharesUrlResponseDefault | ShareURLSchema | None:
    """Generates a URL for the shared object


    Required roles:
     - can_write_shares

    Args:
        object_type (str):
        object_id (str):
        body (ShareURLCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostByObjectTypeByObjectIdSharesUrlResponseDefault | ShareURLSchema
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            object_id=object_id,
            client=client,
            body=body,
        )
    ).parsed
