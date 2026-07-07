from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transcoder_read_schema_type import TranscoderReadSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_read_schema import StorageReadSchema
    from ..models.transcoder_read_schema_settings import TranscoderReadSchemaSettings


T = TypeVar("T", bound="TranscoderReadSchema")


@_attrs_define
class TranscoderReadSchema:
    """
    Attributes:
        name (str):
        settings (TranscoderReadSchemaSettings):
        type_ (TranscoderReadSchemaType):
        id (UUID | Unset):
        storages (list[StorageReadSchema] | Unset):
    """

    name: str
    settings: TranscoderReadSchemaSettings
    type_: TranscoderReadSchemaType
    id: UUID | Unset = UNSET
    storages: list[StorageReadSchema] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        settings = self.settings.to_dict()

        type_ = self.type_.value

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        storages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.storages, Unset):
            storages = []
            for storages_item_data in self.storages:
                storages_item = storages_item_data.to_dict()
                storages.append(storages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "settings": settings,
                "type": type_,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if storages is not UNSET:
            field_dict["storages"] = storages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_read_schema import StorageReadSchema
        from ..models.transcoder_read_schema_settings import (
            TranscoderReadSchemaSettings,
        )

        d = dict(src_dict)
        name = d.pop("name")

        settings = TranscoderReadSchemaSettings.from_dict(d.pop("settings"))

        type_ = TranscoderReadSchemaType(d.pop("type"))

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _storages = d.pop("storages", UNSET)
        storages: list[StorageReadSchema] | Unset = UNSET
        if _storages is not UNSET:
            storages = []
            for storages_item_data in _storages:
                storages_item = StorageReadSchema.from_dict(storages_item_data)

                storages.append(storages_item)

        transcoder_read_schema = cls(
            name=name,
            settings=settings,
            type_=type_,
            id=id,
            storages=storages,
        )

        transcoder_read_schema.additional_properties = d
        return transcoder_read_schema

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
