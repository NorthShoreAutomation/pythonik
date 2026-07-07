from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ElementalMediaConvertSchema")


@_attrs_define
class ElementalMediaConvertSchema:
    """
    Attributes:
        access_key (str):
        endpoint_url (str):
        file_group_custom_name (str):
        iam_role (str):
        job_template_name (str):
        region_name (str):
        s3_endpoint_url (str):
        secret_key (str):
        edit_proxy_directory_path (None | str | Unset):
        edit_proxy_storage_id (None | Unset | UUID):
        exclude_patterns (list[str] | Unset):
        include_patterns (list[str] | Unset):
        keyframe_storage_id (None | Unset | UUID):
        local (bool | Unset):
        priority (int | None | Unset):
        proxy_storage_id (None | Unset | UUID):
        queue_name (str | Unset):
        s3_region_name (str | Unset):
        temp_upload_path (str | Unset):
    """

    access_key: str
    endpoint_url: str
    file_group_custom_name: str
    iam_role: str
    job_template_name: str
    region_name: str
    s3_endpoint_url: str
    secret_key: str
    edit_proxy_directory_path: None | str | Unset = UNSET
    edit_proxy_storage_id: None | Unset | UUID = UNSET
    exclude_patterns: list[str] | Unset = UNSET
    include_patterns: list[str] | Unset = UNSET
    keyframe_storage_id: None | Unset | UUID = UNSET
    local: bool | Unset = UNSET
    priority: int | None | Unset = UNSET
    proxy_storage_id: None | Unset | UUID = UNSET
    queue_name: str | Unset = UNSET
    s3_region_name: str | Unset = UNSET
    temp_upload_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_key = self.access_key

        endpoint_url = self.endpoint_url

        file_group_custom_name = self.file_group_custom_name

        iam_role = self.iam_role

        job_template_name = self.job_template_name

        region_name = self.region_name

        s3_endpoint_url = self.s3_endpoint_url

        secret_key = self.secret_key

        edit_proxy_directory_path: None | str | Unset
        if isinstance(self.edit_proxy_directory_path, Unset):
            edit_proxy_directory_path = UNSET
        else:
            edit_proxy_directory_path = self.edit_proxy_directory_path

        edit_proxy_storage_id: None | str | Unset
        if isinstance(self.edit_proxy_storage_id, Unset):
            edit_proxy_storage_id = UNSET
        elif isinstance(self.edit_proxy_storage_id, UUID):
            edit_proxy_storage_id = str(self.edit_proxy_storage_id)
        else:
            edit_proxy_storage_id = self.edit_proxy_storage_id

        exclude_patterns: list[str] | Unset = UNSET
        if not isinstance(self.exclude_patterns, Unset):
            exclude_patterns = self.exclude_patterns

        include_patterns: list[str] | Unset = UNSET
        if not isinstance(self.include_patterns, Unset):
            include_patterns = self.include_patterns

        keyframe_storage_id: None | str | Unset
        if isinstance(self.keyframe_storage_id, Unset):
            keyframe_storage_id = UNSET
        elif isinstance(self.keyframe_storage_id, UUID):
            keyframe_storage_id = str(self.keyframe_storage_id)
        else:
            keyframe_storage_id = self.keyframe_storage_id

        local = self.local

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        proxy_storage_id: None | str | Unset
        if isinstance(self.proxy_storage_id, Unset):
            proxy_storage_id = UNSET
        elif isinstance(self.proxy_storage_id, UUID):
            proxy_storage_id = str(self.proxy_storage_id)
        else:
            proxy_storage_id = self.proxy_storage_id

        queue_name = self.queue_name

        s3_region_name = self.s3_region_name

        temp_upload_path = self.temp_upload_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_key": access_key,
                "endpoint_url": endpoint_url,
                "file_group_custom_name": file_group_custom_name,
                "iam_role": iam_role,
                "job_template_name": job_template_name,
                "region_name": region_name,
                "s3_endpoint_url": s3_endpoint_url,
                "secret_key": secret_key,
            }
        )
        if edit_proxy_directory_path is not UNSET:
            field_dict["edit_proxy_directory_path"] = edit_proxy_directory_path
        if edit_proxy_storage_id is not UNSET:
            field_dict["edit_proxy_storage_id"] = edit_proxy_storage_id
        if exclude_patterns is not UNSET:
            field_dict["exclude_patterns"] = exclude_patterns
        if include_patterns is not UNSET:
            field_dict["include_patterns"] = include_patterns
        if keyframe_storage_id is not UNSET:
            field_dict["keyframe_storage_id"] = keyframe_storage_id
        if local is not UNSET:
            field_dict["local"] = local
        if priority is not UNSET:
            field_dict["priority"] = priority
        if proxy_storage_id is not UNSET:
            field_dict["proxy_storage_id"] = proxy_storage_id
        if queue_name is not UNSET:
            field_dict["queue_name"] = queue_name
        if s3_region_name is not UNSET:
            field_dict["s3_region_name"] = s3_region_name
        if temp_upload_path is not UNSET:
            field_dict["temp_upload_path"] = temp_upload_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_key = d.pop("access_key")

        endpoint_url = d.pop("endpoint_url")

        file_group_custom_name = d.pop("file_group_custom_name")

        iam_role = d.pop("iam_role")

        job_template_name = d.pop("job_template_name")

        region_name = d.pop("region_name")

        s3_endpoint_url = d.pop("s3_endpoint_url")

        secret_key = d.pop("secret_key")

        def _parse_edit_proxy_directory_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edit_proxy_directory_path = _parse_edit_proxy_directory_path(
            d.pop("edit_proxy_directory_path", UNSET)
        )

        def _parse_edit_proxy_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                edit_proxy_storage_id_type_0 = UUID(data)

                return edit_proxy_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        edit_proxy_storage_id = _parse_edit_proxy_storage_id(
            d.pop("edit_proxy_storage_id", UNSET)
        )

        exclude_patterns = cast(list[str], d.pop("exclude_patterns", UNSET))

        include_patterns = cast(list[str], d.pop("include_patterns", UNSET))

        def _parse_keyframe_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                keyframe_storage_id_type_0 = UUID(data)

                return keyframe_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        keyframe_storage_id = _parse_keyframe_storage_id(
            d.pop("keyframe_storage_id", UNSET)
        )

        local = d.pop("local", UNSET)

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_proxy_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_storage_id_type_0 = UUID(data)

                return proxy_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        proxy_storage_id = _parse_proxy_storage_id(d.pop("proxy_storage_id", UNSET))

        queue_name = d.pop("queue_name", UNSET)

        s3_region_name = d.pop("s3_region_name", UNSET)

        temp_upload_path = d.pop("temp_upload_path", UNSET)

        elemental_media_convert_schema = cls(
            access_key=access_key,
            endpoint_url=endpoint_url,
            file_group_custom_name=file_group_custom_name,
            iam_role=iam_role,
            job_template_name=job_template_name,
            region_name=region_name,
            s3_endpoint_url=s3_endpoint_url,
            secret_key=secret_key,
            edit_proxy_directory_path=edit_proxy_directory_path,
            edit_proxy_storage_id=edit_proxy_storage_id,
            exclude_patterns=exclude_patterns,
            include_patterns=include_patterns,
            keyframe_storage_id=keyframe_storage_id,
            local=local,
            priority=priority,
            proxy_storage_id=proxy_storage_id,
            queue_name=queue_name,
            s3_region_name=s3_region_name,
            temp_upload_path=temp_upload_path,
        )

        elemental_media_convert_schema.additional_properties = d
        return elemental_media_convert_schema

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
