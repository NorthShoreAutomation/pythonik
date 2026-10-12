from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.natural_search_image_similarity import NaturalSearchImageSimilarity
from ..types import UNSET, Unset

T = TypeVar("T", bound="NaturalSearchImage")


@_attrs_define
class NaturalSearchImage:
    """
    Attributes:
        asset_id (UUID):
        similarity (NaturalSearchImageSimilarity | None | Unset):
    """

    asset_id: UUID
    similarity: NaturalSearchImageSimilarity | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = str(self.asset_id)

        similarity: None | str | Unset
        if isinstance(self.similarity, Unset):
            similarity = UNSET
        elif isinstance(self.similarity, NaturalSearchImageSimilarity):
            similarity = self.similarity.value
        else:
            similarity = self.similarity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
            }
        )
        if similarity is not UNSET:
            field_dict["similarity"] = similarity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = UUID(d.pop("asset_id"))

        def _parse_similarity(
            data: object,
        ) -> NaturalSearchImageSimilarity | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                similarity_type_1 = NaturalSearchImageSimilarity(data)

                return similarity_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NaturalSearchImageSimilarity | None | Unset, data)

        similarity = _parse_similarity(d.pop("similarity", UNSET))

        natural_search_image = cls(
            asset_id=asset_id,
            similarity=similarity,
        )

        natural_search_image.additional_properties = d
        return natural_search_image

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
