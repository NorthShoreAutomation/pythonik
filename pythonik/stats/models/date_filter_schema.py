from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DateFilterSchema")


@_attrs_define
class DateFilterSchema:
    """
    Attributes:
        from_date (datetime.datetime | None | Unset):
        to_date (datetime.datetime | None | Unset):
    """

    from_date: datetime.datetime | None | Unset = UNSET
    to_date: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_date: None | str | Unset
        if isinstance(self.from_date, Unset):
            from_date = UNSET
        elif isinstance(self.from_date, datetime.datetime):
            from_date = self.from_date.isoformat()
        else:
            from_date = self.from_date

        to_date: None | str | Unset
        if isinstance(self.to_date, Unset):
            to_date = UNSET
        elif isinstance(self.to_date, datetime.datetime):
            to_date = self.to_date.isoformat()
        else:
            to_date = self.to_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_date is not UNSET:
            field_dict["from_date"] = from_date
        if to_date is not UNSET:
            field_dict["to_date"] = to_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_from_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_date_type_0 = datetime.datetime.fromisoformat(data)

                return from_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        from_date = _parse_from_date(d.pop("from_date", UNSET))

        def _parse_to_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_date_type_0 = datetime.datetime.fromisoformat(data)

                return to_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        to_date = _parse_to_date(d.pop("to_date", UNSET))

        date_filter_schema = cls(
            from_date=from_date,
            to_date=to_date,
        )

        date_filter_schema.additional_properties = d
        return date_filter_schema

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
