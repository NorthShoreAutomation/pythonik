from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionContentOrderingSchema")


@_attrs_define
class CollectionContentOrderingSchema:
    """
    Attributes:
        after_object_id (None | Unset | UUID):
        before_object_id (None | Unset | UUID):
        position (int | None | Unset): Position the member will be moved to. To insert athe the end send -1
    """

    after_object_id: None | Unset | UUID = UNSET
    before_object_id: None | Unset | UUID = UNSET
    position: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after_object_id: None | str | Unset
        if isinstance(self.after_object_id, Unset):
            after_object_id = UNSET
        elif isinstance(self.after_object_id, UUID):
            after_object_id = str(self.after_object_id)
        else:
            after_object_id = self.after_object_id

        before_object_id: None | str | Unset
        if isinstance(self.before_object_id, Unset):
            before_object_id = UNSET
        elif isinstance(self.before_object_id, UUID):
            before_object_id = str(self.before_object_id)
        else:
            before_object_id = self.before_object_id

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after_object_id is not UNSET:
            field_dict["after_object_id"] = after_object_id
        if before_object_id is not UNSET:
            field_dict["before_object_id"] = before_object_id
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_after_object_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                after_object_id_type_0 = UUID(data)

                return after_object_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        after_object_id = _parse_after_object_id(d.pop("after_object_id", UNSET))

        def _parse_before_object_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                before_object_id_type_0 = UUID(data)

                return before_object_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        before_object_id = _parse_before_object_id(d.pop("before_object_id", UNSET))

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        collection_content_ordering_schema = cls(
            after_object_id=after_object_id,
            before_object_id=before_object_id,
            position=position,
        )

        collection_content_ordering_schema.additional_properties = d
        return collection_content_ordering_schema

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
