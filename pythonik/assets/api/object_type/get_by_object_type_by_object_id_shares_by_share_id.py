from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_by_object_type_by_object_id_shares_by_share_id_response_default_type_0 import (
    GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType0,
)
from ...models.get_by_object_type_by_object_id_shares_by_share_id_response_default_type_1 import (
    GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType1,
)
from ...models.get_share_schema import GetShareSchema
from ...types import Response


def _get_kwargs(
    object_type: str,
    object_id: str,
    share_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/{object_type}/{object_id}/shares/{share_id}/".format(
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
            share_id=quote(str(share_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType0
    | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType1
    | GetShareSchema
):
    if response.status_code == 200:
        response_200 = GetShareSchema.from_dict(response.json())

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
        GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType0
        | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType0
    | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType1
    | GetShareSchema
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
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType0
    | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType1
    | GetShareSchema
]:
    """Returns a particular share by id

    Args:
        object_type (str):
        object_id (str):
        share_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType0 | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType1 | GetShareSchema]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        share_id=share_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    object_id: str,
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType0
    | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType1
    | GetShareSchema
    | None
):
    """Returns a particular share by id

    Args:
        object_type (str):
        object_id (str):
        share_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType0 | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType1 | GetShareSchema
    """

    return sync_detailed(
        object_type=object_type,
        object_id=object_id,
        share_id=share_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    object_id: str,
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType0
    | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType1
    | GetShareSchema
]:
    """Returns a particular share by id

    Args:
        object_type (str):
        object_id (str):
        share_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType0 | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType1 | GetShareSchema]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        share_id=share_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    object_id: str,
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType0
    | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType1
    | GetShareSchema
    | None
):
    """Returns a particular share by id

    Args:
        object_type (str):
        object_id (str):
        share_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType0 | GetByObjectTypeByObjectIdSharesByShareIdResponseDefaultType1 | GetShareSchema
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            object_id=object_id,
            share_id=share_id,
            client=client,
        )
    ).parsed
