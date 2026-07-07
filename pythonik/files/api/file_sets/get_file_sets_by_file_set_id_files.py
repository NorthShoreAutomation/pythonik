from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.files_schema import FilesSchema
from ...models.get_file_sets_by_file_set_id_files_response_default_type_0 import (
    GetFileSetsByFileSetIdFilesResponseDefaultType0,
)
from ...models.get_file_sets_by_file_set_id_files_response_default_type_1 import (
    GetFileSetsByFileSetIdFilesResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    file_set_id: str,
    *,
    generate_signed_url: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["generate_signed_url"] = generate_signed_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/file_sets/{file_set_id}/files/".format(
            file_set_id=quote(str(file_set_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FilesSchema
    | GetFileSetsByFileSetIdFilesResponseDefaultType0
    | GetFileSetsByFileSetIdFilesResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = FilesSchema.from_dict(response.json())

        return response_200

    def _parse_response_default(
        data: object,
    ) -> (
        GetFileSetsByFileSetIdFilesResponseDefaultType0
        | GetFileSetsByFileSetIdFilesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetFileSetsByFileSetIdFilesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetFileSetsByFileSetIdFilesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FilesSchema
    | GetFileSetsByFileSetIdFilesResponseDefaultType0
    | GetFileSetsByFileSetIdFilesResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
    generate_signed_url: bool | Unset = True,
) -> Response[
    FilesSchema
    | GetFileSetsByFileSetIdFilesResponseDefaultType0
    | GetFileSetsByFileSetIdFilesResponseDefaultType1
]:
    """Get files from a file set


    Required roles:
     - can_read_files

    Args:
        file_set_id (str):
        generate_signed_url (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesSchema | GetFileSetsByFileSetIdFilesResponseDefaultType0 | GetFileSetsByFileSetIdFilesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        file_set_id=file_set_id,
        generate_signed_url=generate_signed_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
    generate_signed_url: bool | Unset = True,
) -> (
    FilesSchema
    | GetFileSetsByFileSetIdFilesResponseDefaultType0
    | GetFileSetsByFileSetIdFilesResponseDefaultType1
    | None
):
    """Get files from a file set


    Required roles:
     - can_read_files

    Args:
        file_set_id (str):
        generate_signed_url (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesSchema | GetFileSetsByFileSetIdFilesResponseDefaultType0 | GetFileSetsByFileSetIdFilesResponseDefaultType1
    """

    return sync_detailed(
        file_set_id=file_set_id,
        client=client,
        generate_signed_url=generate_signed_url,
    ).parsed


async def asyncio_detailed(
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
    generate_signed_url: bool | Unset = True,
) -> Response[
    FilesSchema
    | GetFileSetsByFileSetIdFilesResponseDefaultType0
    | GetFileSetsByFileSetIdFilesResponseDefaultType1
]:
    """Get files from a file set


    Required roles:
     - can_read_files

    Args:
        file_set_id (str):
        generate_signed_url (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesSchema | GetFileSetsByFileSetIdFilesResponseDefaultType0 | GetFileSetsByFileSetIdFilesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        file_set_id=file_set_id,
        generate_signed_url=generate_signed_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_set_id: str,
    *,
    client: AuthenticatedClient | Client,
    generate_signed_url: bool | Unset = True,
) -> (
    FilesSchema
    | GetFileSetsByFileSetIdFilesResponseDefaultType0
    | GetFileSetsByFileSetIdFilesResponseDefaultType1
    | None
):
    """Get files from a file set


    Required roles:
     - can_read_files

    Args:
        file_set_id (str):
        generate_signed_url (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesSchema | GetFileSetsByFileSetIdFilesResponseDefaultType0 | GetFileSetsByFileSetIdFilesResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            file_set_id=file_set_id,
            client=client,
            generate_signed_url=generate_signed_url,
        )
    ).parsed
