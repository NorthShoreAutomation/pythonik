from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.natural_search_request_result_unit import NaturalSearchRequestResultUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.natural_search_image import NaturalSearchImage
    from ..models.natural_search_replay import NaturalSearchReplay
    from ..models.response_filter_input import ResponseFilterInput


T = TypeVar("T", bound="NaturalSearchRequest")


@_attrs_define
class NaturalSearchRequest:
    """
    Attributes:
        filters (list[ResponseFilterInput] | None | Unset): Filters to enforce on top of the query, in the same shape
            the response reports them under `filters.applied` — so a filter from a previous response can be edited and sent
            straight back. Each is applied as given and wins over whatever the query text would have implied for the same
            field; omitting one is how you drop it. A filter on an unknown or reserved field is not enforced and comes back
            under `filters.rejected`, never under `filters.applied`.

            Every filter you send is enforced whatever its `role`, so echoing back all of `filters.applied` searches more
            narrowly than the original search: send only the filters you mean to pin. To reproduce a search, send its block
            as `replay` instead.
        image (NaturalSearchImage | None | Unset): Optional reference image for visual search. **Not supported yet**: a
            request carrying one is rejected with a 400 until a visual-similarity backend serves it.
        limit (int | None | Unset): **Deprecated** alias of `per_page`. When both are given, `per_page` wins. Default:
            20.
        max_sub_items (int | None | Unset): Cap on how many finer-grain sub-items (e.g. localized segments) each nested
            result keeps, trimming the low-signal tail to the top-N most relevant. `null` keeps every matched sub-item. Only
            affects nested results; never changes which items surface or their ranking. Default: 20.
        nested_results (bool | None | Unset): Return items with sub-items instead of a flat list. Default: True.
        page (int | None | Unset): 1-based page to return. Above 1, requires `replay` (the `filters` of the response
            being continued), or the request is rejected with a 400. Ignored when `search_after` is given. Default: 1.
        per_page (int | None | Unset): Number of results per page; replaces `limit`. Exact on a paginated answer
            (`pagination.supported` true); an unpaginated answer may return more ranked results than this.
        query (None | str | Unset): Free-text natural-language query.
        replay (NaturalSearchReplay | None | Unset): A response's `filters` block (or an `interpretations[].filters`
            one), sent back as received, possibly with entries removed from `applied`. The search then runs that
            interpretation instead of reading the query again: no language-model call, one retrieval round, no zero-result
            recovery. Use it to page through an answer, run another reading, or re-run it with a filter dropped. An entry
            this server cannot honour is a 400. Cannot be combined with `filters`.
        result_unit (NaturalSearchRequestResultUnit | None | Unset):
        search_after (list[Any] | None | Unset): Infinite-scroll pagination key, as on `/v2/search/`: the `_sort` of the
            last object of the previous response. Wins over `page`. Requires `replay` (the previous response's `filters`),
            or the request is rejected with a 400.
    """

    filters: list[ResponseFilterInput] | None | Unset = UNSET
    image: NaturalSearchImage | None | Unset = UNSET
    limit: int | None | Unset = 20
    max_sub_items: int | None | Unset = 20
    nested_results: bool | None | Unset = True
    page: int | None | Unset = 1
    per_page: int | None | Unset = UNSET
    query: None | str | Unset = UNSET
    replay: NaturalSearchReplay | None | Unset = UNSET
    result_unit: NaturalSearchRequestResultUnit | None | Unset = UNSET
    search_after: list[Any] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.natural_search_image import NaturalSearchImage
        from ..models.natural_search_replay import NaturalSearchReplay

        filters: list[dict[str, Any]] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, list):
            filters = []
            for filters_type_0_item_data in self.filters:
                filters_type_0_item = filters_type_0_item_data.to_dict()
                filters.append(filters_type_0_item)

        else:
            filters = self.filters

        image: dict[str, Any] | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, NaturalSearchImage):
            image = self.image.to_dict()
        else:
            image = self.image

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        max_sub_items: int | None | Unset
        if isinstance(self.max_sub_items, Unset):
            max_sub_items = UNSET
        else:
            max_sub_items = self.max_sub_items

        nested_results: bool | None | Unset
        if isinstance(self.nested_results, Unset):
            nested_results = UNSET
        else:
            nested_results = self.nested_results

        page: int | None | Unset
        if isinstance(self.page, Unset):
            page = UNSET
        else:
            page = self.page

        per_page: int | None | Unset
        if isinstance(self.per_page, Unset):
            per_page = UNSET
        else:
            per_page = self.per_page

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        replay: dict[str, Any] | None | Unset
        if isinstance(self.replay, Unset):
            replay = UNSET
        elif isinstance(self.replay, NaturalSearchReplay):
            replay = self.replay.to_dict()
        else:
            replay = self.replay

        result_unit: None | str | Unset
        if isinstance(self.result_unit, Unset):
            result_unit = UNSET
        elif isinstance(self.result_unit, NaturalSearchRequestResultUnit):
            result_unit = self.result_unit.value
        else:
            result_unit = self.result_unit

        search_after: list[Any] | None | Unset
        if isinstance(self.search_after, Unset):
            search_after = UNSET
        elif isinstance(self.search_after, list):
            search_after = self.search_after

        else:
            search_after = self.search_after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filters is not UNSET:
            field_dict["filters"] = filters
        if image is not UNSET:
            field_dict["image"] = image
        if limit is not UNSET:
            field_dict["limit"] = limit
        if max_sub_items is not UNSET:
            field_dict["max_sub_items"] = max_sub_items
        if nested_results is not UNSET:
            field_dict["nested_results"] = nested_results
        if page is not UNSET:
            field_dict["page"] = page
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if query is not UNSET:
            field_dict["query"] = query
        if replay is not UNSET:
            field_dict["replay"] = replay
        if result_unit is not UNSET:
            field_dict["result_unit"] = result_unit
        if search_after is not UNSET:
            field_dict["search_after"] = search_after

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.natural_search_image import NaturalSearchImage
        from ..models.natural_search_replay import NaturalSearchReplay
        from ..models.response_filter_input import ResponseFilterInput

        d = dict(src_dict)

        def _parse_filters(data: object) -> list[ResponseFilterInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filters_type_0 = []
                _filters_type_0 = data
                for filters_type_0_item_data in _filters_type_0:
                    filters_type_0_item = ResponseFilterInput.from_dict(
                        filters_type_0_item_data
                    )

                    filters_type_0.append(filters_type_0_item)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ResponseFilterInput] | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_image(data: object) -> NaturalSearchImage | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_type_1 = NaturalSearchImage.from_dict(data)

                return image_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NaturalSearchImage | None | Unset, data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        def _parse_max_sub_items(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_sub_items = _parse_max_sub_items(d.pop("max_sub_items", UNSET))

        def _parse_nested_results(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        nested_results = _parse_nested_results(d.pop("nested_results", UNSET))

        def _parse_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page = _parse_page(d.pop("page", UNSET))

        def _parse_per_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        per_page = _parse_per_page(d.pop("per_page", UNSET))

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_replay(data: object) -> NaturalSearchReplay | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                replay_type_1 = NaturalSearchReplay.from_dict(data)

                return replay_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NaturalSearchReplay | None | Unset, data)

        replay = _parse_replay(d.pop("replay", UNSET))

        def _parse_result_unit(
            data: object,
        ) -> NaturalSearchRequestResultUnit | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                result_unit_type_1 = NaturalSearchRequestResultUnit(data)

                return result_unit_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NaturalSearchRequestResultUnit | None | Unset, data)

        result_unit = _parse_result_unit(d.pop("result_unit", UNSET))

        def _parse_search_after(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                search_after_type_0 = cast(list[Any], data)

                return search_after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        search_after = _parse_search_after(d.pop("search_after", UNSET))

        natural_search_request = cls(
            filters=filters,
            image=image,
            limit=limit,
            max_sub_items=max_sub_items,
            nested_results=nested_results,
            page=page,
            per_page=per_page,
            query=query,
            replay=replay,
            result_unit=result_unit,
            search_after=search_after,
        )

        natural_search_request.additional_properties = d
        return natural_search_request

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
