from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storages_matching_by_purpose_response_default_type_0 import (
    GetStoragesMatchingByPurposeResponseDefaultType0,
)
from ...models.get_storages_matching_by_purpose_response_default_type_1 import (
    GetStoragesMatchingByPurposeResponseDefaultType1,
)
from ...models.storage_schema import StorageSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    purpose: str,
    *,
    storage_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["storage_id"] = storage_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storages/matching/{purpose}/".format(
            purpose=quote(str(purpose), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetStoragesMatchingByPurposeResponseDefaultType0
    | GetStoragesMatchingByPurposeResponseDefaultType1
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
        GetStoragesMatchingByPurposeResponseDefaultType0
        | GetStoragesMatchingByPurposeResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetStoragesMatchingByPurposeResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetStoragesMatchingByPurposeResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetStoragesMatchingByPurposeResponseDefaultType0
    | GetStoragesMatchingByPurposeResponseDefaultType1
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
    *,
    client: AuthenticatedClient | Client,
    storage_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetStoragesMatchingByPurposeResponseDefaultType0
    | GetStoragesMatchingByPurposeResponseDefaultType1
    | StorageSchema
]:
    """Returns a remote storage matching type


    Required roles:
     - can_read_storages

    Args:
        purpose (str):
        storage_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesMatchingByPurposeResponseDefaultType0 | GetStoragesMatchingByPurposeResponseDefaultType1 | StorageSchema]
    """

    kwargs = _get_kwargs(
        purpose=purpose,
        storage_id=storage_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    purpose: str,
    *,
    client: AuthenticatedClient | Client,
    storage_id: str | Unset = UNSET,
) -> (
    Any
    | GetStoragesMatchingByPurposeResponseDefaultType0
    | GetStoragesMatchingByPurposeResponseDefaultType1
    | StorageSchema
    | None
):
    """Returns a remote storage matching type


    Required roles:
     - can_read_storages

    Args:
        purpose (str):
        storage_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesMatchingByPurposeResponseDefaultType0 | GetStoragesMatchingByPurposeResponseDefaultType1 | StorageSchema
    """

    return sync_detailed(
        purpose=purpose,
        client=client,
        storage_id=storage_id,
    ).parsed


async def asyncio_detailed(
    purpose: str,
    *,
    client: AuthenticatedClient | Client,
    storage_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetStoragesMatchingByPurposeResponseDefaultType0
    | GetStoragesMatchingByPurposeResponseDefaultType1
    | StorageSchema
]:
    """Returns a remote storage matching type


    Required roles:
     - can_read_storages

    Args:
        purpose (str):
        storage_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesMatchingByPurposeResponseDefaultType0 | GetStoragesMatchingByPurposeResponseDefaultType1 | StorageSchema]
    """

    kwargs = _get_kwargs(
        purpose=purpose,
        storage_id=storage_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    purpose: str,
    *,
    client: AuthenticatedClient | Client,
    storage_id: str | Unset = UNSET,
) -> (
    Any
    | GetStoragesMatchingByPurposeResponseDefaultType0
    | GetStoragesMatchingByPurposeResponseDefaultType1
    | StorageSchema
    | None
):
    """Returns a remote storage matching type


    Required roles:
     - can_read_storages

    Args:
        purpose (str):
        storage_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesMatchingByPurposeResponseDefaultType0 | GetStoragesMatchingByPurposeResponseDefaultType1 | StorageSchema
    """

    return (
        await asyncio_detailed(
            purpose=purpose,
            client=client,
            storage_id=storage_id,
        )
    ).parsed
