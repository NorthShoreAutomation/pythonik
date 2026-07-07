from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.endpoint_schema_data import EndpointSchemaData
    from ..models.endpoint_schema_headers import EndpointSchemaHeaders


T = TypeVar("T", bound="EndpointSchema")


@_attrs_define
class EndpointSchema:
    """
    Attributes:
        url (str):
        data (EndpointSchemaData | Unset):
        headers (EndpointSchemaHeaders | Unset):
        method (str | Unset):
        storage_method (str | Unset):
        type_ (str | Unset):
    """

    url: str
    data: EndpointSchemaData | Unset = UNSET
    headers: EndpointSchemaHeaders | Unset = UNSET
    method: str | Unset = UNSET
    storage_method: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        method = self.method

        storage_method = self.storage_method

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
        if headers is not UNSET:
            field_dict["headers"] = headers
        if method is not UNSET:
            field_dict["method"] = method
        if storage_method is not UNSET:
            field_dict["storage_method"] = storage_method
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.endpoint_schema_data import EndpointSchemaData
        from ..models.endpoint_schema_headers import EndpointSchemaHeaders

        d = dict(src_dict)
        url = d.pop("url")

        _data = d.pop("data", UNSET)
        data: EndpointSchemaData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = EndpointSchemaData.from_dict(_data)

        _headers = d.pop("headers", UNSET)
        headers: EndpointSchemaHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = EndpointSchemaHeaders.from_dict(_headers)

        method = d.pop("method", UNSET)

        storage_method = d.pop("storage_method", UNSET)

        type_ = d.pop("type", UNSET)

        endpoint_schema = cls(
            url=url,
            data=data,
            headers=headers,
            method=method,
            storage_method=storage_method,
            type_=type_,
        )

        endpoint_schema.additional_properties = d
        return endpoint_schema

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
