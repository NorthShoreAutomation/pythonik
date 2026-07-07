from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_version_lookup_schema import AssetVersionLookupSchema


T = TypeVar("T", bound="GetAssetsVersionsMetadataSchema")


@_attrs_define
class GetAssetsVersionsMetadataSchema:
    """
    Attributes:
        objects (list[AssetVersionLookupSchema]):
        fields (list[str] | None | Unset): Optional list of fields to include in the response. If omitted, all fields
            are returned.
    """

    objects: list[AssetVersionLookupSchema]
    fields: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objects = []
        for objects_item_data in self.objects:
            objects_item = objects_item_data.to_dict()
            objects.append(objects_item)

        fields: list[str] | None | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = self.fields

        else:
            fields = self.fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "objects": objects,
            }
        )
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_version_lookup_schema import AssetVersionLookupSchema

        d = dict(src_dict)
        objects = []
        _objects = d.pop("objects")
        for objects_item_data in _objects:
            objects_item = AssetVersionLookupSchema.from_dict(objects_item_data)

            objects.append(objects_item)

        def _parse_fields(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_0 = cast(list[str], data)

                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        fields = _parse_fields(d.pop("fields", UNSET))

        get_assets_versions_metadata_schema = cls(
            objects=objects,
            fields=fields,
        )

        get_assets_versions_metadata_schema.additional_properties = d
        return get_assets_versions_metadata_schema

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
