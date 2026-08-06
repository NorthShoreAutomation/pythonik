from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoleCategoriesSchema")


@_attrs_define
class RoleCategoriesSchema:
    """
    Attributes:
        assets_edit (bool | None | Unset):
        billing (bool | None | Unset):
        collaborate (bool | None | Unset):
        core (bool | None | Unset):
        download (bool | None | Unset):
        face_recognition (bool | None | Unset):
        integrations_admin (bool | None | Unset):
        metadata_admin (bool | None | Unset):
        organize (bool | None | Unset):
        others (bool | None | Unset):
        storage_admin (bool | None | Unset):
        upload (bool | None | Unset):
        users_groups_admin (bool | None | Unset):
    """

    assets_edit: bool | None | Unset = UNSET
    billing: bool | None | Unset = UNSET
    collaborate: bool | None | Unset = UNSET
    core: bool | None | Unset = UNSET
    download: bool | None | Unset = UNSET
    face_recognition: bool | None | Unset = UNSET
    integrations_admin: bool | None | Unset = UNSET
    metadata_admin: bool | None | Unset = UNSET
    organize: bool | None | Unset = UNSET
    others: bool | None | Unset = UNSET
    storage_admin: bool | None | Unset = UNSET
    upload: bool | None | Unset = UNSET
    users_groups_admin: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assets_edit: bool | None | Unset
        if isinstance(self.assets_edit, Unset):
            assets_edit = UNSET
        else:
            assets_edit = self.assets_edit

        billing: bool | None | Unset
        if isinstance(self.billing, Unset):
            billing = UNSET
        else:
            billing = self.billing

        collaborate: bool | None | Unset
        if isinstance(self.collaborate, Unset):
            collaborate = UNSET
        else:
            collaborate = self.collaborate

        core: bool | None | Unset
        if isinstance(self.core, Unset):
            core = UNSET
        else:
            core = self.core

        download: bool | None | Unset
        if isinstance(self.download, Unset):
            download = UNSET
        else:
            download = self.download

        face_recognition: bool | None | Unset
        if isinstance(self.face_recognition, Unset):
            face_recognition = UNSET
        else:
            face_recognition = self.face_recognition

        integrations_admin: bool | None | Unset
        if isinstance(self.integrations_admin, Unset):
            integrations_admin = UNSET
        else:
            integrations_admin = self.integrations_admin

        metadata_admin: bool | None | Unset
        if isinstance(self.metadata_admin, Unset):
            metadata_admin = UNSET
        else:
            metadata_admin = self.metadata_admin

        organize: bool | None | Unset
        if isinstance(self.organize, Unset):
            organize = UNSET
        else:
            organize = self.organize

        others: bool | None | Unset
        if isinstance(self.others, Unset):
            others = UNSET
        else:
            others = self.others

        storage_admin: bool | None | Unset
        if isinstance(self.storage_admin, Unset):
            storage_admin = UNSET
        else:
            storage_admin = self.storage_admin

        upload: bool | None | Unset
        if isinstance(self.upload, Unset):
            upload = UNSET
        else:
            upload = self.upload

        users_groups_admin: bool | None | Unset
        if isinstance(self.users_groups_admin, Unset):
            users_groups_admin = UNSET
        else:
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

        def _parse_assets_edit(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        assets_edit = _parse_assets_edit(d.pop("assets_edit", UNSET))

        def _parse_billing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        billing = _parse_billing(d.pop("billing", UNSET))

        def _parse_collaborate(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        collaborate = _parse_collaborate(d.pop("collaborate", UNSET))

        def _parse_core(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        core = _parse_core(d.pop("core", UNSET))

        def _parse_download(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        download = _parse_download(d.pop("download", UNSET))

        def _parse_face_recognition(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        face_recognition = _parse_face_recognition(d.pop("face_recognition", UNSET))

        def _parse_integrations_admin(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        integrations_admin = _parse_integrations_admin(
            d.pop("integrations_admin", UNSET)
        )

        def _parse_metadata_admin(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        metadata_admin = _parse_metadata_admin(d.pop("metadata_admin", UNSET))

        def _parse_organize(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        organize = _parse_organize(d.pop("organize", UNSET))

        def _parse_others(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        others = _parse_others(d.pop("others", UNSET))

        def _parse_storage_admin(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        storage_admin = _parse_storage_admin(d.pop("storage_admin", UNSET))

        def _parse_upload(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        upload = _parse_upload(d.pop("upload", UNSET))

        def _parse_users_groups_admin(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        users_groups_admin = _parse_users_groups_admin(
            d.pop("users_groups_admin", UNSET)
        )

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
