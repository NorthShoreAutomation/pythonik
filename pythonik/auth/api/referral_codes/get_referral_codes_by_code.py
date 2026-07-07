from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_referral_codes_by_code_response_default_type_0 import (
    GetReferralCodesByCodeResponseDefaultType0,
)
from ...models.get_referral_codes_by_code_response_default_type_1 import (
    GetReferralCodesByCodeResponseDefaultType1,
)
from ...models.referral_code_schema import ReferralCodeSchema
from ...types import Response


def _get_kwargs(
    code: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/referral_codes/{code}/".format(
            code=quote(str(code), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetReferralCodesByCodeResponseDefaultType0
    | GetReferralCodesByCodeResponseDefaultType1
    | ReferralCodeSchema
):
    if response.status_code == 200:
        response_200 = ReferralCodeSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        GetReferralCodesByCodeResponseDefaultType0
        | GetReferralCodesByCodeResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetReferralCodesByCodeResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetReferralCodesByCodeResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetReferralCodesByCodeResponseDefaultType0
    | GetReferralCodesByCodeResponseDefaultType1
    | ReferralCodeSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    code: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetReferralCodesByCodeResponseDefaultType0
    | GetReferralCodesByCodeResponseDefaultType1
    | ReferralCodeSchema
]:
    """Get a referral_code

    Args:
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetReferralCodesByCodeResponseDefaultType0 | GetReferralCodesByCodeResponseDefaultType1 | ReferralCodeSchema]
    """

    kwargs = _get_kwargs(
        code=code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    code: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetReferralCodesByCodeResponseDefaultType0
    | GetReferralCodesByCodeResponseDefaultType1
    | ReferralCodeSchema
    | None
):
    """Get a referral_code

    Args:
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetReferralCodesByCodeResponseDefaultType0 | GetReferralCodesByCodeResponseDefaultType1 | ReferralCodeSchema
    """

    return sync_detailed(
        code=code,
        client=client,
    ).parsed


async def asyncio_detailed(
    code: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetReferralCodesByCodeResponseDefaultType0
    | GetReferralCodesByCodeResponseDefaultType1
    | ReferralCodeSchema
]:
    """Get a referral_code

    Args:
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetReferralCodesByCodeResponseDefaultType0 | GetReferralCodesByCodeResponseDefaultType1 | ReferralCodeSchema]
    """

    kwargs = _get_kwargs(
        code=code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    code: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetReferralCodesByCodeResponseDefaultType0
    | GetReferralCodesByCodeResponseDefaultType1
    | ReferralCodeSchema
    | None
):
    """Get a referral_code

    Args:
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetReferralCodesByCodeResponseDefaultType0 | GetReferralCodesByCodeResponseDefaultType1 | ReferralCodeSchema
    """

    return (
        await asyncio_detailed(
            code=code,
            client=client,
        )
    ).parsed
