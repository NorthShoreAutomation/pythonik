from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.match_assessment_basis import MatchAssessmentBasis
from ..models.match_assessment_quality import MatchAssessmentQuality
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchAssessment")


@_attrs_define
class MatchAssessment:
    """How a hit was reached — a mechanical fact, not a relevance score.

    Attributes:
        quality (MatchAssessmentQuality):
        basis (MatchAssessmentBasis | None | Unset):
        round_index (int | None | Unset):  Default: 0.
    """

    quality: MatchAssessmentQuality
    basis: MatchAssessmentBasis | None | Unset = UNSET
    round_index: int | None | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quality = self.quality.value

        basis: None | str | Unset
        if isinstance(self.basis, Unset):
            basis = UNSET
        elif isinstance(self.basis, MatchAssessmentBasis):
            basis = self.basis.value
        else:
            basis = self.basis

        round_index: int | None | Unset
        if isinstance(self.round_index, Unset):
            round_index = UNSET
        else:
            round_index = self.round_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quality": quality,
            }
        )
        if basis is not UNSET:
            field_dict["basis"] = basis
        if round_index is not UNSET:
            field_dict["round_index"] = round_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quality = MatchAssessmentQuality(d.pop("quality"))

        def _parse_basis(data: object) -> MatchAssessmentBasis | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                basis_type_1 = MatchAssessmentBasis(data)

                return basis_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MatchAssessmentBasis | None | Unset, data)

        basis = _parse_basis(d.pop("basis", UNSET))

        def _parse_round_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        round_index = _parse_round_index(d.pop("round_index", UNSET))

        match_assessment = cls(
            quality=quality,
            basis=basis,
            round_index=round_index,
        )

        match_assessment.additional_properties = d
        return match_assessment

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
