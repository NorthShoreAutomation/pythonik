from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pagination_refusal import PaginationRefusal
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponsePagination")


@_attrs_define
class ResponsePagination:
    """Whether this answer can be paginated, and where in it we are.

    When ``supported`` is ``False``, :attr:`reason` says why and the answer is a
    single page.

        Attributes:
            page (int | None | Unset):  Default: 1.
            pages (int | None | Unset):  Default: 1.
            per_page (int | None | Unset):  Default: 20.
            reason (None | PaginationRefusal | Unset):
            supported (bool | None | Unset):  Default: False.
            total (int | None | Unset):
    """

    page: int | None | Unset = 1
    pages: int | None | Unset = 1
    per_page: int | None | Unset = 20
    reason: None | PaginationRefusal | Unset = UNSET
    supported: bool | None | Unset = False
    total: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page: int | None | Unset
        if isinstance(self.page, Unset):
            page = UNSET
        else:
            page = self.page

        pages: int | None | Unset
        if isinstance(self.pages, Unset):
            pages = UNSET
        else:
            pages = self.pages

        per_page: int | None | Unset
        if isinstance(self.per_page, Unset):
            per_page = UNSET
        else:
            per_page = self.per_page

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        elif isinstance(self.reason, PaginationRefusal):
            reason = self.reason.value
        else:
            reason = self.reason

        supported: bool | None | Unset
        if isinstance(self.supported, Unset):
            supported = UNSET
        else:
            supported = self.supported

        total: int | None | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if pages is not UNSET:
            field_dict["pages"] = pages
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if reason is not UNSET:
            field_dict["reason"] = reason
        if supported is not UNSET:
            field_dict["supported"] = supported
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page = _parse_page(d.pop("page", UNSET))

        def _parse_pages(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pages = _parse_pages(d.pop("pages", UNSET))

        def _parse_per_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        per_page = _parse_per_page(d.pop("per_page", UNSET))

        def _parse_reason(data: object) -> None | PaginationRefusal | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_1 = PaginationRefusal(data)

                return reason_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginationRefusal | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_supported(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        supported = _parse_supported(d.pop("supported", UNSET))

        def _parse_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total = _parse_total(d.pop("total", UNSET))

        response_pagination = cls(
            page=page,
            pages=pages,
            per_page=per_page,
            reason=reason,
            supported=supported,
            total=total,
        )

        response_pagination.additional_properties = d
        return response_pagination

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
