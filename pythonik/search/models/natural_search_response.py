from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.natural_search_response_match_quality import (
    NaturalSearchResponseMatchQuality,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.natural_search_document import NaturalSearchDocument
    from ..models.natural_search_moment import NaturalSearchMoment
    from ..models.natural_search_response_assets_type_0 import (
        NaturalSearchResponseAssetsType0,
    )
    from ..models.natural_search_response_facets_type_0 import (
        NaturalSearchResponseFacetsType0,
    )
    from ..models.response_filters import ResponseFilters
    from ..models.response_interpretation import ResponseInterpretation
    from ..models.response_pagination import ResponsePagination


T = TypeVar("T", bound="NaturalSearchResponse")


@_attrs_define
class NaturalSearchResponse:
    """Natural-language search results.

    Same envelope as ``/v2/search/`` — `objects` and the pagination fields — so
    both endpoints feed one rendering path.

    When `pagination.supported` is true, `page` / `pages` / `total` mean what
    they do on ``/v2/search/``; otherwise the answer is a single ranked set
    (`page` and `pages` are 1) and `pagination.reason` says why.

    The navigation urls are always null: pagination is driven by re-posting the
    request body (see `pagination`).

        Attributes:
            assets (NaturalSearchResponseAssetsType0 | None | Unset): The documents `objects` refer to but do not contain,
                keyed by asset id. Empty unless the results are moments. Plain documents: the ranking story (`score`,
                `evidence`, `match`) belongs to the moment that matched, not to the asset it happens to sit in.
            degraded (bool | None | Unset): True when at least one search backend failed, timed out or answered partially.
                The results are still usable, just not the full picture. Default: False.
            facets (NaturalSearchResponseFacetsType0 | None | Unset): Always null here; natural search computes no
                aggregations.
            filters (None | ResponseFilters | Unset):
            first_url (None | str | Unset):
            interpretations (list[ResponseInterpretation] | None | Unset): Every way the query was read, best first; more
                than one when the query is ambiguous (e.g. a name to filter on, or a word in the content). The search stops at
                the first reading that finds something; `answered` marks it.

                Show another entry's `why` as a "did you mean ...?" and, if picked, re-post with that entry's `filters` as
                `replay`. Each is shaped like this response's `filters`; the `answered` entry carries it unchanged.
            language (None | str | Unset): BCP-47 tag of the query's language, which the `interpretations` sentences are
                written in. Empty when unknown. Default: ''.
            last_url (None | str | Unset):
            match_quality (NaturalSearchResponseMatchQuality | None | Unset):
            next_url (None | str | Unset):
            objects (list[NaturalSearchDocument | NaturalSearchMoment] | None | Unset): The ranked results, at the requested
                `result_unit`. Documents for an asset/collection grain; moments (see `NaturalSearchMoment`) when `result_unit`
                is `segment`.
            page (int | None | Unset):
            pages (int | None | Unset):
            pagination (None | ResponsePagination | Unset):
            per_page (int | None | Unset):
            prev_url (None | str | Unset):
            scroll_id (None | str | Unset):
            total (int | None | Unset):
    """

    assets: NaturalSearchResponseAssetsType0 | None | Unset = UNSET
    degraded: bool | None | Unset = False
    facets: NaturalSearchResponseFacetsType0 | None | Unset = UNSET
    filters: None | ResponseFilters | Unset = UNSET
    first_url: None | str | Unset = UNSET
    interpretations: list[ResponseInterpretation] | None | Unset = UNSET
    language: None | str | Unset = ""
    last_url: None | str | Unset = UNSET
    match_quality: NaturalSearchResponseMatchQuality | None | Unset = UNSET
    next_url: None | str | Unset = UNSET
    objects: list[NaturalSearchDocument | NaturalSearchMoment] | None | Unset = UNSET
    page: int | None | Unset = UNSET
    pages: int | None | Unset = UNSET
    pagination: None | ResponsePagination | Unset = UNSET
    per_page: int | None | Unset = UNSET
    prev_url: None | str | Unset = UNSET
    scroll_id: None | str | Unset = UNSET
    total: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.natural_search_document import NaturalSearchDocument
        from ..models.natural_search_response_assets_type_0 import (
            NaturalSearchResponseAssetsType0,
        )
        from ..models.natural_search_response_facets_type_0 import (
            NaturalSearchResponseFacetsType0,
        )
        from ..models.response_filters import ResponseFilters
        from ..models.response_pagination import ResponsePagination

        assets: dict[str, Any] | None | Unset
        if isinstance(self.assets, Unset):
            assets = UNSET
        elif isinstance(self.assets, NaturalSearchResponseAssetsType0):
            assets = self.assets.to_dict()
        else:
            assets = self.assets

        degraded: bool | None | Unset
        if isinstance(self.degraded, Unset):
            degraded = UNSET
        else:
            degraded = self.degraded

        facets: dict[str, Any] | None | Unset
        if isinstance(self.facets, Unset):
            facets = UNSET
        elif isinstance(self.facets, NaturalSearchResponseFacetsType0):
            facets = self.facets.to_dict()
        else:
            facets = self.facets

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, ResponseFilters):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        first_url: None | str | Unset
        if isinstance(self.first_url, Unset):
            first_url = UNSET
        else:
            first_url = self.first_url

        interpretations: list[dict[str, Any]] | None | Unset
        if isinstance(self.interpretations, Unset):
            interpretations = UNSET
        elif isinstance(self.interpretations, list):
            interpretations = []
            for interpretations_type_0_item_data in self.interpretations:
                interpretations_type_0_item = interpretations_type_0_item_data.to_dict()
                interpretations.append(interpretations_type_0_item)

        else:
            interpretations = self.interpretations

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        last_url: None | str | Unset
        if isinstance(self.last_url, Unset):
            last_url = UNSET
        else:
            last_url = self.last_url

        match_quality: None | str | Unset
        if isinstance(self.match_quality, Unset):
            match_quality = UNSET
        elif isinstance(self.match_quality, NaturalSearchResponseMatchQuality):
            match_quality = self.match_quality.value
        else:
            match_quality = self.match_quality

        next_url: None | str | Unset
        if isinstance(self.next_url, Unset):
            next_url = UNSET
        else:
            next_url = self.next_url

        objects: list[dict[str, Any]] | None | Unset
        if isinstance(self.objects, Unset):
            objects = UNSET
        elif isinstance(self.objects, list):
            objects = []
            for objects_type_0_item_data in self.objects:
                objects_type_0_item: dict[str, Any]
                if isinstance(objects_type_0_item_data, NaturalSearchDocument):
                    objects_type_0_item = objects_type_0_item_data.to_dict()
                else:
                    objects_type_0_item = objects_type_0_item_data.to_dict()

                objects.append(objects_type_0_item)

        else:
            objects = self.objects

        page: int | None | Unset
        if isinstance(self.page, Unset):
            page = UNSET
        else:
            page = self.page

        pages: int | None | Unset
        if isinstance(self.pages, Unset):
            pages = UNSET
        else:
            pages = self.pages

        pagination: dict[str, Any] | None | Unset
        if isinstance(self.pagination, Unset):
            pagination = UNSET
        elif isinstance(self.pagination, ResponsePagination):
            pagination = self.pagination.to_dict()
        else:
            pagination = self.pagination

        per_page: int | None | Unset
        if isinstance(self.per_page, Unset):
            per_page = UNSET
        else:
            per_page = self.per_page

        prev_url: None | str | Unset
        if isinstance(self.prev_url, Unset):
            prev_url = UNSET
        else:
            prev_url = self.prev_url

        scroll_id: None | str | Unset
        if isinstance(self.scroll_id, Unset):
            scroll_id = UNSET
        else:
            scroll_id = self.scroll_id

        total: int | None | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets is not UNSET:
            field_dict["assets"] = assets
        if degraded is not UNSET:
            field_dict["degraded"] = degraded
        if facets is not UNSET:
            field_dict["facets"] = facets
        if filters is not UNSET:
            field_dict["filters"] = filters
        if first_url is not UNSET:
            field_dict["first_url"] = first_url
        if interpretations is not UNSET:
            field_dict["interpretations"] = interpretations
        if language is not UNSET:
            field_dict["language"] = language
        if last_url is not UNSET:
            field_dict["last_url"] = last_url
        if match_quality is not UNSET:
            field_dict["match_quality"] = match_quality
        if next_url is not UNSET:
            field_dict["next_url"] = next_url
        if objects is not UNSET:
            field_dict["objects"] = objects
        if page is not UNSET:
            field_dict["page"] = page
        if pages is not UNSET:
            field_dict["pages"] = pages
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if prev_url is not UNSET:
            field_dict["prev_url"] = prev_url
        if scroll_id is not UNSET:
            field_dict["scroll_id"] = scroll_id
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.natural_search_document import NaturalSearchDocument
        from ..models.natural_search_moment import NaturalSearchMoment
        from ..models.natural_search_response_assets_type_0 import (
            NaturalSearchResponseAssetsType0,
        )
        from ..models.natural_search_response_facets_type_0 import (
            NaturalSearchResponseFacetsType0,
        )
        from ..models.response_filters import ResponseFilters
        from ..models.response_interpretation import ResponseInterpretation
        from ..models.response_pagination import ResponsePagination

        d = dict(src_dict)

        def _parse_assets(
            data: object,
        ) -> NaturalSearchResponseAssetsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                assets_type_0 = NaturalSearchResponseAssetsType0.from_dict(data)

                return assets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NaturalSearchResponseAssetsType0 | None | Unset, data)

        assets = _parse_assets(d.pop("assets", UNSET))

        def _parse_degraded(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        degraded = _parse_degraded(d.pop("degraded", UNSET))

        def _parse_facets(
            data: object,
        ) -> NaturalSearchResponseFacetsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                facets_type_0 = NaturalSearchResponseFacetsType0.from_dict(data)

                return facets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NaturalSearchResponseFacetsType0 | None | Unset, data)

        facets = _parse_facets(d.pop("facets", UNSET))

        def _parse_filters(data: object) -> None | ResponseFilters | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_1 = ResponseFilters.from_dict(data)

                return filters_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResponseFilters | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_first_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_url = _parse_first_url(d.pop("first_url", UNSET))

        def _parse_interpretations(
            data: object,
        ) -> list[ResponseInterpretation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                interpretations_type_0 = []
                _interpretations_type_0 = data
                for interpretations_type_0_item_data in _interpretations_type_0:
                    interpretations_type_0_item = ResponseInterpretation.from_dict(
                        interpretations_type_0_item_data
                    )

                    interpretations_type_0.append(interpretations_type_0_item)

                return interpretations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ResponseInterpretation] | None | Unset, data)

        interpretations = _parse_interpretations(d.pop("interpretations", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_last_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_url = _parse_last_url(d.pop("last_url", UNSET))

        def _parse_match_quality(
            data: object,
        ) -> NaturalSearchResponseMatchQuality | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                match_quality_type_1 = NaturalSearchResponseMatchQuality(data)

                return match_quality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NaturalSearchResponseMatchQuality | None | Unset, data)

        match_quality = _parse_match_quality(d.pop("match_quality", UNSET))

        def _parse_next_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_url = _parse_next_url(d.pop("next_url", UNSET))

        def _parse_objects(
            data: object,
        ) -> list[NaturalSearchDocument | NaturalSearchMoment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                objects_type_0 = []
                _objects_type_0 = data
                for objects_type_0_item_data in _objects_type_0:

                    def _parse_objects_type_0_item(
                        data: object,
                    ) -> NaturalSearchDocument | NaturalSearchMoment:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            objects_type_0_item_type_0 = (
                                NaturalSearchDocument.from_dict(data)
                            )

                            return objects_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        objects_type_0_item_type_1 = NaturalSearchMoment.from_dict(data)

                        return objects_type_0_item_type_1

                    objects_type_0_item = _parse_objects_type_0_item(
                        objects_type_0_item_data
                    )

                    objects_type_0.append(objects_type_0_item)

                return objects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[NaturalSearchDocument | NaturalSearchMoment] | None | Unset, data
            )

        objects = _parse_objects(d.pop("objects", UNSET))

        def _parse_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page = _parse_page(d.pop("page", UNSET))

        def _parse_pages(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pages = _parse_pages(d.pop("pages", UNSET))

        def _parse_pagination(data: object) -> None | ResponsePagination | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pagination_type_1 = ResponsePagination.from_dict(data)

                return pagination_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResponsePagination | Unset, data)

        pagination = _parse_pagination(d.pop("pagination", UNSET))

        def _parse_per_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        per_page = _parse_per_page(d.pop("per_page", UNSET))

        def _parse_prev_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prev_url = _parse_prev_url(d.pop("prev_url", UNSET))

        def _parse_scroll_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scroll_id = _parse_scroll_id(d.pop("scroll_id", UNSET))

        def _parse_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total = _parse_total(d.pop("total", UNSET))

        natural_search_response = cls(
            assets=assets,
            degraded=degraded,
            facets=facets,
            filters=filters,
            first_url=first_url,
            interpretations=interpretations,
            language=language,
            last_url=last_url,
            match_quality=match_quality,
            next_url=next_url,
            objects=objects,
            page=page,
            pages=pages,
            pagination=pagination,
            per_page=per_page,
            prev_url=prev_url,
            scroll_id=scroll_id,
            total=total,
        )

        natural_search_response.additional_properties = d
        return natural_search_response

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
