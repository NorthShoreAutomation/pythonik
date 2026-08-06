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
        asset_id (None | Unset | UUID):
        date_created (datetime.datetime | None | Unset):
        errors (list[str] | None | Unset):
        field_names (list[str] | None | Unset):
        field_values (Any | Unset):
        job_id (None | Unset | UUID):
        parent_job_id (None | Unset | UUID):
        review_status (MetadataFillingProposalSchemaReviewStatus | None | Unset):
        user_id (None | Unset | UUID):
        version_id (None | Unset | UUID):
        view_id (None | Unset | UUID):
        warnings (list[str] | None | Unset):
    """

    asset_id: None | Unset | UUID = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    errors: list[str] | None | Unset = UNSET
    field_names: list[str] | None | Unset = UNSET
    field_values: Any | Unset = UNSET
    job_id: None | Unset | UUID = UNSET
    parent_job_id: None | Unset | UUID = UNSET
    review_status: MetadataFillingProposalSchemaReviewStatus | None | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    version_id: None | Unset | UUID = UNSET
    view_id: None | Unset | UUID = UNSET
    warnings: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id: None | str | Unset
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        elif isinstance(self.asset_id, UUID):
            asset_id = str(self.asset_id)
        else:
            asset_id = self.asset_id

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        errors: list[str] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = self.errors

        else:
            errors = self.errors

        field_names: list[str] | None | Unset
        if isinstance(self.field_names, Unset):
            field_names = UNSET
        elif isinstance(self.field_names, list):
            field_names = self.field_names

        else:
            field_names = self.field_names

        field_values = self.field_values

        job_id: None | str | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        elif isinstance(self.job_id, UUID):
            job_id = str(self.job_id)
        else:
            job_id = self.job_id

        parent_job_id: None | str | Unset
        if isinstance(self.parent_job_id, Unset):
            parent_job_id = UNSET
        elif isinstance(self.parent_job_id, UUID):
            parent_job_id = str(self.parent_job_id)
        else:
            parent_job_id = self.parent_job_id

        review_status: None | str | Unset
        if isinstance(self.review_status, Unset):
            review_status = UNSET
        elif isinstance(self.review_status, MetadataFillingProposalSchemaReviewStatus):
            review_status = self.review_status.value
        else:
            review_status = self.review_status

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

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

        warnings: list[str] | None | Unset
        if isinstance(self.warnings, Unset):
            warnings = UNSET
        elif isinstance(self.warnings, list):
            warnings = self.warnings

        else:
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

        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        def _parse_errors(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = cast(list[str], data)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        def _parse_field_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                field_names_type_0 = cast(list[str], data)

                return field_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        field_names = _parse_field_names(d.pop("field_names", UNSET))

        field_values = d.pop("field_values", UNSET)

        def _parse_job_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_id_type_0 = UUID(data)

                return job_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        job_id = _parse_job_id(d.pop("job_id", UNSET))

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

        def _parse_review_status(
            data: object,
        ) -> MetadataFillingProposalSchemaReviewStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                review_status_type_1 = MetadataFillingProposalSchemaReviewStatus(data)

                return review_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MetadataFillingProposalSchemaReviewStatus | None | Unset, data)

        review_status = _parse_review_status(d.pop("review_status", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

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

        def _parse_warnings(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = cast(list[str], data)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))

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
