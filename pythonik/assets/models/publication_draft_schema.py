from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_publication_job_thumbnail_keyframe_schema import (
        CreatePublicationJobThumbnailKeyframeSchema,
    )
    from ..models.publication_draft_schema_metadata_overrides_type_0 import (
        PublicationDraftSchemaMetadataOverridesType0,
    )
    from ..models.publication_template import PublicationTemplate


T = TypeVar("T", bound="PublicationDraftSchema")


@_attrs_define
class PublicationDraftSchema:
    """
    Attributes:
        asset_id (None | Unset | UUID):
        metadata_overrides (None | PublicationDraftSchemaMetadataOverridesType0 | Unset):
        publish_at_time (datetime.datetime | None | Unset):
        storage_id (None | Unset | UUID):
        template (None | PublicationTemplate | Unset):
        thumbnail (CreatePublicationJobThumbnailKeyframeSchema | None | Unset):
        title (None | str | Unset):
    """

    asset_id: None | Unset | UUID = UNSET
    metadata_overrides: None | PublicationDraftSchemaMetadataOverridesType0 | Unset = (
        UNSET
    )
    publish_at_time: datetime.datetime | None | Unset = UNSET
    storage_id: None | Unset | UUID = UNSET
    template: None | PublicationTemplate | Unset = UNSET
    thumbnail: CreatePublicationJobThumbnailKeyframeSchema | None | Unset = UNSET
    title: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_publication_job_thumbnail_keyframe_schema import (
            CreatePublicationJobThumbnailKeyframeSchema,
        )
        from ..models.publication_draft_schema_metadata_overrides_type_0 import (
            PublicationDraftSchemaMetadataOverridesType0,
        )
        from ..models.publication_template import PublicationTemplate

        asset_id: None | str | Unset
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        elif isinstance(self.asset_id, UUID):
            asset_id = str(self.asset_id)
        else:
            asset_id = self.asset_id

        metadata_overrides: dict[str, Any] | None | Unset
        if isinstance(self.metadata_overrides, Unset):
            metadata_overrides = UNSET
        elif isinstance(
            self.metadata_overrides, PublicationDraftSchemaMetadataOverridesType0
        ):
            metadata_overrides = self.metadata_overrides.to_dict()
        else:
            metadata_overrides = self.metadata_overrides

        publish_at_time: None | str | Unset
        if isinstance(self.publish_at_time, Unset):
            publish_at_time = UNSET
        elif isinstance(self.publish_at_time, datetime.datetime):
            publish_at_time = self.publish_at_time.isoformat()
        else:
            publish_at_time = self.publish_at_time

        storage_id: None | str | Unset
        if isinstance(self.storage_id, Unset):
            storage_id = UNSET
        elif isinstance(self.storage_id, UUID):
            storage_id = str(self.storage_id)
        else:
            storage_id = self.storage_id

        template: dict[str, Any] | None | Unset
        if isinstance(self.template, Unset):
            template = UNSET
        elif isinstance(self.template, PublicationTemplate):
            template = self.template.to_dict()
        else:
            template = self.template

        thumbnail: dict[str, Any] | None | Unset
        if isinstance(self.thumbnail, Unset):
            thumbnail = UNSET
        elif isinstance(self.thumbnail, CreatePublicationJobThumbnailKeyframeSchema):
            thumbnail = self.thumbnail.to_dict()
        else:
            thumbnail = self.thumbnail

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if metadata_overrides is not UNSET:
            field_dict["metadata_overrides"] = metadata_overrides
        if publish_at_time is not UNSET:
            field_dict["publish_at_time"] = publish_at_time
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id
        if template is not UNSET:
            field_dict["template"] = template
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_publication_job_thumbnail_keyframe_schema import (
            CreatePublicationJobThumbnailKeyframeSchema,
        )
        from ..models.publication_draft_schema_metadata_overrides_type_0 import (
            PublicationDraftSchemaMetadataOverridesType0,
        )
        from ..models.publication_template import PublicationTemplate

        d = dict(src_dict)

        def _parse_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                asset_id_type_0 = UUID(data)

                return asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        asset_id = _parse_asset_id(d.pop("asset_id", UNSET))

        def _parse_metadata_overrides(
            data: object,
        ) -> None | PublicationDraftSchemaMetadataOverridesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_overrides_type_0 = (
                    PublicationDraftSchemaMetadataOverridesType0.from_dict(data)
                )

                return metadata_overrides_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PublicationDraftSchemaMetadataOverridesType0 | Unset, data
            )

        metadata_overrides = _parse_metadata_overrides(
            d.pop("metadata_overrides", UNSET)
        )

        def _parse_publish_at_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                publish_at_time_type_0 = datetime.datetime.fromisoformat(data)

                return publish_at_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        publish_at_time = _parse_publish_at_time(d.pop("publish_at_time", UNSET))

        def _parse_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_id_type_0 = UUID(data)

                return storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        storage_id = _parse_storage_id(d.pop("storage_id", UNSET))

        def _parse_template(data: object) -> None | PublicationTemplate | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                template_type_1 = PublicationTemplate.from_dict(data)

                return template_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PublicationTemplate | Unset, data)

        template = _parse_template(d.pop("template", UNSET))

        def _parse_thumbnail(
            data: object,
        ) -> CreatePublicationJobThumbnailKeyframeSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                thumbnail_type_0 = (
                    CreatePublicationJobThumbnailKeyframeSchema.from_dict(data)
                )

                return thumbnail_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreatePublicationJobThumbnailKeyframeSchema | None | Unset, data
            )

        thumbnail = _parse_thumbnail(d.pop("thumbnail", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        publication_draft_schema = cls(
            asset_id=asset_id,
            metadata_overrides=metadata_overrides,
            publish_at_time=publish_at_time,
            storage_id=storage_id,
            template=template,
            thumbnail=thumbnail,
            title=title,
        )

        publication_draft_schema.additional_properties = d
        return publication_draft_schema

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
