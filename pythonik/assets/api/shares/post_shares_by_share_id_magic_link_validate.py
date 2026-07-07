from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.magic_link_validate_schema import MagicLinkValidateSchema
from ...models.post_shares_by_share_id_magic_link_validate_response_default_type_0 import (
    PostSharesByShareIdMagicLinkValidateResponseDefaultType0,
)
from ...models.post_shares_by_share_id_magic_link_validate_response_default_type_1 import (
    PostSharesByShareIdMagicLinkValidateResponseDefaultType1,
)
from ...models.share_token_schema import ShareTokenSchema
from ...types import Response


def _get_kwargs(
    share_id: str,
    *,
    body: MagicLinkValidateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/shares/{share_id}/magic_link/validate/".format(
            share_id=quote(str(share_id), safe=""),
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
    | PostSharesByShareIdMagicLinkValidateResponseDefaultType0
    | PostSharesByShareIdMagicLinkValidateResponseDefaultType1
    | ShareTokenSchema
):
    if response.status_code == 200:
        response_200 = ShareTokenSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    def _parse_response_default(
        data: object,
    ) -> (
        PostSharesByShareIdMagicLinkValidateResponseDefaultType0
        | PostSharesByShareIdMagicLinkValidateResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostSharesByShareIdMagicLinkValidateResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostSharesByShareIdMagicLinkValidateResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSharesByShareIdMagicLinkValidateResponseDefaultType0
    | PostSharesByShareIdMagicLinkValidateResponseDefaultType1
    | ShareTokenSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MagicLinkValidateSchema,
) -> Response[
    Any
    | PostSharesByShareIdMagicLinkValidateResponseDefaultType0
    | PostSharesByShareIdMagicLinkValidateResponseDefaultType1
    | ShareTokenSchema
]:
    """Validates the email and single-use hash, and returns a share authorization token.

     <br/>The hash is consumed upon first use and cannot be reused.

    Args:
        share_id (str):
        body (MagicLinkValidateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSharesByShareIdMagicLinkValidateResponseDefaultType0 | PostSharesByShareIdMagicLinkValidateResponseDefaultType1 | ShareTokenSchema]
    """

    kwargs = _get_kwargs(
        share_id=share_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MagicLinkValidateSchema,
) -> (
    Any
    | PostSharesByShareIdMagicLinkValidateResponseDefaultType0
    | PostSharesByShareIdMagicLinkValidateResponseDefaultType1
    | ShareTokenSchema
    | None
):
    """Validates the email and single-use hash, and returns a share authorization token.

     <br/>The hash is consumed upon first use and cannot be reused.

    Args:
        share_id (str):
        body (MagicLinkValidateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSharesByShareIdMagicLinkValidateResponseDefaultType0 | PostSharesByShareIdMagicLinkValidateResponseDefaultType1 | ShareTokenSchema
    """

    return sync_detailed(
        share_id=share_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MagicLinkValidateSchema,
) -> Response[
    Any
    | PostSharesByShareIdMagicLinkValidateResponseDefaultType0
    | PostSharesByShareIdMagicLinkValidateResponseDefaultType1
    | ShareTokenSchema
]:
    """Validates the email and single-use hash, and returns a share authorization token.

     <br/>The hash is consumed upon first use and cannot be reused.

    Args:
        share_id (str):
        body (MagicLinkValidateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSharesByShareIdMagicLinkValidateResponseDefaultType0 | PostSharesByShareIdMagicLinkValidateResponseDefaultType1 | ShareTokenSchema]
    """

    kwargs = _get_kwargs(
        share_id=share_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MagicLinkValidateSchema,
) -> (
    Any
    | PostSharesByShareIdMagicLinkValidateResponseDefaultType0
    | PostSharesByShareIdMagicLinkValidateResponseDefaultType1
    | ShareTokenSchema
    | None
):
    """Validates the email and single-use hash, and returns a share authorization token.

     <br/>The hash is consumed upon first use and cannot be reused.

    Args:
        share_id (str):
        body (MagicLinkValidateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSharesByShareIdMagicLinkValidateResponseDefaultType0 | PostSharesByShareIdMagicLinkValidateResponseDefaultType1 | ShareTokenSchema
    """

    return (
        await asyncio_detailed(
            share_id=share_id,
            client=client,
            body=body,
        )
    ).parsed
