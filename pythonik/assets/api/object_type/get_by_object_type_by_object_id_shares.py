from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_by_object_type_by_object_id_shares_response_default_type_0 import (
    GetByObjectTypeByObjectIdSharesResponseDefaultType0,
)
from ...models.get_by_object_type_by_object_id_shares_response_default_type_1 import (
    GetByObjectTypeByObjectIdSharesResponseDefaultType1,
)
from ...models.shares_schema import SharesSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    object_type: str,
    object_id: str,
    *,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["last_id"] = last_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{object_type}/{object_id}/shares/".format(
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
    | GetByObjectTypeByObjectIdSharesResponseDefaultType0
    | GetByObjectTypeByObjectIdSharesResponseDefaultType1
    | SharesSchema
):
    if response.status_code == 200:
        response_200 = SharesSchema.from_dict(response.json())

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
        GetByObjectTypeByObjectIdSharesResponseDefaultType0
        | GetByObjectTypeByObjectIdSharesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetByObjectTypeByObjectIdSharesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetByObjectTypeByObjectIdSharesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetByObjectTypeByObjectIdSharesResponseDefaultType0
    | GetByObjectTypeByObjectIdSharesResponseDefaultType1
    | SharesSchema
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
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetByObjectTypeByObjectIdSharesResponseDefaultType0
    | GetByObjectTypeByObjectIdSharesResponseDefaultType1
    | SharesSchema
]:
    """Get list of object shares


    Required roles:
     - can_read_shares

    Args:
        object_type (str):
        object_id (str):
        per_page (int | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetByObjectTypeByObjectIdSharesResponseDefaultType0 | GetByObjectTypeByObjectIdSharesResponseDefaultType1 | SharesSchema]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        per_page=per_page,
        last_id=last_id,
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
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetByObjectTypeByObjectIdSharesResponseDefaultType0
    | GetByObjectTypeByObjectIdSharesResponseDefaultType1
    | SharesSchema
    | None
):
    """Get list of object shares


    Required roles:
     - can_read_shares

    Args:
        object_type (str):
        object_id (str):
        per_page (int | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetByObjectTypeByObjectIdSharesResponseDefaultType0 | GetByObjectTypeByObjectIdSharesResponseDefaultType1 | SharesSchema
    """

    return sync_detailed(
        object_type=object_type,
        object_id=object_id,
        client=client,
        per_page=per_page,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetByObjectTypeByObjectIdSharesResponseDefaultType0
    | GetByObjectTypeByObjectIdSharesResponseDefaultType1
    | SharesSchema
]:
    """Get list of object shares


    Required roles:
     - can_read_shares

    Args:
        object_type (str):
        object_id (str):
        per_page (int | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetByObjectTypeByObjectIdSharesResponseDefaultType0 | GetByObjectTypeByObjectIdSharesResponseDefaultType1 | SharesSchema]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        per_page=per_page,
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetByObjectTypeByObjectIdSharesResponseDefaultType0
    | GetByObjectTypeByObjectIdSharesResponseDefaultType1
    | SharesSchema
    | None
):
    """Get list of object shares


    Required roles:
     - can_read_shares

    Args:
        object_type (str):
        object_id (str):
        per_page (int | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetByObjectTypeByObjectIdSharesResponseDefaultType0 | GetByObjectTypeByObjectIdSharesResponseDefaultType1 | SharesSchema
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            object_id=object_id,
            client=client,
            per_page=per_page,
            last_id=last_id,
        )
    ).parsed
