from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceContext")


@_attrs_define
class SourceContext:
    """
    Attributes:
        external_id (None | str | Unset): external storage path / id
        root_collection_path (None | str | Unset): root collection path
        root_collection_storage_id (None | Unset | UUID): root collection storage ID
        storage_id (None | Unset | UUID):
    """

    external_id: None | str | Unset = UNSET
    root_collection_path: None | str | Unset = UNSET
    root_collection_storage_id: None | Unset | UUID = UNSET
    storage_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        root_collection_path: None | str | Unset
        if isinstance(self.root_collection_path, Unset):
            root_collection_path = UNSET
        else:
            root_collection_path = self.root_collection_path

        root_collection_storage_id: None | str | Unset
        if isinstance(self.root_collection_storage_id, Unset):
            root_collection_storage_id = UNSET
        elif isinstance(self.root_collection_storage_id, UUID):
            root_collection_storage_id = str(self.root_collection_storage_id)
        else:
            root_collection_storage_id = self.root_collection_storage_id

        storage_id: None | str | Unset
        if isinstance(self.storage_id, Unset):
            storage_id = UNSET
        elif isinstance(self.storage_id, UUID):
            storage_id = str(self.storage_id)
        else:
            storage_id = self.storage_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if root_collection_path is not UNSET:
            field_dict["root_collection_path"] = root_collection_path
        if root_collection_storage_id is not UNSET:
            field_dict["root_collection_storage_id"] = root_collection_storage_id
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_root_collection_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        root_collection_path = _parse_root_collection_path(
            d.pop("root_collection_path", UNSET)
        )

        def _parse_root_collection_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                root_collection_storage_id_type_0 = UUID(data)

                return root_collection_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        root_collection_storage_id = _parse_root_collection_storage_id(
            d.pop("root_collection_storage_id", UNSET)
        )

        def _parse_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_id_type_0 = UUID(data)

                return storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        storage_id = _parse_storage_id(d.pop("storage_id", UNSET))

        source_context = cls(
            external_id=external_id,
            root_collection_path=root_collection_path,
            root_collection_storage_id=root_collection_storage_id,
            storage_id=storage_id,
        )

        source_context.additional_properties = d
        return source_context

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
