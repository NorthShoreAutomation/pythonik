from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_collections_tree_schema import (
        DashboardCollectionsTreeSchema,
    )
    from ..models.dashboard_comments_feed_schema import DashboardCommentsFeedSchema
    from ..models.dashboard_header_schema import DashboardHeaderSchema
    from ..models.dashboard_schema_view_type_type_1 import DashboardSchemaViewTypeType1
    from ..models.dashboard_widget import DashboardWidget


T = TypeVar("T", bound="DashboardSchema")


@_attrs_define
class DashboardSchema:
    """
    Attributes:
        collections_tree (DashboardCollectionsTreeSchema | None | Unset):
        comments_feed (DashboardCommentsFeedSchema | None | Unset):
        header (DashboardHeaderSchema | None | Unset):
        view_type (DashboardSchemaViewTypeType1 | None | Unset):
        widgets (list[DashboardWidget] | None | Unset):
    """

    collections_tree: DashboardCollectionsTreeSchema | None | Unset = UNSET
    comments_feed: DashboardCommentsFeedSchema | None | Unset = UNSET
    header: DashboardHeaderSchema | None | Unset = UNSET
    view_type: DashboardSchemaViewTypeType1 | None | Unset = UNSET
    widgets: list[DashboardWidget] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_collections_tree_schema import (
            DashboardCollectionsTreeSchema,
        )
        from ..models.dashboard_comments_feed_schema import DashboardCommentsFeedSchema
        from ..models.dashboard_header_schema import DashboardHeaderSchema
        from ..models.dashboard_schema_view_type_type_1 import (
            DashboardSchemaViewTypeType1,
        )

        collections_tree: dict[str, Any] | None | Unset
        if isinstance(self.collections_tree, Unset):
            collections_tree = UNSET
        elif isinstance(self.collections_tree, DashboardCollectionsTreeSchema):
            collections_tree = self.collections_tree.to_dict()
        else:
            collections_tree = self.collections_tree

        comments_feed: dict[str, Any] | None | Unset
        if isinstance(self.comments_feed, Unset):
            comments_feed = UNSET
        elif isinstance(self.comments_feed, DashboardCommentsFeedSchema):
            comments_feed = self.comments_feed.to_dict()
        else:
            comments_feed = self.comments_feed

        header: dict[str, Any] | None | Unset
        if isinstance(self.header, Unset):
            header = UNSET
        elif isinstance(self.header, DashboardHeaderSchema):
            header = self.header.to_dict()
        else:
            header = self.header

        view_type: dict[str, Any] | None | Unset
        if isinstance(self.view_type, Unset):
            view_type = UNSET
        elif isinstance(self.view_type, DashboardSchemaViewTypeType1):
            view_type = self.view_type.to_dict()
        else:
            view_type = self.view_type

        widgets: list[dict[str, Any]] | None | Unset
        if isinstance(self.widgets, Unset):
            widgets = UNSET
        elif isinstance(self.widgets, list):
            widgets = []
            for widgets_type_0_item_data in self.widgets:
                widgets_type_0_item = widgets_type_0_item_data.to_dict()
                widgets.append(widgets_type_0_item)

        else:
            widgets = self.widgets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collections_tree is not UNSET:
            field_dict["collections_tree"] = collections_tree
        if comments_feed is not UNSET:
            field_dict["comments_feed"] = comments_feed
        if header is not UNSET:
            field_dict["header"] = header
        if view_type is not UNSET:
            field_dict["view_type"] = view_type
        if widgets is not UNSET:
            field_dict["widgets"] = widgets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_collections_tree_schema import (
            DashboardCollectionsTreeSchema,
        )
        from ..models.dashboard_comments_feed_schema import DashboardCommentsFeedSchema
        from ..models.dashboard_header_schema import DashboardHeaderSchema
        from ..models.dashboard_schema_view_type_type_1 import (
            DashboardSchemaViewTypeType1,
        )
        from ..models.dashboard_widget import DashboardWidget

        d = dict(src_dict)

        def _parse_collections_tree(
            data: object,
        ) -> DashboardCollectionsTreeSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                collections_tree_type_1 = DashboardCollectionsTreeSchema.from_dict(data)

                return collections_tree_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardCollectionsTreeSchema | None | Unset, data)

        collections_tree = _parse_collections_tree(d.pop("collections_tree", UNSET))

        def _parse_comments_feed(
            data: object,
        ) -> DashboardCommentsFeedSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                comments_feed_type_1 = DashboardCommentsFeedSchema.from_dict(data)

                return comments_feed_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardCommentsFeedSchema | None | Unset, data)

        comments_feed = _parse_comments_feed(d.pop("comments_feed", UNSET))

        def _parse_header(data: object) -> DashboardHeaderSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                header_type_1 = DashboardHeaderSchema.from_dict(data)

                return header_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardHeaderSchema | None | Unset, data)

        header = _parse_header(d.pop("header", UNSET))

        def _parse_view_type(
            data: object,
        ) -> DashboardSchemaViewTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                view_type_type_1 = DashboardSchemaViewTypeType1.from_dict(data)

                return view_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardSchemaViewTypeType1 | None | Unset, data)

        view_type = _parse_view_type(d.pop("view_type", UNSET))

        def _parse_widgets(data: object) -> list[DashboardWidget] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                widgets_type_0 = []
                _widgets_type_0 = data
                for widgets_type_0_item_data in _widgets_type_0:
                    widgets_type_0_item = DashboardWidget.from_dict(
                        widgets_type_0_item_data
                    )

                    widgets_type_0.append(widgets_type_0_item)

                return widgets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DashboardWidget] | None | Unset, data)

        widgets = _parse_widgets(d.pop("widgets", UNSET))

        dashboard_schema = cls(
            collections_tree=collections_tree,
            comments_feed=comments_feed,
            header=header,
            view_type=view_type,
            widgets=widgets,
        )

        dashboard_schema.additional_properties = d
        return dashboard_schema

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
