from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_job_created_schema import BulkJobCreatedSchema
from ...models.jobs_bulk_edit_schema import JobsBulkEditSchema
from ...models.patch_jobs_response_default import PatchJobsResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: JobsBulkEditSchema,
    parent_id: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    merge_metadata: str | Unset = UNSET,
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

    params["merge_metadata"] = merge_metadata

    params["metadata.automation_id"] = metadata_automation_id

    params["_missing_"] = field_missing

    params["_exists_"] = field_exists

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/jobs/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BulkJobCreatedSchema | PatchJobsResponseDefault:
    if response.status_code == 202:
        response_202 = BulkJobCreatedSchema.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PatchJobsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BulkJobCreatedSchema | PatchJobsResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: JobsBulkEditSchema,
    parent_id: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    merge_metadata: str | Unset = UNSET,
    metadata_automation_id: str | Unset = UNSET,
    field_missing: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
) -> Response[Any | BulkJobCreatedSchema | PatchJobsResponseDefault]:
    """Edit jobs


    Required roles:
     - can_write_jobs

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
        merge_metadata (str | Unset):
        metadata_automation_id (str | Unset):
        field_missing (str | Unset):
        field_exists (str | Unset):
        body (JobsBulkEditSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BulkJobCreatedSchema | PatchJobsResponseDefault]
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
        merge_metadata=merge_metadata,
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
    body: JobsBulkEditSchema,
    parent_id: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    merge_metadata: str | Unset = UNSET,
    metadata_automation_id: str | Unset = UNSET,
    field_missing: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
) -> Any | BulkJobCreatedSchema | PatchJobsResponseDefault | None:
    """Edit jobs


    Required roles:
     - can_write_jobs

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
        merge_metadata (str | Unset):
        metadata_automation_id (str | Unset):
        field_missing (str | Unset):
        field_exists (str | Unset):
        body (JobsBulkEditSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BulkJobCreatedSchema | PatchJobsResponseDefault
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
        merge_metadata=merge_metadata,
        metadata_automation_id=metadata_automation_id,
        field_missing=field_missing,
        field_exists=field_exists,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: JobsBulkEditSchema,
    parent_id: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    merge_metadata: str | Unset = UNSET,
    metadata_automation_id: str | Unset = UNSET,
    field_missing: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
) -> Response[Any | BulkJobCreatedSchema | PatchJobsResponseDefault]:
    """Edit jobs


    Required roles:
     - can_write_jobs

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
        merge_metadata (str | Unset):
        metadata_automation_id (str | Unset):
        field_missing (str | Unset):
        field_exists (str | Unset):
        body (JobsBulkEditSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BulkJobCreatedSchema | PatchJobsResponseDefault]
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
        merge_metadata=merge_metadata,
        metadata_automation_id=metadata_automation_id,
        field_missing=field_missing,
        field_exists=field_exists,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: JobsBulkEditSchema,
    parent_id: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    merge_metadata: str | Unset = UNSET,
    metadata_automation_id: str | Unset = UNSET,
    field_missing: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
) -> Any | BulkJobCreatedSchema | PatchJobsResponseDefault | None:
    """Edit jobs


    Required roles:
     - can_write_jobs

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
        merge_metadata (str | Unset):
        metadata_automation_id (str | Unset):
        field_missing (str | Unset):
        field_exists (str | Unset):
        body (JobsBulkEditSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BulkJobCreatedSchema | PatchJobsResponseDefault
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
            merge_metadata=merge_metadata,
            metadata_automation_id=metadata_automation_id,
            field_missing=field_missing,
            field_exists=field_exists,
        )
    ).parsed
