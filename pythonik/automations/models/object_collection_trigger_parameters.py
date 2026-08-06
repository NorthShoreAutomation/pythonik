from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectCollectionTriggerParameters")


@_attrs_define
class ObjectCollectionTriggerParameters:
    """
    Attributes:
        collection_ids (list[UUID]):
        object_type (str):
        include_subcollections (bool | None | Unset):  Default: False.
    """

    collection_ids: list[UUID]
    object_type: str
    include_subcollections: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_ids = []
        for collection_ids_item_data in self.collection_ids:
            collection_ids_item = str(collection_ids_item_data)
            collection_ids.append(collection_ids_item)

        object_type = self.object_type

        include_subcollections: bool | None | Unset
        if isinstance(self.include_subcollections, Unset):
            include_subcollections = UNSET
        else:
            include_subcollections = self.include_subcollections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_ids": collection_ids,
                "object_type": object_type,
            }
        )
        if include_subcollections is not UNSET:
            field_dict["include_subcollections"] = include_subcollections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection_ids = []
        _collection_ids = d.pop("collection_ids")
        for collection_ids_item_data in _collection_ids:
            collection_ids_item = UUID(collection_ids_item_data)

            collection_ids.append(collection_ids_item)

        object_type = d.pop("object_type")

        def _parse_include_subcollections(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_subcollections = _parse_include_subcollections(
            d.pop("include_subcollections", UNSET)
        )

        object_collection_trigger_parameters = cls(
            collection_ids=collection_ids,
            object_type=object_type,
            include_subcollections=include_subcollections,
        )

        object_collection_trigger_parameters.additional_properties = d
        return object_collection_trigger_parameters

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
