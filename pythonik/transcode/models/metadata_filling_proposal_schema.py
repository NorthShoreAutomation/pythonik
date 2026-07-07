from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metadata_filling_proposal_schema_review_status import (
    MetadataFillingProposalSchemaReviewStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataFillingProposalSchema")


@_attrs_define
class MetadataFillingProposalSchema:
    """
    Attributes:
        asset_id (UUID | Unset):
        date_created (datetime.datetime | Unset):
        errors (list[str] | Unset):
        field_names (list[str] | Unset):
        field_values (Any | Unset):
        job_id (UUID | Unset):
        parent_job_id (None | Unset | UUID):
        review_status (MetadataFillingProposalSchemaReviewStatus | Unset):
        user_id (UUID | Unset):
        version_id (None | Unset | UUID):
        view_id (None | Unset | UUID):
        warnings (list[str] | Unset):
    """

    asset_id: UUID | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    errors: list[str] | Unset = UNSET
    field_names: list[str] | Unset = UNSET
    field_values: Any | Unset = UNSET
    job_id: UUID | Unset = UNSET
    parent_job_id: None | Unset | UUID = UNSET
    review_status: MetadataFillingProposalSchemaReviewStatus | Unset = UNSET
    user_id: UUID | Unset = UNSET
    version_id: None | Unset | UUID = UNSET
    view_id: None | Unset | UUID = UNSET
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id: str | Unset = UNSET
        if not isinstance(self.asset_id, Unset):
            asset_id = str(self.asset_id)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        field_names: list[str] | Unset = UNSET
        if not isinstance(self.field_names, Unset):
            field_names = self.field_names

        field_values = self.field_values

        job_id: str | Unset = UNSET
        if not isinstance(self.job_id, Unset):
            job_id = str(self.job_id)

        parent_job_id: None | str | Unset
        if isinstance(self.parent_job_id, Unset):
            parent_job_id = UNSET
        elif isinstance(self.parent_job_id, UUID):
            parent_job_id = str(self.parent_job_id)
        else:
            parent_job_id = self.parent_job_id

        review_status: str | Unset = UNSET
        if not isinstance(self.review_status, Unset):
            review_status = self.review_status.value

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        version_id: None | str | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        elif isinstance(self.version_id, UUID):
            version_id = str(self.version_id)
        else:
            version_id = self.version_id

        view_id: None | str | Unset
        if isinstance(self.view_id, Unset):
            view_id = UNSET
        elif isinstance(self.view_id, UUID):
            view_id = str(self.view_id)
        else:
            view_id = self.view_id

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if errors is not UNSET:
            field_dict["errors"] = errors
        if field_names is not UNSET:
            field_dict["field_names"] = field_names
        if field_values is not UNSET:
            field_dict["field_values"] = field_values
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if parent_job_id is not UNSET:
            field_dict["parent_job_id"] = parent_job_id
        if review_status is not UNSET:
            field_dict["review_status"] = review_status
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if version_id is not UNSET:
            field_dict["version_id"] = version_id
        if view_id is not UNSET:
            field_dict["view_id"] = view_id
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _asset_id = d.pop("asset_id", UNSET)
        asset_id: UUID | Unset
        if isinstance(_asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = UUID(_asset_id)

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        errors = cast(list[str], d.pop("errors", UNSET))

        field_names = cast(list[str], d.pop("field_names", UNSET))

        field_values = d.pop("field_values", UNSET)

        _job_id = d.pop("job_id", UNSET)
        job_id: UUID | Unset
        if isinstance(_job_id, Unset):
            job_id = UNSET
        else:
            job_id = UUID(_job_id)

        def _parse_parent_job_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_job_id_type_0 = UUID(data)

                return parent_job_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_job_id = _parse_parent_job_id(d.pop("parent_job_id", UNSET))

        _review_status = d.pop("review_status", UNSET)
        review_status: MetadataFillingProposalSchemaReviewStatus | Unset
        if isinstance(_review_status, Unset):
            review_status = UNSET
        else:
            review_status = MetadataFillingProposalSchemaReviewStatus(_review_status)

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        def _parse_version_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                version_id_type_0 = UUID(data)

                return version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        version_id = _parse_version_id(d.pop("version_id", UNSET))

        def _parse_view_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                view_id_type_0 = UUID(data)

                return view_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        view_id = _parse_view_id(d.pop("view_id", UNSET))

        warnings = cast(list[str], d.pop("warnings", UNSET))

        metadata_filling_proposal_schema = cls(
            asset_id=asset_id,
            date_created=date_created,
            errors=errors,
            field_names=field_names,
            field_values=field_values,
            job_id=job_id,
            parent_job_id=parent_job_id,
            review_status=review_status,
            user_id=user_id,
            version_id=version_id,
            view_id=view_id,
            warnings=warnings,
        )

        metadata_filling_proposal_schema.additional_properties = d
        return metadata_filling_proposal_schema

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
