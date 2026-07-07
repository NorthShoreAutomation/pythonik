from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storages_by_storage_id_transcode_by_record_id_response_default_type_0 import (
    GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0,
)
from ...models.get_storages_by_storage_id_transcode_by_record_id_response_default_type_1 import (
    GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1,
)
from ...models.local_storage_file_transcode_job_schema import (
    LocalStorageFileTranscodeJobSchema,
)
from ...types import Response


def _get_kwargs(
    storage_id: str,
    record_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storages/{storage_id}/transcode/{record_id}/".format(
            storage_id=quote(str(storage_id), safe=""),
            record_id=quote(str(record_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0
    | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1
    | LocalStorageFileTranscodeJobSchema
):
    if response.status_code == 200:
        response_200 = LocalStorageFileTranscodeJobSchema.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0
        | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1.from_dict(
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
    | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0
    | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1
    | LocalStorageFileTranscodeJobSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_id: str,
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0
    | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1
    | LocalStorageFileTranscodeJobSchema
]:
    """Get local storage transcode job.


    Required roles:
     - can_read_transcode_jobs

    Args:
        storage_id (str):
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0 | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1 | LocalStorageFileTranscodeJobSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        record_id=record_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0
    | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1
    | LocalStorageFileTranscodeJobSchema
    | None
):
    """Get local storage transcode job.


    Required roles:
     - can_read_transcode_jobs

    Args:
        storage_id (str):
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0 | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1 | LocalStorageFileTranscodeJobSchema
    """

    return sync_detailed(
        storage_id=storage_id,
        record_id=record_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0
    | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1
    | LocalStorageFileTranscodeJobSchema
]:
    """Get local storage transcode job.


    Required roles:
     - can_read_transcode_jobs

    Args:
        storage_id (str):
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0 | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1 | LocalStorageFileTranscodeJobSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        record_id=record_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0
    | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1
    | LocalStorageFileTranscodeJobSchema
    | None
):
    """Get local storage transcode job.


    Required roles:
     - can_read_transcode_jobs

    Args:
        storage_id (str):
        record_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType0 | GetStoragesByStorageIdTranscodeByRecordIdResponseDefaultType1 | LocalStorageFileTranscodeJobSchema
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            record_id=record_id,
            client=client,
        )
    ).parsed
