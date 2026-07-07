from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_transcode_by_transcode_job_id_priority_by_priority_response_default_type_0 import (
    PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType0,
)
from ...models.put_transcode_by_transcode_job_id_priority_by_priority_response_default_type_1 import (
    PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    transcode_job_id: str,
    priority: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/transcode/{transcode_job_id}/priority/{priority}/".format(
            transcode_job_id=quote(str(transcode_job_id), safe=""),
            priority=quote(str(priority), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType0
    | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1
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
        PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType0
        | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType0
    | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transcode_job_id: str,
    priority: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType0
    | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1
]:
    """Change transcode job priority


    Required roles:
     - can_write_transcode_jobs

    Args:
        transcode_job_id (str):
        priority (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType0 | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        transcode_job_id=transcode_job_id,
        priority=priority,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transcode_job_id: str,
    priority: int,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType0
    | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1
    | None
):
    """Change transcode job priority


    Required roles:
     - can_write_transcode_jobs

    Args:
        transcode_job_id (str):
        priority (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType0 | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1
    """

    return sync_detailed(
        transcode_job_id=transcode_job_id,
        priority=priority,
        client=client,
    ).parsed


async def asyncio_detailed(
    transcode_job_id: str,
    priority: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType0
    | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1
]:
    """Change transcode job priority


    Required roles:
     - can_write_transcode_jobs

    Args:
        transcode_job_id (str):
        priority (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType0 | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        transcode_job_id=transcode_job_id,
        priority=priority,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transcode_job_id: str,
    priority: int,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType0
    | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1
    | None
):
    """Change transcode job priority


    Required roles:
     - can_write_transcode_jobs

    Args:
        transcode_job_id (str):
        priority (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType0 | PutTranscodeByTranscodeJobIdPriorityByPriorityResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            transcode_job_id=transcode_job_id,
            priority=priority,
            client=client,
        )
    ).parsed
