from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddToCollectionActionParameters")


@_attrs_define
class AddToCollectionActionParameters:
    """
    Attributes:
        collection_id (UUID):
        index_immediately (bool | None | Unset):
    """

    collection_id: UUID
    index_immediately: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_id = str(self.collection_id)

        index_immediately: bool | None | Unset
        if isinstance(self.index_immediately, Unset):
            index_immediately = UNSET
        else:
            index_immediately = self.index_immediately

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_id": collection_id,
            }
        )
        if index_immediately is not UNSET:
            field_dict["index_immediately"] = index_immediately

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection_id = UUID(d.pop("collection_id"))

        def _parse_index_immediately(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        index_immediately = _parse_index_immediately(d.pop("index_immediately", UNSET))

        add_to_collection_action_parameters = cls(
            collection_id=collection_id,
            index_immediately=index_immediately,
        )

        add_to_collection_action_parameters.additional_properties = d
        return add_to_collection_action_parameters

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
