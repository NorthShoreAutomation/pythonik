from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_with_separated_groups_schema_type import (
    UserWithSeparatedGroupsSchemaType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_system_metadata_schema import UserSystemMetadataSchema
    from ..models.user_with_separated_groups_schema_onboarding_goal_type_1 import (
        UserWithSeparatedGroupsSchemaOnboardingGoalType1,
    )
    from ..models.user_with_separated_groups_schema_status_type_1 import (
        UserWithSeparatedGroupsSchemaStatusType1,
    )


T = TypeVar("T", bound="UserWithSeparatedGroupsSchema")


@_attrs_define
class UserWithSeparatedGroupsSchema:
    """
    Attributes:
        type_ (UserWithSeparatedGroupsSchemaType):
        app_id (None | Unset | UUID):
        date_checklist_completed (datetime.datetime | None | Unset):
        date_created (datetime.datetime | None | Unset):
        date_first_uploaded (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        date_returned (datetime.datetime | None | Unset):
        date_terms_accepted (datetime.datetime | None | Unset):
        date_visited_dashboard (datetime.datetime | None | Unset):
        date_welcomed (datetime.datetime | None | Unset):
        description (None | str | Unset): Available only for admin users
        disable_mixpanel (bool | None | Unset):
        email (None | str | Unset):
        email_marketing_consent (bool | None | Unset):
        first_name (None | str | Unset):
        groups (list[UUID] | None | Unset):
        has_domain_been_migrated_to_simplified_acls (bool | None | Unset):
        hide_email (bool | None | Unset):
        hide_phone (bool | None | Unset):
        id (None | Unset | UUID):
        identity_provider_id (None | Unset | UUID):
        is_admin (bool | None | Unset):
        is_super_admin (bool | None | Unset):
        is_super_admin_light (bool | None | Unset):
        last_name (None | str | Unset):
        last_successful_auth (datetime.datetime | None | Unset):
        last_unsuccessful_auth (datetime.datetime | None | Unset):
        last_web_login (datetime.datetime | None | Unset):
        metadata (Any | Unset):
        onboarding_goal (None | Unset | UserWithSeparatedGroupsSchemaOnboardingGoalType1):
        password (None | str | Unset):
        password_changed (datetime.datetime | None | Unset):
        phone (None | str | Unset):
        photo (None | str | Unset):
        photo_big (None | str | Unset):
        photo_small (None | str | Unset):
        photo_storage_id (None | Unset | UUID):
        primary_group (None | Unset | UUID):
        role_groups (list[UUID] | None | Unset):
        status (None | Unset | UserWithSeparatedGroupsSchemaStatusType1):
        system_domain_id (None | Unset | UUID):
        system_domains (list[UUID] | None | Unset):
        system_metadata (None | Unset | UserSystemMetadataSchema):
        system_name (None | str | Unset):
        teams (list[UUID] | None | Unset):
    """

    type_: UserWithSeparatedGroupsSchemaType
    app_id: None | Unset | UUID = UNSET
    date_checklist_completed: datetime.datetime | None | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_first_uploaded: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    date_returned: datetime.datetime | None | Unset = UNSET
    date_terms_accepted: datetime.datetime | None | Unset = UNSET
    date_visited_dashboard: datetime.datetime | None | Unset = UNSET
    date_welcomed: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    disable_mixpanel: bool | None | Unset = UNSET
    email: None | str | Unset = UNSET
    email_marketing_consent: bool | None | Unset = UNSET
    first_name: None | str | Unset = UNSET
    groups: list[UUID] | None | Unset = UNSET
    has_domain_been_migrated_to_simplified_acls: bool | None | Unset = UNSET
    hide_email: bool | None | Unset = UNSET
    hide_phone: bool | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    identity_provider_id: None | Unset | UUID = UNSET
    is_admin: bool | None | Unset = UNSET
    is_super_admin: bool | None | Unset = UNSET
    is_super_admin_light: bool | None | Unset = UNSET
    last_name: None | str | Unset = UNSET
    last_successful_auth: datetime.datetime | None | Unset = UNSET
    last_unsuccessful_auth: datetime.datetime | None | Unset = UNSET
    last_web_login: datetime.datetime | None | Unset = UNSET
    metadata: Any | Unset = UNSET
    onboarding_goal: None | Unset | UserWithSeparatedGroupsSchemaOnboardingGoalType1 = (
        UNSET
    )
    password: None | str | Unset = UNSET
    password_changed: datetime.datetime | None | Unset = UNSET
    phone: None | str | Unset = UNSET
    photo: None | str | Unset = UNSET
    photo_big: None | str | Unset = UNSET
    photo_small: None | str | Unset = UNSET
    photo_storage_id: None | Unset | UUID = UNSET
    primary_group: None | Unset | UUID = UNSET
    role_groups: list[UUID] | None | Unset = UNSET
    status: None | Unset | UserWithSeparatedGroupsSchemaStatusType1 = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    system_domains: list[UUID] | None | Unset = UNSET
    system_metadata: None | Unset | UserSystemMetadataSchema = UNSET
    system_name: None | str | Unset = UNSET
    teams: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_system_metadata_schema import UserSystemMetadataSchema
        from ..models.user_with_separated_groups_schema_onboarding_goal_type_1 import (
            UserWithSeparatedGroupsSchemaOnboardingGoalType1,
        )
        from ..models.user_with_separated_groups_schema_status_type_1 import (
            UserWithSeparatedGroupsSchemaStatusType1,
        )

        type_ = self.type_.value

        app_id: None | str | Unset
        if isinstance(self.app_id, Unset):
            app_id = UNSET
        elif isinstance(self.app_id, UUID):
            app_id = str(self.app_id)
        else:
            app_id = self.app_id

        date_checklist_completed: None | str | Unset
        if isinstance(self.date_checklist_completed, Unset):
            date_checklist_completed = UNSET
        elif isinstance(self.date_checklist_completed, datetime.datetime):
            date_checklist_completed = self.date_checklist_completed.isoformat()
        else:
            date_checklist_completed = self.date_checklist_completed

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_first_uploaded: None | str | Unset
        if isinstance(self.date_first_uploaded, Unset):
            date_first_uploaded = UNSET
        elif isinstance(self.date_first_uploaded, datetime.datetime):
            date_first_uploaded = self.date_first_uploaded.isoformat()
        else:
            date_first_uploaded = self.date_first_uploaded

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

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

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        disable_mixpanel: bool | None | Unset
        if isinstance(self.disable_mixpanel, Unset):
            disable_mixpanel = UNSET
        else:
            disable_mixpanel = self.disable_mixpanel

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
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

        has_domain_been_migrated_to_simplified_acls: bool | None | Unset
        if isinstance(self.has_domain_been_migrated_to_simplified_acls, Unset):
            has_domain_been_migrated_to_simplified_acls = UNSET
        else:
            has_domain_been_migrated_to_simplified_acls = (
                self.has_domain_been_migrated_to_simplified_acls
            )

        hide_email: bool | None | Unset
        if isinstance(self.hide_email, Unset):
            hide_email = UNSET
        else:
            hide_email = self.hide_email

        hide_phone: bool | None | Unset
        if isinstance(self.hide_phone, Unset):
            hide_phone = UNSET
        else:
            hide_phone = self.hide_phone

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        identity_provider_id: None | str | Unset
        if isinstance(self.identity_provider_id, Unset):
            identity_provider_id = UNSET
        elif isinstance(self.identity_provider_id, UUID):
            identity_provider_id = str(self.identity_provider_id)
        else:
            identity_provider_id = self.identity_provider_id

        is_admin: bool | None | Unset
        if isinstance(self.is_admin, Unset):
            is_admin = UNSET
        else:
            is_admin = self.is_admin

        is_super_admin: bool | None | Unset
        if isinstance(self.is_super_admin, Unset):
            is_super_admin = UNSET
        else:
            is_super_admin = self.is_super_admin

        is_super_admin_light: bool | None | Unset
        if isinstance(self.is_super_admin_light, Unset):
            is_super_admin_light = UNSET
        else:
            is_super_admin_light = self.is_super_admin_light

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        last_successful_auth: None | str | Unset
        if isinstance(self.last_successful_auth, Unset):
            last_successful_auth = UNSET
        elif isinstance(self.last_successful_auth, datetime.datetime):
            last_successful_auth = self.last_successful_auth.isoformat()
        else:
            last_successful_auth = self.last_successful_auth

        last_unsuccessful_auth: None | str | Unset
        if isinstance(self.last_unsuccessful_auth, Unset):
            last_unsuccessful_auth = UNSET
        elif isinstance(self.last_unsuccessful_auth, datetime.datetime):
            last_unsuccessful_auth = self.last_unsuccessful_auth.isoformat()
        else:
            last_unsuccessful_auth = self.last_unsuccessful_auth

        last_web_login: None | str | Unset
        if isinstance(self.last_web_login, Unset):
            last_web_login = UNSET
        elif isinstance(self.last_web_login, datetime.datetime):
            last_web_login = self.last_web_login.isoformat()
        else:
            last_web_login = self.last_web_login

        metadata = self.metadata

        onboarding_goal: dict[str, Any] | None | Unset
        if isinstance(self.onboarding_goal, Unset):
            onboarding_goal = UNSET
        elif isinstance(
            self.onboarding_goal, UserWithSeparatedGroupsSchemaOnboardingGoalType1
        ):
            onboarding_goal = self.onboarding_goal.to_dict()
        else:
            onboarding_goal = self.onboarding_goal

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        password_changed: None | str | Unset
        if isinstance(self.password_changed, Unset):
            password_changed = UNSET
        elif isinstance(self.password_changed, datetime.datetime):
            password_changed = self.password_changed.isoformat()
        else:
            password_changed = self.password_changed

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        photo: None | str | Unset
        if isinstance(self.photo, Unset):
            photo = UNSET
        else:
            photo = self.photo

        photo_big: None | str | Unset
        if isinstance(self.photo_big, Unset):
            photo_big = UNSET
        else:
            photo_big = self.photo_big

        photo_small: None | str | Unset
        if isinstance(self.photo_small, Unset):
            photo_small = UNSET
        else:
            photo_small = self.photo_small

        photo_storage_id: None | str | Unset
        if isinstance(self.photo_storage_id, Unset):
            photo_storage_id = UNSET
        elif isinstance(self.photo_storage_id, UUID):
            photo_storage_id = str(self.photo_storage_id)
        else:
            photo_storage_id = self.photo_storage_id

        primary_group: None | str | Unset
        if isinstance(self.primary_group, Unset):
            primary_group = UNSET
        elif isinstance(self.primary_group, UUID):
            primary_group = str(self.primary_group)
        else:
            primary_group = self.primary_group

        role_groups: list[str] | None | Unset
        if isinstance(self.role_groups, Unset):
            role_groups = UNSET
        elif isinstance(self.role_groups, list):
            role_groups = []
            for role_groups_type_0_item_data in self.role_groups:
                role_groups_type_0_item = str(role_groups_type_0_item_data)
                role_groups.append(role_groups_type_0_item)

        else:
            role_groups = self.role_groups

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, UserWithSeparatedGroupsSchemaStatusType1):
            status = self.status.to_dict()
        else:
            status = self.status

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

        system_domains: list[str] | None | Unset
        if isinstance(self.system_domains, Unset):
            system_domains = UNSET
        elif isinstance(self.system_domains, list):
            system_domains = []
            for system_domains_type_0_item_data in self.system_domains:
                system_domains_type_0_item = str(system_domains_type_0_item_data)
                system_domains.append(system_domains_type_0_item)

        else:
            system_domains = self.system_domains

        system_metadata: dict[str, Any] | None | Unset
        if isinstance(self.system_metadata, Unset):
            system_metadata = UNSET
        elif isinstance(self.system_metadata, UserSystemMetadataSchema):
            system_metadata = self.system_metadata.to_dict()
        else:
            system_metadata = self.system_metadata

        system_name: None | str | Unset
        if isinstance(self.system_name, Unset):
            system_name = UNSET
        else:
            system_name = self.system_name

        teams: list[str] | None | Unset
        if isinstance(self.teams, Unset):
            teams = UNSET
        elif isinstance(self.teams, list):
            teams = []
            for teams_type_0_item_data in self.teams:
                teams_type_0_item = str(teams_type_0_item_data)
                teams.append(teams_type_0_item)

        else:
            teams = self.teams

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if date_checklist_completed is not UNSET:
            field_dict["date_checklist_completed"] = date_checklist_completed
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_first_uploaded is not UNSET:
            field_dict["date_first_uploaded"] = date_first_uploaded
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
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
        if disable_mixpanel is not UNSET:
            field_dict["disable_mixpanel"] = disable_mixpanel
        if email is not UNSET:
            field_dict["email"] = email
        if email_marketing_consent is not UNSET:
            field_dict["email_marketing_consent"] = email_marketing_consent
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if groups is not UNSET:
            field_dict["groups"] = groups
        if has_domain_been_migrated_to_simplified_acls is not UNSET:
            field_dict["has_domain_been_migrated_to_simplified_acls"] = (
                has_domain_been_migrated_to_simplified_acls
            )
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
        if photo_storage_id is not UNSET:
            field_dict["photo_storage_id"] = photo_storage_id
        if primary_group is not UNSET:
            field_dict["primary_group"] = primary_group
        if role_groups is not UNSET:
            field_dict["role_groups"] = role_groups
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
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_system_metadata_schema import UserSystemMetadataSchema
        from ..models.user_with_separated_groups_schema_onboarding_goal_type_1 import (
            UserWithSeparatedGroupsSchemaOnboardingGoalType1,
        )
        from ..models.user_with_separated_groups_schema_status_type_1 import (
            UserWithSeparatedGroupsSchemaStatusType1,
        )

        d = dict(src_dict)
        type_ = UserWithSeparatedGroupsSchemaType(d.pop("type"))

        def _parse_app_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                app_id_type_0 = UUID(data)

                return app_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        app_id = _parse_app_id(d.pop("app_id", UNSET))

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

        def _parse_date_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_modified_type_0 = datetime.datetime.fromisoformat(data)

                return date_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_modified = _parse_date_modified(d.pop("date_modified", UNSET))

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_disable_mixpanel(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        disable_mixpanel = _parse_disable_mixpanel(d.pop("disable_mixpanel", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

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

        def _parse_has_domain_been_migrated_to_simplified_acls(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_domain_been_migrated_to_simplified_acls = (
            _parse_has_domain_been_migrated_to_simplified_acls(
                d.pop("has_domain_been_migrated_to_simplified_acls", UNSET)
            )
        )

        def _parse_hide_email(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hide_email = _parse_hide_email(d.pop("hide_email", UNSET))

        def _parse_hide_phone(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hide_phone = _parse_hide_phone(d.pop("hide_phone", UNSET))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_identity_provider_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                identity_provider_id_type_0 = UUID(data)

                return identity_provider_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        identity_provider_id = _parse_identity_provider_id(
            d.pop("identity_provider_id", UNSET)
        )

        def _parse_is_admin(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_admin = _parse_is_admin(d.pop("is_admin", UNSET))

        def _parse_is_super_admin(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_super_admin = _parse_is_super_admin(d.pop("is_super_admin", UNSET))

        def _parse_is_super_admin_light(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_super_admin_light = _parse_is_super_admin_light(
            d.pop("is_super_admin_light", UNSET)
        )

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_last_successful_auth(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_successful_auth_type_0 = datetime.datetime.fromisoformat(data)

                return last_successful_auth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_successful_auth = _parse_last_successful_auth(
            d.pop("last_successful_auth", UNSET)
        )

        def _parse_last_unsuccessful_auth(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_unsuccessful_auth_type_0 = datetime.datetime.fromisoformat(data)

                return last_unsuccessful_auth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_unsuccessful_auth = _parse_last_unsuccessful_auth(
            d.pop("last_unsuccessful_auth", UNSET)
        )

        def _parse_last_web_login(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_web_login_type_0 = datetime.datetime.fromisoformat(data)

                return last_web_login_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_web_login = _parse_last_web_login(d.pop("last_web_login", UNSET))

        metadata = d.pop("metadata", UNSET)

        def _parse_onboarding_goal(
            data: object,
        ) -> None | Unset | UserWithSeparatedGroupsSchemaOnboardingGoalType1:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                onboarding_goal_type_1 = (
                    UserWithSeparatedGroupsSchemaOnboardingGoalType1.from_dict(data)
                )

                return onboarding_goal_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | Unset | UserWithSeparatedGroupsSchemaOnboardingGoalType1, data
            )

        onboarding_goal = _parse_onboarding_goal(d.pop("onboarding_goal", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_password_changed(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                password_changed_type_0 = datetime.datetime.fromisoformat(data)

                return password_changed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        password_changed = _parse_password_changed(d.pop("password_changed", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_photo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo = _parse_photo(d.pop("photo", UNSET))

        def _parse_photo_big(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_big = _parse_photo_big(d.pop("photo_big", UNSET))

        def _parse_photo_small(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_small = _parse_photo_small(d.pop("photo_small", UNSET))

        def _parse_photo_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                photo_storage_id_type_0 = UUID(data)

                return photo_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        photo_storage_id = _parse_photo_storage_id(d.pop("photo_storage_id", UNSET))

        def _parse_primary_group(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                primary_group_type_0 = UUID(data)

                return primary_group_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        primary_group = _parse_primary_group(d.pop("primary_group", UNSET))

        def _parse_role_groups(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                role_groups_type_0 = []
                _role_groups_type_0 = data
                for role_groups_type_0_item_data in _role_groups_type_0:
                    role_groups_type_0_item = UUID(role_groups_type_0_item_data)

                    role_groups_type_0.append(role_groups_type_0_item)

                return role_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        role_groups = _parse_role_groups(d.pop("role_groups", UNSET))

        def _parse_status(
            data: object,
        ) -> None | Unset | UserWithSeparatedGroupsSchemaStatusType1:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = UserWithSeparatedGroupsSchemaStatusType1.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserWithSeparatedGroupsSchemaStatusType1, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_system_domain_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                system_domain_id_type_0 = UUID(data)

                return system_domain_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        system_domain_id = _parse_system_domain_id(d.pop("system_domain_id", UNSET))

        def _parse_system_domains(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                system_domains_type_0 = []
                _system_domains_type_0 = data
                for system_domains_type_0_item_data in _system_domains_type_0:
                    system_domains_type_0_item = UUID(system_domains_type_0_item_data)

                    system_domains_type_0.append(system_domains_type_0_item)

                return system_domains_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        system_domains = _parse_system_domains(d.pop("system_domains", UNSET))

        def _parse_system_metadata(
            data: object,
        ) -> None | Unset | UserSystemMetadataSchema:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                system_metadata_type_1 = UserSystemMetadataSchema.from_dict(data)

                return system_metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserSystemMetadataSchema, data)

        system_metadata = _parse_system_metadata(d.pop("system_metadata", UNSET))

        def _parse_system_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_name = _parse_system_name(d.pop("system_name", UNSET))

        def _parse_teams(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                teams_type_0 = []
                _teams_type_0 = data
                for teams_type_0_item_data in _teams_type_0:
                    teams_type_0_item = UUID(teams_type_0_item_data)

                    teams_type_0.append(teams_type_0_item)

                return teams_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        teams = _parse_teams(d.pop("teams", UNSET))

        user_with_separated_groups_schema = cls(
            type_=type_,
            app_id=app_id,
            date_checklist_completed=date_checklist_completed,
            date_created=date_created,
            date_first_uploaded=date_first_uploaded,
            date_modified=date_modified,
            date_returned=date_returned,
            date_terms_accepted=date_terms_accepted,
            date_visited_dashboard=date_visited_dashboard,
            date_welcomed=date_welcomed,
            description=description,
            disable_mixpanel=disable_mixpanel,
            email=email,
            email_marketing_consent=email_marketing_consent,
            first_name=first_name,
            groups=groups,
            has_domain_been_migrated_to_simplified_acls=has_domain_been_migrated_to_simplified_acls,
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
            photo_storage_id=photo_storage_id,
            primary_group=primary_group,
            role_groups=role_groups,
            status=status,
            system_domain_id=system_domain_id,
            system_domains=system_domains,
            system_metadata=system_metadata,
            system_name=system_name,
            teams=teams,
        )

        user_with_separated_groups_schema.additional_properties = d
        return user_with_separated_groups_schema

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
