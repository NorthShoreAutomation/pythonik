from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_metadata_filling_proposals_by_parent_job_id_bulk_accept_response_default import (
    PostMetadataFillingProposalsByParentJobIdBulkAcceptResponseDefault,
)
from ...types import Response


def _get_kwargs(
    parent_job_id: str,
    *,
    user_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["User-ID"] = user_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/metadata_filling/proposals/{parent_job_id}/bulk/accept/".format(
            parent_job_id=quote(str(parent_job_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostMetadataFillingProposalsByParentJobIdBulkAcceptResponseDefault:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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

    if response.status_code == 502:
        response_502 = cast(Any, None)
        return response_502

    response_default = (
        PostMetadataFillingProposalsByParentJobIdBulkAcceptResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostMetadataFillingProposalsByParentJobIdBulkAcceptResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    parent_job_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str,
) -> Response[Any | PostMetadataFillingProposalsByParentJobIdBulkAcceptResponseDefault]:
    """Accept every pending AI metadata-filling proposal under a bulk job

     <br/>Each proposal's values are written to the asset through the job's metadata view before<br/>the
    proposal is accepted. Only the user who triggered the job may run this. A regenerated<br/>proposal
    belongs to a new standalone job and is not part of this review.<br/>Each proposal's values are
    written to the asset through the job's metadata view before<br/>the proposal is accepted. Only the
    user who triggered the job may run this. A regenerated<br/>proposal belongs to a new standalone job
    and is not part of this review.
    Required roles:
     - can_write_metadata_values

    Args:
        parent_job_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostMetadataFillingProposalsByParentJobIdBulkAcceptResponseDefault]
    """

    kwargs = _get_kwargs(
        parent_job_id=parent_job_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    parent_job_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str,
) -> Any | PostMetadataFillingProposalsByParentJobIdBulkAcceptResponseDefault | None:
    """Accept every pending AI metadata-filling proposal under a bulk job

     <br/>Each proposal's values are written to the asset through the job's metadata view before<br/>the
    proposal is accepted. Only the user who triggered the job may run this. A regenerated<br/>proposal
    belongs to a new standalone job and is not part of this review.<br/>Each proposal's values are
    written to the asset through the job's metadata view before<br/>the proposal is accepted. Only the
    user who triggered the job may run this. A regenerated<br/>proposal belongs to a new standalone job
    and is not part of this review.
    Required roles:
     - can_write_metadata_values

    Args:
        parent_job_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostMetadataFillingProposalsByParentJobIdBulkAcceptResponseDefault
    """

    return sync_detailed(
        parent_job_id=parent_job_id,
        client=client,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    parent_job_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str,
) -> Response[Any | PostMetadataFillingProposalsByParentJobIdBulkAcceptResponseDefault]:
    """Accept every pending AI metadata-filling proposal under a bulk job

     <br/>Each proposal's values are written to the asset through the job's metadata view before<br/>the
    proposal is accepted. Only the user who triggered the job may run this. A regenerated<br/>proposal
    belongs to a new standalone job and is not part of this review.<br/>Each proposal's values are
    written to the asset through the job's metadata view before<br/>the proposal is accepted. Only the
    user who triggered the job may run this. A regenerated<br/>proposal belongs to a new standalone job
    and is not part of this review.
    Required roles:
     - can_write_metadata_values

    Args:
        parent_job_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostMetadataFillingProposalsByParentJobIdBulkAcceptResponseDefault]
    """

    kwargs = _get_kwargs(
        parent_job_id=parent_job_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    parent_job_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str,
) -> Any | PostMetadataFillingProposalsByParentJobIdBulkAcceptResponseDefault | None:
    """Accept every pending AI metadata-filling proposal under a bulk job

     <br/>Each proposal's values are written to the asset through the job's metadata view before<br/>the
    proposal is accepted. Only the user who triggered the job may run this. A regenerated<br/>proposal
    belongs to a new standalone job and is not part of this review.<br/>Each proposal's values are
    written to the asset through the job's metadata view before<br/>the proposal is accepted. Only the
    user who triggered the job may run this. A regenerated<br/>proposal belongs to a new standalone job
    and is not part of this review.
    Required roles:
     - can_write_metadata_values

    Args:
        parent_job_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostMetadataFillingProposalsByParentJobIdBulkAcceptResponseDefault
    """

    return (
        await asyncio_detailed(
            parent_job_id=parent_job_id,
            client=client,
            user_id=user_id,
        )
    ).parsed
