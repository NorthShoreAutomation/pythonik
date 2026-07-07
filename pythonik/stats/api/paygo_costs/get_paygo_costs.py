from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_paygo_costs_response_default_type_0 import (
    GetPaygoCostsResponseDefaultType0,
)
from ...models.get_paygo_costs_response_default_type_1 import (
    GetPaygoCostsResponseDefaultType1,
)
from ...models.paygo_costs_schema import PaygoCostsSchema
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/paygo_costs/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetPaygoCostsResponseDefaultType0
    | GetPaygoCostsResponseDefaultType1
    | PaygoCostsSchema
):
    if response.status_code == 200:
        response_200 = PaygoCostsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> GetPaygoCostsResponseDefaultType0 | GetPaygoCostsResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetPaygoCostsResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetPaygoCostsResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetPaygoCostsResponseDefaultType0
    | GetPaygoCostsResponseDefaultType1
    | PaygoCostsSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetPaygoCostsResponseDefaultType0
    | GetPaygoCostsResponseDefaultType1
    | PaygoCostsSchema
]:
    """Returns monthly costs from billing


    Required roles:
     - can_read_billing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPaygoCostsResponseDefaultType0 | GetPaygoCostsResponseDefaultType1 | PaygoCostsSchema]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetPaygoCostsResponseDefaultType0
    | GetPaygoCostsResponseDefaultType1
    | PaygoCostsSchema
    | None
):
    """Returns monthly costs from billing


    Required roles:
     - can_read_billing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPaygoCostsResponseDefaultType0 | GetPaygoCostsResponseDefaultType1 | PaygoCostsSchema
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetPaygoCostsResponseDefaultType0
    | GetPaygoCostsResponseDefaultType1
    | PaygoCostsSchema
]:
    """Returns monthly costs from billing


    Required roles:
     - can_read_billing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPaygoCostsResponseDefaultType0 | GetPaygoCostsResponseDefaultType1 | PaygoCostsSchema]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetPaygoCostsResponseDefaultType0
    | GetPaygoCostsResponseDefaultType1
    | PaygoCostsSchema
    | None
):
    """Returns monthly costs from billing


    Required roles:
     - can_read_billing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPaygoCostsResponseDefaultType0 | GetPaygoCostsResponseDefaultType1 | PaygoCostsSchema
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
