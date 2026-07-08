from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.create_publication_job_schema import CreatePublicationJobSchema
from ...models.post_publications_jobs_response_default import (
    PostPublicationsJobsResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    body: CreatePublicationJobSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/publications/jobs/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostPublicationsJobsResponseDefault:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PostPublicationsJobsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostPublicationsJobsResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePublicationJobSchema,
) -> Response[Any | PostPublicationsJobsResponseDefault]:
    """⚠️ Beta: Schedules publishing for an asset to a list of destinations based on template_id


    Required roles:
     - can_publish

    Args:
        body (CreatePublicationJobSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostPublicationsJobsResponseDefault]
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
    body: CreatePublicationJobSchema,
) -> Any | PostPublicationsJobsResponseDefault | None:
    """⚠️ Beta: Schedules publishing for an asset to a list of destinations based on template_id


    Required roles:
     - can_publish

    Args:
        body (CreatePublicationJobSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostPublicationsJobsResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePublicationJobSchema,
) -> Response[Any | PostPublicationsJobsResponseDefault]:
    """⚠️ Beta: Schedules publishing for an asset to a list of destinations based on template_id


    Required roles:
     - can_publish

    Args:
        body (CreatePublicationJobSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostPublicationsJobsResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePublicationJobSchema,
) -> Any | PostPublicationsJobsResponseDefault | None:
    """⚠️ Beta: Schedules publishing for an asset to a list of destinations based on template_id


    Required roles:
     - can_publish

    Args:
        body (CreatePublicationJobSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostPublicationsJobsResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
