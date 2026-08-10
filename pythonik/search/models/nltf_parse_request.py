from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nltf_context import NltfContext


T = TypeVar("T", bound="NltfParseRequest")


@_attrs_define
class NltfParseRequest:
    """
    Attributes:
        query (str):
        context (NltfContext | None | Unset):
    """

    query: str
    context: NltfContext | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.nltf_context import NltfContext

        query = self.query

        context: dict[str, Any] | None | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        elif isinstance(self.context, NltfContext):
            context = self.context.to_dict()
        else:
            context = self.context

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
        from ..models.nltf_context import NltfContext

        d = dict(src_dict)
        query = d.pop("query")

        def _parse_context(data: object) -> NltfContext | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_type_1 = NltfContext.from_dict(data)

                return context_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NltfContext | None | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        nltf_parse_request = cls(
            query=query,
            context=context,
        )

        nltf_parse_request.additional_properties = d
        return nltf_parse_request

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
