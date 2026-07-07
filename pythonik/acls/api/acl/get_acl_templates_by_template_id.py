from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.acl_template_schema import ACLTemplateSchema
from ...models.get_acl_templates_by_template_id_response_default_type_0 import (
    GetAclTemplatesByTemplateIdResponseDefaultType0,
)
from ...models.get_acl_templates_by_template_id_response_default_type_1 import (
    GetAclTemplatesByTemplateIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    template_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/acl/templates/{template_id}/".format(
            template_id=quote(str(template_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ACLTemplateSchema
    | Any
    | GetAclTemplatesByTemplateIdResponseDefaultType0
    | GetAclTemplatesByTemplateIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = ACLTemplateSchema.from_dict(response.json())

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
        GetAclTemplatesByTemplateIdResponseDefaultType0
        | GetAclTemplatesByTemplateIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetAclTemplatesByTemplateIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetAclTemplatesByTemplateIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ACLTemplateSchema
    | Any
    | GetAclTemplatesByTemplateIdResponseDefaultType0
    | GetAclTemplatesByTemplateIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    ACLTemplateSchema
    | Any
    | GetAclTemplatesByTemplateIdResponseDefaultType0
    | GetAclTemplatesByTemplateIdResponseDefaultType1
]:
    """Retreive an acl template


    Required roles:
     - can_read_acl_templates

    Args:
        template_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ACLTemplateSchema | Any | GetAclTemplatesByTemplateIdResponseDefaultType0 | GetAclTemplatesByTemplateIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    ACLTemplateSchema
    | Any
    | GetAclTemplatesByTemplateIdResponseDefaultType0
    | GetAclTemplatesByTemplateIdResponseDefaultType1
    | None
):
    """Retreive an acl template


    Required roles:
     - can_read_acl_templates

    Args:
        template_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ACLTemplateSchema | Any | GetAclTemplatesByTemplateIdResponseDefaultType0 | GetAclTemplatesByTemplateIdResponseDefaultType1
    """

    return sync_detailed(
        template_id=template_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    ACLTemplateSchema
    | Any
    | GetAclTemplatesByTemplateIdResponseDefaultType0
    | GetAclTemplatesByTemplateIdResponseDefaultType1
]:
    """Retreive an acl template


    Required roles:
     - can_read_acl_templates

    Args:
        template_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ACLTemplateSchema | Any | GetAclTemplatesByTemplateIdResponseDefaultType0 | GetAclTemplatesByTemplateIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    ACLTemplateSchema
    | Any
    | GetAclTemplatesByTemplateIdResponseDefaultType0
    | GetAclTemplatesByTemplateIdResponseDefaultType1
    | None
):
    """Retreive an acl template


    Required roles:
     - can_read_acl_templates

    Args:
        template_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ACLTemplateSchema | Any | GetAclTemplatesByTemplateIdResponseDefaultType0 | GetAclTemplatesByTemplateIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            template_id=template_id,
            client=client,
        )
    ).parsed
