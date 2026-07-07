from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_endpoint_schema_headers import OutputEndpointSchemaHeaders


T = TypeVar("T", bound="OutputEndpointSchema")


@_attrs_define
class OutputEndpointSchema:
    """
    Attributes:
        key (str):
        headers (OutputEndpointSchemaHeaders | Unset):
    """

    key: str
    headers: OutputEndpointSchemaHeaders | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_endpoint_schema_headers import OutputEndpointSchemaHeaders

        d = dict(src_dict)
        key = d.pop("key")

        _headers = d.pop("headers", UNSET)
        headers: OutputEndpointSchemaHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = OutputEndpointSchemaHeaders.from_dict(_headers)

        output_endpoint_schema = cls(
            key=key,
            headers=headers,
        )

        output_endpoint_schema.additional_properties = d
        return output_endpoint_schema

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
