from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_by_object_type_by_object_id_response_200 import (
    GetByObjectTypeByObjectIdResponse200,
)
from ...models.get_by_object_type_by_object_id_response_default_type_0 import (
    GetByObjectTypeByObjectIdResponseDefaultType0,
)
from ...models.get_by_object_type_by_object_id_response_default_type_1 import (
    GetByObjectTypeByObjectIdResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    object_type: str,
    object_id: str,
    *,
    check_if_subclip: bool | Unset = UNSET,
    include_values_for_deleted_fields: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["check_if_subclip"] = check_if_subclip

    params["include_values_for_deleted_fields"] = include_values_for_deleted_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{object_type}/{object_id}/".format(
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetByObjectTypeByObjectIdResponse200
    | GetByObjectTypeByObjectIdResponseDefaultType0
    | GetByObjectTypeByObjectIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = GetByObjectTypeByObjectIdResponse200.from_dict(response.json())

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
        GetByObjectTypeByObjectIdResponseDefaultType0
        | GetByObjectTypeByObjectIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetByObjectTypeByObjectIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetByObjectTypeByObjectIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetByObjectTypeByObjectIdResponse200
    | GetByObjectTypeByObjectIdResponseDefaultType0
    | GetByObjectTypeByObjectIdResponseDefaultType1
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
    check_if_subclip: bool | Unset = UNSET,
    include_values_for_deleted_fields: bool | Unset = False,
) -> Response[
    Any
    | GetByObjectTypeByObjectIdResponse200
    | GetByObjectTypeByObjectIdResponseDefaultType0
    | GetByObjectTypeByObjectIdResponseDefaultType1
]:
    """Get object metadata by object type and object ID

    Args:
        object_type (str):
        object_id (str):
        check_if_subclip (bool | Unset):
        include_values_for_deleted_fields (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetByObjectTypeByObjectIdResponse200 | GetByObjectTypeByObjectIdResponseDefaultType0 | GetByObjectTypeByObjectIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        check_if_subclip=check_if_subclip,
        include_values_for_deleted_fields=include_values_for_deleted_fields,
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
    check_if_subclip: bool | Unset = UNSET,
    include_values_for_deleted_fields: bool | Unset = False,
) -> (
    Any
    | GetByObjectTypeByObjectIdResponse200
    | GetByObjectTypeByObjectIdResponseDefaultType0
    | GetByObjectTypeByObjectIdResponseDefaultType1
    | None
):
    """Get object metadata by object type and object ID

    Args:
        object_type (str):
        object_id (str):
        check_if_subclip (bool | Unset):
        include_values_for_deleted_fields (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetByObjectTypeByObjectIdResponse200 | GetByObjectTypeByObjectIdResponseDefaultType0 | GetByObjectTypeByObjectIdResponseDefaultType1
    """

    return sync_detailed(
        object_type=object_type,
        object_id=object_id,
        client=client,
        check_if_subclip=check_if_subclip,
        include_values_for_deleted_fields=include_values_for_deleted_fields,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
    check_if_subclip: bool | Unset = UNSET,
    include_values_for_deleted_fields: bool | Unset = False,
) -> Response[
    Any
    | GetByObjectTypeByObjectIdResponse200
    | GetByObjectTypeByObjectIdResponseDefaultType0
    | GetByObjectTypeByObjectIdResponseDefaultType1
]:
    """Get object metadata by object type and object ID

    Args:
        object_type (str):
        object_id (str):
        check_if_subclip (bool | Unset):
        include_values_for_deleted_fields (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetByObjectTypeByObjectIdResponse200 | GetByObjectTypeByObjectIdResponseDefaultType0 | GetByObjectTypeByObjectIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        check_if_subclip=check_if_subclip,
        include_values_for_deleted_fields=include_values_for_deleted_fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
    check_if_subclip: bool | Unset = UNSET,
    include_values_for_deleted_fields: bool | Unset = False,
) -> (
    Any
    | GetByObjectTypeByObjectIdResponse200
    | GetByObjectTypeByObjectIdResponseDefaultType0
    | GetByObjectTypeByObjectIdResponseDefaultType1
    | None
):
    """Get object metadata by object type and object ID

    Args:
        object_type (str):
        object_id (str):
        check_if_subclip (bool | Unset):
        include_values_for_deleted_fields (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetByObjectTypeByObjectIdResponse200 | GetByObjectTypeByObjectIdResponseDefaultType0 | GetByObjectTypeByObjectIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            object_id=object_id,
            client=client,
            check_if_subclip=check_if_subclip,
            include_values_for_deleted_fields=include_values_for_deleted_fields,
        )
    ).parsed
