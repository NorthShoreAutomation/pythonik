from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.acl_template_schema import ACLTemplateSchema
from ...models.post_acl_templates_response_default import (
    PostAclTemplatesResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    body: ACLTemplateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/acl/templates/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ACLTemplateSchema | Any | PostAclTemplatesResponseDefault:
    if response.status_code == 201:
        response_201 = ACLTemplateSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostAclTemplatesResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ACLTemplateSchema | Any | PostAclTemplatesResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ACLTemplateSchema,
) -> Response[ACLTemplateSchema | Any | PostAclTemplatesResponseDefault]:
    """Create an acl template


    Required roles:
     - can_write_acl_templates

    Args:
        body (ACLTemplateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ACLTemplateSchema | Any | PostAclTemplatesResponseDefault]
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
    body: ACLTemplateSchema,
) -> ACLTemplateSchema | Any | PostAclTemplatesResponseDefault | None:
    """Create an acl template


    Required roles:
     - can_write_acl_templates

    Args:
        body (ACLTemplateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ACLTemplateSchema | Any | PostAclTemplatesResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ACLTemplateSchema,
) -> Response[ACLTemplateSchema | Any | PostAclTemplatesResponseDefault]:
    """Create an acl template


    Required roles:
     - can_write_acl_templates

    Args:
        body (ACLTemplateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ACLTemplateSchema | Any | PostAclTemplatesResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ACLTemplateSchema,
) -> ACLTemplateSchema | Any | PostAclTemplatesResponseDefault | None:
    """Create an acl template


    Required roles:
     - can_write_acl_templates

    Args:
        body (ACLTemplateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ACLTemplateSchema | Any | PostAclTemplatesResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
