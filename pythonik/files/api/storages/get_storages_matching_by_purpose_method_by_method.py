from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storages_matching_by_purpose_method_by_method_response_default_type_0 import (
    GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType0,
)
from ...models.get_storages_matching_by_purpose_method_by_method_response_default_type_1 import (
    GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType1,
)
from ...models.storage_schema import StorageSchema
from ...types import Response


def _get_kwargs(
    purpose: str,
    method: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storages/matching/{purpose}/method/{method}/".format(
            purpose=quote(str(purpose), safe=""),
            method=quote(str(method), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType0
    | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType1
    | StorageSchema
):
    if response.status_code == 200:
        response_200 = StorageSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType0
        | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType1.from_dict(
                data
            )
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType0
    | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType1
    | StorageSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    purpose: str,
    method: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType0
    | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType1
    | StorageSchema
]:
    """Returns a remote storage matching type and method


    Required roles:
     - can_read_storages

    Args:
        purpose (str):
        method (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType0 | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType1 | StorageSchema]
    """

    kwargs = _get_kwargs(
        purpose=purpose,
        method=method,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    purpose: str,
    method: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType0
    | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType1
    | StorageSchema
    | None
):
    """Returns a remote storage matching type and method


    Required roles:
     - can_read_storages

    Args:
        purpose (str):
        method (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType0 | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType1 | StorageSchema
    """

    return sync_detailed(
        purpose=purpose,
        method=method,
        client=client,
    ).parsed


async def asyncio_detailed(
    purpose: str,
    method: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType0
    | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType1
    | StorageSchema
]:
    """Returns a remote storage matching type and method


    Required roles:
     - can_read_storages

    Args:
        purpose (str):
        method (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType0 | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType1 | StorageSchema]
    """

    kwargs = _get_kwargs(
        purpose=purpose,
        method=method,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    purpose: str,
    method: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType0
    | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType1
    | StorageSchema
    | None
):
    """Returns a remote storage matching type and method


    Required roles:
     - can_read_storages

    Args:
        purpose (str):
        method (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType0 | GetStoragesMatchingByPurposeMethodByMethodResponseDefaultType1 | StorageSchema
    """

    return (
        await asyncio_detailed(
            purpose=purpose,
            method=method,
            client=client,
        )
    ).parsed
