from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.job_schema import JobSchema
from ...models.job_step_schema import JobStepSchema
from ...models.put_jobs_by_job_id_steps_by_job_step_id_response_default import (
    PutJobsByJobIdStepsByJobStepIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    job_id: str,
    job_step_id: str,
    *,
    body: JobStepSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/jobs/{job_id}/steps/{job_step_id}/".format(
            job_id=quote(str(job_id), safe=""),
            job_step_id=quote(str(job_step_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | JobSchema | PutJobsByJobIdStepsByJobStepIdResponseDefault:
    if response.status_code == 200:
        response_200 = JobSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PutJobsByJobIdStepsByJobStepIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | JobSchema | PutJobsByJobIdStepsByJobStepIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    job_step_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: JobStepSchema,
) -> Response[Any | JobSchema | PutJobsByJobIdStepsByJobStepIdResponseDefault]:
    """Update job step


    Required roles:
     - can_write_jobs

    Args:
        job_id (str):
        job_step_id (str):
        body (JobStepSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JobSchema | PutJobsByJobIdStepsByJobStepIdResponseDefault]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        job_step_id=job_step_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    job_step_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: JobStepSchema,
) -> Any | JobSchema | PutJobsByJobIdStepsByJobStepIdResponseDefault | None:
    """Update job step


    Required roles:
     - can_write_jobs

    Args:
        job_id (str):
        job_step_id (str):
        body (JobStepSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JobSchema | PutJobsByJobIdStepsByJobStepIdResponseDefault
    """

    return sync_detailed(
        job_id=job_id,
        job_step_id=job_step_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    job_step_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: JobStepSchema,
) -> Response[Any | JobSchema | PutJobsByJobIdStepsByJobStepIdResponseDefault]:
    """Update job step


    Required roles:
     - can_write_jobs

    Args:
        job_id (str):
        job_step_id (str):
        body (JobStepSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JobSchema | PutJobsByJobIdStepsByJobStepIdResponseDefault]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        job_step_id=job_step_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    job_step_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: JobStepSchema,
) -> Any | JobSchema | PutJobsByJobIdStepsByJobStepIdResponseDefault | None:
    """Update job step


    Required roles:
     - can_write_jobs

    Args:
        job_id (str):
        job_step_id (str):
        body (JobStepSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JobSchema | PutJobsByJobIdStepsByJobStepIdResponseDefault
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            job_step_id=job_step_id,
            client=client,
            body=body,
        )
    ).parsed
