from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_edit_schema_onboarding_goal import UserEditSchemaOnboardingGoal
from ..models.user_edit_schema_status import UserEditSchemaStatus
from ..models.user_edit_schema_type import UserEditSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_system_metadata import UserSystemMetadata


T = TypeVar("T", bound="UserEditSchema")


@_attrs_define
class UserEditSchema:
    """
    Attributes:
        type_ (UserEditSchemaType):
        current_password (str | Unset):
        date_checklist_completed (datetime.datetime | None | Unset):
        date_first_uploaded (datetime.datetime | None | Unset):
        date_returned (datetime.datetime | None | Unset):
        date_terms_accepted (datetime.datetime | None | Unset):
        date_visited_dashboard (datetime.datetime | None | Unset):
        date_welcomed (datetime.datetime | None | Unset):
        description (str | Unset): Available only for admin users
        email (str | Unset):
        email_marketing_consent (bool | None | Unset):
        first_name (None | str | Unset):
        groups (list[UUID] | Unset):
        hide_email (bool | Unset):
        hide_phone (bool | Unset):
        id (UUID | Unset):
        identity_provider_id (UUID | Unset):
        is_admin (bool | Unset):
        is_super_admin (bool | Unset):
        is_super_admin_light (bool | Unset):
        last_name (None | str | Unset):
        last_successful_auth (datetime.datetime | Unset):
        last_unsuccessful_auth (datetime.datetime | Unset):
        last_web_login (datetime.datetime | Unset):
        metadata (Any | Unset):
        onboarding_goal (UserEditSchemaOnboardingGoal | Unset):
        password (str | Unset):
        password_changed (datetime.datetime | Unset):
        phone (str | Unset):
        photo (str | Unset):
        photo_big (str | Unset):
        photo_small (str | Unset):
        primary_group (UUID | Unset):
        status (UserEditSchemaStatus | Unset):
        system_domain_id (UUID | Unset):
        system_domains (list[UUID] | Unset):
        system_metadata (UserSystemMetadata | Unset):
        system_name (str | Unset):
    """

    type_: UserEditSchemaType
    current_password: str | Unset = UNSET
    date_checklist_completed: datetime.datetime | None | Unset = UNSET
    date_first_uploaded: datetime.datetime | None | Unset = UNSET
    date_returned: datetime.datetime | None | Unset = UNSET
    date_terms_accepted: datetime.datetime | None | Unset = UNSET
    date_visited_dashboard: datetime.datetime | None | Unset = UNSET
    date_welcomed: datetime.datetime | None | Unset = UNSET
    description: str | Unset = UNSET
    email: str | Unset = UNSET
    email_marketing_consent: bool | None | Unset = UNSET
    first_name: None | str | Unset = UNSET
    groups: list[UUID] | Unset = UNSET
    hide_email: bool | Unset = UNSET
    hide_phone: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    identity_provider_id: UUID | Unset = UNSET
    is_admin: bool | Unset = UNSET
    is_super_admin: bool | Unset = UNSET
    is_super_admin_light: bool | Unset = UNSET
    last_name: None | str | Unset = UNSET
    last_successful_auth: datetime.datetime | Unset = UNSET
    last_unsuccessful_auth: datetime.datetime | Unset = UNSET
    last_web_login: datetime.datetime | Unset = UNSET
    metadata: Any | Unset = UNSET
    onboarding_goal: UserEditSchemaOnboardingGoal | Unset = UNSET
    password: str | Unset = UNSET
    password_changed: datetime.datetime | Unset = UNSET
    phone: str | Unset = UNSET
    photo: str | Unset = UNSET
    photo_big: str | Unset = UNSET
    photo_small: str | Unset = UNSET
    primary_group: UUID | Unset = UNSET
    status: UserEditSchemaStatus | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    system_domains: list[UUID] | Unset = UNSET
    system_metadata: UserSystemMetadata | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        current_password = self.current_password

        date_checklist_completed: None | str | Unset
        if isinstance(self.date_checklist_completed, Unset):
            date_checklist_completed = UNSET
        elif isinstance(self.date_checklist_completed, datetime.datetime):
            date_checklist_completed = self.date_checklist_completed.isoformat()
        else:
            date_checklist_completed = self.date_checklist_completed

        date_first_uploaded: None | str | Unset
        if isinstance(self.date_first_uploaded, Unset):
            date_first_uploaded = UNSET
        elif isinstance(self.date_first_uploaded, datetime.datetime):
            date_first_uploaded = self.date_first_uploaded.isoformat()
        else:
            date_first_uploaded = self.date_first_uploaded

        date_returned: None | str | Unset
        if isinstance(self.date_returned, Unset):
            date_returned = UNSET
        elif isinstance(self.date_returned, datetime.datetime):
            date_returned = self.date_returned.isoformat()
        else:
            date_returned = self.date_returned

        date_terms_accepted: None | str | Unset
        if isinstance(self.date_terms_accepted, Unset):
            date_terms_accepted = UNSET
        elif isinstance(self.date_terms_accepted, datetime.datetime):
            date_terms_accepted = self.date_terms_accepted.isoformat()
        else:
            date_terms_accepted = self.date_terms_accepted

        date_visited_dashboard: None | str | Unset
        if isinstance(self.date_visited_dashboard, Unset):
            date_visited_dashboard = UNSET
        elif isinstance(self.date_visited_dashboard, datetime.datetime):
            date_visited_dashboard = self.date_visited_dashboard.isoformat()
        else:
            date_visited_dashboard = self.date_visited_dashboard

        date_welcomed: None | str | Unset
        if isinstance(self.date_welcomed, Unset):
            date_welcomed = UNSET
        elif isinstance(self.date_welcomed, datetime.datetime):
            date_welcomed = self.date_welcomed.isoformat()
        else:
            date_welcomed = self.date_welcomed

        description = self.description

        email = self.email

        email_marketing_consent: bool | None | Unset
        if isinstance(self.email_marketing_consent, Unset):
            email_marketing_consent = UNSET
        else:
            email_marketing_consent = self.email_marketing_consent

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = str(groups_item_data)
                groups.append(groups_item)

        hide_email = self.hide_email

        hide_phone = self.hide_phone

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        identity_provider_id: str | Unset = UNSET
        if not isinstance(self.identity_provider_id, Unset):
            identity_provider_id = str(self.identity_provider_id)

        is_admin = self.is_admin

        is_super_admin = self.is_super_admin

        is_super_admin_light = self.is_super_admin_light

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        last_successful_auth: str | Unset = UNSET
        if not isinstance(self.last_successful_auth, Unset):
            last_successful_auth = self.last_successful_auth.isoformat()

        last_unsuccessful_auth: str | Unset = UNSET
        if not isinstance(self.last_unsuccessful_auth, Unset):
            last_unsuccessful_auth = self.last_unsuccessful_auth.isoformat()

        last_web_login: str | Unset = UNSET
        if not isinstance(self.last_web_login, Unset):
            last_web_login = self.last_web_login.isoformat()

        metadata = self.metadata

        onboarding_goal: str | Unset = UNSET
        if not isinstance(self.onboarding_goal, Unset):
            onboarding_goal = self.onboarding_goal.value

        password = self.password

        password_changed: str | Unset = UNSET
        if not isinstance(self.password_changed, Unset):
            password_changed = self.password_changed.isoformat()

        phone = self.phone

        photo = self.photo

        photo_big = self.photo_big

        photo_small = self.photo_small

        primary_group: str | Unset = UNSET
        if not isinstance(self.primary_group, Unset):
            primary_group = str(self.primary_group)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        system_domains: list[str] | Unset = UNSET
        if not isinstance(self.system_domains, Unset):
            system_domains = []
            for system_domains_item_data in self.system_domains:
                system_domains_item = str(system_domains_item_data)
                system_domains.append(system_domains_item)

        system_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.system_metadata, Unset):
            system_metadata = self.system_metadata.to_dict()

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if current_password is not UNSET:
            field_dict["current_password"] = current_password
        if date_checklist_completed is not UNSET:
            field_dict["date_checklist_completed"] = date_checklist_completed
        if date_first_uploaded is not UNSET:
            field_dict["date_first_uploaded"] = date_first_uploaded
        if date_returned is not UNSET:
            field_dict["date_returned"] = date_returned
        if date_terms_accepted is not UNSET:
            field_dict["date_terms_accepted"] = date_terms_accepted
        if date_visited_dashboard is not UNSET:
            field_dict["date_visited_dashboard"] = date_visited_dashboard
        if date_welcomed is not UNSET:
            field_dict["date_welcomed"] = date_welcomed
        if description is not UNSET:
            field_dict["description"] = description
        if email is not UNSET:
            field_dict["email"] = email
        if email_marketing_consent is not UNSET:
            field_dict["email_marketing_consent"] = email_marketing_consent
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if groups is not UNSET:
            field_dict["groups"] = groups
        if hide_email is not UNSET:
            field_dict["hide_email"] = hide_email
        if hide_phone is not UNSET:
            field_dict["hide_phone"] = hide_phone
        if id is not UNSET:
            field_dict["id"] = id
        if identity_provider_id is not UNSET:
            field_dict["identity_provider_id"] = identity_provider_id
        if is_admin is not UNSET:
            field_dict["is_admin"] = is_admin
        if is_super_admin is not UNSET:
            field_dict["is_super_admin"] = is_super_admin
        if is_super_admin_light is not UNSET:
            field_dict["is_super_admin_light"] = is_super_admin_light
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if last_successful_auth is not UNSET:
            field_dict["last_successful_auth"] = last_successful_auth
        if last_unsuccessful_auth is not UNSET:
            field_dict["last_unsuccessful_auth"] = last_unsuccessful_auth
        if last_web_login is not UNSET:
            field_dict["last_web_login"] = last_web_login
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if onboarding_goal is not UNSET:
            field_dict["onboarding_goal"] = onboarding_goal
        if password is not UNSET:
            field_dict["password"] = password
        if password_changed is not UNSET:
            field_dict["password_changed"] = password_changed
        if phone is not UNSET:
            field_dict["phone"] = phone
        if photo is not UNSET:
            field_dict["photo"] = photo
        if photo_big is not UNSET:
            field_dict["photo_big"] = photo_big
        if photo_small is not UNSET:
            field_dict["photo_small"] = photo_small
        if primary_group is not UNSET:
            field_dict["primary_group"] = primary_group
        if status is not UNSET:
            field_dict["status"] = status
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if system_domains is not UNSET:
            field_dict["system_domains"] = system_domains
        if system_metadata is not UNSET:
            field_dict["system_metadata"] = system_metadata
        if system_name is not UNSET:
            field_dict["system_name"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_system_metadata import UserSystemMetadata

        d = dict(src_dict)
        type_ = UserEditSchemaType(d.pop("type"))

        current_password = d.pop("current_password", UNSET)

        def _parse_date_checklist_completed(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_checklist_completed_type_0 = datetime.datetime.fromisoformat(data)

                return date_checklist_completed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_checklist_completed = _parse_date_checklist_completed(
            d.pop("date_checklist_completed", UNSET)
        )

        def _parse_date_first_uploaded(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_first_uploaded_type_0 = datetime.datetime.fromisoformat(data)

                return date_first_uploaded_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_first_uploaded = _parse_date_first_uploaded(
            d.pop("date_first_uploaded", UNSET)
        )

        def _parse_date_returned(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_returned_type_0 = datetime.datetime.fromisoformat(data)

                return date_returned_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_returned = _parse_date_returned(d.pop("date_returned", UNSET))

        def _parse_date_terms_accepted(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_terms_accepted_type_0 = datetime.datetime.fromisoformat(data)

                return date_terms_accepted_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_terms_accepted = _parse_date_terms_accepted(
            d.pop("date_terms_accepted", UNSET)
        )

        def _parse_date_visited_dashboard(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_visited_dashboard_type_0 = datetime.datetime.fromisoformat(data)

                return date_visited_dashboard_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_visited_dashboard = _parse_date_visited_dashboard(
            d.pop("date_visited_dashboard", UNSET)
        )

        def _parse_date_welcomed(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_welcomed_type_0 = datetime.datetime.fromisoformat(data)

                return date_welcomed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_welcomed = _parse_date_welcomed(d.pop("date_welcomed", UNSET))

        description = d.pop("description", UNSET)

        email = d.pop("email", UNSET)

        def _parse_email_marketing_consent(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        email_marketing_consent = _parse_email_marketing_consent(
            d.pop("email_marketing_consent", UNSET)
        )

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        _groups = d.pop("groups", UNSET)
        groups: list[UUID] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = UUID(groups_item_data)

                groups.append(groups_item)

        hide_email = d.pop("hide_email", UNSET)

        hide_phone = d.pop("hide_phone", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _identity_provider_id = d.pop("identity_provider_id", UNSET)
        identity_provider_id: UUID | Unset
        if isinstance(_identity_provider_id, Unset):
            identity_provider_id = UNSET
        else:
            identity_provider_id = UUID(_identity_provider_id)

        is_admin = d.pop("is_admin", UNSET)

        is_super_admin = d.pop("is_super_admin", UNSET)

        is_super_admin_light = d.pop("is_super_admin_light", UNSET)

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        _last_successful_auth = d.pop("last_successful_auth", UNSET)
        last_successful_auth: datetime.datetime | Unset
        if isinstance(_last_successful_auth, Unset):
            last_successful_auth = UNSET
        else:
            last_successful_auth = datetime.datetime.fromisoformat(
                _last_successful_auth
            )

        _last_unsuccessful_auth = d.pop("last_unsuccessful_auth", UNSET)
        last_unsuccessful_auth: datetime.datetime | Unset
        if isinstance(_last_unsuccessful_auth, Unset):
            last_unsuccessful_auth = UNSET
        else:
            last_unsuccessful_auth = datetime.datetime.fromisoformat(
                _last_unsuccessful_auth
            )

        _last_web_login = d.pop("last_web_login", UNSET)
        last_web_login: datetime.datetime | Unset
        if isinstance(_last_web_login, Unset):
            last_web_login = UNSET
        else:
            last_web_login = datetime.datetime.fromisoformat(_last_web_login)

        metadata = d.pop("metadata", UNSET)

        _onboarding_goal = d.pop("onboarding_goal", UNSET)
        onboarding_goal: UserEditSchemaOnboardingGoal | Unset
        if isinstance(_onboarding_goal, Unset):
            onboarding_goal = UNSET
        else:
            onboarding_goal = UserEditSchemaOnboardingGoal(_onboarding_goal)

        password = d.pop("password", UNSET)

        _password_changed = d.pop("password_changed", UNSET)
        password_changed: datetime.datetime | Unset
        if isinstance(_password_changed, Unset):
            password_changed = UNSET
        else:
            password_changed = datetime.datetime.fromisoformat(_password_changed)

        phone = d.pop("phone", UNSET)

        photo = d.pop("photo", UNSET)

        photo_big = d.pop("photo_big", UNSET)

        photo_small = d.pop("photo_small", UNSET)

        _primary_group = d.pop("primary_group", UNSET)
        primary_group: UUID | Unset
        if isinstance(_primary_group, Unset):
            primary_group = UNSET
        else:
            primary_group = UUID(_primary_group)

        _status = d.pop("status", UNSET)
        status: UserEditSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UserEditSchemaStatus(_status)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        _system_domains = d.pop("system_domains", UNSET)
        system_domains: list[UUID] | Unset = UNSET
        if _system_domains is not UNSET:
            system_domains = []
            for system_domains_item_data in _system_domains:
                system_domains_item = UUID(system_domains_item_data)

                system_domains.append(system_domains_item)

        _system_metadata = d.pop("system_metadata", UNSET)
        system_metadata: UserSystemMetadata | Unset
        if isinstance(_system_metadata, Unset):
            system_metadata = UNSET
        else:
            system_metadata = UserSystemMetadata.from_dict(_system_metadata)

        system_name = d.pop("system_name", UNSET)

        user_edit_schema = cls(
            type_=type_,
            current_password=current_password,
            date_checklist_completed=date_checklist_completed,
            date_first_uploaded=date_first_uploaded,
            date_returned=date_returned,
            date_terms_accepted=date_terms_accepted,
            date_visited_dashboard=date_visited_dashboard,
            date_welcomed=date_welcomed,
            description=description,
            email=email,
            email_marketing_consent=email_marketing_consent,
            first_name=first_name,
            groups=groups,
            hide_email=hide_email,
            hide_phone=hide_phone,
            id=id,
            identity_provider_id=identity_provider_id,
            is_admin=is_admin,
            is_super_admin=is_super_admin,
            is_super_admin_light=is_super_admin_light,
            last_name=last_name,
            last_successful_auth=last_successful_auth,
            last_unsuccessful_auth=last_unsuccessful_auth,
            last_web_login=last_web_login,
            metadata=metadata,
            onboarding_goal=onboarding_goal,
            password=password,
            password_changed=password_changed,
            phone=phone,
            photo=photo,
            photo_big=photo_big,
            photo_small=photo_small,
            primary_group=primary_group,
            status=status,
            system_domain_id=system_domain_id,
            system_domains=system_domains,
            system_metadata=system_metadata,
            system_name=system_name,
        )

        user_edit_schema.additional_properties = d
        return user_edit_schema

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
