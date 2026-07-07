from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.abort_storage_transcode_jobs_schema import (
    AbortStorageTranscodeJobsSchema,
)
from ...models.delete_storages_by_storage_id_response_default_type_0 import (
    DeleteStoragesByStorageIdResponseDefaultType0,
)
from ...models.delete_storages_by_storage_id_response_default_type_1 import (
    DeleteStoragesByStorageIdResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    storage_id: str,
    *,
    body: AbortStorageTranscodeJobsSchema | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/storages/{storage_id}/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteStoragesByStorageIdResponseDefaultType0
    | DeleteStoragesByStorageIdResponseDefaultType1
):
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

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
        DeleteStoragesByStorageIdResponseDefaultType0
        | DeleteStoragesByStorageIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteStoragesByStorageIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteStoragesByStorageIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteStoragesByStorageIdResponseDefaultType0
    | DeleteStoragesByStorageIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AbortStorageTranscodeJobsSchema | Unset = UNSET,
) -> Response[
    Any
    | DeleteStoragesByStorageIdResponseDefaultType0
    | DeleteStoragesByStorageIdResponseDefaultType1
]:
    """Cancel all transcode jobs linked to the storage


    Required roles:
     - can_delete_transcode_jobs

    Args:
        storage_id (str):
        body (AbortStorageTranscodeJobsSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStoragesByStorageIdResponseDefaultType0 | DeleteStoragesByStorageIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AbortStorageTranscodeJobsSchema | Unset = UNSET,
) -> (
    Any
    | DeleteStoragesByStorageIdResponseDefaultType0
    | DeleteStoragesByStorageIdResponseDefaultType1
    | None
):
    """Cancel all transcode jobs linked to the storage


    Required roles:
     - can_delete_transcode_jobs

    Args:
        storage_id (str):
        body (AbortStorageTranscodeJobsSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStoragesByStorageIdResponseDefaultType0 | DeleteStoragesByStorageIdResponseDefaultType1
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AbortStorageTranscodeJobsSchema | Unset = UNSET,
) -> Response[
    Any
    | DeleteStoragesByStorageIdResponseDefaultType0
    | DeleteStoragesByStorageIdResponseDefaultType1
]:
    """Cancel all transcode jobs linked to the storage


    Required roles:
     - can_delete_transcode_jobs

    Args:
        storage_id (str):
        body (AbortStorageTranscodeJobsSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStoragesByStorageIdResponseDefaultType0 | DeleteStoragesByStorageIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AbortStorageTranscodeJobsSchema | Unset = UNSET,
) -> (
    Any
    | DeleteStoragesByStorageIdResponseDefaultType0
    | DeleteStoragesByStorageIdResponseDefaultType1
    | None
):
    """Cancel all transcode jobs linked to the storage


    Required roles:
     - can_delete_transcode_jobs

    Args:
        storage_id (str):
        body (AbortStorageTranscodeJobsSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStoragesByStorageIdResponseDefaultType0 | DeleteStoragesByStorageIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            body=body,
        )
    ).parsed
