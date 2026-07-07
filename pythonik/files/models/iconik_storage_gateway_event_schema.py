from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.iconik_storage_gateway_event_schema_type import (
    IconikStorageGatewayEventSchemaType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iconik_storage_gateway_event_schema_data import (
        IconikStorageGatewayEventSchemaData,
    )


T = TypeVar("T", bound="IconikStorageGatewayEventSchema")


@_attrs_define
class IconikStorageGatewayEventSchema:
    """
    Attributes:
        type_ (IconikStorageGatewayEventSchemaType):
        data (IconikStorageGatewayEventSchemaData | Unset):
        date_created (datetime.datetime | Unset):
        id (UUID | Unset):
    """

    type_: IconikStorageGatewayEventSchemaType
    data: IconikStorageGatewayEventSchemaData | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iconik_storage_gateway_event_schema_data import (
            IconikStorageGatewayEventSchemaData,
        )

        d = dict(src_dict)
        type_ = IconikStorageGatewayEventSchemaType(d.pop("type"))

        _data = d.pop("data", UNSET)
        data: IconikStorageGatewayEventSchemaData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = IconikStorageGatewayEventSchemaData.from_dict(_data)

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        iconik_storage_gateway_event_schema = cls(
            type_=type_,
            data=data,
            date_created=date_created,
            id=id,
        )

        iconik_storage_gateway_event_schema.additional_properties = d
        return iconik_storage_gateway_event_schema

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
