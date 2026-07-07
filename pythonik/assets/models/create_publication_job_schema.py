from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_publication_job_schema_metadata_overrides import (
        CreatePublicationJobSchemaMetadataOverrides,
    )
    from ..models.create_publication_job_thumbnail_keyframe import (
        CreatePublicationJobThumbnailKeyframe,
    )
    from ..models.create_publication_template import CreatePublicationTemplate


T = TypeVar("T", bound="CreatePublicationJobSchema")


@_attrs_define
class CreatePublicationJobSchema:
    """
    Attributes:
        asset_id (UUID):
        allow_transfer (bool | Unset):  Default: True.
        metadata_overrides (CreatePublicationJobSchemaMetadataOverrides | Unset):
        storage_id (None | Unset | UUID):
        template (CreatePublicationTemplate | Unset):
        thumbnail (CreatePublicationJobThumbnailKeyframe | Unset):
        title (str | Unset):
    """

    asset_id: UUID
    allow_transfer: bool | Unset = True
    metadata_overrides: CreatePublicationJobSchemaMetadataOverrides | Unset = UNSET
    storage_id: None | Unset | UUID = UNSET
    template: CreatePublicationTemplate | Unset = UNSET
    thumbnail: CreatePublicationJobThumbnailKeyframe | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = str(self.asset_id)

        allow_transfer = self.allow_transfer

        metadata_overrides: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata_overrides, Unset):
            metadata_overrides = self.metadata_overrides.to_dict()

        storage_id: None | str | Unset
        if isinstance(self.storage_id, Unset):
            storage_id = UNSET
        elif isinstance(self.storage_id, UUID):
            storage_id = str(self.storage_id)
        else:
            storage_id = self.storage_id

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        thumbnail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail, Unset):
            thumbnail = self.thumbnail.to_dict()

        title = self.title

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
        from ..models.create_publication_job_schema_metadata_overrides import (
            CreatePublicationJobSchemaMetadataOverrides,
        )
        from ..models.create_publication_job_thumbnail_keyframe import (
            CreatePublicationJobThumbnailKeyframe,
        )
        from ..models.create_publication_template import CreatePublicationTemplate

        d = dict(src_dict)
        asset_id = UUID(d.pop("asset_id"))

        allow_transfer = d.pop("allow_transfer", UNSET)

        _metadata_overrides = d.pop("metadata_overrides", UNSET)
        metadata_overrides: CreatePublicationJobSchemaMetadataOverrides | Unset
        if isinstance(_metadata_overrides, Unset):
            metadata_overrides = UNSET
        else:
            metadata_overrides = CreatePublicationJobSchemaMetadataOverrides.from_dict(
                _metadata_overrides
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

        _template = d.pop("template", UNSET)
        template: CreatePublicationTemplate | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = CreatePublicationTemplate.from_dict(_template)

        _thumbnail = d.pop("thumbnail", UNSET)
        thumbnail: CreatePublicationJobThumbnailKeyframe | Unset
        if isinstance(_thumbnail, Unset):
            thumbnail = UNSET
        else:
            thumbnail = CreatePublicationJobThumbnailKeyframe.from_dict(_thumbnail)

        title = d.pop("title", UNSET)

        create_publication_job_schema = cls(
            asset_id=asset_id,
            allow_transfer=allow_transfer,
            metadata_overrides=metadata_overrides,
            storage_id=storage_id,
            template=template,
            thumbnail=thumbnail,
            title=title,
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
