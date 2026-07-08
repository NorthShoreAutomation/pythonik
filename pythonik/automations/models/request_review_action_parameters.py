from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_share_action_parameters import CreateShareActionParameters
    from ..models.request_review_action_parameters_status_type_1 import (
        RequestReviewActionParametersStatusType1,
    )


T = TypeVar("T", bound="RequestReviewActionParameters")


@_attrs_define
class RequestReviewActionParameters:
    """
    Attributes:
        share (CreateShareActionParameters):
        externals (list[str] | None | Unset):
        groups (list[UUID] | None | Unset):
        min_number (int | None | Unset):  Default: 1.
        status (None | RequestReviewActionParametersStatusType1 | Unset):
        users (list[UUID] | None | Unset):
    """

    share: CreateShareActionParameters
    externals: list[str] | None | Unset = UNSET
    groups: list[UUID] | None | Unset = UNSET
    min_number: int | None | Unset = 1
    status: None | RequestReviewActionParametersStatusType1 | Unset = UNSET
    users: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.request_review_action_parameters_status_type_1 import (
            RequestReviewActionParametersStatusType1,
        )

        share = self.share.to_dict()

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

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, RequestReviewActionParametersStatusType1):
            status = self.status.to_dict()
        else:
            status = self.status

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "share": share,
            }
        )
        if externals is not UNSET:
            field_dict["externals"] = externals
        if groups is not UNSET:
            field_dict["groups"] = groups
        if min_number is not UNSET:
            field_dict["min_number"] = min_number
        if status is not UNSET:
            field_dict["status"] = status
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_share_action_parameters import CreateShareActionParameters
        from ..models.request_review_action_parameters_status_type_1 import (
            RequestReviewActionParametersStatusType1,
        )

        d = dict(src_dict)
        share = CreateShareActionParameters.from_dict(d.pop("share"))

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

        def _parse_status(
            data: object,
        ) -> None | RequestReviewActionParametersStatusType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = RequestReviewActionParametersStatusType1.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RequestReviewActionParametersStatusType1 | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

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

        request_review_action_parameters = cls(
            share=share,
            externals=externals,
            groups=groups,
            min_number=min_number,
            status=status,
            users=users,
        )

        request_review_action_parameters.additional_properties = d
        return request_review_action_parameters

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
