from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.range_filter_schema import RangeFilterSchema
    from ..models.term_schema_external_type_0 import TermSchemaExternalType0


T = TypeVar("T", bound="TermSchema")


@_attrs_define
class TermSchema:
    """
    Attributes:
        name (str):
        exists (bool | None | Unset):
        external (None | TermSchemaExternalType0 | Unset):
        missing (bool | None | Unset):
        range_ (None | RangeFilterSchema | Unset):
        value (Any | Unset):
        value_in (list[str] | None | Unset):
    """

    name: str
    exists: bool | None | Unset = UNSET
    external: None | TermSchemaExternalType0 | Unset = UNSET
    missing: bool | None | Unset = UNSET
    range_: None | RangeFilterSchema | Unset = UNSET
    value: Any | Unset = UNSET
    value_in: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.range_filter_schema import RangeFilterSchema
        from ..models.term_schema_external_type_0 import TermSchemaExternalType0

        name = self.name

        exists: bool | None | Unset
        if isinstance(self.exists, Unset):
            exists = UNSET
        else:
            exists = self.exists

        external: dict[str, Any] | None | Unset
        if isinstance(self.external, Unset):
            external = UNSET
        elif isinstance(self.external, TermSchemaExternalType0):
            external = self.external.to_dict()
        else:
            external = self.external

        missing: bool | None | Unset
        if isinstance(self.missing, Unset):
            missing = UNSET
        else:
            missing = self.missing

        range_: dict[str, Any] | None | Unset
        if isinstance(self.range_, Unset):
            range_ = UNSET
        elif isinstance(self.range_, RangeFilterSchema):
            range_ = self.range_.to_dict()
        else:
            range_ = self.range_

        value = self.value

        value_in: list[str] | None | Unset
        if isinstance(self.value_in, Unset):
            value_in = UNSET
        elif isinstance(self.value_in, list):
            value_in = self.value_in

        else:
            value_in = self.value_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if exists is not UNSET:
            field_dict["exists"] = exists
        if external is not UNSET:
            field_dict["external"] = external
        if missing is not UNSET:
            field_dict["missing"] = missing
        if range_ is not UNSET:
            field_dict["range"] = range_
        if value is not UNSET:
            field_dict["value"] = value
        if value_in is not UNSET:
            field_dict["value_in"] = value_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.range_filter_schema import RangeFilterSchema
        from ..models.term_schema_external_type_0 import TermSchemaExternalType0

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_exists(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        exists = _parse_exists(d.pop("exists", UNSET))

        def _parse_external(data: object) -> None | TermSchemaExternalType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                external_type_0 = TermSchemaExternalType0.from_dict(data)

                return external_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TermSchemaExternalType0 | Unset, data)

        external = _parse_external(d.pop("external", UNSET))

        def _parse_missing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        missing = _parse_missing(d.pop("missing", UNSET))

        def _parse_range_(data: object) -> None | RangeFilterSchema | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                range_type_1 = RangeFilterSchema.from_dict(data)

                return range_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RangeFilterSchema | Unset, data)

        range_ = _parse_range_(d.pop("range", UNSET))

        value = d.pop("value", UNSET)

        def _parse_value_in(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_in_type_0 = cast(list[str], data)

                return value_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        value_in = _parse_value_in(d.pop("value_in", UNSET))

        term_schema = cls(
            name=name,
            exists=exists,
            external=external,
            missing=missing,
            range_=range_,
            value=value,
            value_in=value_in,
        )

        term_schema.additional_properties = d
        return term_schema

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
