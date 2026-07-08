from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_jobs_response_default import DeleteJobsResponseDefault
from ...models.jobs_bulk_delete_schema import JobsBulkDeleteSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: JobsBulkDeleteSchema | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    metadata_automation_id: str | Unset = UNSET,
    field_missing: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["parent_id"] = parent_id

    params["object_id"] = object_id

    params["created_by"] = created_by

    params["status"] = status

    params["type"] = type_

    params["date_created"] = date_created

    params["date_modified"] = date_modified

    params["query"] = query

    params["ids"] = ids

    params["metadata.automation_id"] = metadata_automation_id

    params["_missing_"] = field_missing

    params["_exists_"] = field_exists

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/jobs/",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteJobsResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = DeleteJobsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteJobsResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: JobsBulkDeleteSchema | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    metadata_automation_id: str | Unset = UNSET,
    field_missing: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
) -> Response[Any | DeleteJobsResponseDefault]:
    """Delete multiple jobs


    Required roles:
     - can_delete_jobs

    Args:
        parent_id (str | Unset):
        object_id (str | Unset):
        created_by (str | Unset):
        status (str | Unset):
        type_ (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        query (str | Unset):
        ids (str | Unset):
        metadata_automation_id (str | Unset):
        field_missing (str | Unset):
        field_exists (str | Unset):
        body (JobsBulkDeleteSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteJobsResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
        parent_id=parent_id,
        object_id=object_id,
        created_by=created_by,
        status=status,
        type_=type_,
        date_created=date_created,
        date_modified=date_modified,
        query=query,
        ids=ids,
        metadata_automation_id=metadata_automation_id,
        field_missing=field_missing,
        field_exists=field_exists,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: JobsBulkDeleteSchema | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    metadata_automation_id: str | Unset = UNSET,
    field_missing: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
) -> Any | DeleteJobsResponseDefault | None:
    """Delete multiple jobs


    Required roles:
     - can_delete_jobs

    Args:
        parent_id (str | Unset):
        object_id (str | Unset):
        created_by (str | Unset):
        status (str | Unset):
        type_ (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        query (str | Unset):
        ids (str | Unset):
        metadata_automation_id (str | Unset):
        field_missing (str | Unset):
        field_exists (str | Unset):
        body (JobsBulkDeleteSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteJobsResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
        parent_id=parent_id,
        object_id=object_id,
        created_by=created_by,
        status=status,
        type_=type_,
        date_created=date_created,
        date_modified=date_modified,
        query=query,
        ids=ids,
        metadata_automation_id=metadata_automation_id,
        field_missing=field_missing,
        field_exists=field_exists,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: JobsBulkDeleteSchema | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    metadata_automation_id: str | Unset = UNSET,
    field_missing: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
) -> Response[Any | DeleteJobsResponseDefault]:
    """Delete multiple jobs


    Required roles:
     - can_delete_jobs

    Args:
        parent_id (str | Unset):
        object_id (str | Unset):
        created_by (str | Unset):
        status (str | Unset):
        type_ (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        query (str | Unset):
        ids (str | Unset):
        metadata_automation_id (str | Unset):
        field_missing (str | Unset):
        field_exists (str | Unset):
        body (JobsBulkDeleteSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteJobsResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
        parent_id=parent_id,
        object_id=object_id,
        created_by=created_by,
        status=status,
        type_=type_,
        date_created=date_created,
        date_modified=date_modified,
        query=query,
        ids=ids,
        metadata_automation_id=metadata_automation_id,
        field_missing=field_missing,
        field_exists=field_exists,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: JobsBulkDeleteSchema | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    metadata_automation_id: str | Unset = UNSET,
    field_missing: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
) -> Any | DeleteJobsResponseDefault | None:
    """Delete multiple jobs


    Required roles:
     - can_delete_jobs

    Args:
        parent_id (str | Unset):
        object_id (str | Unset):
        created_by (str | Unset):
        status (str | Unset):
        type_ (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        query (str | Unset):
        ids (str | Unset):
        metadata_automation_id (str | Unset):
        field_missing (str | Unset):
        field_exists (str | Unset):
        body (JobsBulkDeleteSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteJobsResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            parent_id=parent_id,
            object_id=object_id,
            created_by=created_by,
            status=status,
            type_=type_,
            date_created=date_created,
            date_modified=date_modified,
            query=query,
            ids=ids,
            metadata_automation_id=metadata_automation_id,
            field_missing=field_missing,
            field_exists=field_exists,
        )
    ).parsed
