from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.files_schema import FilesSchema
from ...models.get_files_checksum_by_checksum_response_default import (
    GetFilesChecksumByChecksumResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    checksum: str,
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
        "url": "/v1/files/checksum/{checksum}/".format(
            checksum=quote(str(checksum), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FilesSchema | GetFilesChecksumByChecksumResponseDefault:
    if response.status_code == 200:
        response_200 = FilesSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = GetFilesChecksumByChecksumResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | FilesSchema | GetFilesChecksumByChecksumResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    checksum: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> Response[Any | FilesSchema | GetFilesChecksumByChecksumResponseDefault]:
    """Get files by checksum


    Required roles:
     - can_read_files

    Args:
        checksum (str):
        per_page (int | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FilesSchema | GetFilesChecksumByChecksumResponseDefault]
    """

    kwargs = _get_kwargs(
        checksum=checksum,
        per_page=per_page,
        last_id=last_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    checksum: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> Any | FilesSchema | GetFilesChecksumByChecksumResponseDefault | None:
    """Get files by checksum


    Required roles:
     - can_read_files

    Args:
        checksum (str):
        per_page (int | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FilesSchema | GetFilesChecksumByChecksumResponseDefault
    """

    return sync_detailed(
        checksum=checksum,
        client=client,
        per_page=per_page,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    checksum: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> Response[Any | FilesSchema | GetFilesChecksumByChecksumResponseDefault]:
    """Get files by checksum


    Required roles:
     - can_read_files

    Args:
        checksum (str):
        per_page (int | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FilesSchema | GetFilesChecksumByChecksumResponseDefault]
    """

    kwargs = _get_kwargs(
        checksum=checksum,
        per_page=per_page,
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    checksum: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    last_id: str | Unset = UNSET,
) -> Any | FilesSchema | GetFilesChecksumByChecksumResponseDefault | None:
    """Get files by checksum


    Required roles:
     - can_read_files

    Args:
        checksum (str):
        per_page (int | Unset):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FilesSchema | GetFilesChecksumByChecksumResponseDefault
    """

    return (
        await asyncio_detailed(
            checksum=checksum,
            client=client,
            per_page=per_page,
            last_id=last_id,
        )
    ).parsed
