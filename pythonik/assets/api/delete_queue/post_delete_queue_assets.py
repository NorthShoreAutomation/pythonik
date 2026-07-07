from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_queue_schema import DeleteQueueSchema
from ...models.post_delete_queue_assets_response_default_type_0 import (
    PostDeleteQueueAssetsResponseDefaultType0,
)
from ...models.post_delete_queue_assets_response_default_type_1 import (
    PostDeleteQueueAssetsResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    *,
    body: DeleteQueueSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/delete_queue/assets/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostDeleteQueueAssetsResponseDefaultType0
    | PostDeleteQueueAssetsResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PostDeleteQueueAssetsResponseDefaultType0
        | PostDeleteQueueAssetsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostDeleteQueueAssetsResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostDeleteQueueAssetsResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostDeleteQueueAssetsResponseDefaultType0
    | PostDeleteQueueAssetsResponseDefaultType1
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
    body: DeleteQueueSchema,
) -> Response[
    Any
    | PostDeleteQueueAssetsResponseDefaultType0
    | PostDeleteQueueAssetsResponseDefaultType1
]:
    """Add assets to a delete queue (Mark assets as deleted)


    Required roles:
     - can_delete_assets

    Args:
        body (DeleteQueueSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostDeleteQueueAssetsResponseDefaultType0 | PostDeleteQueueAssetsResponseDefaultType1]
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
    body: DeleteQueueSchema,
) -> (
    Any
    | PostDeleteQueueAssetsResponseDefaultType0
    | PostDeleteQueueAssetsResponseDefaultType1
    | None
):
    """Add assets to a delete queue (Mark assets as deleted)


    Required roles:
     - can_delete_assets

    Args:
        body (DeleteQueueSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostDeleteQueueAssetsResponseDefaultType0 | PostDeleteQueueAssetsResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteQueueSchema,
) -> Response[
    Any
    | PostDeleteQueueAssetsResponseDefaultType0
    | PostDeleteQueueAssetsResponseDefaultType1
]:
    """Add assets to a delete queue (Mark assets as deleted)


    Required roles:
     - can_delete_assets

    Args:
        body (DeleteQueueSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostDeleteQueueAssetsResponseDefaultType0 | PostDeleteQueueAssetsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteQueueSchema,
) -> (
    Any
    | PostDeleteQueueAssetsResponseDefaultType0
    | PostDeleteQueueAssetsResponseDefaultType1
    | None
):
    """Add assets to a delete queue (Mark assets as deleted)


    Required roles:
     - can_delete_assets

    Args:
        body (DeleteQueueSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostDeleteQueueAssetsResponseDefaultType0 | PostDeleteQueueAssetsResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
