from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.modality import Modality
from ..models.ranking_unit import RankingUnit
from ..models.result_order import ResultOrder
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_filter_output import ResponseFilterOutput
    from ..models.response_scoring import ResponseScoring
    from ..models.response_source import ResponseSource


T = TypeVar("T", bound="ResponseFilters")


@_attrs_define
class ResponseFilters:
    """The whole query behind these results, in a form a client can edit and
    send back whole as the request's ``replay`` to chain a follow-up or next page.

    The compiled plan (rounds, tiers, weights) is deliberately not exposed; a
    multi-round answer reports the last round and refuses pagination.

    Three lists, not a partition (a field may appear in two):

    - ``applied`` -- what built the answering query; each entry's ``role`` says
      whether it excluded or only ranked;
    - ``relaxed`` -- restrictions an earlier round enforced and found too
      narrow. Re-sending one narrows the search back down;
    - ``rejected`` -- could not be honoured (unknown field, off the public
      surface). Re-sending one changes nothing.

    E.g. a facet a tier demoted to a boost is in ``applied`` as ``SCORING`` and
    in ``relaxed``; likewise ``relaxed`` may carry ``ceremonoy`` while
    ``applied`` carries ``ceremonoy~1``. Entries outside ``applied`` carry a
    ``reason`` and no ``role``. Invariant: a filter not honoured is never
    reported as applied.

    ``ranking_unit`` and ``order`` are part of the replayed query: they fix the
    ranking grain and the sort the cursor walks. ``exact_text`` / ``meaning_led``
    are replayed so a later page grades its hits as the first did.

        Attributes:
            applied (list[ResponseFilterOutput] | None | Unset):
            exact_text (bool | None | Unset):  Default: True.
            meaning_led (bool | None | Unset):  Default: False.
            modalities (list[Modality] | None | Unset):
            order (None | ResultOrder | Unset):
            query (None | str | Unset):
            ranking_unit (None | RankingUnit | Unset):
            rejected (list[ResponseFilterOutput] | None | Unset):
            relaxed (list[ResponseFilterOutput] | None | Unset):
            result_unit (None | RankingUnit | Unset):
            scoring (None | ResponseScoring | Unset):
            sources (list[ResponseSource] | None | Unset):
            version (int | None | Unset):  Default: 1.
    """

    applied: list[ResponseFilterOutput] | None | Unset = UNSET
    exact_text: bool | None | Unset = True
    meaning_led: bool | None | Unset = False
    modalities: list[Modality] | None | Unset = UNSET
    order: None | ResultOrder | Unset = UNSET
    query: None | str | Unset = UNSET
    ranking_unit: None | RankingUnit | Unset = UNSET
    rejected: list[ResponseFilterOutput] | None | Unset = UNSET
    relaxed: list[ResponseFilterOutput] | None | Unset = UNSET
    result_unit: None | RankingUnit | Unset = UNSET
    scoring: None | ResponseScoring | Unset = UNSET
    sources: list[ResponseSource] | None | Unset = UNSET
    version: int | None | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.response_scoring import ResponseScoring

        applied: list[dict[str, Any]] | None | Unset
        if isinstance(self.applied, Unset):
            applied = UNSET
        elif isinstance(self.applied, list):
            applied = []
            for applied_type_0_item_data in self.applied:
                applied_type_0_item = applied_type_0_item_data.to_dict()
                applied.append(applied_type_0_item)

        else:
            applied = self.applied

        exact_text: bool | None | Unset
        if isinstance(self.exact_text, Unset):
            exact_text = UNSET
        else:
            exact_text = self.exact_text

        meaning_led: bool | None | Unset
        if isinstance(self.meaning_led, Unset):
            meaning_led = UNSET
        else:
            meaning_led = self.meaning_led

        modalities: list[str] | None | Unset
        if isinstance(self.modalities, Unset):
            modalities = UNSET
        elif isinstance(self.modalities, list):
            modalities = []
            for modalities_type_0_item_data in self.modalities:
                modalities_type_0_item = modalities_type_0_item_data.value
                modalities.append(modalities_type_0_item)

        else:
            modalities = self.modalities

        order: None | str | Unset
        if isinstance(self.order, Unset):
            order = UNSET
        elif isinstance(self.order, ResultOrder):
            order = self.order.value
        else:
            order = self.order

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        ranking_unit: None | str | Unset
        if isinstance(self.ranking_unit, Unset):
            ranking_unit = UNSET
        elif isinstance(self.ranking_unit, RankingUnit):
            ranking_unit = self.ranking_unit.value
        else:
            ranking_unit = self.ranking_unit

        rejected: list[dict[str, Any]] | None | Unset
        if isinstance(self.rejected, Unset):
            rejected = UNSET
        elif isinstance(self.rejected, list):
            rejected = []
            for rejected_type_0_item_data in self.rejected:
                rejected_type_0_item = rejected_type_0_item_data.to_dict()
                rejected.append(rejected_type_0_item)

        else:
            rejected = self.rejected

        relaxed: list[dict[str, Any]] | None | Unset
        if isinstance(self.relaxed, Unset):
            relaxed = UNSET
        elif isinstance(self.relaxed, list):
            relaxed = []
            for relaxed_type_0_item_data in self.relaxed:
                relaxed_type_0_item = relaxed_type_0_item_data.to_dict()
                relaxed.append(relaxed_type_0_item)

        else:
            relaxed = self.relaxed

        result_unit: None | str | Unset
        if isinstance(self.result_unit, Unset):
            result_unit = UNSET
        elif isinstance(self.result_unit, RankingUnit):
            result_unit = self.result_unit.value
        else:
            result_unit = self.result_unit

        scoring: dict[str, Any] | None | Unset
        if isinstance(self.scoring, Unset):
            scoring = UNSET
        elif isinstance(self.scoring, ResponseScoring):
            scoring = self.scoring.to_dict()
        else:
            scoring = self.scoring

        sources: list[dict[str, Any]] | None | Unset
        if isinstance(self.sources, Unset):
            sources = UNSET
        elif isinstance(self.sources, list):
            sources = []
            for sources_type_0_item_data in self.sources:
                sources_type_0_item = sources_type_0_item_data.to_dict()
                sources.append(sources_type_0_item)

        else:
            sources = self.sources

        version: int | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applied is not UNSET:
            field_dict["applied"] = applied
        if exact_text is not UNSET:
            field_dict["exact_text"] = exact_text
        if meaning_led is not UNSET:
            field_dict["meaning_led"] = meaning_led
        if modalities is not UNSET:
            field_dict["modalities"] = modalities
        if order is not UNSET:
            field_dict["order"] = order
        if query is not UNSET:
            field_dict["query"] = query
        if ranking_unit is not UNSET:
            field_dict["ranking_unit"] = ranking_unit
        if rejected is not UNSET:
            field_dict["rejected"] = rejected
        if relaxed is not UNSET:
            field_dict["relaxed"] = relaxed
        if result_unit is not UNSET:
            field_dict["result_unit"] = result_unit
        if scoring is not UNSET:
            field_dict["scoring"] = scoring
        if sources is not UNSET:
            field_dict["sources"] = sources
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_filter_output import ResponseFilterOutput
        from ..models.response_scoring import ResponseScoring
        from ..models.response_source import ResponseSource

        d = dict(src_dict)

        def _parse_applied(data: object) -> list[ResponseFilterOutput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                applied_type_0 = []
                _applied_type_0 = data
                for applied_type_0_item_data in _applied_type_0:
                    applied_type_0_item = ResponseFilterOutput.from_dict(
                        applied_type_0_item_data
                    )

                    applied_type_0.append(applied_type_0_item)

                return applied_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ResponseFilterOutput] | None | Unset, data)

        applied = _parse_applied(d.pop("applied", UNSET))

        def _parse_exact_text(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        exact_text = _parse_exact_text(d.pop("exact_text", UNSET))

        def _parse_meaning_led(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        meaning_led = _parse_meaning_led(d.pop("meaning_led", UNSET))

        def _parse_modalities(data: object) -> list[Modality] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                modalities_type_0 = []
                _modalities_type_0 = data
                for modalities_type_0_item_data in _modalities_type_0:
                    modalities_type_0_item = Modality(modalities_type_0_item_data)

                    modalities_type_0.append(modalities_type_0_item)

                return modalities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Modality] | None | Unset, data)

        modalities = _parse_modalities(d.pop("modalities", UNSET))

        def _parse_order(data: object) -> None | ResultOrder | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_type_1 = ResultOrder(data)

                return order_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResultOrder | Unset, data)

        order = _parse_order(d.pop("order", UNSET))

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_ranking_unit(data: object) -> None | RankingUnit | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ranking_unit_type_1 = RankingUnit(data)

                return ranking_unit_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RankingUnit | Unset, data)

        ranking_unit = _parse_ranking_unit(d.pop("ranking_unit", UNSET))

        def _parse_rejected(data: object) -> list[ResponseFilterOutput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rejected_type_0 = []
                _rejected_type_0 = data
                for rejected_type_0_item_data in _rejected_type_0:
                    rejected_type_0_item = ResponseFilterOutput.from_dict(
                        rejected_type_0_item_data
                    )

                    rejected_type_0.append(rejected_type_0_item)

                return rejected_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ResponseFilterOutput] | None | Unset, data)

        rejected = _parse_rejected(d.pop("rejected", UNSET))

        def _parse_relaxed(data: object) -> list[ResponseFilterOutput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                relaxed_type_0 = []
                _relaxed_type_0 = data
                for relaxed_type_0_item_data in _relaxed_type_0:
                    relaxed_type_0_item = ResponseFilterOutput.from_dict(
                        relaxed_type_0_item_data
                    )

                    relaxed_type_0.append(relaxed_type_0_item)

                return relaxed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ResponseFilterOutput] | None | Unset, data)

        relaxed = _parse_relaxed(d.pop("relaxed", UNSET))

        def _parse_result_unit(data: object) -> None | RankingUnit | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                result_unit_type_1 = RankingUnit(data)

                return result_unit_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RankingUnit | Unset, data)

        result_unit = _parse_result_unit(d.pop("result_unit", UNSET))

        def _parse_scoring(data: object) -> None | ResponseScoring | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scoring_type_1 = ResponseScoring.from_dict(data)

                return scoring_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResponseScoring | Unset, data)

        scoring = _parse_scoring(d.pop("scoring", UNSET))

        def _parse_sources(data: object) -> list[ResponseSource] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_type_0 = []
                _sources_type_0 = data
                for sources_type_0_item_data in _sources_type_0:
                    sources_type_0_item = ResponseSource.from_dict(
                        sources_type_0_item_data
                    )

                    sources_type_0.append(sources_type_0_item)

                return sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ResponseSource] | None | Unset, data)

        sources = _parse_sources(d.pop("sources", UNSET))

        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        response_filters = cls(
            applied=applied,
            exact_text=exact_text,
            meaning_led=meaning_led,
            modalities=modalities,
            order=order,
            query=query,
            ranking_unit=ranking_unit,
            rejected=rejected,
            relaxed=relaxed,
            result_unit=result_unit,
            scoring=scoring,
            sources=sources,
            version=version,
        )

        response_filters.additional_properties = d
        return response_filters

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
