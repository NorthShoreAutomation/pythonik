from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edge_transcode_endpoint_schema_data_type_0 import (
        EdgeTranscodeEndpointSchemaDataType0,
    )


T = TypeVar("T", bound="EdgeTranscodeEndpointSchema")


@_attrs_define
class EdgeTranscodeEndpointSchema:
    """
    Attributes:
        url (str):
        data (EdgeTranscodeEndpointSchemaDataType0 | None | Unset):
        method (None | str | Unset):
        storage_method (None | str | Unset):
        type_ (None | str | Unset):
    """

    url: str
    data: EdgeTranscodeEndpointSchemaDataType0 | None | Unset = UNSET
    method: None | str | Unset = UNSET
    storage_method: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.edge_transcode_endpoint_schema_data_type_0 import (
            EdgeTranscodeEndpointSchemaDataType0,
        )

        url = self.url

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, EdgeTranscodeEndpointSchemaDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        method: None | str | Unset
        if isinstance(self.method, Unset):
            method = UNSET
        else:
            method = self.method

        storage_method: None | str | Unset
        if isinstance(self.storage_method, Unset):
            storage_method = UNSET
        else:
            storage_method = self.storage_method

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if method is not UNSET:
            field_dict["method"] = method
        if storage_method is not UNSET:
            field_dict["storage_method"] = storage_method
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edge_transcode_endpoint_schema_data_type_0 import (
            EdgeTranscodeEndpointSchemaDataType0,
        )

        d = dict(src_dict)
        url = d.pop("url")

        def _parse_data(
            data: object,
        ) -> EdgeTranscodeEndpointSchemaDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = EdgeTranscodeEndpointSchemaDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EdgeTranscodeEndpointSchemaDataType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        method = _parse_method(d.pop("method", UNSET))

        def _parse_storage_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_method = _parse_storage_method(d.pop("storage_method", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        edge_transcode_endpoint_schema = cls(
            url=url,
            data=data,
            method=method,
            storage_method=storage_method,
            type_=type_,
        )

        edge_transcode_endpoint_schema.additional_properties = d
        return edge_transcode_endpoint_schema

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
