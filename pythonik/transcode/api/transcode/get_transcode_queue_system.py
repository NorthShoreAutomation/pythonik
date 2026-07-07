from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_transcode_queue_system_response_default_type_0 import (
    GetTranscodeQueueSystemResponseDefaultType0,
)
from ...models.get_transcode_queue_system_response_default_type_1 import (
    GetTranscodeQueueSystemResponseDefaultType1,
)
from ...models.transcode_queue_schema import TranscodeQueueSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_domain_id: bool | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_domain_id"] = per_domain_id

    params["per_page"] = per_page

    params["page"] = page

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/transcode/queue/system/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetTranscodeQueueSystemResponseDefaultType0
    | GetTranscodeQueueSystemResponseDefaultType1
    | TranscodeQueueSchema
):
    if response.status_code == 200:
        response_200 = TranscodeQueueSchema.from_dict(response.json())

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
        GetTranscodeQueueSystemResponseDefaultType0
        | GetTranscodeQueueSystemResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetTranscodeQueueSystemResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetTranscodeQueueSystemResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetTranscodeQueueSystemResponseDefaultType0
    | GetTranscodeQueueSystemResponseDefaultType1
    | TranscodeQueueSchema
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
    per_domain_id: bool | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[
    Any
    | GetTranscodeQueueSystemResponseDefaultType0
    | GetTranscodeQueueSystemResponseDefaultType1
    | TranscodeQueueSchema
]:
    """Get the status of the transcode job queues

    Args:
        per_domain_id (bool | Unset):
        per_page (int | Unset):
        page (int | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTranscodeQueueSystemResponseDefaultType0 | GetTranscodeQueueSystemResponseDefaultType1 | TranscodeQueueSchema]
    """

    kwargs = _get_kwargs(
        per_domain_id=per_domain_id,
        per_page=per_page,
        page=page,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_domain_id: bool | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> (
    Any
    | GetTranscodeQueueSystemResponseDefaultType0
    | GetTranscodeQueueSystemResponseDefaultType1
    | TranscodeQueueSchema
    | None
):
    """Get the status of the transcode job queues

    Args:
        per_domain_id (bool | Unset):
        per_page (int | Unset):
        page (int | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTranscodeQueueSystemResponseDefaultType0 | GetTranscodeQueueSystemResponseDefaultType1 | TranscodeQueueSchema
    """

    return sync_detailed(
        client=client,
        per_domain_id=per_domain_id,
        per_page=per_page,
        page=page,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_domain_id: bool | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[
    Any
    | GetTranscodeQueueSystemResponseDefaultType0
    | GetTranscodeQueueSystemResponseDefaultType1
    | TranscodeQueueSchema
]:
    """Get the status of the transcode job queues

    Args:
        per_domain_id (bool | Unset):
        per_page (int | Unset):
        page (int | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTranscodeQueueSystemResponseDefaultType0 | GetTranscodeQueueSystemResponseDefaultType1 | TranscodeQueueSchema]
    """

    kwargs = _get_kwargs(
        per_domain_id=per_domain_id,
        per_page=per_page,
        page=page,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_domain_id: bool | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> (
    Any
    | GetTranscodeQueueSystemResponseDefaultType0
    | GetTranscodeQueueSystemResponseDefaultType1
    | TranscodeQueueSchema
    | None
):
    """Get the status of the transcode job queues

    Args:
        per_domain_id (bool | Unset):
        per_page (int | Unset):
        page (int | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTranscodeQueueSystemResponseDefaultType0 | GetTranscodeQueueSystemResponseDefaultType1 | TranscodeQueueSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            per_domain_id=per_domain_id,
            per_page=per_page,
            page=page,
            sort=sort,
        )
    ).parsed
