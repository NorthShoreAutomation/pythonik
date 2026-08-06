from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_endpoint_schema_headers_type_0 import (
        OutputEndpointSchemaHeadersType0,
    )


T = TypeVar("T", bound="OutputEndpointSchema")


@_attrs_define
class OutputEndpointSchema:
    """
    Attributes:
        key (str):
        headers (None | OutputEndpointSchemaHeadersType0 | Unset):
    """

    key: str
    headers: None | OutputEndpointSchemaHeadersType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.output_endpoint_schema_headers_type_0 import (
            OutputEndpointSchemaHeadersType0,
        )

        key = self.key

        headers: dict[str, Any] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, OutputEndpointSchemaHeadersType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

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
        from ..models.output_endpoint_schema_headers_type_0 import (
            OutputEndpointSchemaHeadersType0,
        )

        d = dict(src_dict)
        key = d.pop("key")

        def _parse_headers(
            data: object,
        ) -> None | OutputEndpointSchemaHeadersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headers_type_0 = OutputEndpointSchemaHeadersType0.from_dict(data)

                return headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OutputEndpointSchemaHeadersType0 | Unset, data)

        headers = _parse_headers(d.pop("headers", UNSET))

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
