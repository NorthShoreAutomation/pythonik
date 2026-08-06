from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.saved_search_copy_from_template_schema_metadata_view_map import (
        SavedSearchCopyFromTemplateSchemaMetadataViewMap,
    )


T = TypeVar("T", bound="SavedSearchCopyFromTemplateSchema")


@_attrs_define
class SavedSearchCopyFromTemplateSchema:
    """
    Attributes:
        from_domain (UUID):
        metadata_view_map (SavedSearchCopyFromTemplateSchemaMetadataViewMap):
        to_domain (UUID):
    """

    from_domain: UUID
    metadata_view_map: SavedSearchCopyFromTemplateSchemaMetadataViewMap
    to_domain: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_domain = str(self.from_domain)

        metadata_view_map = self.metadata_view_map.to_dict()

        to_domain = str(self.to_domain)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_domain": from_domain,
                "metadata_view_map": metadata_view_map,
                "to_domain": to_domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.saved_search_copy_from_template_schema_metadata_view_map import (
            SavedSearchCopyFromTemplateSchemaMetadataViewMap,
        )

        d = dict(src_dict)
        from_domain = UUID(d.pop("from_domain"))

        metadata_view_map = SavedSearchCopyFromTemplateSchemaMetadataViewMap.from_dict(
            d.pop("metadata_view_map")
        )

        to_domain = UUID(d.pop("to_domain"))

        saved_search_copy_from_template_schema = cls(
            from_domain=from_domain,
            metadata_view_map=metadata_view_map,
            to_domain=to_domain,
        )

        saved_search_copy_from_template_schema.additional_properties = d
        return saved_search_copy_from_template_schema

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
