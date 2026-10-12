from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.evidence import Evidence
    from ..models.match_assessment import MatchAssessment


T = TypeVar("T", bound="NaturalSearchMoment")


@_attrs_define
class NaturalSearchMoment:
    """A matched moment standing as a result of its own.

    What `objects` holds when `result_unit` is `segment`: the search ranked
    moments, so each result *is* a moment rather than an asset that contains
    some. The asset it belongs to is named by `asset_id` and its document is in
    the response's `assets` map — several moments commonly share one asset, so
    repeating a whole document per moment would be most of the payload.

        Attributes:
            asset_id (str): The asset this moment is part of; its key in `assets`.
            id (str):
            end_s (float | None | Unset):
            evidence (list[Evidence] | None | Unset): Why this moment matched: every account, from every source that found
                it. Empty when nothing matched textually — see `match`.
            match (MatchAssessment | None | Unset): How this hit was retrieved, not how relevant it is: `quality` is `exact`
                when the query as typed matched, `related` when the query asked for what a result shows and it was matched by
                stand-in words, `approximate` when only a recovery round matched (fuzzed terms, a broadened phrase), and
                `filters_only` when no text matched and the filters alone selected it. `basis` names the evidence behind that
                verdict — `retrieval` today.
            score (float | None | Unset):  Default: 0.0.
            start_s (float | None | Unset):
            thumbnail_s (float | None | Unset):
    """

    asset_id: str
    id: str
    end_s: float | None | Unset = UNSET
    evidence: list[Evidence] | None | Unset = UNSET
    match: MatchAssessment | None | Unset = UNSET
    score: float | None | Unset = 0.0
    start_s: float | None | Unset = UNSET
    thumbnail_s: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.match_assessment import MatchAssessment

        asset_id = self.asset_id

        id = self.id

        end_s: float | None | Unset
        if isinstance(self.end_s, Unset):
            end_s = UNSET
        else:
            end_s = self.end_s

        evidence: list[dict[str, Any]] | None | Unset
        if isinstance(self.evidence, Unset):
            evidence = UNSET
        elif isinstance(self.evidence, list):
            evidence = []
            for evidence_type_0_item_data in self.evidence:
                evidence_type_0_item = evidence_type_0_item_data.to_dict()
                evidence.append(evidence_type_0_item)

        else:
            evidence = self.evidence

        match: dict[str, Any] | None | Unset
        if isinstance(self.match, Unset):
            match = UNSET
        elif isinstance(self.match, MatchAssessment):
            match = self.match.to_dict()
        else:
            match = self.match

        score: float | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        start_s: float | None | Unset
        if isinstance(self.start_s, Unset):
            start_s = UNSET
        else:
            start_s = self.start_s

        thumbnail_s: float | None | Unset
        if isinstance(self.thumbnail_s, Unset):
            thumbnail_s = UNSET
        else:
            thumbnail_s = self.thumbnail_s

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
                "id": id,
            }
        )
        if end_s is not UNSET:
            field_dict["end_s"] = end_s
        if evidence is not UNSET:
            field_dict["evidence"] = evidence
        if match is not UNSET:
            field_dict["match"] = match
        if score is not UNSET:
            field_dict["score"] = score
        if start_s is not UNSET:
            field_dict["start_s"] = start_s
        if thumbnail_s is not UNSET:
            field_dict["thumbnail_s"] = thumbnail_s

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evidence import Evidence
        from ..models.match_assessment import MatchAssessment

        d = dict(src_dict)
        asset_id = d.pop("asset_id")

        id = d.pop("id")

        def _parse_end_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        end_s = _parse_end_s(d.pop("end_s", UNSET))

        def _parse_evidence(data: object) -> list[Evidence] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                evidence_type_0 = []
                _evidence_type_0 = data
                for evidence_type_0_item_data in _evidence_type_0:
                    evidence_type_0_item = Evidence.from_dict(evidence_type_0_item_data)

                    evidence_type_0.append(evidence_type_0_item)

                return evidence_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Evidence] | None | Unset, data)

        evidence = _parse_evidence(d.pop("evidence", UNSET))

        def _parse_match(data: object) -> MatchAssessment | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                match_type_1 = MatchAssessment.from_dict(data)

                return match_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MatchAssessment | None | Unset, data)

        match = _parse_match(d.pop("match", UNSET))

        def _parse_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))

        def _parse_start_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        start_s = _parse_start_s(d.pop("start_s", UNSET))

        def _parse_thumbnail_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        thumbnail_s = _parse_thumbnail_s(d.pop("thumbnail_s", UNSET))

        natural_search_moment = cls(
            asset_id=asset_id,
            id=id,
            end_s=end_s,
            evidence=evidence,
            match=match,
            score=score,
            start_s=start_s,
            thumbnail_s=thumbnail_s,
        )

        natural_search_moment.additional_properties = d
        return natural_search_moment

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
