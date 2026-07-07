from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.range_filter_schema import RangeFilterSchema
    from ..models.term_schema_external import TermSchemaExternal


T = TypeVar("T", bound="TermSchema")


@_attrs_define
class TermSchema:
    """
    Attributes:
        name (str):
        exists (bool | Unset):
        external (TermSchemaExternal | Unset):
        missing (bool | Unset):
        range_ (RangeFilterSchema | Unset):
        value (Any | Unset):
        value_in (list[str] | Unset):
    """

    name: str
    exists: bool | Unset = UNSET
    external: TermSchemaExternal | Unset = UNSET
    missing: bool | Unset = UNSET
    range_: RangeFilterSchema | Unset = UNSET
    value: Any | Unset = UNSET
    value_in: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        exists = self.exists

        external: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external, Unset):
            external = self.external.to_dict()

        missing = self.missing

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        value = self.value

        value_in: list[str] | Unset = UNSET
        if not isinstance(self.value_in, Unset):
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
        from ..models.term_schema_external import TermSchemaExternal

        d = dict(src_dict)
        name = d.pop("name")

        exists = d.pop("exists", UNSET)

        _external = d.pop("external", UNSET)
        external: TermSchemaExternal | Unset
        if isinstance(_external, Unset):
            external = UNSET
        else:
            external = TermSchemaExternal.from_dict(_external)

        missing = d.pop("missing", UNSET)

        _range_ = d.pop("range", UNSET)
        range_: RangeFilterSchema | Unset
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = RangeFilterSchema.from_dict(_range_)

        value = d.pop("value", UNSET)

        value_in = cast(list[str], d.pop("value_in", UNSET))

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
