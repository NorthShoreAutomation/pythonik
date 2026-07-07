from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_system_domains_by_system_domain_id_logo_body import (
    PostSystemDomainsBySystemDomainIdLogoBody,
)
from ...models.post_system_domains_by_system_domain_id_logo_response_201 import (
    PostSystemDomainsBySystemDomainIdLogoResponse201,
)
from ...models.post_system_domains_by_system_domain_id_logo_response_default_type_0 import (
    PostSystemDomainsBySystemDomainIdLogoResponseDefaultType0,
)
from ...models.post_system_domains_by_system_domain_id_logo_response_default_type_1 import (
    PostSystemDomainsBySystemDomainIdLogoResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    system_domain_id: str,
    *,
    body: PostSystemDomainsBySystemDomainIdLogoBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/system_domains/{system_domain_id}/logo/".format(
            system_domain_id=quote(str(system_domain_id), safe=""),
        ),
    }

    _kwargs["content"] = body.payload
    headers["Content-Type"] = "image/*"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostSystemDomainsBySystemDomainIdLogoResponse201
    | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType0
    | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = PostSystemDomainsBySystemDomainIdLogoResponse201.from_dict(
            response.json()
        )

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        PostSystemDomainsBySystemDomainIdLogoResponseDefaultType0
        | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostSystemDomainsBySystemDomainIdLogoResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostSystemDomainsBySystemDomainIdLogoResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSystemDomainsBySystemDomainIdLogoResponse201
    | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType0
    | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_domain_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemDomainsBySystemDomainIdLogoBody,
) -> Response[
    Any
    | PostSystemDomainsBySystemDomainIdLogoResponse201
    | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType0
    | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType1
]:
    """Upload system domain logo image.

    Args:
        system_domain_id (str):
        body (PostSystemDomainsBySystemDomainIdLogoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSystemDomainsBySystemDomainIdLogoResponse201 | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType0 | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        system_domain_id=system_domain_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_domain_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemDomainsBySystemDomainIdLogoBody,
) -> (
    Any
    | PostSystemDomainsBySystemDomainIdLogoResponse201
    | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType0
    | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType1
    | None
):
    """Upload system domain logo image.

    Args:
        system_domain_id (str):
        body (PostSystemDomainsBySystemDomainIdLogoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSystemDomainsBySystemDomainIdLogoResponse201 | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType0 | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType1
    """

    return sync_detailed(
        system_domain_id=system_domain_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    system_domain_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemDomainsBySystemDomainIdLogoBody,
) -> Response[
    Any
    | PostSystemDomainsBySystemDomainIdLogoResponse201
    | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType0
    | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType1
]:
    """Upload system domain logo image.

    Args:
        system_domain_id (str):
        body (PostSystemDomainsBySystemDomainIdLogoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSystemDomainsBySystemDomainIdLogoResponse201 | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType0 | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        system_domain_id=system_domain_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_domain_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSystemDomainsBySystemDomainIdLogoBody,
) -> (
    Any
    | PostSystemDomainsBySystemDomainIdLogoResponse201
    | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType0
    | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType1
    | None
):
    """Upload system domain logo image.

    Args:
        system_domain_id (str):
        body (PostSystemDomainsBySystemDomainIdLogoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSystemDomainsBySystemDomainIdLogoResponse201 | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType0 | PostSystemDomainsBySystemDomainIdLogoResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            system_domain_id=system_domain_id,
            client=client,
            body=body,
        )
    ).parsed
