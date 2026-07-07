from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WatchFolderVideoTranscoderSchema")


@_attrs_define
class WatchFolderVideoTranscoderSchema:
    """
    Attributes:
        file_grow_threshold (int):
        proxy_folder_name (str):
        watch_folder_location (str):
        create_web_proxy_from_edit_proxy (bool | Unset):
        edit_proxy_local_storage_path (str | Unset):
        edit_proxy_upload_storage_id (str | Unset):
        edit_proxy_upload_storage_path (str | Unset):
        exclude_patterns (list[str] | Unset):
        include_patterns (list[str] | Unset):
        keep_as_edit_proxy (bool | Unset):
        keyframe_folder_name (str | Unset):
        keyframe_map_folder_name (str | Unset):
        local (bool | Unset):
        proxy_timeout (int | Unset):
        use_symlink (bool | Unset): If enabled a soft link is used to add original to the watch folder, if disabled a
            hard link is used with a fallback to copy.
        use_unique_sub_folder_workflow (bool | Unset): A sub-folder is created with a unique name inside the watch
            folder per job.
    """

    file_grow_threshold: int
    proxy_folder_name: str
    watch_folder_location: str
    create_web_proxy_from_edit_proxy: bool | Unset = UNSET
    edit_proxy_local_storage_path: str | Unset = UNSET
    edit_proxy_upload_storage_id: str | Unset = UNSET
    edit_proxy_upload_storage_path: str | Unset = UNSET
    exclude_patterns: list[str] | Unset = UNSET
    include_patterns: list[str] | Unset = UNSET
    keep_as_edit_proxy: bool | Unset = UNSET
    keyframe_folder_name: str | Unset = UNSET
    keyframe_map_folder_name: str | Unset = UNSET
    local: bool | Unset = UNSET
    proxy_timeout: int | Unset = UNSET
    use_symlink: bool | Unset = UNSET
    use_unique_sub_folder_workflow: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_grow_threshold = self.file_grow_threshold

        proxy_folder_name = self.proxy_folder_name

        watch_folder_location = self.watch_folder_location

        create_web_proxy_from_edit_proxy = self.create_web_proxy_from_edit_proxy

        edit_proxy_local_storage_path = self.edit_proxy_local_storage_path

        edit_proxy_upload_storage_id = self.edit_proxy_upload_storage_id

        edit_proxy_upload_storage_path = self.edit_proxy_upload_storage_path

        exclude_patterns: list[str] | Unset = UNSET
        if not isinstance(self.exclude_patterns, Unset):
            exclude_patterns = self.exclude_patterns

        include_patterns: list[str] | Unset = UNSET
        if not isinstance(self.include_patterns, Unset):
            include_patterns = self.include_patterns

        keep_as_edit_proxy = self.keep_as_edit_proxy

        keyframe_folder_name = self.keyframe_folder_name

        keyframe_map_folder_name = self.keyframe_map_folder_name

        local = self.local

        proxy_timeout = self.proxy_timeout

        use_symlink = self.use_symlink

        use_unique_sub_folder_workflow = self.use_unique_sub_folder_workflow

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_grow_threshold": file_grow_threshold,
                "proxy_folder_name": proxy_folder_name,
                "watch_folder_location": watch_folder_location,
            }
        )
        if create_web_proxy_from_edit_proxy is not UNSET:
            field_dict["create_web_proxy_from_edit_proxy"] = (
                create_web_proxy_from_edit_proxy
            )
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
        if include_patterns is not UNSET:
            field_dict["include_patterns"] = include_patterns
        if keep_as_edit_proxy is not UNSET:
            field_dict["keep_as_edit_proxy"] = keep_as_edit_proxy
        if keyframe_folder_name is not UNSET:
            field_dict["keyframe_folder_name"] = keyframe_folder_name
        if keyframe_map_folder_name is not UNSET:
            field_dict["keyframe_map_folder_name"] = keyframe_map_folder_name
        if local is not UNSET:
            field_dict["local"] = local
        if proxy_timeout is not UNSET:
            field_dict["proxy_timeout"] = proxy_timeout
        if use_symlink is not UNSET:
            field_dict["use_symlink"] = use_symlink
        if use_unique_sub_folder_workflow is not UNSET:
            field_dict["use_unique_sub_folder_workflow"] = (
                use_unique_sub_folder_workflow
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_grow_threshold = d.pop("file_grow_threshold")

        proxy_folder_name = d.pop("proxy_folder_name")

        watch_folder_location = d.pop("watch_folder_location")

        create_web_proxy_from_edit_proxy = d.pop(
            "create_web_proxy_from_edit_proxy", UNSET
        )

        edit_proxy_local_storage_path = d.pop("edit_proxy_local_storage_path", UNSET)

        edit_proxy_upload_storage_id = d.pop("edit_proxy_upload_storage_id", UNSET)

        edit_proxy_upload_storage_path = d.pop("edit_proxy_upload_storage_path", UNSET)

        exclude_patterns = cast(list[str], d.pop("exclude_patterns", UNSET))

        include_patterns = cast(list[str], d.pop("include_patterns", UNSET))

        keep_as_edit_proxy = d.pop("keep_as_edit_proxy", UNSET)

        keyframe_folder_name = d.pop("keyframe_folder_name", UNSET)

        keyframe_map_folder_name = d.pop("keyframe_map_folder_name", UNSET)

        local = d.pop("local", UNSET)

        proxy_timeout = d.pop("proxy_timeout", UNSET)

        use_symlink = d.pop("use_symlink", UNSET)

        use_unique_sub_folder_workflow = d.pop("use_unique_sub_folder_workflow", UNSET)

        watch_folder_video_transcoder_schema = cls(
            file_grow_threshold=file_grow_threshold,
            proxy_folder_name=proxy_folder_name,
            watch_folder_location=watch_folder_location,
            create_web_proxy_from_edit_proxy=create_web_proxy_from_edit_proxy,
            edit_proxy_local_storage_path=edit_proxy_local_storage_path,
            edit_proxy_upload_storage_id=edit_proxy_upload_storage_id,
            edit_proxy_upload_storage_path=edit_proxy_upload_storage_path,
            exclude_patterns=exclude_patterns,
            include_patterns=include_patterns,
            keep_as_edit_proxy=keep_as_edit_proxy,
            keyframe_folder_name=keyframe_folder_name,
            keyframe_map_folder_name=keyframe_map_folder_name,
            local=local,
            proxy_timeout=proxy_timeout,
            use_symlink=use_symlink,
            use_unique_sub_folder_workflow=use_unique_sub_folder_workflow,
        )

        watch_folder_video_transcoder_schema.additional_properties = d
        return watch_folder_video_transcoder_schema

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
