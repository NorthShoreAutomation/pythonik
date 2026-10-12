from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.natural_search_replay_order import NaturalSearchReplayOrder
from ..models.natural_search_replay_ranking_unit import NaturalSearchReplayRankingUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_filter_input import ResponseFilterInput


T = TypeVar("T", bound="NaturalSearchReplay")


@_attrs_define
class NaturalSearchReplay:
    """The response `filters` block sent back as-is; only what a replay needs is read.

    Attributes:
        version (int): The block's `version`. One this server no longer replays is a 400.
        applied (list[ResponseFilterInput] | None | Unset): The query to run. Each entry's `role` is honoured, so the
            block as received reproduces the same search; drop an entry to drop that filter.
        exact_text (bool | None | Unset):  Default: True.
        meaning_led (bool | None | Unset):  Default: False.
        order (NaturalSearchReplayOrder | None | Unset):
        ranking_unit (NaturalSearchReplayRankingUnit | None | Unset):
    """

    version: int
    applied: list[ResponseFilterInput] | None | Unset = UNSET
    exact_text: bool | None | Unset = True
    meaning_led: bool | None | Unset = False
    order: NaturalSearchReplayOrder | None | Unset = UNSET
    ranking_unit: NaturalSearchReplayRankingUnit | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

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

        order: None | str | Unset
        if isinstance(self.order, Unset):
            order = UNSET
        elif isinstance(self.order, NaturalSearchReplayOrder):
            order = self.order.value
        else:
            order = self.order

        ranking_unit: None | str | Unset
        if isinstance(self.ranking_unit, Unset):
            ranking_unit = UNSET
        elif isinstance(self.ranking_unit, NaturalSearchReplayRankingUnit):
            ranking_unit = self.ranking_unit.value
        else:
            ranking_unit = self.ranking_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
            }
        )
        if applied is not UNSET:
            field_dict["applied"] = applied
        if exact_text is not UNSET:
            field_dict["exact_text"] = exact_text
        if meaning_led is not UNSET:
            field_dict["meaning_led"] = meaning_led
        if order is not UNSET:
            field_dict["order"] = order
        if ranking_unit is not UNSET:
            field_dict["ranking_unit"] = ranking_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_filter_input import ResponseFilterInput

        d = dict(src_dict)
        version = d.pop("version")

        def _parse_applied(data: object) -> list[ResponseFilterInput] | None | Unset:
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
                    applied_type_0_item = ResponseFilterInput.from_dict(
                        applied_type_0_item_data
                    )

                    applied_type_0.append(applied_type_0_item)

                return applied_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ResponseFilterInput] | None | Unset, data)

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

        def _parse_order(data: object) -> NaturalSearchReplayOrder | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_type_1 = NaturalSearchReplayOrder(data)

                return order_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NaturalSearchReplayOrder | None | Unset, data)

        order = _parse_order(d.pop("order", UNSET))

        def _parse_ranking_unit(
            data: object,
        ) -> NaturalSearchReplayRankingUnit | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ranking_unit_type_1 = NaturalSearchReplayRankingUnit(data)

                return ranking_unit_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NaturalSearchReplayRankingUnit | None | Unset, data)

        ranking_unit = _parse_ranking_unit(d.pop("ranking_unit", UNSET))

        natural_search_replay = cls(
            version=version,
            applied=applied,
            exact_text=exact_text,
            meaning_led=meaning_led,
            order=order,
            ranking_unit=ranking_unit,
        )

        natural_search_replay.additional_properties = d
        return natural_search_replay

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
