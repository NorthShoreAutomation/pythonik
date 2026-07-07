from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_jobs_response_default_type_0 import GetJobsResponseDefaultType0
from ...models.get_jobs_response_default_type_1 import GetJobsResponseDefaultType1
from ...models.jobs_schema import JobsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    facets: bool | Unset = True,
    aggregations: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    metadata_automation_id: str | Unset = UNSET,
    metadata_field: str | Unset = UNSET,
    field_missing: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["facets"] = facets

    params["aggregations"] = aggregations

    params["page"] = page

    params["per_page"] = per_page

    params["scroll"] = scroll

    params["scroll_id"] = scroll_id

    params["sort"] = sort

    params["type"] = type_

    params["object_type"] = object_type

    params["parent_id"] = parent_id

    params["object_id"] = object_id

    params["status"] = status

    params["created_by"] = created_by

    params["date_created"] = date_created

    params["date_modified"] = date_modified

    params["query"] = query

    params["ids"] = ids

    params["metadata.automation_id"] = metadata_automation_id

    params["metadata.<field>"] = metadata_field

    params["_missing_"] = field_missing

    params["_exists_"] = field_exists

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/jobs/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetJobsResponseDefaultType0 | GetJobsResponseDefaultType1 | JobsSchema:
    if response.status_code == 200:
        response_200 = JobsSchema.from_dict(response.json())

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
    ) -> GetJobsResponseDefaultType0 | GetJobsResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetJobsResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetJobsResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetJobsResponseDefaultType0 | GetJobsResponseDefaultType1 | JobsSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    facets: bool | Unset = True,
    aggregations: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    metadata_automation_id: str | Unset = UNSET,
    metadata_field: str | Unset = UNSET,
    field_missing: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
) -> Response[
    Any | GetJobsResponseDefaultType0 | GetJobsResponseDefaultType1 | JobsSchema
]:
    """Get list of jobs


    Required roles:
     - can_read_jobs

    Args:
        facets (bool | Unset):  Default: True.
        aggregations (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        type_ (str | Unset):
        object_type (str | Unset):
        parent_id (str | Unset):
        object_id (str | Unset):
        status (str | Unset):
        created_by (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        query (str | Unset):
        ids (str | Unset):
        metadata_automation_id (str | Unset):
        metadata_field (str | Unset):
        field_missing (str | Unset):
        field_exists (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetJobsResponseDefaultType0 | GetJobsResponseDefaultType1 | JobsSchema]
    """

    kwargs = _get_kwargs(
        facets=facets,
        aggregations=aggregations,
        page=page,
        per_page=per_page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
        type_=type_,
        object_type=object_type,
        parent_id=parent_id,
        object_id=object_id,
        status=status,
        created_by=created_by,
        date_created=date_created,
        date_modified=date_modified,
        query=query,
        ids=ids,
        metadata_automation_id=metadata_automation_id,
        metadata_field=metadata_field,
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
    facets: bool | Unset = True,
    aggregations: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    metadata_automation_id: str | Unset = UNSET,
    metadata_field: str | Unset = UNSET,
    field_missing: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
) -> (
    Any | GetJobsResponseDefaultType0 | GetJobsResponseDefaultType1 | JobsSchema | None
):
    """Get list of jobs


    Required roles:
     - can_read_jobs

    Args:
        facets (bool | Unset):  Default: True.
        aggregations (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        type_ (str | Unset):
        object_type (str | Unset):
        parent_id (str | Unset):
        object_id (str | Unset):
        status (str | Unset):
        created_by (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        query (str | Unset):
        ids (str | Unset):
        metadata_automation_id (str | Unset):
        metadata_field (str | Unset):
        field_missing (str | Unset):
        field_exists (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetJobsResponseDefaultType0 | GetJobsResponseDefaultType1 | JobsSchema
    """

    return sync_detailed(
        client=client,
        facets=facets,
        aggregations=aggregations,
        page=page,
        per_page=per_page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
        type_=type_,
        object_type=object_type,
        parent_id=parent_id,
        object_id=object_id,
        status=status,
        created_by=created_by,
        date_created=date_created,
        date_modified=date_modified,
        query=query,
        ids=ids,
        metadata_automation_id=metadata_automation_id,
        metadata_field=metadata_field,
        field_missing=field_missing,
        field_exists=field_exists,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    facets: bool | Unset = True,
    aggregations: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    metadata_automation_id: str | Unset = UNSET,
    metadata_field: str | Unset = UNSET,
    field_missing: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
) -> Response[
    Any | GetJobsResponseDefaultType0 | GetJobsResponseDefaultType1 | JobsSchema
]:
    """Get list of jobs


    Required roles:
     - can_read_jobs

    Args:
        facets (bool | Unset):  Default: True.
        aggregations (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        type_ (str | Unset):
        object_type (str | Unset):
        parent_id (str | Unset):
        object_id (str | Unset):
        status (str | Unset):
        created_by (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        query (str | Unset):
        ids (str | Unset):
        metadata_automation_id (str | Unset):
        metadata_field (str | Unset):
        field_missing (str | Unset):
        field_exists (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetJobsResponseDefaultType0 | GetJobsResponseDefaultType1 | JobsSchema]
    """

    kwargs = _get_kwargs(
        facets=facets,
        aggregations=aggregations,
        page=page,
        per_page=per_page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
        type_=type_,
        object_type=object_type,
        parent_id=parent_id,
        object_id=object_id,
        status=status,
        created_by=created_by,
        date_created=date_created,
        date_modified=date_modified,
        query=query,
        ids=ids,
        metadata_automation_id=metadata_automation_id,
        metadata_field=metadata_field,
        field_missing=field_missing,
        field_exists=field_exists,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    facets: bool | Unset = True,
    aggregations: str | Unset = UNSET,
    page: int | Unset = 1,
    per_page: int | Unset = 10,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    object_type: str | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    object_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    metadata_automation_id: str | Unset = UNSET,
    metadata_field: str | Unset = UNSET,
    field_missing: str | Unset = UNSET,
    field_exists: str | Unset = UNSET,
) -> (
    Any | GetJobsResponseDefaultType0 | GetJobsResponseDefaultType1 | JobsSchema | None
):
    """Get list of jobs


    Required roles:
     - can_read_jobs

    Args:
        facets (bool | Unset):  Default: True.
        aggregations (str | Unset):
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 10.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        type_ (str | Unset):
        object_type (str | Unset):
        parent_id (str | Unset):
        object_id (str | Unset):
        status (str | Unset):
        created_by (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        query (str | Unset):
        ids (str | Unset):
        metadata_automation_id (str | Unset):
        metadata_field (str | Unset):
        field_missing (str | Unset):
        field_exists (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetJobsResponseDefaultType0 | GetJobsResponseDefaultType1 | JobsSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            facets=facets,
            aggregations=aggregations,
            page=page,
            per_page=per_page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
            type_=type_,
            object_type=object_type,
            parent_id=parent_id,
            object_id=object_id,
            status=status,
            created_by=created_by,
            date_created=date_created,
            date_modified=date_modified,
            query=query,
            ids=ids,
            metadata_automation_id=metadata_automation_id,
            metadata_field=metadata_field,
            field_missing=field_missing,
            field_exists=field_exists,
        )
    ).parsed
