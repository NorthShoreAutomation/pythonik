from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_jobs_by_job_id_reindex_response_default import (
    PostJobsByJobIdReindexResponseDefault,
)
from ...models.reindex_job_schema import ReindexJobSchema
from ...types import Response


def _get_kwargs(
    job_id: str,
    *,
    body: ReindexJobSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/jobs/{job_id}/reindex/".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostJobsByJobIdReindexResponseDefault:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostJobsByJobIdReindexResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostJobsByJobIdReindexResponseDefault]:
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
    body: ReindexJobSchema,
) -> Response[Any | PostJobsByJobIdReindexResponseDefault]:
    """Reindex job


    Required roles:
     - can_write_jobs

    Args:
        job_id (str):
        body (ReindexJobSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostJobsByJobIdReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReindexJobSchema,
) -> Any | PostJobsByJobIdReindexResponseDefault | None:
    """Reindex job


    Required roles:
     - can_write_jobs

    Args:
        job_id (str):
        body (ReindexJobSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostJobsByJobIdReindexResponseDefault
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReindexJobSchema,
) -> Response[Any | PostJobsByJobIdReindexResponseDefault]:
    """Reindex job


    Required roles:
     - can_write_jobs

    Args:
        job_id (str):
        body (ReindexJobSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostJobsByJobIdReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReindexJobSchema,
) -> Any | PostJobsByJobIdReindexResponseDefault | None:
    """Reindex job


    Required roles:
     - can_write_jobs

    Args:
        job_id (str):
        body (ReindexJobSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostJobsByJobIdReindexResponseDefault
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            body=body,
        )
    ).parsed
