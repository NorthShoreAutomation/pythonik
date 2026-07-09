from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlicsTranscoderSchema")


@_attrs_define
class FlicsTranscoderSchema:
    """
    Attributes:
        audio_template_id (None | str | Unset):
        create_edit_proxy (bool | None | Unset):
        delete_after_upload (bool | None | Unset):
        edit_proxy_local_storage_path (None | str | Unset):
        edit_proxy_upload_storage_id (None | str | Unset):
        edit_proxy_upload_storage_path (None | str | Unset):
        exclude_patterns (list[str] | None | Unset):
        host (None | str | Unset):
        image_template_id (None | str | Unset):
        include_patterns (list[str] | None | Unset):
        local (bool | None | Unset):
        max_concurrency (int | None | Unset):
        secret_key (None | str | Unset):
        storage_id_path_mapping (Any | Unset):
        storage_ids_mapping (Any | Unset):
        template_id (None | str | Unset):
    """

    audio_template_id: None | str | Unset = UNSET
    create_edit_proxy: bool | None | Unset = UNSET
    delete_after_upload: bool | None | Unset = UNSET
    edit_proxy_local_storage_path: None | str | Unset = UNSET
    edit_proxy_upload_storage_id: None | str | Unset = UNSET
    edit_proxy_upload_storage_path: None | str | Unset = UNSET
    exclude_patterns: list[str] | None | Unset = UNSET
    host: None | str | Unset = UNSET
    image_template_id: None | str | Unset = UNSET
    include_patterns: list[str] | None | Unset = UNSET
    local: bool | None | Unset = UNSET
    max_concurrency: int | None | Unset = UNSET
    secret_key: None | str | Unset = UNSET
    storage_id_path_mapping: Any | Unset = UNSET
    storage_ids_mapping: Any | Unset = UNSET
    template_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audio_template_id: None | str | Unset
        if isinstance(self.audio_template_id, Unset):
            audio_template_id = UNSET
        else:
            audio_template_id = self.audio_template_id

        create_edit_proxy: bool | None | Unset
        if isinstance(self.create_edit_proxy, Unset):
            create_edit_proxy = UNSET
        else:
            create_edit_proxy = self.create_edit_proxy

        delete_after_upload: bool | None | Unset
        if isinstance(self.delete_after_upload, Unset):
            delete_after_upload = UNSET
        else:
            delete_after_upload = self.delete_after_upload

        edit_proxy_local_storage_path: None | str | Unset
        if isinstance(self.edit_proxy_local_storage_path, Unset):
            edit_proxy_local_storage_path = UNSET
        else:
            edit_proxy_local_storage_path = self.edit_proxy_local_storage_path

        edit_proxy_upload_storage_id: None | str | Unset
        if isinstance(self.edit_proxy_upload_storage_id, Unset):
            edit_proxy_upload_storage_id = UNSET
        else:
            edit_proxy_upload_storage_id = self.edit_proxy_upload_storage_id

        edit_proxy_upload_storage_path: None | str | Unset
        if isinstance(self.edit_proxy_upload_storage_path, Unset):
            edit_proxy_upload_storage_path = UNSET
        else:
            edit_proxy_upload_storage_path = self.edit_proxy_upload_storage_path

        exclude_patterns: list[str] | None | Unset
        if isinstance(self.exclude_patterns, Unset):
            exclude_patterns = UNSET
        elif isinstance(self.exclude_patterns, list):
            exclude_patterns = self.exclude_patterns

        else:
            exclude_patterns = self.exclude_patterns

        host: None | str | Unset
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        image_template_id: None | str | Unset
        if isinstance(self.image_template_id, Unset):
            image_template_id = UNSET
        else:
            image_template_id = self.image_template_id

        include_patterns: list[str] | None | Unset
        if isinstance(self.include_patterns, Unset):
            include_patterns = UNSET
        elif isinstance(self.include_patterns, list):
            include_patterns = self.include_patterns

        else:
            include_patterns = self.include_patterns

        local: bool | None | Unset
        if isinstance(self.local, Unset):
            local = UNSET
        else:
            local = self.local

        max_concurrency: int | None | Unset
        if isinstance(self.max_concurrency, Unset):
            max_concurrency = UNSET
        else:
            max_concurrency = self.max_concurrency

        secret_key: None | str | Unset
        if isinstance(self.secret_key, Unset):
            secret_key = UNSET
        else:
            secret_key = self.secret_key

        storage_id_path_mapping = self.storage_id_path_mapping

        storage_ids_mapping = self.storage_ids_mapping

        template_id: None | str | Unset
        if isinstance(self.template_id, Unset):
            template_id = UNSET
        else:
            template_id = self.template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audio_template_id is not UNSET:
            field_dict["audio_template_id"] = audio_template_id
        if create_edit_proxy is not UNSET:
            field_dict["create_edit_proxy"] = create_edit_proxy
        if delete_after_upload is not UNSET:
            field_dict["delete_after_upload"] = delete_after_upload
        if edit_proxy_local_storage_path is not UNSET:
            field_dict["edit_proxy_local_storage_path"] = edit_proxy_local_storage_path
        if edit_proxy_upload_storage_id is not UNSET:
            field_dict["edit_proxy_upload_storage_id"] = edit_proxy_upload_storage_id
        if edit_proxy_upload_storage_path is not UNSET:
            field_dict["edit_proxy_upload_storage_path"] = (
                edit_proxy_upload_storage_path
            )
        if exclude_patterns is not UNSET:
            field_dict["exclude_patterns"] = exclude_patterns
        if host is not UNSET:
            field_dict["host"] = host
        if image_template_id is not UNSET:
            field_dict["image_template_id"] = image_template_id
        if include_patterns is not UNSET:
            field_dict["include_patterns"] = include_patterns
        if local is not UNSET:
            field_dict["local"] = local
        if max_concurrency is not UNSET:
            field_dict["max_concurrency"] = max_concurrency
        if secret_key is not UNSET:
            field_dict["secret_key"] = secret_key
        if storage_id_path_mapping is not UNSET:
            field_dict["storage_id_path_mapping"] = storage_id_path_mapping
        if storage_ids_mapping is not UNSET:
            field_dict["storage_ids_mapping"] = storage_ids_mapping
        if template_id is not UNSET:
            field_dict["template_id"] = template_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_audio_template_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        audio_template_id = _parse_audio_template_id(d.pop("audio_template_id", UNSET))

        def _parse_create_edit_proxy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        create_edit_proxy = _parse_create_edit_proxy(d.pop("create_edit_proxy", UNSET))

        def _parse_delete_after_upload(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete_after_upload = _parse_delete_after_upload(
            d.pop("delete_after_upload", UNSET)
        )

        def _parse_edit_proxy_local_storage_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edit_proxy_local_storage_path = _parse_edit_proxy_local_storage_path(
            d.pop("edit_proxy_local_storage_path", UNSET)
        )

        def _parse_edit_proxy_upload_storage_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edit_proxy_upload_storage_id = _parse_edit_proxy_upload_storage_id(
            d.pop("edit_proxy_upload_storage_id", UNSET)
        )

        def _parse_edit_proxy_upload_storage_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edit_proxy_upload_storage_path = _parse_edit_proxy_upload_storage_path(
            d.pop("edit_proxy_upload_storage_path", UNSET)
        )

        def _parse_exclude_patterns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_patterns_type_0 = cast(list[str], data)

                return exclude_patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclude_patterns = _parse_exclude_patterns(d.pop("exclude_patterns", UNSET))

        def _parse_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host = _parse_host(d.pop("host", UNSET))

        def _parse_image_template_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_template_id = _parse_image_template_id(d.pop("image_template_id", UNSET))

        def _parse_include_patterns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                include_patterns_type_0 = cast(list[str], data)

                return include_patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        include_patterns = _parse_include_patterns(d.pop("include_patterns", UNSET))

        def _parse_local(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        local = _parse_local(d.pop("local", UNSET))

        def _parse_max_concurrency(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_concurrency = _parse_max_concurrency(d.pop("max_concurrency", UNSET))

        def _parse_secret_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secret_key = _parse_secret_key(d.pop("secret_key", UNSET))

        storage_id_path_mapping = d.pop("storage_id_path_mapping", UNSET)

        storage_ids_mapping = d.pop("storage_ids_mapping", UNSET)

        def _parse_template_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_id = _parse_template_id(d.pop("template_id", UNSET))

        flics_transcoder_schema = cls(
            audio_template_id=audio_template_id,
            create_edit_proxy=create_edit_proxy,
            delete_after_upload=delete_after_upload,
            edit_proxy_local_storage_path=edit_proxy_local_storage_path,
            edit_proxy_upload_storage_id=edit_proxy_upload_storage_id,
            edit_proxy_upload_storage_path=edit_proxy_upload_storage_path,
            exclude_patterns=exclude_patterns,
            host=host,
            image_template_id=image_template_id,
            include_patterns=include_patterns,
            local=local,
            max_concurrency=max_concurrency,
            secret_key=secret_key,
            storage_id_path_mapping=storage_id_path_mapping,
            storage_ids_mapping=storage_ids_mapping,
            template_id=template_id,
        )

        flics_transcoder_schema.additional_properties = d
        return flics_transcoder_schema

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
