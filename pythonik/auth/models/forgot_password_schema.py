from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForgotPasswordSchema")


@_attrs_define
class ForgotPasswordSchema:
    """
    Attributes:
        email (str):
        reset_hash (None | str | Unset):
    """

    email: str
    reset_hash: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        reset_hash: None | str | Unset
        if isinstance(self.reset_hash, Unset):
            reset_hash = UNSET
        else:
            reset_hash = self.reset_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if reset_hash is not UNSET:
            field_dict["reset_hash"] = reset_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        def _parse_reset_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reset_hash = _parse_reset_hash(d.pop("reset_hash", UNSET))

        forgot_password_schema = cls(
            email=email,
            reset_hash=reset_hash,
        )

        forgot_password_schema.additional_properties = d
        return forgot_password_schema

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
