from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transcoder_by_storage_read_schema_type import (
    TranscoderByStorageReadSchemaType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transcoder_by_storage_read_schema_settings import (
        TranscoderByStorageReadSchemaSettings,
    )


T = TypeVar("T", bound="TranscoderByStorageReadSchema")


@_attrs_define
class TranscoderByStorageReadSchema:
    """
    Attributes:
        id (UUID | Unset):
        name (str | Unset):
        settings (TranscoderByStorageReadSchemaSettings | Unset):
        storage_id (UUID | Unset):
        type_ (TranscoderByStorageReadSchemaType | Unset):
    """

    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    settings: TranscoderByStorageReadSchemaSettings | Unset = UNSET
    storage_id: UUID | Unset = UNSET
    type_: TranscoderByStorageReadSchemaType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        storage_id: str | Unset = UNSET
        if not isinstance(self.storage_id, Unset):
            storage_id = str(self.storage_id)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if settings is not UNSET:
            field_dict["settings"] = settings
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transcoder_by_storage_read_schema_settings import (
            TranscoderByStorageReadSchemaSettings,
        )

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: TranscoderByStorageReadSchemaSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = TranscoderByStorageReadSchemaSettings.from_dict(_settings)

        _storage_id = d.pop("storage_id", UNSET)
        storage_id: UUID | Unset
        if isinstance(_storage_id, Unset):
            storage_id = UNSET
        else:
            storage_id = UUID(_storage_id)

        _type_ = d.pop("type", UNSET)
        type_: TranscoderByStorageReadSchemaType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TranscoderByStorageReadSchemaType(_type_)

        transcoder_by_storage_read_schema = cls(
            id=id,
            name=name,
            settings=settings,
            storage_id=storage_id,
            type_=type_,
        )

        transcoder_by_storage_read_schema.additional_properties = d
        return transcoder_by_storage_read_schema

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
