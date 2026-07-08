from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.jobs_state_schema import JobsStateSchema
from ...models.put_face_recognition_jobs_state_response_default import (
    PutFaceRecognitionJobsStateResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    body: JobsStateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/face_recognition/jobs/state/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutFaceRecognitionJobsStateResponseDefault:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PutFaceRecognitionJobsStateResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PutFaceRecognitionJobsStateResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: JobsStateSchema,
) -> Response[Any | PutFaceRecognitionJobsStateResponseDefault]:
    """Bulk-abort / restart FR extraction jobs


    Required roles:
     - can_write_jobs

    Args:
        body (JobsStateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutFaceRecognitionJobsStateResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: JobsStateSchema,
) -> Any | PutFaceRecognitionJobsStateResponseDefault | None:
    """Bulk-abort / restart FR extraction jobs


    Required roles:
     - can_write_jobs

    Args:
        body (JobsStateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutFaceRecognitionJobsStateResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: JobsStateSchema,
) -> Response[Any | PutFaceRecognitionJobsStateResponseDefault]:
    """Bulk-abort / restart FR extraction jobs


    Required roles:
     - can_write_jobs

    Args:
        body (JobsStateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutFaceRecognitionJobsStateResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: JobsStateSchema,
) -> Any | PutFaceRecognitionJobsStateResponseDefault | None:
    """Bulk-abort / restart FR extraction jobs


    Required roles:
     - can_write_jobs

    Args:
        body (JobsStateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutFaceRecognitionJobsStateResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
