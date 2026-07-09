from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        metadata (NltfParseMetadataSchema | None | Unset):
        result (NltfParseResult | None | Unset):
    """

    metadata: NltfParseMetadataSchema | None | Unset = UNSET
    result: NltfParseResult | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.nltf_parse_metadata_schema import NltfParseMetadataSchema
        from ..models.nltf_parse_result import NltfParseResult

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, NltfParseMetadataSchema):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        result: dict[str, Any] | None | Unset
        if isinstance(self.result, Unset):
            result = UNSET
        elif isinstance(self.result, NltfParseResult):
            result = self.result.to_dict()
        else:
            result = self.result

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

        def _parse_metadata(data: object) -> NltfParseMetadataSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_1 = NltfParseMetadataSchema.from_dict(data)

                return metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NltfParseMetadataSchema | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_result(data: object) -> NltfParseResult | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_1 = NltfParseResult.from_dict(data)

                return result_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NltfParseResult | None | Unset, data)

        result = _parse_result(d.pop("result", UNSET))

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
