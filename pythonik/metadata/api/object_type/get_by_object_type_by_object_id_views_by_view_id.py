from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_by_object_type_by_object_id_views_by_view_id_response_default import (
    GetByObjectTypeByObjectIdViewsByViewIdResponseDefault,
)
from ...models.metadata_values_schema import MetadataValuesSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    object_type: str,
    object_id: str,
    view_id: str,
    *,
    check_if_subclip: bool | Unset = UNSET,
    reencode_values_to_string: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["check_if_subclip"] = check_if_subclip

    params["reencode_values_to_string"] = reencode_values_to_string

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{object_type}/{object_id}/views/{view_id}/".format(
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
            view_id=quote(str(view_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetByObjectTypeByObjectIdViewsByViewIdResponseDefault | MetadataValuesSchema:
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

    response_default = GetByObjectTypeByObjectIdViewsByViewIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetByObjectTypeByObjectIdViewsByViewIdResponseDefault | MetadataValuesSchema
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
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    check_if_subclip: bool | Unset = UNSET,
    reencode_values_to_string: bool | Unset = UNSET,
) -> Response[
    Any | GetByObjectTypeByObjectIdViewsByViewIdResponseDefault | MetadataValuesSchema
]:
    """Get object metadata by object type, object ID and view ID


    Required roles:
     - can_read_metadata_values

    Args:
        object_type (str):
        object_id (str):
        view_id (str):
        check_if_subclip (bool | Unset):
        reencode_values_to_string (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetByObjectTypeByObjectIdViewsByViewIdResponseDefault | MetadataValuesSchema]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        view_id=view_id,
        check_if_subclip=check_if_subclip,
        reencode_values_to_string=reencode_values_to_string,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    object_id: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    check_if_subclip: bool | Unset = UNSET,
    reencode_values_to_string: bool | Unset = UNSET,
) -> (
    Any
    | GetByObjectTypeByObjectIdViewsByViewIdResponseDefault
    | MetadataValuesSchema
    | None
):
    """Get object metadata by object type, object ID and view ID


    Required roles:
     - can_read_metadata_values

    Args:
        object_type (str):
        object_id (str):
        view_id (str):
        check_if_subclip (bool | Unset):
        reencode_values_to_string (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetByObjectTypeByObjectIdViewsByViewIdResponseDefault | MetadataValuesSchema
    """

    return sync_detailed(
        object_type=object_type,
        object_id=object_id,
        view_id=view_id,
        client=client,
        check_if_subclip=check_if_subclip,
        reencode_values_to_string=reencode_values_to_string,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    object_id: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    check_if_subclip: bool | Unset = UNSET,
    reencode_values_to_string: bool | Unset = UNSET,
) -> Response[
    Any | GetByObjectTypeByObjectIdViewsByViewIdResponseDefault | MetadataValuesSchema
]:
    """Get object metadata by object type, object ID and view ID


    Required roles:
     - can_read_metadata_values

    Args:
        object_type (str):
        object_id (str):
        view_id (str):
        check_if_subclip (bool | Unset):
        reencode_values_to_string (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetByObjectTypeByObjectIdViewsByViewIdResponseDefault | MetadataValuesSchema]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        view_id=view_id,
        check_if_subclip=check_if_subclip,
        reencode_values_to_string=reencode_values_to_string,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    object_id: str,
    view_id: str,
    *,
    client: AuthenticatedClient | Client,
    check_if_subclip: bool | Unset = UNSET,
    reencode_values_to_string: bool | Unset = UNSET,
) -> (
    Any
    | GetByObjectTypeByObjectIdViewsByViewIdResponseDefault
    | MetadataValuesSchema
    | None
):
    """Get object metadata by object type, object ID and view ID


    Required roles:
     - can_read_metadata_values

    Args:
        object_type (str):
        object_id (str):
        view_id (str):
        check_if_subclip (bool | Unset):
        reencode_values_to_string (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetByObjectTypeByObjectIdViewsByViewIdResponseDefault | MetadataValuesSchema
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            object_id=object_id,
            view_id=view_id,
            client=client,
            check_if_subclip=check_if_subclip,
            reencode_values_to_string=reencode_values_to_string,
        )
    ).parsed
