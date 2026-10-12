from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_publication_job_schema_metadata_overrides_type_0 import (
        CreatePublicationJobSchemaMetadataOverridesType0,
    )
    from ..models.create_publication_job_thumbnail_keyframe import (
        CreatePublicationJobThumbnailKeyframe,
    )
    from ..models.create_publication_template import CreatePublicationTemplate
    from ..models.video_source import VideoSource


T = TypeVar("T", bound="CreatePublicationJobSchema")


@_attrs_define
class CreatePublicationJobSchema:
    """
    Attributes:
        asset_id (UUID):
        allow_transfer (bool | None | Unset):  Default: True.
        metadata_overrides (CreatePublicationJobSchemaMetadataOverridesType0 | None | Unset):
        publish_at_time (datetime.datetime | None | Unset): Schedule publishing at this date/time instead of
            immediately. Naive values are interpreted as UTC.
        save_clip_as_draft (bool | None | Unset): Whether to immediately create a draft clip for this asset without
            waiting for ingestion. The clip is created right away and appears in clip management like any other clip, while
            the media is ingested in the background. This lets the asset be opened/edited before the media is available.
            This is mutually exclusive with publishing the clip when done. Default: False.
        storage_id (None | Unset | UUID):
        template (CreatePublicationTemplate | None | Unset):
        thumbnail (CreatePublicationJobThumbnailKeyframe | None | Unset):
        title (None | str | Unset):
        video_source (None | Unset | VideoSource):
    """

    asset_id: UUID
    allow_transfer: bool | None | Unset = True
    metadata_overrides: (
        CreatePublicationJobSchemaMetadataOverridesType0 | None | Unset
    ) = UNSET
    publish_at_time: datetime.datetime | None | Unset = UNSET
    save_clip_as_draft: bool | None | Unset = False
    storage_id: None | Unset | UUID = UNSET
    template: CreatePublicationTemplate | None | Unset = UNSET
    thumbnail: CreatePublicationJobThumbnailKeyframe | None | Unset = UNSET
    title: None | str | Unset = UNSET
    video_source: None | Unset | VideoSource = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_publication_job_schema_metadata_overrides_type_0 import (
            CreatePublicationJobSchemaMetadataOverridesType0,
        )
        from ..models.create_publication_job_thumbnail_keyframe import (
            CreatePublicationJobThumbnailKeyframe,
        )
        from ..models.create_publication_template import CreatePublicationTemplate
        from ..models.video_source import VideoSource

        asset_id = str(self.asset_id)

        allow_transfer: bool | None | Unset
        if isinstance(self.allow_transfer, Unset):
            allow_transfer = UNSET
        else:
            allow_transfer = self.allow_transfer

        metadata_overrides: dict[str, Any] | None | Unset
        if isinstance(self.metadata_overrides, Unset):
            metadata_overrides = UNSET
        elif isinstance(
            self.metadata_overrides, CreatePublicationJobSchemaMetadataOverridesType0
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

        save_clip_as_draft: bool | None | Unset
        if isinstance(self.save_clip_as_draft, Unset):
            save_clip_as_draft = UNSET
        else:
            save_clip_as_draft = self.save_clip_as_draft

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
        elif isinstance(self.template, CreatePublicationTemplate):
            template = self.template.to_dict()
        else:
            template = self.template

        thumbnail: dict[str, Any] | None | Unset
        if isinstance(self.thumbnail, Unset):
            thumbnail = UNSET
        elif isinstance(self.thumbnail, CreatePublicationJobThumbnailKeyframe):
            thumbnail = self.thumbnail.to_dict()
        else:
            thumbnail = self.thumbnail

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        video_source: dict[str, Any] | None | Unset
        if isinstance(self.video_source, Unset):
            video_source = UNSET
        elif isinstance(self.video_source, VideoSource):
            video_source = self.video_source.to_dict()
        else:
            video_source = self.video_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
            }
        )
        if allow_transfer is not UNSET:
            field_dict["allow_transfer"] = allow_transfer
        if metadata_overrides is not UNSET:
            field_dict["metadata_overrides"] = metadata_overrides
        if publish_at_time is not UNSET:
            field_dict["publish_at_time"] = publish_at_time
        if save_clip_as_draft is not UNSET:
            field_dict["save_clip_as_draft"] = save_clip_as_draft
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id
        if template is not UNSET:
            field_dict["template"] = template
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if title is not UNSET:
            field_dict["title"] = title
        if video_source is not UNSET:
            field_dict["video_source"] = video_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_publication_job_schema_metadata_overrides_type_0 import (
            CreatePublicationJobSchemaMetadataOverridesType0,
        )
        from ..models.create_publication_job_thumbnail_keyframe import (
            CreatePublicationJobThumbnailKeyframe,
        )
        from ..models.create_publication_template import CreatePublicationTemplate
        from ..models.video_source import VideoSource

        d = dict(src_dict)
        asset_id = UUID(d.pop("asset_id"))

        def _parse_allow_transfer(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_transfer = _parse_allow_transfer(d.pop("allow_transfer", UNSET))

        def _parse_metadata_overrides(
            data: object,
        ) -> CreatePublicationJobSchemaMetadataOverridesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_overrides_type_0 = (
                    CreatePublicationJobSchemaMetadataOverridesType0.from_dict(data)
                )

                return metadata_overrides_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreatePublicationJobSchemaMetadataOverridesType0 | None | Unset, data
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

        def _parse_save_clip_as_draft(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        save_clip_as_draft = _parse_save_clip_as_draft(
            d.pop("save_clip_as_draft", UNSET)
        )

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

        def _parse_template(data: object) -> CreatePublicationTemplate | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                template_type_1 = CreatePublicationTemplate.from_dict(data)

                return template_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreatePublicationTemplate | None | Unset, data)

        template = _parse_template(d.pop("template", UNSET))

        def _parse_thumbnail(
            data: object,
        ) -> CreatePublicationJobThumbnailKeyframe | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                thumbnail_type_0 = CreatePublicationJobThumbnailKeyframe.from_dict(data)

                return thumbnail_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreatePublicationJobThumbnailKeyframe | None | Unset, data)

        thumbnail = _parse_thumbnail(d.pop("thumbnail", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_video_source(data: object) -> None | Unset | VideoSource:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                video_source_type_1 = VideoSource.from_dict(data)

                return video_source_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VideoSource, data)

        video_source = _parse_video_source(d.pop("video_source", UNSET))

        create_publication_job_schema = cls(
            asset_id=asset_id,
            allow_transfer=allow_transfer,
            metadata_overrides=metadata_overrides,
            publish_at_time=publish_at_time,
            save_clip_as_draft=save_clip_as_draft,
            storage_id=storage_id,
            template=template,
            thumbnail=thumbnail,
            title=title,
            video_source=video_source,
        )

        create_publication_job_schema.additional_properties = d
        return create_publication_job_schema

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
