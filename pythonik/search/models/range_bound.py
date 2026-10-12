from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RangeBound")


@_attrs_define
class RangeBound:
    """Bounds for a ``range`` keyword predicate (every bound is optional).

    ``gte`` / ``lte`` are the inclusive pair and the ones producers normally
    reach for (the Understanding prompt only ever asks for those). ``gt`` / ``lt``
    are their strict counterparts, here so a producer that *does* mean "strictly
    after" can say it instead of being silently rounded to the inclusive bound:
    every backend honours all four, and the naming matches Elasticsearch's so
    there is nothing to remember.

    Bounds AND together, so several on one side simply intersect
    (``gte=1, gt=5`` is ``x > 5``) -- a pointless-but-harmless combination that
    is deliberately not rejected, since the producer is often an LLM and a
    well-defined narrowing beats a failed compile.

    Read them with :meth:`bounds` rather than four ``is not None`` checks: it is
    the one place the set of bounds is enumerated, so a backend adapter cannot
    quietly ignore one.

        Attributes:
            gt (bool | float | int | None | str | Unset):
            gte (bool | float | int | None | str | Unset):
            lt (bool | float | int | None | str | Unset):
            lte (bool | float | int | None | str | Unset):
    """

    gt: bool | float | int | None | str | Unset = UNSET
    gte: bool | float | int | None | str | Unset = UNSET
    lt: bool | float | int | None | str | Unset = UNSET
    lte: bool | float | int | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gt: bool | float | int | None | str | Unset
        if isinstance(self.gt, Unset):
            gt = UNSET
        else:
            gt = self.gt

        gte: bool | float | int | None | str | Unset
        if isinstance(self.gte, Unset):
            gte = UNSET
        else:
            gte = self.gte

        lt: bool | float | int | None | str | Unset
        if isinstance(self.lt, Unset):
            lt = UNSET
        else:
            lt = self.lt

        lte: bool | float | int | None | str | Unset
        if isinstance(self.lte, Unset):
            lte = UNSET
        else:
            lte = self.lte

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gt is not UNSET:
            field_dict["gt"] = gt
        if gte is not UNSET:
            field_dict["gte"] = gte
        if lt is not UNSET:
            field_dict["lt"] = lt
        if lte is not UNSET:
            field_dict["lte"] = lte

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_gt(data: object) -> bool | float | int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | float | int | None | str | Unset, data)

        gt = _parse_gt(d.pop("gt", UNSET))

        def _parse_gte(data: object) -> bool | float | int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | float | int | None | str | Unset, data)

        gte = _parse_gte(d.pop("gte", UNSET))

        def _parse_lt(data: object) -> bool | float | int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | float | int | None | str | Unset, data)

        lt = _parse_lt(d.pop("lt", UNSET))

        def _parse_lte(data: object) -> bool | float | int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | float | int | None | str | Unset, data)

        lte = _parse_lte(d.pop("lte", UNSET))

        range_bound = cls(
            gt=gt,
            gte=gte,
            lt=lt,
            lte=lte,
        )

        range_bound.additional_properties = d
        return range_bound

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
