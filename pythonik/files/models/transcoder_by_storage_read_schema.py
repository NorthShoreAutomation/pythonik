from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transcoder_by_storage_read_schema_settings_type_0 import (
        TranscoderByStorageReadSchemaSettingsType0,
    )
    from ..models.transcoder_by_storage_read_schema_type_type_1 import (
        TranscoderByStorageReadSchemaTypeType1,
    )


T = TypeVar("T", bound="TranscoderByStorageReadSchema")


@_attrs_define
class TranscoderByStorageReadSchema:
    """
    Attributes:
        id (None | Unset | UUID):
        name (None | str | Unset):
        settings (None | TranscoderByStorageReadSchemaSettingsType0 | Unset):
        storage_id (None | Unset | UUID):
        type_ (None | TranscoderByStorageReadSchemaTypeType1 | Unset):
    """

    id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    settings: None | TranscoderByStorageReadSchemaSettingsType0 | Unset = UNSET
    storage_id: None | Unset | UUID = UNSET
    type_: None | TranscoderByStorageReadSchemaTypeType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transcoder_by_storage_read_schema_settings_type_0 import (
            TranscoderByStorageReadSchemaSettingsType0,
        )
        from ..models.transcoder_by_storage_read_schema_type_type_1 import (
            TranscoderByStorageReadSchemaTypeType1,
        )

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        settings: dict[str, Any] | None | Unset
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, TranscoderByStorageReadSchemaSettingsType0):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        storage_id: None | str | Unset
        if isinstance(self.storage_id, Unset):
            storage_id = UNSET
        elif isinstance(self.storage_id, UUID):
            storage_id = str(self.storage_id)
        else:
            storage_id = self.storage_id

        type_: dict[str, Any] | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, TranscoderByStorageReadSchemaTypeType1):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

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
        from ..models.transcoder_by_storage_read_schema_settings_type_0 import (
            TranscoderByStorageReadSchemaSettingsType0,
        )
        from ..models.transcoder_by_storage_read_schema_type_type_1 import (
            TranscoderByStorageReadSchemaTypeType1,
        )

        d = dict(src_dict)

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_settings(
            data: object,
        ) -> None | TranscoderByStorageReadSchemaSettingsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_0 = TranscoderByStorageReadSchemaSettingsType0.from_dict(
                    data
                )

                return settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TranscoderByStorageReadSchemaSettingsType0 | Unset, data)

        settings = _parse_settings(d.pop("settings", UNSET))

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

        def _parse_type_(
            data: object,
        ) -> None | TranscoderByStorageReadSchemaTypeType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_type_1 = TranscoderByStorageReadSchemaTypeType1.from_dict(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TranscoderByStorageReadSchemaTypeType1 | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

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
