from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoleCategoriesSchema")


@_attrs_define
class RoleCategoriesSchema:
    """
    Attributes:
        assets_edit (bool | Unset):
        billing (bool | Unset):
        collaborate (bool | Unset):
        core (bool | Unset):
        download (bool | Unset):
        face_recognition (bool | Unset):
        integrations_admin (bool | Unset):
        metadata_admin (bool | Unset):
        organize (bool | Unset):
        others (bool | Unset):
        storage_admin (bool | Unset):
        upload (bool | Unset):
        users_groups_admin (bool | Unset):
    """

    assets_edit: bool | Unset = UNSET
    billing: bool | Unset = UNSET
    collaborate: bool | Unset = UNSET
    core: bool | Unset = UNSET
    download: bool | Unset = UNSET
    face_recognition: bool | Unset = UNSET
    integrations_admin: bool | Unset = UNSET
    metadata_admin: bool | Unset = UNSET
    organize: bool | Unset = UNSET
    others: bool | Unset = UNSET
    storage_admin: bool | Unset = UNSET
    upload: bool | Unset = UNSET
    users_groups_admin: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets_edit = self.assets_edit

        billing = self.billing

        collaborate = self.collaborate

        core = self.core

        download = self.download

        face_recognition = self.face_recognition

        integrations_admin = self.integrations_admin

        metadata_admin = self.metadata_admin

        organize = self.organize

        others = self.others

        storage_admin = self.storage_admin

        upload = self.upload

        users_groups_admin = self.users_groups_admin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assets_edit is not UNSET:
            field_dict["assets_edit"] = assets_edit
        if billing is not UNSET:
            field_dict["billing"] = billing
        if collaborate is not UNSET:
            field_dict["collaborate"] = collaborate
        if core is not UNSET:
            field_dict["core"] = core
        if download is not UNSET:
            field_dict["download"] = download
        if face_recognition is not UNSET:
            field_dict["face_recognition"] = face_recognition
        if integrations_admin is not UNSET:
            field_dict["integrations_admin"] = integrations_admin
        if metadata_admin is not UNSET:
            field_dict["metadata_admin"] = metadata_admin
        if organize is not UNSET:
            field_dict["organize"] = organize
        if others is not UNSET:
            field_dict["others"] = others
        if storage_admin is not UNSET:
            field_dict["storage_admin"] = storage_admin
        if upload is not UNSET:
            field_dict["upload"] = upload
        if users_groups_admin is not UNSET:
            field_dict["users_groups_admin"] = users_groups_admin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assets_edit = d.pop("assets_edit", UNSET)

        billing = d.pop("billing", UNSET)

        collaborate = d.pop("collaborate", UNSET)

        core = d.pop("core", UNSET)

        download = d.pop("download", UNSET)

        face_recognition = d.pop("face_recognition", UNSET)

        integrations_admin = d.pop("integrations_admin", UNSET)

        metadata_admin = d.pop("metadata_admin", UNSET)

        organize = d.pop("organize", UNSET)

        others = d.pop("others", UNSET)

        storage_admin = d.pop("storage_admin", UNSET)

        upload = d.pop("upload", UNSET)

        users_groups_admin = d.pop("users_groups_admin", UNSET)

        role_categories_schema = cls(
            assets_edit=assets_edit,
            billing=billing,
            collaborate=collaborate,
            core=core,
            download=download,
            face_recognition=face_recognition,
            integrations_admin=integrations_admin,
            metadata_admin=metadata_admin,
            organize=organize,
            others=others,
            storage_admin=storage_admin,
            upload=upload,
            users_groups_admin=users_groups_admin,
        )

        role_categories_schema.additional_properties = d
        return role_categories_schema

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
