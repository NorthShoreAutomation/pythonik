from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.metadata_values_schema import MetadataValuesSchema
from ...models.put_by_object_type_by_object_id_response_default import (
    PutByObjectTypeByObjectIdResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    object_type: str,
    object_id: str,
    *,
    body: MetadataValuesSchema,
    check_if_subclip: bool | Unset = UNSET,
    ignore_unchanged: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["check_if_subclip"] = check_if_subclip

    params["ignore_unchanged"] = ignore_unchanged

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/{object_type}/{object_id}/".format(
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MetadataValuesSchema | PutByObjectTypeByObjectIdResponseDefault:
    if response.status_code == 200:
        response_200 = MetadataValuesSchema.from_dict(response.json())

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

    response_default = PutByObjectTypeByObjectIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | MetadataValuesSchema | PutByObjectTypeByObjectIdResponseDefault]:
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
    body: MetadataValuesSchema,
    check_if_subclip: bool | Unset = UNSET,
    ignore_unchanged: bool | Unset = UNSET,
) -> Response[Any | MetadataValuesSchema | PutByObjectTypeByObjectIdResponseDefault]:
    """Edit metadata values directly without a view. Admin access required.

    Args:
        object_type (str):
        object_id (str):
        check_if_subclip (bool | Unset):
        ignore_unchanged (bool | Unset):
        body (MetadataValuesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MetadataValuesSchema | PutByObjectTypeByObjectIdResponseDefault]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        body=body,
        check_if_subclip=check_if_subclip,
        ignore_unchanged=ignore_unchanged,
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
    body: MetadataValuesSchema,
    check_if_subclip: bool | Unset = UNSET,
    ignore_unchanged: bool | Unset = UNSET,
) -> Any | MetadataValuesSchema | PutByObjectTypeByObjectIdResponseDefault | None:
    """Edit metadata values directly without a view. Admin access required.

    Args:
        object_type (str):
        object_id (str):
        check_if_subclip (bool | Unset):
        ignore_unchanged (bool | Unset):
        body (MetadataValuesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MetadataValuesSchema | PutByObjectTypeByObjectIdResponseDefault
    """

    return sync_detailed(
        object_type=object_type,
        object_id=object_id,
        client=client,
        body=body,
        check_if_subclip=check_if_subclip,
        ignore_unchanged=ignore_unchanged,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MetadataValuesSchema,
    check_if_subclip: bool | Unset = UNSET,
    ignore_unchanged: bool | Unset = UNSET,
) -> Response[Any | MetadataValuesSchema | PutByObjectTypeByObjectIdResponseDefault]:
    """Edit metadata values directly without a view. Admin access required.

    Args:
        object_type (str):
        object_id (str):
        check_if_subclip (bool | Unset):
        ignore_unchanged (bool | Unset):
        body (MetadataValuesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MetadataValuesSchema | PutByObjectTypeByObjectIdResponseDefault]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        body=body,
        check_if_subclip=check_if_subclip,
        ignore_unchanged=ignore_unchanged,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MetadataValuesSchema,
    check_if_subclip: bool | Unset = UNSET,
    ignore_unchanged: bool | Unset = UNSET,
) -> Any | MetadataValuesSchema | PutByObjectTypeByObjectIdResponseDefault | None:
    """Edit metadata values directly without a view. Admin access required.

    Args:
        object_type (str):
        object_id (str):
        check_if_subclip (bool | Unset):
        ignore_unchanged (bool | Unset):
        body (MetadataValuesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MetadataValuesSchema | PutByObjectTypeByObjectIdResponseDefault
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            object_id=object_id,
            client=client,
            body=body,
            check_if_subclip=check_if_subclip,
            ignore_unchanged=ignore_unchanged,
        )
    ).parsed
