from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.jobs_priority_schema import JobsPrioritySchema
from ...models.put_jobs_priority_response_default import PutJobsPriorityResponseDefault
from ...types import Response


def _get_kwargs(
    *,
    body: JobsPrioritySchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/jobs/priority/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | JobsPrioritySchema | PutJobsPriorityResponseDefault:
    if response.status_code == 200:
        response_200 = JobsPrioritySchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    response_default = PutJobsPriorityResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | JobsPrioritySchema | PutJobsPriorityResponseDefault]:
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
) -> Response[Any | JobsPrioritySchema | PutJobsPriorityResponseDefault]:
    """Change jobs priority


    Required roles:
     - can_write_jobs

    Args:
        body (JobsPrioritySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JobsPrioritySchema | PutJobsPriorityResponseDefault]
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
) -> Any | JobsPrioritySchema | PutJobsPriorityResponseDefault | None:
    """Change jobs priority


    Required roles:
     - can_write_jobs

    Args:
        body (JobsPrioritySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JobsPrioritySchema | PutJobsPriorityResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: JobsPrioritySchema,
) -> Response[Any | JobsPrioritySchema | PutJobsPriorityResponseDefault]:
    """Change jobs priority


    Required roles:
     - can_write_jobs

    Args:
        body (JobsPrioritySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JobsPrioritySchema | PutJobsPriorityResponseDefault]
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
) -> Any | JobsPrioritySchema | PutJobsPriorityResponseDefault | None:
    """Change jobs priority


    Required roles:
     - can_write_jobs

    Args:
        body (JobsPrioritySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JobsPrioritySchema | PutJobsPriorityResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
