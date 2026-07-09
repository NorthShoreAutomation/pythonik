from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_metadata_filling_proposals_by_job_id_regenerate_response_default import (
    PostMetadataFillingProposalsByJobIdRegenerateResponseDefault,
)
from ...types import Response


def _get_kwargs(
    job_id: str,
    *,
    user_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["User-ID"] = user_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/metadata_filling/proposals/{job_id}/regenerate/".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostMetadataFillingProposalsByJobIdRegenerateResponseDefault:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    response_default = (
        PostMetadataFillingProposalsByJobIdRegenerateResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostMetadataFillingProposalsByJobIdRegenerateResponseDefault]:
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
    user_id: str,
) -> Response[Any | PostMetadataFillingProposalsByJobIdRegenerateResponseDefault]:
    """Regenerate an AI metadata-filling proposal


    Required roles:
     - can_write_metadata_values

    Args:
        job_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostMetadataFillingProposalsByJobIdRegenerateResponseDefault]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str,
) -> Any | PostMetadataFillingProposalsByJobIdRegenerateResponseDefault | None:
    """Regenerate an AI metadata-filling proposal


    Required roles:
     - can_write_metadata_values

    Args:
        job_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostMetadataFillingProposalsByJobIdRegenerateResponseDefault
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str,
) -> Response[Any | PostMetadataFillingProposalsByJobIdRegenerateResponseDefault]:
    """Regenerate an AI metadata-filling proposal


    Required roles:
     - can_write_metadata_values

    Args:
        job_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostMetadataFillingProposalsByJobIdRegenerateResponseDefault]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str,
) -> Any | PostMetadataFillingProposalsByJobIdRegenerateResponseDefault | None:
    """Regenerate an AI metadata-filling proposal


    Required roles:
     - can_write_metadata_values

    Args:
        job_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostMetadataFillingProposalsByJobIdRegenerateResponseDefault
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            user_id=user_id,
        )
    ).parsed
