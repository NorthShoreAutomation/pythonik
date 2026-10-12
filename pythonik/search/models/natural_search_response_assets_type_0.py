from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_document import SearchDocument


T = TypeVar("T", bound="NaturalSearchResponseAssetsType0")


@_attrs_define
class NaturalSearchResponseAssetsType0:
    """The documents `objects` refer to but do not contain, keyed by asset id. Empty unless the results are moments. Plain
    documents: the ranking story (`score`, `evidence`, `match`) belongs to the moment that matched, not to the asset it
    happens to sit in.

    """

    additional_properties: dict[str, SearchDocument] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_document import SearchDocument

        d = dict(src_dict)
        natural_search_response_assets_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = SearchDocument.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        natural_search_response_assets_type_0.additional_properties = (
            additional_properties
        )
        return natural_search_response_assets_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> SearchDocument:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: SearchDocument) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
