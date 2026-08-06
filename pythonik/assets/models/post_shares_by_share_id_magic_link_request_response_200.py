from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSharesByShareIdMagicLinkRequestResponse200")


@_attrs_define
class PostSharesByShareIdMagicLinkRequestResponse200:
    """
    Attributes:
        expires_in_minutes (int | None | Unset):
        message (None | str | Unset):
    """

    expires_in_minutes: int | None | Unset = UNSET
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_in_minutes: int | None | Unset
        if isinstance(self.expires_in_minutes, Unset):
            expires_in_minutes = UNSET
        else:
            expires_in_minutes = self.expires_in_minutes

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_in_minutes is not UNSET:
            field_dict["expires_in_minutes"] = expires_in_minutes
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_expires_in_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_in_minutes = _parse_expires_in_minutes(
            d.pop("expires_in_minutes", UNSET)
        )

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        post_shares_by_share_id_magic_link_request_response_200 = cls(
            expires_in_minutes=expires_in_minutes,
            message=message,
        )

        post_shares_by_share_id_magic_link_request_response_200.additional_properties = d
        return post_shares_by_share_id_magic_link_request_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
