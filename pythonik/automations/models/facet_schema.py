from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bucket_schema import BucketSchema


T = TypeVar("T", bound="FacetSchema")


@_attrs_define
class FacetSchema:
    """
    Attributes:
        buckets (list[BucketSchema] | Unset):
        doc_count_error_upper_bound (int | Unset):
        sum_other_doc_count (int | Unset):
    """

    buckets: list[BucketSchema] | Unset = UNSET
    doc_count_error_upper_bound: int | Unset = UNSET
    sum_other_doc_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buckets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for buckets_item_data in self.buckets:
                buckets_item = buckets_item_data.to_dict()
                buckets.append(buckets_item)

        doc_count_error_upper_bound = self.doc_count_error_upper_bound

        sum_other_doc_count = self.sum_other_doc_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if doc_count_error_upper_bound is not UNSET:
            field_dict["doc_count_error_upper_bound"] = doc_count_error_upper_bound
        if sum_other_doc_count is not UNSET:
            field_dict["sum_other_doc_count"] = sum_other_doc_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bucket_schema import BucketSchema

        d = dict(src_dict)
        _buckets = d.pop("buckets", UNSET)
        buckets: list[BucketSchema] | Unset = UNSET
        if _buckets is not UNSET:
            buckets = []
            for buckets_item_data in _buckets:
                buckets_item = BucketSchema.from_dict(buckets_item_data)

                buckets.append(buckets_item)

        doc_count_error_upper_bound = d.pop("doc_count_error_upper_bound", UNSET)

        sum_other_doc_count = d.pop("sum_other_doc_count", UNSET)

        facet_schema = cls(
            buckets=buckets,
            doc_count_error_upper_bound=doc_count_error_upper_bound,
            sum_other_doc_count=sum_other_doc_count,
        )

        facet_schema.additional_properties = d
        return facet_schema

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
