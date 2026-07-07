from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_edge_transcode_jobs_by_job_id_acknowledge_response_default_type_0 import (
    PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType0,
)
from ...models.post_edge_transcode_jobs_by_job_id_acknowledge_response_default_type_1 import (
    PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    job_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/edge_transcode/jobs/{job_id}/acknowledge/".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType0
    | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
    ) -> (
        PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType0
        | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType0
    | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1
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
    | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType0
    | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1
]:
    """Acknowledge an edge transcode job


    Required roles:
     - can_read_transcode_jobs

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType0 | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1]
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
    | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType0
    | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1
    | None
):
    """Acknowledge an edge transcode job


    Required roles:
     - can_read_transcode_jobs

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType0 | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1
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
    | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType0
    | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1
]:
    """Acknowledge an edge transcode job


    Required roles:
     - can_read_transcode_jobs

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType0 | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1]
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
    | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType0
    | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1
    | None
):
    """Acknowledge an edge transcode job


    Required roles:
     - can_read_transcode_jobs

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType0 | PostEdgeTranscodeJobsByJobIdAcknowledgeResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
