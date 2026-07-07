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
        audio_template_id (str | Unset):
        create_edit_proxy (bool | Unset):
        delete_after_upload (bool | Unset):
        edit_proxy_local_storage_path (str | Unset):
        edit_proxy_upload_storage_id (str | Unset):
        edit_proxy_upload_storage_path (str | Unset):
        exclude_patterns (list[str] | Unset):
        host (str | Unset):
        image_template_id (str | Unset):
        include_patterns (list[str] | Unset):
        local (bool | Unset):
        max_concurrency (int | None | Unset):
        secret_key (str | Unset):
        storage_id_path_mapping (Any | Unset):
        storage_ids_mapping (Any | Unset):
        template_id (str | Unset):
    """

    audio_template_id: str | Unset = UNSET
    create_edit_proxy: bool | Unset = UNSET
    delete_after_upload: bool | Unset = UNSET
    edit_proxy_local_storage_path: str | Unset = UNSET
    edit_proxy_upload_storage_id: str | Unset = UNSET
    edit_proxy_upload_storage_path: str | Unset = UNSET
    exclude_patterns: list[str] | Unset = UNSET
    host: str | Unset = UNSET
    image_template_id: str | Unset = UNSET
    include_patterns: list[str] | Unset = UNSET
    local: bool | Unset = UNSET
    max_concurrency: int | None | Unset = UNSET
    secret_key: str | Unset = UNSET
    storage_id_path_mapping: Any | Unset = UNSET
    storage_ids_mapping: Any | Unset = UNSET
    template_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audio_template_id = self.audio_template_id

        create_edit_proxy = self.create_edit_proxy

        delete_after_upload = self.delete_after_upload

        edit_proxy_local_storage_path = self.edit_proxy_local_storage_path

        edit_proxy_upload_storage_id = self.edit_proxy_upload_storage_id

        edit_proxy_upload_storage_path = self.edit_proxy_upload_storage_path

        exclude_patterns: list[str] | Unset = UNSET
        if not isinstance(self.exclude_patterns, Unset):
            exclude_patterns = self.exclude_patterns

        host = self.host

        image_template_id = self.image_template_id

        include_patterns: list[str] | Unset = UNSET
        if not isinstance(self.include_patterns, Unset):
            include_patterns = self.include_patterns

        local = self.local

        max_concurrency: int | None | Unset
        if isinstance(self.max_concurrency, Unset):
            max_concurrency = UNSET
        else:
            max_concurrency = self.max_concurrency

        secret_key = self.secret_key

        storage_id_path_mapping = self.storage_id_path_mapping

        storage_ids_mapping = self.storage_ids_mapping

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
        audio_template_id = d.pop("audio_template_id", UNSET)

        create_edit_proxy = d.pop("create_edit_proxy", UNSET)

        delete_after_upload = d.pop("delete_after_upload", UNSET)

        edit_proxy_local_storage_path = d.pop("edit_proxy_local_storage_path", UNSET)

        edit_proxy_upload_storage_id = d.pop("edit_proxy_upload_storage_id", UNSET)

        edit_proxy_upload_storage_path = d.pop("edit_proxy_upload_storage_path", UNSET)

        exclude_patterns = cast(list[str], d.pop("exclude_patterns", UNSET))

        host = d.pop("host", UNSET)

        image_template_id = d.pop("image_template_id", UNSET)

        include_patterns = cast(list[str], d.pop("include_patterns", UNSET))

        local = d.pop("local", UNSET)

        def _parse_max_concurrency(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_concurrency = _parse_max_concurrency(d.pop("max_concurrency", UNSET))

        secret_key = d.pop("secret_key", UNSET)

        storage_id_path_mapping = d.pop("storage_id_path_mapping", UNSET)

        storage_ids_mapping = d.pop("storage_ids_mapping", UNSET)

        template_id = d.pop("template_id", UNSET)

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
