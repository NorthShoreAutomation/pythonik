from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scoring_method import ScoringMethod


T = TypeVar("T", bound="ResponseScoring")


@_attrs_define
class ResponseScoring:
    """How these results were ranked: the fusion / rerank methods that ran.

    Attributes:
        methods (list[ScoringMethod] | None | Unset):
    """

    methods: list[ScoringMethod] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        methods: list[dict[str, Any]] | None | Unset
        if isinstance(self.methods, Unset):
            methods = UNSET
        elif isinstance(self.methods, list):
            methods = []
            for methods_type_0_item_data in self.methods:
                methods_type_0_item = methods_type_0_item_data.to_dict()
                methods.append(methods_type_0_item)

        else:
            methods = self.methods

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if methods is not UNSET:
            field_dict["methods"] = methods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scoring_method import ScoringMethod

        d = dict(src_dict)

        def _parse_methods(data: object) -> list[ScoringMethod] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                methods_type_0 = []
                _methods_type_0 = data
                for methods_type_0_item_data in _methods_type_0:
                    methods_type_0_item = ScoringMethod.from_dict(
                        methods_type_0_item_data
                    )

                    methods_type_0.append(methods_type_0_item)

                return methods_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ScoringMethod] | None | Unset, data)

        methods = _parse_methods(d.pop("methods", UNSET))

        response_scoring = cls(
            methods=methods,
        )

        response_scoring.additional_properties = d
        return response_scoring

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
