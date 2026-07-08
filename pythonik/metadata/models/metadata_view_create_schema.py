from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_view_field import MetadataViewField


T = TypeVar("T", bound="MetadataViewCreateSchema")


@_attrs_define
class MetadataViewCreateSchema:
    """
    Attributes:
        name (str):
        view_fields (list[MetadataViewField]):
        description (None | str | Unset):
        id (None | Unset | UUID):
        write_access_for_everyone (bool | None | Unset):
    """

    name: str
    view_fields: list[MetadataViewField]
    description: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    write_access_for_everyone: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        view_fields = []
        for view_fields_item_data in self.view_fields:
            view_fields_item = view_fields_item_data.to_dict()
            view_fields.append(view_fields_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        write_access_for_everyone: bool | None | Unset
        if isinstance(self.write_access_for_everyone, Unset):
            write_access_for_everyone = UNSET
        else:
            write_access_for_everyone = self.write_access_for_everyone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "view_fields": view_fields,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if write_access_for_everyone is not UNSET:
            field_dict["write_access_for_everyone"] = write_access_for_everyone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_view_field import MetadataViewField

        d = dict(src_dict)
        name = d.pop("name")

        view_fields = []
        _view_fields = d.pop("view_fields")
        for view_fields_item_data in _view_fields:
            view_fields_item = MetadataViewField.from_dict(view_fields_item_data)

            view_fields.append(view_fields_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_write_access_for_everyone(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        write_access_for_everyone = _parse_write_access_for_everyone(
            d.pop("write_access_for_everyone", UNSET)
        )

        metadata_view_create_schema = cls(
            name=name,
            view_fields=view_fields,
            description=description,
            id=id,
            write_access_for_everyone=write_access_for_everyone,
        )

        metadata_view_create_schema.additional_properties = d
        return metadata_view_create_schema

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
