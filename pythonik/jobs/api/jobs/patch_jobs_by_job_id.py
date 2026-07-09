from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.job_schema import JobSchema
from ...models.patch_jobs_by_job_id_response_default import (
    PatchJobsByJobIdResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    body: JobSchema,
    merge_metadata: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["merge_metadata"] = merge_metadata

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/jobs/{job_id}/".format(
            job_id=quote(str(job_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | JobSchema | PatchJobsByJobIdResponseDefault:
    if response.status_code == 200:
        response_200 = JobSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PatchJobsByJobIdResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | JobSchema | PatchJobsByJobIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: JobSchema,
    merge_metadata: str | Unset = UNSET,
) -> Response[Any | JobSchema | PatchJobsByJobIdResponseDefault]:
    """Update job


    Required roles:
     - can_write_jobs

    Args:
        job_id (str):
        merge_metadata (str | Unset):
        body (JobSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JobSchema | PatchJobsByJobIdResponseDefault]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
        merge_metadata=merge_metadata,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: JobSchema,
    merge_metadata: str | Unset = UNSET,
) -> Any | JobSchema | PatchJobsByJobIdResponseDefault | None:
    """Update job


    Required roles:
     - can_write_jobs

    Args:
        job_id (str):
        merge_metadata (str | Unset):
        body (JobSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JobSchema | PatchJobsByJobIdResponseDefault
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        body=body,
        merge_metadata=merge_metadata,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: JobSchema,
    merge_metadata: str | Unset = UNSET,
) -> Response[Any | JobSchema | PatchJobsByJobIdResponseDefault]:
    """Update job


    Required roles:
     - can_write_jobs

    Args:
        job_id (str):
        merge_metadata (str | Unset):
        body (JobSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JobSchema | PatchJobsByJobIdResponseDefault]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
        merge_metadata=merge_metadata,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: JobSchema,
    merge_metadata: str | Unset = UNSET,
) -> Any | JobSchema | PatchJobsByJobIdResponseDefault | None:
    """Update job


    Required roles:
     - can_write_jobs

    Args:
        job_id (str):
        merge_metadata (str | Unset):
        body (JobSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JobSchema | PatchJobsByJobIdResponseDefault
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            body=body,
            merge_metadata=merge_metadata,
        )
    ).parsed
