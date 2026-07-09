from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.assets_schema import AssetsSchema
from ...models.get_persons_by_person_id_response_default import (
    GetPersonsByPersonIdResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: str,
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    asset_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["asset_id"] = asset_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/persons/{person_id}/".format(
            person_id=quote(str(person_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | AssetsSchema | GetPersonsByPersonIdResponseDefault:
    if response.status_code == 200:
        response_200 = AssetsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetPersonsByPersonIdResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | AssetsSchema | GetPersonsByPersonIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    asset_id: str | Unset = UNSET,
) -> Response[Any | AssetsSchema | GetPersonsByPersonIdResponseDefault]:
    """Get all assets containing a person_id or specific versions of an asset containing a person_id

    Args:
        person_id (str):
        page (int | Unset):
        per_page (int | Unset):
        asset_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetsSchema | GetPersonsByPersonIdResponseDefault]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        page=page,
        per_page=per_page,
        asset_id=asset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    asset_id: str | Unset = UNSET,
) -> Any | AssetsSchema | GetPersonsByPersonIdResponseDefault | None:
    """Get all assets containing a person_id or specific versions of an asset containing a person_id

    Args:
        person_id (str):
        page (int | Unset):
        per_page (int | Unset):
        asset_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetsSchema | GetPersonsByPersonIdResponseDefault
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        page=page,
        per_page=per_page,
        asset_id=asset_id,
    ).parsed


async def asyncio_detailed(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    asset_id: str | Unset = UNSET,
) -> Response[Any | AssetsSchema | GetPersonsByPersonIdResponseDefault]:
    """Get all assets containing a person_id or specific versions of an asset containing a person_id

    Args:
        person_id (str):
        page (int | Unset):
        per_page (int | Unset):
        asset_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetsSchema | GetPersonsByPersonIdResponseDefault]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        page=page,
        per_page=per_page,
        asset_id=asset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    asset_id: str | Unset = UNSET,
) -> Any | AssetsSchema | GetPersonsByPersonIdResponseDefault | None:
    """Get all assets containing a person_id or specific versions of an asset containing a person_id

    Args:
        person_id (str):
        page (int | Unset):
        per_page (int | Unset):
        asset_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetsSchema | GetPersonsByPersonIdResponseDefault
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            page=page,
            per_page=per_page,
            asset_id=asset_id,
        )
    ).parsed
