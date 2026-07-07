from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nltf_parse_metadata_schema import NltfParseMetadataSchema
    from ..models.nltf_parse_result import NltfParseResult


T = TypeVar("T", bound="NltfParseResponseSchema")


@_attrs_define
class NltfParseResponseSchema:
    """
    Attributes:
        metadata (NltfParseMetadataSchema | Unset):
        result (NltfParseResult | Unset):
    """

    metadata: NltfParseMetadataSchema | Unset = UNSET
    result: NltfParseResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nltf_parse_metadata_schema import NltfParseMetadataSchema
        from ..models.nltf_parse_result import NltfParseResult

        d = dict(src_dict)
        _metadata = d.pop("metadata", UNSET)
        metadata: NltfParseMetadataSchema | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = NltfParseMetadataSchema.from_dict(_metadata)

        _result = d.pop("result", UNSET)
        result: NltfParseResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = NltfParseResult.from_dict(_result)

        nltf_parse_response_schema = cls(
            metadata=metadata,
            result=result,
        )

        nltf_parse_response_schema.additional_properties = d
        return nltf_parse_response_schema

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
