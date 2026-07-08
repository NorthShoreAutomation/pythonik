from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_action_schema_context import CustomActionSchemaContext
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_action_schema_headers_type_0 import (
        CustomActionSchemaHeadersType0,
    )
    from ..models.custom_action_schema_status_type_1 import (
        CustomActionSchemaStatusType1,
    )
    from ..models.custom_action_schema_type_type_1 import CustomActionSchemaTypeType1


T = TypeVar("T", bound="CustomActionSchema")


@_attrs_define
class CustomActionSchema:
    """
    Attributes:
        context (CustomActionSchemaContext):
        title (str):
        url (str):
        app_id (None | Unset | UUID):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        disabled (bool | None | Unset):
        headers (CustomActionSchemaHeadersType0 | None | Unset):
        id (None | Unset | UUID):
        last_error (None | str | Unset):
        last_error_date (datetime.datetime | None | Unset):
        metadata_view (None | Unset | UUID):
        publish_template_id (None | str | Unset):
        status (CustomActionSchemaStatusType1 | None | Unset):
        system_domain_id (None | Unset | UUID):
        transcoder_id (None | Unset | UUID):
        type_ (CustomActionSchemaTypeType1 | None | Unset):
    """

    context: CustomActionSchemaContext
    title: str
    url: str
    app_id: None | Unset | UUID = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    disabled: bool | None | Unset = UNSET
    headers: CustomActionSchemaHeadersType0 | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    last_error: None | str | Unset = UNSET
    last_error_date: datetime.datetime | None | Unset = UNSET
    metadata_view: None | Unset | UUID = UNSET
    publish_template_id: None | str | Unset = UNSET
    status: CustomActionSchemaStatusType1 | None | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    transcoder_id: None | Unset | UUID = UNSET
    type_: CustomActionSchemaTypeType1 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_action_schema_headers_type_0 import (
            CustomActionSchemaHeadersType0,
        )
        from ..models.custom_action_schema_status_type_1 import (
            CustomActionSchemaStatusType1,
        )
        from ..models.custom_action_schema_type_type_1 import (
            CustomActionSchemaTypeType1,
        )

        context = self.context.value

        title = self.title

        url = self.url

        app_id: None | str | Unset
        if isinstance(self.app_id, Unset):
            app_id = UNSET
        elif isinstance(self.app_id, UUID):
            app_id = str(self.app_id)
        else:
            app_id = self.app_id

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        disabled: bool | None | Unset
        if isinstance(self.disabled, Unset):
            disabled = UNSET
        else:
            disabled = self.disabled

        headers: dict[str, Any] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, CustomActionSchemaHeadersType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        last_error: None | str | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error

        last_error_date: None | str | Unset
        if isinstance(self.last_error_date, Unset):
            last_error_date = UNSET
        elif isinstance(self.last_error_date, datetime.datetime):
            last_error_date = self.last_error_date.isoformat()
        else:
            last_error_date = self.last_error_date

        metadata_view: None | str | Unset
        if isinstance(self.metadata_view, Unset):
            metadata_view = UNSET
        elif isinstance(self.metadata_view, UUID):
            metadata_view = str(self.metadata_view)
        else:
            metadata_view = self.metadata_view

        publish_template_id: None | str | Unset
        if isinstance(self.publish_template_id, Unset):
            publish_template_id = UNSET
        else:
            publish_template_id = self.publish_template_id

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, CustomActionSchemaStatusType1):
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

        transcoder_id: None | str | Unset
        if isinstance(self.transcoder_id, Unset):
            transcoder_id = UNSET
        elif isinstance(self.transcoder_id, UUID):
            transcoder_id = str(self.transcoder_id)
        else:
            transcoder_id = self.transcoder_id

        type_: dict[str, Any] | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, CustomActionSchemaTypeType1):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "context": context,
                "title": title,
                "url": url,
            }
        )
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if headers is not UNSET:
            field_dict["headers"] = headers
        if id is not UNSET:
            field_dict["id"] = id
        if last_error is not UNSET:
            field_dict["last_error"] = last_error
        if last_error_date is not UNSET:
            field_dict["last_error_date"] = last_error_date
        if metadata_view is not UNSET:
            field_dict["metadata_view"] = metadata_view
        if publish_template_id is not UNSET:
            field_dict["publish_template_id"] = publish_template_id
        if status is not UNSET:
            field_dict["status"] = status
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if transcoder_id is not UNSET:
            field_dict["transcoder_id"] = transcoder_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_action_schema_headers_type_0 import (
            CustomActionSchemaHeadersType0,
        )
        from ..models.custom_action_schema_status_type_1 import (
            CustomActionSchemaStatusType1,
        )
        from ..models.custom_action_schema_type_type_1 import (
            CustomActionSchemaTypeType1,
        )

        d = dict(src_dict)
        context = CustomActionSchemaContext(d.pop("context"))

        title = d.pop("title")

        url = d.pop("url")

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

        def _parse_disabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        disabled = _parse_disabled(d.pop("disabled", UNSET))

        def _parse_headers(
            data: object,
        ) -> CustomActionSchemaHeadersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headers_type_0 = CustomActionSchemaHeadersType0.from_dict(data)

                return headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomActionSchemaHeadersType0 | None | Unset, data)

        headers = _parse_headers(d.pop("headers", UNSET))

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

        def _parse_last_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error = _parse_last_error(d.pop("last_error", UNSET))

        def _parse_last_error_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_error_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_error_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_error_date = _parse_last_error_date(d.pop("last_error_date", UNSET))

        def _parse_metadata_view(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                metadata_view_type_0 = UUID(data)

                return metadata_view_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        metadata_view = _parse_metadata_view(d.pop("metadata_view", UNSET))

        def _parse_publish_template_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publish_template_id = _parse_publish_template_id(
            d.pop("publish_template_id", UNSET)
        )

        def _parse_status(data: object) -> CustomActionSchemaStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = CustomActionSchemaStatusType1.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomActionSchemaStatusType1 | None | Unset, data)

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

        def _parse_transcoder_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                transcoder_id_type_0 = UUID(data)

                return transcoder_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        transcoder_id = _parse_transcoder_id(d.pop("transcoder_id", UNSET))

        def _parse_type_(data: object) -> CustomActionSchemaTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_type_1 = CustomActionSchemaTypeType1.from_dict(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomActionSchemaTypeType1 | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        custom_action_schema = cls(
            context=context,
            title=title,
            url=url,
            app_id=app_id,
            date_created=date_created,
            date_modified=date_modified,
            disabled=disabled,
            headers=headers,
            id=id,
            last_error=last_error,
            last_error_date=last_error_date,
            metadata_view=metadata_view,
            publish_template_id=publish_template_id,
            status=status,
            system_domain_id=system_domain_id,
            transcoder_id=transcoder_id,
            type_=type_,
        )

        custom_action_schema.additional_properties = d
        return custom_action_schema

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
