from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_user_licensed_by_response_default_type_0 import (
    GetUserLicensedByResponseDefaultType0,
)
from ...models.get_user_licensed_by_response_default_type_1 import (
    GetUserLicensedByResponseDefaultType1,
)
from ...models.user_usages_schema import UserUsagesSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    system_domain_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from_date"] = from_date

    params["to_date"] = to_date

    params["system_domain_id"] = system_domain_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/user/licensed/by/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetUserLicensedByResponseDefaultType0
    | GetUserLicensedByResponseDefaultType1
    | UserUsagesSchema
):
    if response.status_code == 200:
        response_200 = UserUsagesSchema.from_dict(response.json())

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
    ) -> GetUserLicensedByResponseDefaultType0 | GetUserLicensedByResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetUserLicensedByResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetUserLicensedByResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetUserLicensedByResponseDefaultType0
    | GetUserLicensedByResponseDefaultType1
    | UserUsagesSchema
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
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    system_domain_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetUserLicensedByResponseDefaultType0
    | GetUserLicensedByResponseDefaultType1
    | UserUsagesSchema
]:
    """Returns licensed user usage


    Required roles:
     - can_read_stats

    Args:
        from_date (str | Unset):
        to_date (str | Unset):
        system_domain_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUserLicensedByResponseDefaultType0 | GetUserLicensedByResponseDefaultType1 | UserUsagesSchema]
    """

    kwargs = _get_kwargs(
        from_date=from_date,
        to_date=to_date,
        system_domain_id=system_domain_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    system_domain_id: str | Unset = UNSET,
) -> (
    Any
    | GetUserLicensedByResponseDefaultType0
    | GetUserLicensedByResponseDefaultType1
    | UserUsagesSchema
    | None
):
    """Returns licensed user usage


    Required roles:
     - can_read_stats

    Args:
        from_date (str | Unset):
        to_date (str | Unset):
        system_domain_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUserLicensedByResponseDefaultType0 | GetUserLicensedByResponseDefaultType1 | UserUsagesSchema
    """

    return sync_detailed(
        client=client,
        from_date=from_date,
        to_date=to_date,
        system_domain_id=system_domain_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    system_domain_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetUserLicensedByResponseDefaultType0
    | GetUserLicensedByResponseDefaultType1
    | UserUsagesSchema
]:
    """Returns licensed user usage


    Required roles:
     - can_read_stats

    Args:
        from_date (str | Unset):
        to_date (str | Unset):
        system_domain_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUserLicensedByResponseDefaultType0 | GetUserLicensedByResponseDefaultType1 | UserUsagesSchema]
    """

    kwargs = _get_kwargs(
        from_date=from_date,
        to_date=to_date,
        system_domain_id=system_domain_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    system_domain_id: str | Unset = UNSET,
) -> (
    Any
    | GetUserLicensedByResponseDefaultType0
    | GetUserLicensedByResponseDefaultType1
    | UserUsagesSchema
    | None
):
    """Returns licensed user usage


    Required roles:
     - can_read_stats

    Args:
        from_date (str | Unset):
        to_date (str | Unset):
        system_domain_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUserLicensedByResponseDefaultType0 | GetUserLicensedByResponseDefaultType1 | UserUsagesSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            from_date=from_date,
            to_date=to_date,
            system_domain_id=system_domain_id,
        )
    ).parsed
