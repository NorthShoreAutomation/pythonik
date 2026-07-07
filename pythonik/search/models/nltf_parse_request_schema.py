from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nltf_context_schema import NltfContextSchema


T = TypeVar("T", bound="NltfParseRequestSchema")


@_attrs_define
class NltfParseRequestSchema:
    """
    Attributes:
        query (str):
        context (NltfContextSchema | Unset):
    """

    query: str
    context: NltfContextSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nltf_context_schema import NltfContextSchema

        d = dict(src_dict)
        query = d.pop("query")

        _context = d.pop("context", UNSET)
        context: NltfContextSchema | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = NltfContextSchema.from_dict(_context)

        nltf_parse_request_schema = cls(
            query=query,
            context=context,
        )

        nltf_parse_request_schema.additional_properties = d
        return nltf_parse_request_schema

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
