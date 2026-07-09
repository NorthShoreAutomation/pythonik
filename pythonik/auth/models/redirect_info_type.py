from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.redirect_info_type_headers_type_0 import RedirectInfoTypeHeadersType0


T = TypeVar("T", bound="RedirectInfoType")


@_attrs_define
class RedirectInfoType:
    """
    Attributes:
        headers (None | RedirectInfoTypeHeadersType0 | Unset):
        url (None | str | Unset):
    """

    headers: None | RedirectInfoTypeHeadersType0 | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.redirect_info_type_headers_type_0 import (
            RedirectInfoTypeHeadersType0,
        )

        headers: dict[str, Any] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, RedirectInfoTypeHeadersType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headers is not UNSET:
            field_dict["headers"] = headers
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.redirect_info_type_headers_type_0 import (
            RedirectInfoTypeHeadersType0,
        )

        d = dict(src_dict)

        def _parse_headers(data: object) -> None | RedirectInfoTypeHeadersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headers_type_0 = RedirectInfoTypeHeadersType0.from_dict(data)

                return headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RedirectInfoTypeHeadersType0 | Unset, data)

        headers = _parse_headers(d.pop("headers", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        redirect_info_type = cls(
            headers=headers,
            url=url,
        )

        redirect_info_type.additional_properties = d
        return redirect_info_type

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
