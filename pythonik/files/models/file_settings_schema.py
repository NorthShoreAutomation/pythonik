from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prio_dir import PrioDir
    from ..models.prio_pattern import PrioPattern


T = TypeVar("T", bound="FileSettingsSchema")


@_attrs_define
class FileSettingsSchema:
    """
    Attributes:
        mount_point (str):
        access_group_id (None | Unset | UUID):
        acl_template_id (None | Unset | UUID):
        aggregate_identical_files (bool | None | Unset):
        aggregate_ignore (list[str] | None | Unset):
        aggregate_only_on_same_storage (bool | None | Unset):
        allow_access_outside_scan_directories (bool | None | Unset):
        asset_versions_suffix (None | str | Unset):
        auto_version_ignore (list[str] | None | Unset):
        auto_version_ingest_throttle_value (int | None | Unset):
        delete (bool | None | Unset):
        directory_assets_original_patterns (list[str] | None | Unset):
        directory_assets_transcode_patterns (list[str] | None | Unset):
        enable_auto_versioning (bool | None | Unset):
        enable_collection_directory_mapping (bool | None | Unset):
        enable_directory_assets (bool | None | Unset):
        filename_is_external_id (bool | None | Unset):
        folder_name_tags_metadata_field_name (None | str | Unset):
        folder_name_tags_metadata_view_id (None | Unset | UUID):
        gateway_user_id (None | Unset | UUID):
        growing_files_threshold (int | None | Unset):
        is_system (bool | None | Unset):
        local_keyframe_creation (bool | None | Unset):
        local_proxy_creation (bool | None | Unset):
        metadata_conversion_url (None | str | Unset):
        metadata_conversion_url_headers (None | str | Unset):
        metadata_view_id (None | Unset | UUID):
        prio_dirs (list[PrioDir] | None | Unset):
        prio_patterns (list[PrioPattern] | None | Unset):
        public_identity (None | str | Unset):
        read (bool | None | Unset):
        remote_path (None | str | Unset):
        remote_storage_id (None | Unset | UUID):
        scan (bool | None | Unset):
        scan_directories (list[str] | None | Unset):
        scan_ignore (list[str] | None | Unset):
        scan_include (list[str] | None | Unset):
        scan_interval_seconds (int | None | Unset):
        sidecar_metadata_required (bool | None | Unset):
        skip_upload_on_any_remote_copy_found (bool | None | Unset):
        storage_addr (None | str | Unset):
        title_includes_extension (bool | None | Unset):
        transcode_ignore (list[str] | None | Unset):
        transcode_include (list[str] | None | Unset):
        upload_files (bool | None | Unset):
        upload_ignore (list[str] | None | Unset):
        write (bool | None | Unset):
    """

    mount_point: str
    access_group_id: None | Unset | UUID = UNSET
    acl_template_id: None | Unset | UUID = UNSET
    aggregate_identical_files: bool | None | Unset = UNSET
    aggregate_ignore: list[str] | None | Unset = UNSET
    aggregate_only_on_same_storage: bool | None | Unset = UNSET
    allow_access_outside_scan_directories: bool | None | Unset = UNSET
    asset_versions_suffix: None | str | Unset = UNSET
    auto_version_ignore: list[str] | None | Unset = UNSET
    auto_version_ingest_throttle_value: int | None | Unset = UNSET
    delete: bool | None | Unset = UNSET
    directory_assets_original_patterns: list[str] | None | Unset = UNSET
    directory_assets_transcode_patterns: list[str] | None | Unset = UNSET
    enable_auto_versioning: bool | None | Unset = UNSET
    enable_collection_directory_mapping: bool | None | Unset = UNSET
    enable_directory_assets: bool | None | Unset = UNSET
    filename_is_external_id: bool | None | Unset = UNSET
    folder_name_tags_metadata_field_name: None | str | Unset = UNSET
    folder_name_tags_metadata_view_id: None | Unset | UUID = UNSET
    gateway_user_id: None | Unset | UUID = UNSET
    growing_files_threshold: int | None | Unset = UNSET
    is_system: bool | None | Unset = UNSET
    local_keyframe_creation: bool | None | Unset = UNSET
    local_proxy_creation: bool | None | Unset = UNSET
    metadata_conversion_url: None | str | Unset = UNSET
    metadata_conversion_url_headers: None | str | Unset = UNSET
    metadata_view_id: None | Unset | UUID = UNSET
    prio_dirs: list[PrioDir] | None | Unset = UNSET
    prio_patterns: list[PrioPattern] | None | Unset = UNSET
    public_identity: None | str | Unset = UNSET
    read: bool | None | Unset = UNSET
    remote_path: None | str | Unset = UNSET
    remote_storage_id: None | Unset | UUID = UNSET
    scan: bool | None | Unset = UNSET
    scan_directories: list[str] | None | Unset = UNSET
    scan_ignore: list[str] | None | Unset = UNSET
    scan_include: list[str] | None | Unset = UNSET
    scan_interval_seconds: int | None | Unset = UNSET
    sidecar_metadata_required: bool | None | Unset = UNSET
    skip_upload_on_any_remote_copy_found: bool | None | Unset = UNSET
    storage_addr: None | str | Unset = UNSET
    title_includes_extension: bool | None | Unset = UNSET
    transcode_ignore: list[str] | None | Unset = UNSET
    transcode_include: list[str] | None | Unset = UNSET
    upload_files: bool | None | Unset = UNSET
    upload_ignore: list[str] | None | Unset = UNSET
    write: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mount_point = self.mount_point

        access_group_id: None | str | Unset
        if isinstance(self.access_group_id, Unset):
            access_group_id = UNSET
        elif isinstance(self.access_group_id, UUID):
            access_group_id = str(self.access_group_id)
        else:
            access_group_id = self.access_group_id

        acl_template_id: None | str | Unset
        if isinstance(self.acl_template_id, Unset):
            acl_template_id = UNSET
        elif isinstance(self.acl_template_id, UUID):
            acl_template_id = str(self.acl_template_id)
        else:
            acl_template_id = self.acl_template_id

        aggregate_identical_files: bool | None | Unset
        if isinstance(self.aggregate_identical_files, Unset):
            aggregate_identical_files = UNSET
        else:
            aggregate_identical_files = self.aggregate_identical_files

        aggregate_ignore: list[str] | None | Unset
        if isinstance(self.aggregate_ignore, Unset):
            aggregate_ignore = UNSET
        elif isinstance(self.aggregate_ignore, list):
            aggregate_ignore = self.aggregate_ignore

        else:
            aggregate_ignore = self.aggregate_ignore

        aggregate_only_on_same_storage: bool | None | Unset
        if isinstance(self.aggregate_only_on_same_storage, Unset):
            aggregate_only_on_same_storage = UNSET
        else:
            aggregate_only_on_same_storage = self.aggregate_only_on_same_storage

        allow_access_outside_scan_directories: bool | None | Unset
        if isinstance(self.allow_access_outside_scan_directories, Unset):
            allow_access_outside_scan_directories = UNSET
        else:
            allow_access_outside_scan_directories = (
                self.allow_access_outside_scan_directories
            )

        asset_versions_suffix: None | str | Unset
        if isinstance(self.asset_versions_suffix, Unset):
            asset_versions_suffix = UNSET
        else:
            asset_versions_suffix = self.asset_versions_suffix

        auto_version_ignore: list[str] | None | Unset
        if isinstance(self.auto_version_ignore, Unset):
            auto_version_ignore = UNSET
        elif isinstance(self.auto_version_ignore, list):
            auto_version_ignore = self.auto_version_ignore

        else:
            auto_version_ignore = self.auto_version_ignore

        auto_version_ingest_throttle_value: int | None | Unset
        if isinstance(self.auto_version_ingest_throttle_value, Unset):
            auto_version_ingest_throttle_value = UNSET
        else:
            auto_version_ingest_throttle_value = self.auto_version_ingest_throttle_value

        delete: bool | None | Unset
        if isinstance(self.delete, Unset):
            delete = UNSET
        else:
            delete = self.delete

        directory_assets_original_patterns: list[str] | None | Unset
        if isinstance(self.directory_assets_original_patterns, Unset):
            directory_assets_original_patterns = UNSET
        elif isinstance(self.directory_assets_original_patterns, list):
            directory_assets_original_patterns = self.directory_assets_original_patterns

        else:
            directory_assets_original_patterns = self.directory_assets_original_patterns

        directory_assets_transcode_patterns: list[str] | None | Unset
        if isinstance(self.directory_assets_transcode_patterns, Unset):
            directory_assets_transcode_patterns = UNSET
        elif isinstance(self.directory_assets_transcode_patterns, list):
            directory_assets_transcode_patterns = (
                self.directory_assets_transcode_patterns
            )

        else:
            directory_assets_transcode_patterns = (
                self.directory_assets_transcode_patterns
            )

        enable_auto_versioning: bool | None | Unset
        if isinstance(self.enable_auto_versioning, Unset):
            enable_auto_versioning = UNSET
        else:
            enable_auto_versioning = self.enable_auto_versioning

        enable_collection_directory_mapping: bool | None | Unset
        if isinstance(self.enable_collection_directory_mapping, Unset):
            enable_collection_directory_mapping = UNSET
        else:
            enable_collection_directory_mapping = (
                self.enable_collection_directory_mapping
            )

        enable_directory_assets: bool | None | Unset
        if isinstance(self.enable_directory_assets, Unset):
            enable_directory_assets = UNSET
        else:
            enable_directory_assets = self.enable_directory_assets

        filename_is_external_id: bool | None | Unset
        if isinstance(self.filename_is_external_id, Unset):
            filename_is_external_id = UNSET
        else:
            filename_is_external_id = self.filename_is_external_id

        folder_name_tags_metadata_field_name: None | str | Unset
        if isinstance(self.folder_name_tags_metadata_field_name, Unset):
            folder_name_tags_metadata_field_name = UNSET
        else:
            folder_name_tags_metadata_field_name = (
                self.folder_name_tags_metadata_field_name
            )

        folder_name_tags_metadata_view_id: None | str | Unset
        if isinstance(self.folder_name_tags_metadata_view_id, Unset):
            folder_name_tags_metadata_view_id = UNSET
        elif isinstance(self.folder_name_tags_metadata_view_id, UUID):
            folder_name_tags_metadata_view_id = str(
                self.folder_name_tags_metadata_view_id
            )
        else:
            folder_name_tags_metadata_view_id = self.folder_name_tags_metadata_view_id

        gateway_user_id: None | str | Unset
        if isinstance(self.gateway_user_id, Unset):
            gateway_user_id = UNSET
        elif isinstance(self.gateway_user_id, UUID):
            gateway_user_id = str(self.gateway_user_id)
        else:
            gateway_user_id = self.gateway_user_id

        growing_files_threshold: int | None | Unset
        if isinstance(self.growing_files_threshold, Unset):
            growing_files_threshold = UNSET
        else:
            growing_files_threshold = self.growing_files_threshold

        is_system: bool | None | Unset
        if isinstance(self.is_system, Unset):
            is_system = UNSET
        else:
            is_system = self.is_system

        local_keyframe_creation: bool | None | Unset
        if isinstance(self.local_keyframe_creation, Unset):
            local_keyframe_creation = UNSET
        else:
            local_keyframe_creation = self.local_keyframe_creation

        local_proxy_creation: bool | None | Unset
        if isinstance(self.local_proxy_creation, Unset):
            local_proxy_creation = UNSET
        else:
            local_proxy_creation = self.local_proxy_creation

        metadata_conversion_url: None | str | Unset
        if isinstance(self.metadata_conversion_url, Unset):
            metadata_conversion_url = UNSET
        else:
            metadata_conversion_url = self.metadata_conversion_url

        metadata_conversion_url_headers: None | str | Unset
        if isinstance(self.metadata_conversion_url_headers, Unset):
            metadata_conversion_url_headers = UNSET
        else:
            metadata_conversion_url_headers = self.metadata_conversion_url_headers

        metadata_view_id: None | str | Unset
        if isinstance(self.metadata_view_id, Unset):
            metadata_view_id = UNSET
        elif isinstance(self.metadata_view_id, UUID):
            metadata_view_id = str(self.metadata_view_id)
        else:
            metadata_view_id = self.metadata_view_id

        prio_dirs: list[dict[str, Any]] | None | Unset
        if isinstance(self.prio_dirs, Unset):
            prio_dirs = UNSET
        elif isinstance(self.prio_dirs, list):
            prio_dirs = []
            for prio_dirs_type_0_item_data in self.prio_dirs:
                prio_dirs_type_0_item = prio_dirs_type_0_item_data.to_dict()
                prio_dirs.append(prio_dirs_type_0_item)

        else:
            prio_dirs = self.prio_dirs

        prio_patterns: list[dict[str, Any]] | None | Unset
        if isinstance(self.prio_patterns, Unset):
            prio_patterns = UNSET
        elif isinstance(self.prio_patterns, list):
            prio_patterns = []
            for prio_patterns_type_0_item_data in self.prio_patterns:
                prio_patterns_type_0_item = prio_patterns_type_0_item_data.to_dict()
                prio_patterns.append(prio_patterns_type_0_item)

        else:
            prio_patterns = self.prio_patterns

        public_identity: None | str | Unset
        if isinstance(self.public_identity, Unset):
            public_identity = UNSET
        else:
            public_identity = self.public_identity

        read: bool | None | Unset
        if isinstance(self.read, Unset):
            read = UNSET
        else:
            read = self.read

        remote_path: None | str | Unset
        if isinstance(self.remote_path, Unset):
            remote_path = UNSET
        else:
            remote_path = self.remote_path

        remote_storage_id: None | str | Unset
        if isinstance(self.remote_storage_id, Unset):
            remote_storage_id = UNSET
        elif isinstance(self.remote_storage_id, UUID):
            remote_storage_id = str(self.remote_storage_id)
        else:
            remote_storage_id = self.remote_storage_id

        scan: bool | None | Unset
        if isinstance(self.scan, Unset):
            scan = UNSET
        else:
            scan = self.scan

        scan_directories: list[str] | None | Unset
        if isinstance(self.scan_directories, Unset):
            scan_directories = UNSET
        elif isinstance(self.scan_directories, list):
            scan_directories = self.scan_directories

        else:
            scan_directories = self.scan_directories

        scan_ignore: list[str] | None | Unset
        if isinstance(self.scan_ignore, Unset):
            scan_ignore = UNSET
        elif isinstance(self.scan_ignore, list):
            scan_ignore = self.scan_ignore

        else:
            scan_ignore = self.scan_ignore

        scan_include: list[str] | None | Unset
        if isinstance(self.scan_include, Unset):
            scan_include = UNSET
        elif isinstance(self.scan_include, list):
            scan_include = self.scan_include

        else:
            scan_include = self.scan_include

        scan_interval_seconds: int | None | Unset
        if isinstance(self.scan_interval_seconds, Unset):
            scan_interval_seconds = UNSET
        else:
            scan_interval_seconds = self.scan_interval_seconds

        sidecar_metadata_required: bool | None | Unset
        if isinstance(self.sidecar_metadata_required, Unset):
            sidecar_metadata_required = UNSET
        else:
            sidecar_metadata_required = self.sidecar_metadata_required

        skip_upload_on_any_remote_copy_found: bool | None | Unset
        if isinstance(self.skip_upload_on_any_remote_copy_found, Unset):
            skip_upload_on_any_remote_copy_found = UNSET
        else:
            skip_upload_on_any_remote_copy_found = (
                self.skip_upload_on_any_remote_copy_found
            )

        storage_addr: None | str | Unset
        if isinstance(self.storage_addr, Unset):
            storage_addr = UNSET
        else:
            storage_addr = self.storage_addr

        title_includes_extension: bool | None | Unset
        if isinstance(self.title_includes_extension, Unset):
            title_includes_extension = UNSET
        else:
            title_includes_extension = self.title_includes_extension

        transcode_ignore: list[str] | None | Unset
        if isinstance(self.transcode_ignore, Unset):
            transcode_ignore = UNSET
        elif isinstance(self.transcode_ignore, list):
            transcode_ignore = self.transcode_ignore

        else:
            transcode_ignore = self.transcode_ignore

        transcode_include: list[str] | None | Unset
        if isinstance(self.transcode_include, Unset):
            transcode_include = UNSET
        elif isinstance(self.transcode_include, list):
            transcode_include = self.transcode_include

        else:
            transcode_include = self.transcode_include

        upload_files: bool | None | Unset
        if isinstance(self.upload_files, Unset):
            upload_files = UNSET
        else:
            upload_files = self.upload_files

        upload_ignore: list[str] | None | Unset
        if isinstance(self.upload_ignore, Unset):
            upload_ignore = UNSET
        elif isinstance(self.upload_ignore, list):
            upload_ignore = self.upload_ignore

        else:
            upload_ignore = self.upload_ignore

        write: bool | None | Unset
        if isinstance(self.write, Unset):
            write = UNSET
        else:
            write = self.write

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mount_point": mount_point,
            }
        )
        if access_group_id is not UNSET:
            field_dict["access_group_id"] = access_group_id
        if acl_template_id is not UNSET:
            field_dict["acl_template_id"] = acl_template_id
        if aggregate_identical_files is not UNSET:
            field_dict["aggregate_identical_files"] = aggregate_identical_files
        if aggregate_ignore is not UNSET:
            field_dict["aggregate_ignore"] = aggregate_ignore
        if aggregate_only_on_same_storage is not UNSET:
            field_dict["aggregate_only_on_same_storage"] = (
                aggregate_only_on_same_storage
            )
        if allow_access_outside_scan_directories is not UNSET:
            field_dict["allow_access_outside_scan_directories"] = (
                allow_access_outside_scan_directories
            )
        if asset_versions_suffix is not UNSET:
            field_dict["asset_versions_suffix"] = asset_versions_suffix
        if auto_version_ignore is not UNSET:
            field_dict["auto_version_ignore"] = auto_version_ignore
        if auto_version_ingest_throttle_value is not UNSET:
            field_dict["auto_version_ingest_throttle_value"] = (
                auto_version_ingest_throttle_value
            )
        if delete is not UNSET:
            field_dict["delete"] = delete
        if directory_assets_original_patterns is not UNSET:
            field_dict["directory_assets_original_patterns"] = (
                directory_assets_original_patterns
            )
        if directory_assets_transcode_patterns is not UNSET:
            field_dict["directory_assets_transcode_patterns"] = (
                directory_assets_transcode_patterns
            )
        if enable_auto_versioning is not UNSET:
            field_dict["enable_auto_versioning"] = enable_auto_versioning
        if enable_collection_directory_mapping is not UNSET:
            field_dict["enable_collection_directory_mapping"] = (
                enable_collection_directory_mapping
            )
        if enable_directory_assets is not UNSET:
            field_dict["enable_directory_assets"] = enable_directory_assets
        if filename_is_external_id is not UNSET:
            field_dict["filename_is_external_id"] = filename_is_external_id
        if folder_name_tags_metadata_field_name is not UNSET:
            field_dict["folder_name_tags_metadata_field_name"] = (
                folder_name_tags_metadata_field_name
            )
        if folder_name_tags_metadata_view_id is not UNSET:
            field_dict["folder_name_tags_metadata_view_id"] = (
                folder_name_tags_metadata_view_id
            )
        if gateway_user_id is not UNSET:
            field_dict["gateway_user_id"] = gateway_user_id
        if growing_files_threshold is not UNSET:
            field_dict["growing_files_threshold"] = growing_files_threshold
        if is_system is not UNSET:
            field_dict["is_system"] = is_system
        if local_keyframe_creation is not UNSET:
            field_dict["local_keyframe_creation"] = local_keyframe_creation
        if local_proxy_creation is not UNSET:
            field_dict["local_proxy_creation"] = local_proxy_creation
        if metadata_conversion_url is not UNSET:
            field_dict["metadata_conversion_url"] = metadata_conversion_url
        if metadata_conversion_url_headers is not UNSET:
            field_dict["metadata_conversion_url_headers"] = (
                metadata_conversion_url_headers
            )
        if metadata_view_id is not UNSET:
            field_dict["metadata_view_id"] = metadata_view_id
        if prio_dirs is not UNSET:
            field_dict["prio_dirs"] = prio_dirs
        if prio_patterns is not UNSET:
            field_dict["prio_patterns"] = prio_patterns
        if public_identity is not UNSET:
            field_dict["public_identity"] = public_identity
        if read is not UNSET:
            field_dict["read"] = read
        if remote_path is not UNSET:
            field_dict["remote_path"] = remote_path
        if remote_storage_id is not UNSET:
            field_dict["remote_storage_id"] = remote_storage_id
        if scan is not UNSET:
            field_dict["scan"] = scan
        if scan_directories is not UNSET:
            field_dict["scan_directories"] = scan_directories
        if scan_ignore is not UNSET:
            field_dict["scan_ignore"] = scan_ignore
        if scan_include is not UNSET:
            field_dict["scan_include"] = scan_include
        if scan_interval_seconds is not UNSET:
            field_dict["scan_interval_seconds"] = scan_interval_seconds
        if sidecar_metadata_required is not UNSET:
            field_dict["sidecar_metadata_required"] = sidecar_metadata_required
        if skip_upload_on_any_remote_copy_found is not UNSET:
            field_dict["skip_upload_on_any_remote_copy_found"] = (
                skip_upload_on_any_remote_copy_found
            )
        if storage_addr is not UNSET:
            field_dict["storage_addr"] = storage_addr
        if title_includes_extension is not UNSET:
            field_dict["title_includes_extension"] = title_includes_extension
        if transcode_ignore is not UNSET:
            field_dict["transcode_ignore"] = transcode_ignore
        if transcode_include is not UNSET:
            field_dict["transcode_include"] = transcode_include
        if upload_files is not UNSET:
            field_dict["upload_files"] = upload_files
        if upload_ignore is not UNSET:
            field_dict["upload_ignore"] = upload_ignore
        if write is not UNSET:
            field_dict["write"] = write

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prio_dir import PrioDir
        from ..models.prio_pattern import PrioPattern

        d = dict(src_dict)
        mount_point = d.pop("mount_point")

        def _parse_access_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_group_id_type_0 = UUID(data)

                return access_group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        access_group_id = _parse_access_group_id(d.pop("access_group_id", UNSET))

        def _parse_acl_template_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acl_template_id_type_0 = UUID(data)

                return acl_template_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        acl_template_id = _parse_acl_template_id(d.pop("acl_template_id", UNSET))

        def _parse_aggregate_identical_files(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        aggregate_identical_files = _parse_aggregate_identical_files(
            d.pop("aggregate_identical_files", UNSET)
        )

        def _parse_aggregate_ignore(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aggregate_ignore_type_0 = cast(list[str], data)

                return aggregate_ignore_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        aggregate_ignore = _parse_aggregate_ignore(d.pop("aggregate_ignore", UNSET))

        def _parse_aggregate_only_on_same_storage(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        aggregate_only_on_same_storage = _parse_aggregate_only_on_same_storage(
            d.pop("aggregate_only_on_same_storage", UNSET)
        )

        def _parse_allow_access_outside_scan_directories(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_access_outside_scan_directories = (
            _parse_allow_access_outside_scan_directories(
                d.pop("allow_access_outside_scan_directories", UNSET)
            )
        )

        def _parse_asset_versions_suffix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_versions_suffix = _parse_asset_versions_suffix(
            d.pop("asset_versions_suffix", UNSET)
        )

        def _parse_auto_version_ignore(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                auto_version_ignore_type_0 = cast(list[str], data)

                return auto_version_ignore_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        auto_version_ignore = _parse_auto_version_ignore(
            d.pop("auto_version_ignore", UNSET)
        )

        def _parse_auto_version_ingest_throttle_value(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_version_ingest_throttle_value = _parse_auto_version_ingest_throttle_value(
            d.pop("auto_version_ingest_throttle_value", UNSET)
        )

        def _parse_delete(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete = _parse_delete(d.pop("delete", UNSET))

        def _parse_directory_assets_original_patterns(
            data: object,
        ) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                directory_assets_original_patterns_type_0 = cast(list[str], data)

                return directory_assets_original_patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        directory_assets_original_patterns = _parse_directory_assets_original_patterns(
            d.pop("directory_assets_original_patterns", UNSET)
        )

        def _parse_directory_assets_transcode_patterns(
            data: object,
        ) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                directory_assets_transcode_patterns_type_0 = cast(list[str], data)

                return directory_assets_transcode_patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        directory_assets_transcode_patterns = (
            _parse_directory_assets_transcode_patterns(
                d.pop("directory_assets_transcode_patterns", UNSET)
            )
        )

        def _parse_enable_auto_versioning(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_auto_versioning = _parse_enable_auto_versioning(
            d.pop("enable_auto_versioning", UNSET)
        )

        def _parse_enable_collection_directory_mapping(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_collection_directory_mapping = (
            _parse_enable_collection_directory_mapping(
                d.pop("enable_collection_directory_mapping", UNSET)
            )
        )

        def _parse_enable_directory_assets(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_directory_assets = _parse_enable_directory_assets(
            d.pop("enable_directory_assets", UNSET)
        )

        def _parse_filename_is_external_id(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        filename_is_external_id = _parse_filename_is_external_id(
            d.pop("filename_is_external_id", UNSET)
        )

        def _parse_folder_name_tags_metadata_field_name(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        folder_name_tags_metadata_field_name = (
            _parse_folder_name_tags_metadata_field_name(
                d.pop("folder_name_tags_metadata_field_name", UNSET)
            )
        )

        def _parse_folder_name_tags_metadata_view_id(
            data: object,
        ) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                folder_name_tags_metadata_view_id_type_0 = UUID(data)

                return folder_name_tags_metadata_view_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        folder_name_tags_metadata_view_id = _parse_folder_name_tags_metadata_view_id(
            d.pop("folder_name_tags_metadata_view_id", UNSET)
        )

        def _parse_gateway_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gateway_user_id_type_0 = UUID(data)

                return gateway_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        gateway_user_id = _parse_gateway_user_id(d.pop("gateway_user_id", UNSET))

        def _parse_growing_files_threshold(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        growing_files_threshold = _parse_growing_files_threshold(
            d.pop("growing_files_threshold", UNSET)
        )

        def _parse_is_system(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_system = _parse_is_system(d.pop("is_system", UNSET))

        def _parse_local_keyframe_creation(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        local_keyframe_creation = _parse_local_keyframe_creation(
            d.pop("local_keyframe_creation", UNSET)
        )

        def _parse_local_proxy_creation(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        local_proxy_creation = _parse_local_proxy_creation(
            d.pop("local_proxy_creation", UNSET)
        )

        def _parse_metadata_conversion_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metadata_conversion_url = _parse_metadata_conversion_url(
            d.pop("metadata_conversion_url", UNSET)
        )

        def _parse_metadata_conversion_url_headers(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metadata_conversion_url_headers = _parse_metadata_conversion_url_headers(
            d.pop("metadata_conversion_url_headers", UNSET)
        )

        def _parse_metadata_view_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                metadata_view_id_type_0 = UUID(data)

                return metadata_view_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        metadata_view_id = _parse_metadata_view_id(d.pop("metadata_view_id", UNSET))

        def _parse_prio_dirs(data: object) -> list[PrioDir] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prio_dirs_type_0 = []
                _prio_dirs_type_0 = data
                for prio_dirs_type_0_item_data in _prio_dirs_type_0:
                    prio_dirs_type_0_item = PrioDir.from_dict(
                        prio_dirs_type_0_item_data
                    )

                    prio_dirs_type_0.append(prio_dirs_type_0_item)

                return prio_dirs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PrioDir] | None | Unset, data)

        prio_dirs = _parse_prio_dirs(d.pop("prio_dirs", UNSET))

        def _parse_prio_patterns(data: object) -> list[PrioPattern] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prio_patterns_type_0 = []
                _prio_patterns_type_0 = data
                for prio_patterns_type_0_item_data in _prio_patterns_type_0:
                    prio_patterns_type_0_item = PrioPattern.from_dict(
                        prio_patterns_type_0_item_data
                    )

                    prio_patterns_type_0.append(prio_patterns_type_0_item)

                return prio_patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PrioPattern] | None | Unset, data)

        prio_patterns = _parse_prio_patterns(d.pop("prio_patterns", UNSET))

        def _parse_public_identity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_identity = _parse_public_identity(d.pop("public_identity", UNSET))

        def _parse_read(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        read = _parse_read(d.pop("read", UNSET))

        def _parse_remote_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remote_path = _parse_remote_path(d.pop("remote_path", UNSET))

        def _parse_remote_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                remote_storage_id_type_0 = UUID(data)

                return remote_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        remote_storage_id = _parse_remote_storage_id(d.pop("remote_storage_id", UNSET))

        def _parse_scan(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        scan = _parse_scan(d.pop("scan", UNSET))

        def _parse_scan_directories(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scan_directories_type_0 = cast(list[str], data)

                return scan_directories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        scan_directories = _parse_scan_directories(d.pop("scan_directories", UNSET))

        def _parse_scan_ignore(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scan_ignore_type_0 = cast(list[str], data)

                return scan_ignore_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        scan_ignore = _parse_scan_ignore(d.pop("scan_ignore", UNSET))

        def _parse_scan_include(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scan_include_type_0 = cast(list[str], data)

                return scan_include_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        scan_include = _parse_scan_include(d.pop("scan_include", UNSET))

        def _parse_scan_interval_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        scan_interval_seconds = _parse_scan_interval_seconds(
            d.pop("scan_interval_seconds", UNSET)
        )

        def _parse_sidecar_metadata_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sidecar_metadata_required = _parse_sidecar_metadata_required(
            d.pop("sidecar_metadata_required", UNSET)
        )

        def _parse_skip_upload_on_any_remote_copy_found(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_upload_on_any_remote_copy_found = (
            _parse_skip_upload_on_any_remote_copy_found(
                d.pop("skip_upload_on_any_remote_copy_found", UNSET)
            )
        )

        def _parse_storage_addr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_addr = _parse_storage_addr(d.pop("storage_addr", UNSET))

        def _parse_title_includes_extension(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        title_includes_extension = _parse_title_includes_extension(
            d.pop("title_includes_extension", UNSET)
        )

        def _parse_transcode_ignore(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                transcode_ignore_type_0 = cast(list[str], data)

                return transcode_ignore_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        transcode_ignore = _parse_transcode_ignore(d.pop("transcode_ignore", UNSET))

        def _parse_transcode_include(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                transcode_include_type_0 = cast(list[str], data)

                return transcode_include_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        transcode_include = _parse_transcode_include(d.pop("transcode_include", UNSET))

        def _parse_upload_files(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        upload_files = _parse_upload_files(d.pop("upload_files", UNSET))

        def _parse_upload_ignore(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                upload_ignore_type_0 = cast(list[str], data)

                return upload_ignore_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        upload_ignore = _parse_upload_ignore(d.pop("upload_ignore", UNSET))

        def _parse_write(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        write = _parse_write(d.pop("write", UNSET))

        file_settings_schema = cls(
            mount_point=mount_point,
            access_group_id=access_group_id,
            acl_template_id=acl_template_id,
            aggregate_identical_files=aggregate_identical_files,
            aggregate_ignore=aggregate_ignore,
            aggregate_only_on_same_storage=aggregate_only_on_same_storage,
            allow_access_outside_scan_directories=allow_access_outside_scan_directories,
            asset_versions_suffix=asset_versions_suffix,
            auto_version_ignore=auto_version_ignore,
            auto_version_ingest_throttle_value=auto_version_ingest_throttle_value,
            delete=delete,
            directory_assets_original_patterns=directory_assets_original_patterns,
            directory_assets_transcode_patterns=directory_assets_transcode_patterns,
            enable_auto_versioning=enable_auto_versioning,
            enable_collection_directory_mapping=enable_collection_directory_mapping,
            enable_directory_assets=enable_directory_assets,
            filename_is_external_id=filename_is_external_id,
            folder_name_tags_metadata_field_name=folder_name_tags_metadata_field_name,
            folder_name_tags_metadata_view_id=folder_name_tags_metadata_view_id,
            gateway_user_id=gateway_user_id,
            growing_files_threshold=growing_files_threshold,
            is_system=is_system,
            local_keyframe_creation=local_keyframe_creation,
            local_proxy_creation=local_proxy_creation,
            metadata_conversion_url=metadata_conversion_url,
            metadata_conversion_url_headers=metadata_conversion_url_headers,
            metadata_view_id=metadata_view_id,
            prio_dirs=prio_dirs,
            prio_patterns=prio_patterns,
            public_identity=public_identity,
            read=read,
            remote_path=remote_path,
            remote_storage_id=remote_storage_id,
            scan=scan,
            scan_directories=scan_directories,
            scan_ignore=scan_ignore,
            scan_include=scan_include,
            scan_interval_seconds=scan_interval_seconds,
            sidecar_metadata_required=sidecar_metadata_required,
            skip_upload_on_any_remote_copy_found=skip_upload_on_any_remote_copy_found,
            storage_addr=storage_addr,
            title_includes_extension=title_includes_extension,
            transcode_ignore=transcode_ignore,
            transcode_include=transcode_include,
            upload_files=upload_files,
            upload_ignore=upload_ignore,
            write=write,
        )

        file_settings_schema.additional_properties = d
        return file_settings_schema

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
