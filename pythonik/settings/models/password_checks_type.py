from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PasswordChecksType")


@_attrs_define
class PasswordChecksType:
    """
    Attributes:
        digits (int | None | Unset):
        lowercase (int | None | Unset):
        max_length (int | None | Unset):
        min_length (int | None | Unset):
        special_symbols (int | None | Unset):
        uppercase (int | None | Unset):
    """

    digits: int | None | Unset = UNSET
    lowercase: int | None | Unset = UNSET
    max_length: int | None | Unset = UNSET
    min_length: int | None | Unset = UNSET
    special_symbols: int | None | Unset = UNSET
    uppercase: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        digits: int | None | Unset
        if isinstance(self.digits, Unset):
            digits = UNSET
        else:
            digits = self.digits

        lowercase: int | None | Unset
        if isinstance(self.lowercase, Unset):
            lowercase = UNSET
        else:
            lowercase = self.lowercase

        max_length: int | None | Unset
        if isinstance(self.max_length, Unset):
            max_length = UNSET
        else:
            max_length = self.max_length

        min_length: int | None | Unset
        if isinstance(self.min_length, Unset):
            min_length = UNSET
        else:
            min_length = self.min_length

        special_symbols: int | None | Unset
        if isinstance(self.special_symbols, Unset):
            special_symbols = UNSET
        else:
            special_symbols = self.special_symbols

        uppercase: int | None | Unset
        if isinstance(self.uppercase, Unset):
            uppercase = UNSET
        else:
            uppercase = self.uppercase

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if digits is not UNSET:
            field_dict["digits"] = digits
        if lowercase is not UNSET:
            field_dict["lowercase"] = lowercase
        if max_length is not UNSET:
            field_dict["max_length"] = max_length
        if min_length is not UNSET:
            field_dict["min_length"] = min_length
        if special_symbols is not UNSET:
            field_dict["special_symbols"] = special_symbols
        if uppercase is not UNSET:
            field_dict["uppercase"] = uppercase

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_digits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        digits = _parse_digits(d.pop("digits", UNSET))

        def _parse_lowercase(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lowercase = _parse_lowercase(d.pop("lowercase", UNSET))

        def _parse_max_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_length = _parse_max_length(d.pop("max_length", UNSET))

        def _parse_min_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_length = _parse_min_length(d.pop("min_length", UNSET))

        def _parse_special_symbols(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        special_symbols = _parse_special_symbols(d.pop("special_symbols", UNSET))

        def _parse_uppercase(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        uppercase = _parse_uppercase(d.pop("uppercase", UNSET))

        password_checks_type = cls(
            digits=digits,
            lowercase=lowercase,
            max_length=max_length,
            min_length=min_length,
            special_symbols=special_symbols,
            uppercase=uppercase,
        )

        password_checks_type.additional_properties = d
        return password_checks_type

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
