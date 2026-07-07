from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiplatformUserPasswordEditSchema")


@_attrs_define
class MultiplatformUserPasswordEditSchema:
    """
    Attributes:
        email (str):
        password (str):
        current_password (str | Unset):
        ignore_current_password (bool | None | Unset):
    """

    email: str
    password: str
    current_password: str | Unset = UNSET
    ignore_current_password: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        password = self.password

        current_password = self.current_password

        ignore_current_password: bool | None | Unset
        if isinstance(self.ignore_current_password, Unset):
            ignore_current_password = UNSET
        else:
            ignore_current_password = self.ignore_current_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "password": password,
            }
        )
        if current_password is not UNSET:
            field_dict["current_password"] = current_password
        if ignore_current_password is not UNSET:
            field_dict["ignore_current_password"] = ignore_current_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        password = d.pop("password")

        current_password = d.pop("current_password", UNSET)

        def _parse_ignore_current_password(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ignore_current_password = _parse_ignore_current_password(
            d.pop("ignore_current_password", UNSET)
        )

        multiplatform_user_password_edit_schema = cls(
            email=email,
            password=password,
            current_password=current_password,
            ignore_current_password=ignore_current_password,
        )

        multiplatform_user_password_edit_schema.additional_properties = d
        return multiplatform_user_password_edit_schema

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
