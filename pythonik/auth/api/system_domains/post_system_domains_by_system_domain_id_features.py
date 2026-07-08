from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.enable_system_domain_feature_schema import (
    EnableSystemDomainFeatureSchema,
)
from ...models.post_system_domains_by_system_domain_id_features_response_default import (
    PostSystemDomainsBySystemDomainIdFeaturesResponseDefault,
)
from ...types import Response


def _get_kwargs(
    system_domain_id: str,
    *,
    body: EnableSystemDomainFeatureSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/system_domains/{system_domain_id}/features/".format(
            system_domain_id=quote(str(system_domain_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | EnableSystemDomainFeatureSchema
    | PostSystemDomainsBySystemDomainIdFeaturesResponseDefault
):
    if response.status_code == 200:
        response_200 = EnableSystemDomainFeatureSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        PostSystemDomainsBySystemDomainIdFeaturesResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | EnableSystemDomainFeatureSchema
    | PostSystemDomainsBySystemDomainIdFeaturesResponseDefault
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
    body: EnableSystemDomainFeatureSchema,
) -> Response[
    Any
    | EnableSystemDomainFeatureSchema
    | PostSystemDomainsBySystemDomainIdFeaturesResponseDefault
]:
    """Enable specified feature on a system domain

    Args:
        system_domain_id (str):
        body (EnableSystemDomainFeatureSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EnableSystemDomainFeatureSchema | PostSystemDomainsBySystemDomainIdFeaturesResponseDefault]
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
    body: EnableSystemDomainFeatureSchema,
) -> (
    Any
    | EnableSystemDomainFeatureSchema
    | PostSystemDomainsBySystemDomainIdFeaturesResponseDefault
    | None
):
    """Enable specified feature on a system domain

    Args:
        system_domain_id (str):
        body (EnableSystemDomainFeatureSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EnableSystemDomainFeatureSchema | PostSystemDomainsBySystemDomainIdFeaturesResponseDefault
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
    body: EnableSystemDomainFeatureSchema,
) -> Response[
    Any
    | EnableSystemDomainFeatureSchema
    | PostSystemDomainsBySystemDomainIdFeaturesResponseDefault
]:
    """Enable specified feature on a system domain

    Args:
        system_domain_id (str):
        body (EnableSystemDomainFeatureSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EnableSystemDomainFeatureSchema | PostSystemDomainsBySystemDomainIdFeaturesResponseDefault]
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
    body: EnableSystemDomainFeatureSchema,
) -> (
    Any
    | EnableSystemDomainFeatureSchema
    | PostSystemDomainsBySystemDomainIdFeaturesResponseDefault
    | None
):
    """Enable specified feature on a system domain

    Args:
        system_domain_id (str):
        body (EnableSystemDomainFeatureSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EnableSystemDomainFeatureSchema | PostSystemDomainsBySystemDomainIdFeaturesResponseDefault
    """

    return (
        await asyncio_detailed(
            system_domain_id=system_domain_id,
            client=client,
            body=body,
        )
    ).parsed
