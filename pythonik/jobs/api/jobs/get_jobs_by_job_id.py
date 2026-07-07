from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_jobs_by_job_id_response_default_type_0 import (
    GetJobsByJobIdResponseDefaultType0,
)
from ...models.get_jobs_by_job_id_response_default_type_1 import (
    GetJobsByJobIdResponseDefaultType1,
)
from ...models.job_schema import JobSchema
from ...types import Response


def _get_kwargs(
    job_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/jobs/{job_id}/".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetJobsByJobIdResponseDefaultType0
    | GetJobsByJobIdResponseDefaultType1
    | JobSchema
):
    if response.status_code == 200:
        response_200 = JobSchema.from_dict(response.json())

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
    ) -> GetJobsByJobIdResponseDefaultType0 | GetJobsByJobIdResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetJobsByJobIdResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetJobsByJobIdResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetJobsByJobIdResponseDefaultType0
    | GetJobsByJobIdResponseDefaultType1
    | JobSchema
]:
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
) -> Response[
    Any
    | GetJobsByJobIdResponseDefaultType0
    | GetJobsByJobIdResponseDefaultType1
    | JobSchema
]:
    """Returns a particular job by id


    Required roles:
     - can_read_jobs

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetJobsByJobIdResponseDefaultType0 | GetJobsByJobIdResponseDefaultType1 | JobSchema]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetJobsByJobIdResponseDefaultType0
    | GetJobsByJobIdResponseDefaultType1
    | JobSchema
    | None
):
    """Returns a particular job by id


    Required roles:
     - can_read_jobs

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetJobsByJobIdResponseDefaultType0 | GetJobsByJobIdResponseDefaultType1 | JobSchema
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetJobsByJobIdResponseDefaultType0
    | GetJobsByJobIdResponseDefaultType1
    | JobSchema
]:
    """Returns a particular job by id


    Required roles:
     - can_read_jobs

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetJobsByJobIdResponseDefaultType0 | GetJobsByJobIdResponseDefaultType1 | JobSchema]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetJobsByJobIdResponseDefaultType0
    | GetJobsByJobIdResponseDefaultType1
    | JobSchema
    | None
):
    """Returns a particular job by id


    Required roles:
     - can_read_jobs

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetJobsByJobIdResponseDefaultType0 | GetJobsByJobIdResponseDefaultType1 | JobSchema
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
