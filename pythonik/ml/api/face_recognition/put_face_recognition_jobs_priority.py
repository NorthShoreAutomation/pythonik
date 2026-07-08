from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.jobs_priority_schema import JobsPrioritySchema
from ...models.put_face_recognition_jobs_priority_response_default import (
    PutFaceRecognitionJobsPriorityResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    body: JobsPrioritySchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/face_recognition/jobs/priority/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutFaceRecognitionJobsPriorityResponseDefault:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PutFaceRecognitionJobsPriorityResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PutFaceRecognitionJobsPriorityResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: JobsPrioritySchema,
) -> Response[Any | PutFaceRecognitionJobsPriorityResponseDefault]:
    """Bulk-change priority of FR jobs


    Required roles:
     - can_write_jobs

    Args:
        body (JobsPrioritySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutFaceRecognitionJobsPriorityResponseDefault]
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
    body: JobsPrioritySchema,
) -> Any | PutFaceRecognitionJobsPriorityResponseDefault | None:
    """Bulk-change priority of FR jobs


    Required roles:
     - can_write_jobs

    Args:
        body (JobsPrioritySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutFaceRecognitionJobsPriorityResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: JobsPrioritySchema,
) -> Response[Any | PutFaceRecognitionJobsPriorityResponseDefault]:
    """Bulk-change priority of FR jobs


    Required roles:
     - can_write_jobs

    Args:
        body (JobsPrioritySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutFaceRecognitionJobsPriorityResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: JobsPrioritySchema,
) -> Any | PutFaceRecognitionJobsPriorityResponseDefault | None:
    """Bulk-change priority of FR jobs


    Required roles:
     - can_write_jobs

    Args:
        body (JobsPrioritySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutFaceRecognitionJobsPriorityResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
