from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_schema_status import ApprovalSchemaStatus
from ..models.approval_schema_user_status import ApprovalSchemaUserStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_by_schema import ApprovalBySchema
    from ..models.user import User


T = TypeVar("T", bound="ApprovalSchema")


@_attrs_define
class ApprovalSchema:
    """
    Attributes:
        approvals_by (list[ApprovalBySchema] | None | Unset):
        change_date (datetime.datetime | Unset):
        externals (list[str] | Unset):
        groups (list[UUID] | Unset):
        min_number (int | Unset):  Default: 1.
        object_id (UUID | Unset):
        object_type (str | Unset):
        request_date (datetime.datetime | Unset):
        requested_by (UUID | Unset):
        share_id (None | Unset | UUID):
        status (ApprovalSchemaStatus | Unset):
        user_status (ApprovalSchemaUserStatus | Unset):
        users (list[UUID] | Unset):
        users_info (list[User] | Unset):
        version_id (UUID | Unset):
    """

    approvals_by: list[ApprovalBySchema] | None | Unset = UNSET
    change_date: datetime.datetime | Unset = UNSET
    externals: list[str] | Unset = UNSET
    groups: list[UUID] | Unset = UNSET
    min_number: int | Unset = 1
    object_id: UUID | Unset = UNSET
    object_type: str | Unset = UNSET
    request_date: datetime.datetime | Unset = UNSET
    requested_by: UUID | Unset = UNSET
    share_id: None | Unset | UUID = UNSET
    status: ApprovalSchemaStatus | Unset = UNSET
    user_status: ApprovalSchemaUserStatus | Unset = UNSET
    users: list[UUID] | Unset = UNSET
    users_info: list[User] | Unset = UNSET
    version_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        change_date: str | Unset = UNSET
        if not isinstance(self.change_date, Unset):
            change_date = self.change_date.isoformat()

        externals: list[str] | Unset = UNSET
        if not isinstance(self.externals, Unset):
            externals = self.externals

        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = str(groups_item_data)
                groups.append(groups_item)

        min_number = self.min_number

        object_id: str | Unset = UNSET
        if not isinstance(self.object_id, Unset):
            object_id = str(self.object_id)

        object_type = self.object_type

        request_date: str | Unset = UNSET
        if not isinstance(self.request_date, Unset):
            request_date = self.request_date.isoformat()

        requested_by: str | Unset = UNSET
        if not isinstance(self.requested_by, Unset):
            requested_by = str(self.requested_by)

        share_id: None | str | Unset
        if isinstance(self.share_id, Unset):
            share_id = UNSET
        elif isinstance(self.share_id, UUID):
            share_id = str(self.share_id)
        else:
            share_id = self.share_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        user_status: str | Unset = UNSET
        if not isinstance(self.user_status, Unset):
            user_status = self.user_status.value

        users: list[str] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = str(users_item_data)
                users.append(users_item)

        users_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users_info, Unset):
            users_info = []
            for users_info_item_data in self.users_info:
                users_info_item = users_info_item_data.to_dict()
                users_info.append(users_info_item)

        version_id: str | Unset = UNSET
        if not isinstance(self.version_id, Unset):
            version_id = str(self.version_id)

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

        _change_date = d.pop("change_date", UNSET)
        change_date: datetime.datetime | Unset
        if isinstance(_change_date, Unset):
            change_date = UNSET
        else:
            change_date = datetime.datetime.fromisoformat(_change_date)

        externals = cast(list[str], d.pop("externals", UNSET))

        _groups = d.pop("groups", UNSET)
        groups: list[UUID] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = UUID(groups_item_data)

                groups.append(groups_item)

        min_number = d.pop("min_number", UNSET)

        _object_id = d.pop("object_id", UNSET)
        object_id: UUID | Unset
        if isinstance(_object_id, Unset):
            object_id = UNSET
        else:
            object_id = UUID(_object_id)

        object_type = d.pop("object_type", UNSET)

        _request_date = d.pop("request_date", UNSET)
        request_date: datetime.datetime | Unset
        if isinstance(_request_date, Unset):
            request_date = UNSET
        else:
            request_date = datetime.datetime.fromisoformat(_request_date)

        _requested_by = d.pop("requested_by", UNSET)
        requested_by: UUID | Unset
        if isinstance(_requested_by, Unset):
            requested_by = UNSET
        else:
            requested_by = UUID(_requested_by)

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

        _status = d.pop("status", UNSET)
        status: ApprovalSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApprovalSchemaStatus(_status)

        _user_status = d.pop("user_status", UNSET)
        user_status: ApprovalSchemaUserStatus | Unset
        if isinstance(_user_status, Unset):
            user_status = UNSET
        else:
            user_status = ApprovalSchemaUserStatus(_user_status)

        _users = d.pop("users", UNSET)
        users: list[UUID] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = UUID(users_item_data)

                users.append(users_item)

        _users_info = d.pop("users_info", UNSET)
        users_info: list[User] | Unset = UNSET
        if _users_info is not UNSET:
            users_info = []
            for users_info_item_data in _users_info:
                users_info_item = User.from_dict(users_info_item_data)

                users_info.append(users_info_item)

        _version_id = d.pop("version_id", UNSET)
        version_id: UUID | Unset
        if isinstance(_version_id, Unset):
            version_id = UNSET
        else:
            version_id = UUID(_version_id)

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
