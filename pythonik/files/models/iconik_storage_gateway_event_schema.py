from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.iconik_storage_gateway_event_schema_type import (
    IconikStorageGatewayEventSchemaType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iconik_storage_gateway_event_schema_data_type_0 import (
        IconikStorageGatewayEventSchemaDataType0,
    )


T = TypeVar("T", bound="IconikStorageGatewayEventSchema")


@_attrs_define
class IconikStorageGatewayEventSchema:
    """
    Attributes:
        type_ (IconikStorageGatewayEventSchemaType):
        data (IconikStorageGatewayEventSchemaDataType0 | None | Unset):
        date_created (datetime.datetime | None | Unset):
        id (None | Unset | UUID):
    """

    type_: IconikStorageGatewayEventSchemaType
    data: IconikStorageGatewayEventSchemaDataType0 | None | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.iconik_storage_gateway_event_schema_data_type_0 import (
            IconikStorageGatewayEventSchemaDataType0,
        )

        type_ = self.type_.value

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, IconikStorageGatewayEventSchemaDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

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
        from ..models.iconik_storage_gateway_event_schema_data_type_0 import (
            IconikStorageGatewayEventSchemaDataType0,
        )

        d = dict(src_dict)
        type_ = IconikStorageGatewayEventSchemaType(d.pop("type"))

        def _parse_data(
            data: object,
        ) -> IconikStorageGatewayEventSchemaDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = IconikStorageGatewayEventSchemaDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IconikStorageGatewayEventSchemaDataType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

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
