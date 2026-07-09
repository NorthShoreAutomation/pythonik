from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
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
        id (None | Unset | UUID):
        storages (list[StorageReadSchema] | None | Unset):
    """

    name: str
    settings: TranscoderReadSchemaSettings
    type_: TranscoderReadSchemaType
    id: None | Unset | UUID = UNSET
    storages: list[StorageReadSchema] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        settings = self.settings.to_dict()

        type_ = self.type_.value

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        storages: list[dict[str, Any]] | None | Unset
        if isinstance(self.storages, Unset):
            storages = UNSET
        elif isinstance(self.storages, list):
            storages = []
            for storages_type_0_item_data in self.storages:
                storages_type_0_item = storages_type_0_item_data.to_dict()
                storages.append(storages_type_0_item)

        else:
            storages = self.storages

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

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_storages(data: object) -> list[StorageReadSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                storages_type_0 = []
                _storages_type_0 = data
                for storages_type_0_item_data in _storages_type_0:
                    storages_type_0_item = StorageReadSchema.from_dict(
                        storages_type_0_item_data
                    )

                    storages_type_0.append(storages_type_0_item)

                return storages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StorageReadSchema] | None | Unset, data)

        storages = _parse_storages(d.pop("storages", UNSET))

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
