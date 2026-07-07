from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_jobs_by_job_id_response_default_type_0 import (
    DeleteJobsByJobIdResponseDefaultType0,
)
from ...models.delete_jobs_by_job_id_response_default_type_1 import (
    DeleteJobsByJobIdResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    recursive: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["recursive"] = recursive

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/jobs/{job_id}/".format(
            job_id=quote(str(job_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any | DeleteJobsByJobIdResponseDefaultType0 | DeleteJobsByJobIdResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
    ) -> DeleteJobsByJobIdResponseDefaultType0 | DeleteJobsByJobIdResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteJobsByJobIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = DeleteJobsByJobIdResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | DeleteJobsByJobIdResponseDefaultType0 | DeleteJobsByJobIdResponseDefaultType1
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
    recursive: bool | Unset = UNSET,
) -> Response[
    Any | DeleteJobsByJobIdResponseDefaultType0 | DeleteJobsByJobIdResponseDefaultType1
]:
    """Delete a particular job by id


    Required roles:
     - can_delete_jobs

    Args:
        job_id (str):
        recursive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteJobsByJobIdResponseDefaultType0 | DeleteJobsByJobIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        recursive=recursive,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    recursive: bool | Unset = UNSET,
) -> (
    Any
    | DeleteJobsByJobIdResponseDefaultType0
    | DeleteJobsByJobIdResponseDefaultType1
    | None
):
    """Delete a particular job by id


    Required roles:
     - can_delete_jobs

    Args:
        job_id (str):
        recursive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteJobsByJobIdResponseDefaultType0 | DeleteJobsByJobIdResponseDefaultType1
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        recursive=recursive,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    recursive: bool | Unset = UNSET,
) -> Response[
    Any | DeleteJobsByJobIdResponseDefaultType0 | DeleteJobsByJobIdResponseDefaultType1
]:
    """Delete a particular job by id


    Required roles:
     - can_delete_jobs

    Args:
        job_id (str):
        recursive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteJobsByJobIdResponseDefaultType0 | DeleteJobsByJobIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        recursive=recursive,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    recursive: bool | Unset = UNSET,
) -> (
    Any
    | DeleteJobsByJobIdResponseDefaultType0
    | DeleteJobsByJobIdResponseDefaultType1
    | None
):
    """Delete a particular job by id


    Required roles:
     - can_delete_jobs

    Args:
        job_id (str):
        recursive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteJobsByJobIdResponseDefaultType0 | DeleteJobsByJobIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            recursive=recursive,
        )
    ).parsed
