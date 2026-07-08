from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_by_schema import ApprovalBySchema
    from ..models.approval_schema_status_type_1 import ApprovalSchemaStatusType1
    from ..models.approval_schema_user_status_type_1 import (
        ApprovalSchemaUserStatusType1,
    )
    from ..models.user import User


T = TypeVar("T", bound="ApprovalSchema")


@_attrs_define
class ApprovalSchema:
    """
    Attributes:
        approvals_by (list[ApprovalBySchema] | None | Unset):
        change_date (datetime.datetime | None | Unset):
        externals (list[str] | None | Unset):
        groups (list[UUID] | None | Unset):
        min_number (int | None | Unset):  Default: 1.
        object_id (None | Unset | UUID):
        object_type (None | str | Unset):
        request_date (datetime.datetime | None | Unset):
        requested_by (None | Unset | UUID):
        share_id (None | Unset | UUID):
        status (ApprovalSchemaStatusType1 | None | Unset):
        user_status (ApprovalSchemaUserStatusType1 | None | Unset):
        users (list[UUID] | None | Unset):
        users_info (list[User] | None | Unset):
        version_id (None | Unset | UUID):
    """

    approvals_by: list[ApprovalBySchema] | None | Unset = UNSET
    change_date: datetime.datetime | None | Unset = UNSET
    externals: list[str] | None | Unset = UNSET
    groups: list[UUID] | None | Unset = UNSET
    min_number: int | None | Unset = 1
    object_id: None | Unset | UUID = UNSET
    object_type: None | str | Unset = UNSET
    request_date: datetime.datetime | None | Unset = UNSET
    requested_by: None | Unset | UUID = UNSET
    share_id: None | Unset | UUID = UNSET
    status: ApprovalSchemaStatusType1 | None | Unset = UNSET
    user_status: ApprovalSchemaUserStatusType1 | None | Unset = UNSET
    users: list[UUID] | None | Unset = UNSET
    users_info: list[User] | None | Unset = UNSET
    version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.approval_schema_status_type_1 import ApprovalSchemaStatusType1
        from ..models.approval_schema_user_status_type_1 import (
            ApprovalSchemaUserStatusType1,
        )

        approvals_by: list[dict[str, Any]] | None | Unset
        if isinstance(self.approvals_by, Unset):
            approvals_by = UNSET
        elif isinstance(self.approvals_by, list):
            approvals_by = []
            for approvals_by_type_0_item_data in self.approvals_by:
                approvals_by_type_0_item = approvals_by_type_0_item_data.to_dict()
                approvals_by.append(approvals_by_type_0_item)

        else:
            approvals_by = self.approvals_by

        change_date: None | str | Unset
        if isinstance(self.change_date, Unset):
            change_date = UNSET
        elif isinstance(self.change_date, datetime.datetime):
            change_date = self.change_date.isoformat()
        else:
            change_date = self.change_date

        externals: list[str] | None | Unset
        if isinstance(self.externals, Unset):
            externals = UNSET
        elif isinstance(self.externals, list):
            externals = self.externals

        else:
            externals = self.externals

        groups: list[str] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = str(groups_type_0_item_data)
                groups.append(groups_type_0_item)

        else:
            groups = self.groups

        min_number: int | None | Unset
        if isinstance(self.min_number, Unset):
            min_number = UNSET
        else:
            min_number = self.min_number

        object_id: None | str | Unset
        if isinstance(self.object_id, Unset):
            object_id = UNSET
        elif isinstance(self.object_id, UUID):
            object_id = str(self.object_id)
        else:
            object_id = self.object_id

        object_type: None | str | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        else:
            object_type = self.object_type

        request_date: None | str | Unset
        if isinstance(self.request_date, Unset):
            request_date = UNSET
        elif isinstance(self.request_date, datetime.datetime):
            request_date = self.request_date.isoformat()
        else:
            request_date = self.request_date

        requested_by: None | str | Unset
        if isinstance(self.requested_by, Unset):
            requested_by = UNSET
        elif isinstance(self.requested_by, UUID):
            requested_by = str(self.requested_by)
        else:
            requested_by = self.requested_by

        share_id: None | str | Unset
        if isinstance(self.share_id, Unset):
            share_id = UNSET
        elif isinstance(self.share_id, UUID):
            share_id = str(self.share_id)
        else:
            share_id = self.share_id

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, ApprovalSchemaStatusType1):
            status = self.status.to_dict()
        else:
            status = self.status

        user_status: dict[str, Any] | None | Unset
        if isinstance(self.user_status, Unset):
            user_status = UNSET
        elif isinstance(self.user_status, ApprovalSchemaUserStatusType1):
            user_status = self.user_status.to_dict()
        else:
            user_status = self.user_status

        users: list[str] | None | Unset
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, list):
            users = []
            for users_type_0_item_data in self.users:
                users_type_0_item = str(users_type_0_item_data)
                users.append(users_type_0_item)

        else:
            users = self.users

        users_info: list[dict[str, Any]] | None | Unset
        if isinstance(self.users_info, Unset):
            users_info = UNSET
        elif isinstance(self.users_info, list):
            users_info = []
            for users_info_type_0_item_data in self.users_info:
                users_info_type_0_item = users_info_type_0_item_data.to_dict()
                users_info.append(users_info_type_0_item)

        else:
            users_info = self.users_info

        version_id: None | str | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        elif isinstance(self.version_id, UUID):
            version_id = str(self.version_id)
        else:
            version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approvals_by is not UNSET:
            field_dict["approvals_by"] = approvals_by
        if change_date is not UNSET:
            field_dict["change_date"] = change_date
        if externals is not UNSET:
            field_dict["externals"] = externals
        if groups is not UNSET:
            field_dict["groups"] = groups
        if min_number is not UNSET:
            field_dict["min_number"] = min_number
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if request_date is not UNSET:
            field_dict["request_date"] = request_date
        if requested_by is not UNSET:
            field_dict["requested_by"] = requested_by
        if share_id is not UNSET:
            field_dict["share_id"] = share_id
        if status is not UNSET:
            field_dict["status"] = status
        if user_status is not UNSET:
            field_dict["user_status"] = user_status
        if users is not UNSET:
            field_dict["users"] = users
        if users_info is not UNSET:
            field_dict["users_info"] = users_info
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_by_schema import ApprovalBySchema
        from ..models.approval_schema_status_type_1 import ApprovalSchemaStatusType1
        from ..models.approval_schema_user_status_type_1 import (
            ApprovalSchemaUserStatusType1,
        )
        from ..models.user import User

        d = dict(src_dict)

        def _parse_approvals_by(data: object) -> list[ApprovalBySchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                approvals_by_type_0 = []
                _approvals_by_type_0 = data
                for approvals_by_type_0_item_data in _approvals_by_type_0:
                    approvals_by_type_0_item = ApprovalBySchema.from_dict(
                        approvals_by_type_0_item_data
                    )

                    approvals_by_type_0.append(approvals_by_type_0_item)

                return approvals_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ApprovalBySchema] | None | Unset, data)

        approvals_by = _parse_approvals_by(d.pop("approvals_by", UNSET))

        def _parse_change_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                change_date_type_0 = datetime.datetime.fromisoformat(data)

                return change_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        change_date = _parse_change_date(d.pop("change_date", UNSET))

        def _parse_externals(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                externals_type_0 = cast(list[str], data)

                return externals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        externals = _parse_externals(d.pop("externals", UNSET))

        def _parse_groups(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in _groups_type_0:
                    groups_type_0_item = UUID(groups_type_0_item_data)

                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))

        def _parse_min_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_number = _parse_min_number(d.pop("min_number", UNSET))

        def _parse_object_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                object_id_type_0 = UUID(data)

                return object_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        object_id = _parse_object_id(d.pop("object_id", UNSET))

        def _parse_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_type = _parse_object_type(d.pop("object_type", UNSET))

        def _parse_request_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_date_type_0 = datetime.datetime.fromisoformat(data)

                return request_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        request_date = _parse_request_date(d.pop("request_date", UNSET))

        def _parse_requested_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                requested_by_type_0 = UUID(data)

                return requested_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        requested_by = _parse_requested_by(d.pop("requested_by", UNSET))

        def _parse_share_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                share_id_type_0 = UUID(data)

                return share_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        share_id = _parse_share_id(d.pop("share_id", UNSET))

        def _parse_status(data: object) -> ApprovalSchemaStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = ApprovalSchemaStatusType1.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApprovalSchemaStatusType1 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_user_status(
            data: object,
        ) -> ApprovalSchemaUserStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_status_type_1 = ApprovalSchemaUserStatusType1.from_dict(data)

                return user_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApprovalSchemaUserStatusType1 | None | Unset, data)

        user_status = _parse_user_status(d.pop("user_status", UNSET))

        def _parse_users(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_type_0 = []
                _users_type_0 = data
                for users_type_0_item_data in _users_type_0:
                    users_type_0_item = UUID(users_type_0_item_data)

                    users_type_0.append(users_type_0_item)

                return users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        users = _parse_users(d.pop("users", UNSET))

        def _parse_users_info(data: object) -> list[User] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_info_type_0 = []
                _users_info_type_0 = data
                for users_info_type_0_item_data in _users_info_type_0:
                    users_info_type_0_item = User.from_dict(users_info_type_0_item_data)

                    users_info_type_0.append(users_info_type_0_item)

                return users_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[User] | None | Unset, data)

        users_info = _parse_users_info(d.pop("users_info", UNSET))

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

        approval_schema = cls(
            approvals_by=approvals_by,
            change_date=change_date,
            externals=externals,
            groups=groups,
            min_number=min_number,
            object_id=object_id,
            object_type=object_type,
            request_date=request_date,
            requested_by=requested_by,
            share_id=share_id,
            status=status,
            user_status=user_status,
            users=users,
            users_info=users_info,
            version_id=version_id,
        )

        approval_schema.additional_properties = d
        return approval_schema

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
