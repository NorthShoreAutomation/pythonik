from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_registrations_content_response_default_type_0 import (
    GetRegistrationsContentResponseDefaultType0,
)
from ...models.get_registrations_content_response_default_type_1 import (
    GetRegistrationsContentResponseDefaultType1,
)
from ...models.webflow_content_schema import WebflowContentSchema
from ...types import UNSET, Response


def _get_kwargs(
    *,
    page_route: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page_route"] = page_route

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/registrations/content/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetRegistrationsContentResponseDefaultType0
    | GetRegistrationsContentResponseDefaultType1
    | WebflowContentSchema
):
    if response.status_code == 200:
        response_200 = WebflowContentSchema.from_dict(response.json())

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
        GetRegistrationsContentResponseDefaultType0
        | GetRegistrationsContentResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetRegistrationsContentResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetRegistrationsContentResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetRegistrationsContentResponseDefaultType0
    | GetRegistrationsContentResponseDefaultType1
    | WebflowContentSchema
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
    page_route: str,
) -> Response[
    Any
    | GetRegistrationsContentResponseDefaultType0
    | GetRegistrationsContentResponseDefaultType1
    | WebflowContentSchema
]:
    """Returns page content from Webflow collection

    Args:
        page_route (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetRegistrationsContentResponseDefaultType0 | GetRegistrationsContentResponseDefaultType1 | WebflowContentSchema]
    """

    kwargs = _get_kwargs(
        page_route=page_route,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page_route: str,
) -> (
    Any
    | GetRegistrationsContentResponseDefaultType0
    | GetRegistrationsContentResponseDefaultType1
    | WebflowContentSchema
    | None
):
    """Returns page content from Webflow collection

    Args:
        page_route (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetRegistrationsContentResponseDefaultType0 | GetRegistrationsContentResponseDefaultType1 | WebflowContentSchema
    """

    return sync_detailed(
        client=client,
        page_route=page_route,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_route: str,
) -> Response[
    Any
    | GetRegistrationsContentResponseDefaultType0
    | GetRegistrationsContentResponseDefaultType1
    | WebflowContentSchema
]:
    """Returns page content from Webflow collection

    Args:
        page_route (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetRegistrationsContentResponseDefaultType0 | GetRegistrationsContentResponseDefaultType1 | WebflowContentSchema]
    """

    kwargs = _get_kwargs(
        page_route=page_route,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_route: str,
) -> (
    Any
    | GetRegistrationsContentResponseDefaultType0
    | GetRegistrationsContentResponseDefaultType1
    | WebflowContentSchema
    | None
):
    """Returns page content from Webflow collection

    Args:
        page_route (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetRegistrationsContentResponseDefaultType0 | GetRegistrationsContentResponseDefaultType1 | WebflowContentSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            page_route=page_route,
        )
    ).parsed
