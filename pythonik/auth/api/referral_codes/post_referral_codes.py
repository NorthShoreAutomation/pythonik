from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_referral_codes_response_default import (
    PostReferralCodesResponseDefault,
)
from ...models.referral_code_schema import ReferralCodeSchema
from ...types import Response


def _get_kwargs(
    *,
    body: ReferralCodeSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/referral_codes/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostReferralCodesResponseDefault | ReferralCodeSchema:
    if response.status_code == 201:
        response_201 = ReferralCodeSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    response_default = PostReferralCodesResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostReferralCodesResponseDefault | ReferralCodeSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReferralCodeSchema,
) -> Response[Any | PostReferralCodesResponseDefault | ReferralCodeSchema]:
    """Create a new referral_code

    Args:
        body (ReferralCodeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostReferralCodesResponseDefault | ReferralCodeSchema]
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
    body: ReferralCodeSchema,
) -> Any | PostReferralCodesResponseDefault | ReferralCodeSchema | None:
    """Create a new referral_code

    Args:
        body (ReferralCodeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostReferralCodesResponseDefault | ReferralCodeSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReferralCodeSchema,
) -> Response[Any | PostReferralCodesResponseDefault | ReferralCodeSchema]:
    """Create a new referral_code

    Args:
        body (ReferralCodeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostReferralCodesResponseDefault | ReferralCodeSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ReferralCodeSchema,
) -> Any | PostReferralCodesResponseDefault | ReferralCodeSchema | None:
    """Create a new referral_code

    Args:
        body (ReferralCodeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostReferralCodesResponseDefault | ReferralCodeSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
