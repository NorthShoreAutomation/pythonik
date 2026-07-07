from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_review_action_parameters_status import (
    RequestReviewActionParametersStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_share_action_parameters import CreateShareActionParameters


T = TypeVar("T", bound="RequestReviewActionParameters")


@_attrs_define
class RequestReviewActionParameters:
    """
    Attributes:
        share (CreateShareActionParameters):
        externals (list[str] | Unset):
        groups (list[UUID] | Unset):
        min_number (int | Unset):  Default: 1.
        status (RequestReviewActionParametersStatus | Unset):
        users (list[UUID] | Unset):
    """

    share: CreateShareActionParameters
    externals: list[str] | Unset = UNSET
    groups: list[UUID] | Unset = UNSET
    min_number: int | Unset = 1
    status: RequestReviewActionParametersStatus | Unset = UNSET
    users: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        share = self.share.to_dict()

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

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        users: list[str] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = str(users_item_data)
                users.append(users_item)

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

        d = dict(src_dict)
        share = CreateShareActionParameters.from_dict(d.pop("share"))

        externals = cast(list[str], d.pop("externals", UNSET))

        _groups = d.pop("groups", UNSET)
        groups: list[UUID] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = UUID(groups_item_data)

                groups.append(groups_item)

        min_number = d.pop("min_number", UNSET)

        _status = d.pop("status", UNSET)
        status: RequestReviewActionParametersStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RequestReviewActionParametersStatus(_status)

        _users = d.pop("users", UNSET)
        users: list[UUID] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = UUID(users_item_data)

                users.append(users_item)

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
