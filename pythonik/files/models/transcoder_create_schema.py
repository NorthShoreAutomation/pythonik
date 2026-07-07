from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transcoder_create_schema_type import TranscoderCreateSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transcoder_create_schema_settings import (
        TranscoderCreateSchemaSettings,
    )


T = TypeVar("T", bound="TranscoderCreateSchema")


@_attrs_define
class TranscoderCreateSchema:
    """
    Attributes:
        name (str):
        settings (TranscoderCreateSchemaSettings):
        type_ (TranscoderCreateSchemaType):
        id (UUID | Unset):
    """

    name: str
    settings: TranscoderCreateSchemaSettings
    type_: TranscoderCreateSchemaType
    id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        settings = self.settings.to_dict()

        type_ = self.type_.value

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transcoder_create_schema_settings import (
            TranscoderCreateSchemaSettings,
        )

        d = dict(src_dict)
        name = d.pop("name")

        settings = TranscoderCreateSchemaSettings.from_dict(d.pop("settings"))

        type_ = TranscoderCreateSchemaType(d.pop("type"))

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        transcoder_create_schema = cls(
            name=name,
            settings=settings,
            type_=type_,
            id=id,
        )

        transcoder_create_schema.additional_properties = d
        return transcoder_create_schema

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
