from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_transcode_by_transcode_job_id_response_default import (
    GetTranscodeByTranscodeJobIdResponseDefault,
)
from ...models.job_schema import JobSchema
from ...types import Response


def _get_kwargs(
    transcode_job_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/transcode/{transcode_job_id}/".format(
            transcode_job_id=quote(str(transcode_job_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetTranscodeByTranscodeJobIdResponseDefault | JobSchema:
    if response.status_code == 200:
        response_200 = JobSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetTranscodeByTranscodeJobIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetTranscodeByTranscodeJobIdResponseDefault | JobSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transcode_job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetTranscodeByTranscodeJobIdResponseDefault | JobSchema]:
    """Get transcode job


    Required roles:
     - can_read_transcode_jobs

    Args:
        transcode_job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTranscodeByTranscodeJobIdResponseDefault | JobSchema]
    """

    kwargs = _get_kwargs(
        transcode_job_id=transcode_job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transcode_job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetTranscodeByTranscodeJobIdResponseDefault | JobSchema | None:
    """Get transcode job


    Required roles:
     - can_read_transcode_jobs

    Args:
        transcode_job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTranscodeByTranscodeJobIdResponseDefault | JobSchema
    """

    return sync_detailed(
        transcode_job_id=transcode_job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    transcode_job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetTranscodeByTranscodeJobIdResponseDefault | JobSchema]:
    """Get transcode job


    Required roles:
     - can_read_transcode_jobs

    Args:
        transcode_job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTranscodeByTranscodeJobIdResponseDefault | JobSchema]
    """

    kwargs = _get_kwargs(
        transcode_job_id=transcode_job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transcode_job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetTranscodeByTranscodeJobIdResponseDefault | JobSchema | None:
    """Get transcode job


    Required roles:
     - can_read_transcode_jobs

    Args:
        transcode_job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTranscodeByTranscodeJobIdResponseDefault | JobSchema
    """

    return (
        await asyncio_detailed(
            transcode_job_id=transcode_job_id,
            client=client,
        )
    ).parsed
