from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.person_by_asset_and_version_in_admin_status import (
    PersonByAssetAndVersionInAdminStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonByAssetAndVersionInAdmin")


@_attrs_define
class PersonByAssetAndVersionInAdmin:
    """
    Attributes:
        asset_id (UUID):
        asset_title (str):
        created_by_user (None | UUID):
        date_created (datetime.datetime):
        date_modified (datetime.datetime):
        has_unconfirmed_instances (bool):
        id (UUID):
        image_url (None | str):
        main_face_id (None | UUID):
        name (None | str):
        person_version_face_id (UUID):
        person_version_face_image_url (None | str):
        status (PersonByAssetAndVersionInAdminStatus):
        version_id (UUID):
        system_domain_id (UUID | Unset):
        version_number (str | Unset):
    """

    asset_id: UUID
    asset_title: str
    created_by_user: None | UUID
    date_created: datetime.datetime
    date_modified: datetime.datetime
    has_unconfirmed_instances: bool
    id: UUID
    image_url: None | str
    main_face_id: None | UUID
    name: None | str
    person_version_face_id: UUID
    person_version_face_image_url: None | str
    status: PersonByAssetAndVersionInAdminStatus
    version_id: UUID
    system_domain_id: UUID | Unset = UNSET
    version_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = str(self.asset_id)

        asset_title = self.asset_title

        created_by_user: None | str
        if isinstance(self.created_by_user, UUID):
            created_by_user = str(self.created_by_user)
        else:
            created_by_user = self.created_by_user

        date_created = self.date_created.isoformat()

        date_modified = self.date_modified.isoformat()

        has_unconfirmed_instances = self.has_unconfirmed_instances

        id = str(self.id)

        image_url: None | str
        image_url = self.image_url

        main_face_id: None | str
        if isinstance(self.main_face_id, UUID):
            main_face_id = str(self.main_face_id)
        else:
            main_face_id = self.main_face_id

        name: None | str
        name = self.name

        person_version_face_id = str(self.person_version_face_id)

        person_version_face_image_url: None | str
        person_version_face_image_url = self.person_version_face_image_url

        status = self.status.value

        version_id = str(self.version_id)

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        version_number = self.version_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
                "asset_title": asset_title,
                "created_by_user": created_by_user,
                "date_created": date_created,
                "date_modified": date_modified,
                "has_unconfirmed_instances": has_unconfirmed_instances,
                "id": id,
                "image_url": image_url,
                "main_face_id": main_face_id,
                "name": name,
                "person_version_face_id": person_version_face_id,
                "person_version_face_image_url": person_version_face_image_url,
                "status": status,
                "version_id": version_id,
            }
        )
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if version_number is not UNSET:
            field_dict["version_number"] = version_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = UUID(d.pop("asset_id"))

        asset_title = d.pop("asset_title")

        def _parse_created_by_user(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_user_type_0 = UUID(data)

                return created_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        created_by_user = _parse_created_by_user(d.pop("created_by_user"))

        date_created = datetime.datetime.fromisoformat(d.pop("date_created"))

        date_modified = datetime.datetime.fromisoformat(d.pop("date_modified"))

        has_unconfirmed_instances = d.pop("has_unconfirmed_instances")

        id = UUID(d.pop("id"))

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("image_url"))

        def _parse_main_face_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                main_face_id_type_0 = UUID(data)

                return main_face_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        main_face_id = _parse_main_face_id(d.pop("main_face_id"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        person_version_face_id = UUID(d.pop("person_version_face_id"))

        def _parse_person_version_face_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        person_version_face_image_url = _parse_person_version_face_image_url(
            d.pop("person_version_face_image_url")
        )

        status = PersonByAssetAndVersionInAdminStatus(d.pop("status"))

        version_id = UUID(d.pop("version_id"))

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        version_number = d.pop("version_number", UNSET)

        person_by_asset_and_version_in_admin = cls(
            asset_id=asset_id,
            asset_title=asset_title,
            created_by_user=created_by_user,
            date_created=date_created,
            date_modified=date_modified,
            has_unconfirmed_instances=has_unconfirmed_instances,
            id=id,
            image_url=image_url,
            main_face_id=main_face_id,
            name=name,
            person_version_face_id=person_version_face_id,
            person_version_face_image_url=person_version_face_image_url,
            status=status,
            version_id=version_id,
            system_domain_id=system_domain_id,
            version_number=version_number,
        )

        person_by_asset_and_version_in_admin.additional_properties = d
        return person_by_asset_and_version_in_admin

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
