from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_id_by_object_id_info_response_default_type_0 import (
    GetIdByObjectIdInfoResponseDefaultType0,
)
from ...models.get_id_by_object_id_info_response_default_type_1 import (
    GetIdByObjectIdInfoResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    object_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/id/{object_id}/info/".format(
            object_id=quote(str(object_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetIdByObjectIdInfoResponseDefaultType0
    | GetIdByObjectIdInfoResponseDefaultType1
):
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
    ) -> (
        GetIdByObjectIdInfoResponseDefaultType0
        | GetIdByObjectIdInfoResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetIdByObjectIdInfoResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetIdByObjectIdInfoResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetIdByObjectIdInfoResponseDefaultType0
    | GetIdByObjectIdInfoResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetIdByObjectIdInfoResponseDefaultType0
    | GetIdByObjectIdInfoResponseDefaultType1
]:
    """Internal endpoint to convert ID to system domain

    Args:
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetIdByObjectIdInfoResponseDefaultType0 | GetIdByObjectIdInfoResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetIdByObjectIdInfoResponseDefaultType0
    | GetIdByObjectIdInfoResponseDefaultType1
    | None
):
    """Internal endpoint to convert ID to system domain

    Args:
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetIdByObjectIdInfoResponseDefaultType0 | GetIdByObjectIdInfoResponseDefaultType1
    """

    return sync_detailed(
        object_id=object_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetIdByObjectIdInfoResponseDefaultType0
    | GetIdByObjectIdInfoResponseDefaultType1
]:
    """Internal endpoint to convert ID to system domain

    Args:
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetIdByObjectIdInfoResponseDefaultType0 | GetIdByObjectIdInfoResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetIdByObjectIdInfoResponseDefaultType0
    | GetIdByObjectIdInfoResponseDefaultType1
    | None
):
    """Internal endpoint to convert ID to system domain

    Args:
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetIdByObjectIdInfoResponseDefaultType0 | GetIdByObjectIdInfoResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            object_id=object_id,
            client=client,
        )
    ).parsed
