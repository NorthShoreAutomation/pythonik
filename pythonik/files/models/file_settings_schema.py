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
        aggregate_identical_files (bool | Unset):
        aggregate_ignore (list[str] | Unset):
        aggregate_only_on_same_storage (bool | Unset):
        allow_access_outside_scan_directories (bool | Unset):
        asset_versions_suffix (str | Unset):
        auto_version_ignore (list[str] | Unset):
        auto_version_ingest_throttle_value (int | Unset):
        delete (bool | Unset):
        directory_assets_original_patterns (list[str] | Unset):
        directory_assets_transcode_patterns (list[str] | Unset):
        enable_auto_versioning (bool | Unset):
        enable_collection_directory_mapping (bool | Unset):
        enable_directory_assets (bool | Unset):
        filename_is_external_id (bool | Unset):
        folder_name_tags_metadata_field_name (str | Unset):
        folder_name_tags_metadata_view_id (None | Unset | UUID):
        gateway_user_id (UUID | Unset):
        growing_files_threshold (int | Unset):
        is_system (bool | Unset):
        local_keyframe_creation (bool | Unset):
        local_proxy_creation (bool | Unset):
        metadata_conversion_url (str | Unset):
        metadata_conversion_url_headers (None | str | Unset):
        metadata_view_id (None | Unset | UUID):
        prio_dirs (list[PrioDir] | None | Unset):
        prio_patterns (list[PrioPattern] | None | Unset):
        public_identity (str | Unset):
        read (bool | Unset):
        remote_path (str | Unset):
        remote_storage_id (UUID | Unset):
        scan (bool | Unset):
        scan_directories (list[str] | Unset):
        scan_ignore (list[str] | Unset):
        scan_include (list[str] | Unset):
        scan_interval_seconds (int | Unset):
        sidecar_metadata_required (bool | Unset):
        skip_upload_on_any_remote_copy_found (bool | Unset):
        storage_addr (str | Unset):
        title_includes_extension (bool | Unset):
        transcode_ignore (list[str] | Unset):
        transcode_include (list[str] | Unset):
        upload_files (bool | Unset):
        upload_ignore (list[str] | Unset):
        write (bool | Unset):
    """

    mount_point: str
    access_group_id: None | Unset | UUID = UNSET
    acl_template_id: None | Unset | UUID = UNSET
    aggregate_identical_files: bool | Unset = UNSET
    aggregate_ignore: list[str] | Unset = UNSET
    aggregate_only_on_same_storage: bool | Unset = UNSET
    allow_access_outside_scan_directories: bool | Unset = UNSET
    asset_versions_suffix: str | Unset = UNSET
    auto_version_ignore: list[str] | Unset = UNSET
    auto_version_ingest_throttle_value: int | Unset = UNSET
    delete: bool | Unset = UNSET
    directory_assets_original_patterns: list[str] | Unset = UNSET
    directory_assets_transcode_patterns: list[str] | Unset = UNSET
    enable_auto_versioning: bool | Unset = UNSET
    enable_collection_directory_mapping: bool | Unset = UNSET
    enable_directory_assets: bool | Unset = UNSET
    filename_is_external_id: bool | Unset = UNSET
    folder_name_tags_metadata_field_name: str | Unset = UNSET
    folder_name_tags_metadata_view_id: None | Unset | UUID = UNSET
    gateway_user_id: UUID | Unset = UNSET
    growing_files_threshold: int | Unset = UNSET
    is_system: bool | Unset = UNSET
    local_keyframe_creation: bool | Unset = UNSET
    local_proxy_creation: bool | Unset = UNSET
    metadata_conversion_url: str | Unset = UNSET
    metadata_conversion_url_headers: None | str | Unset = UNSET
    metadata_view_id: None | Unset | UUID = UNSET
    prio_dirs: list[PrioDir] | None | Unset = UNSET
    prio_patterns: list[PrioPattern] | None | Unset = UNSET
    public_identity: str | Unset = UNSET
    read: bool | Unset = UNSET
    remote_path: str | Unset = UNSET
    remote_storage_id: UUID | Unset = UNSET
    scan: bool | Unset = UNSET
    scan_directories: list[str] | Unset = UNSET
    scan_ignore: list[str] | Unset = UNSET
    scan_include: list[str] | Unset = UNSET
    scan_interval_seconds: int | Unset = UNSET
    sidecar_metadata_required: bool | Unset = UNSET
    skip_upload_on_any_remote_copy_found: bool | Unset = UNSET
    storage_addr: str | Unset = UNSET
    title_includes_extension: bool | Unset = UNSET
    transcode_ignore: list[str] | Unset = UNSET
    transcode_include: list[str] | Unset = UNSET
    upload_files: bool | Unset = UNSET
    upload_ignore: list[str] | Unset = UNSET
    write: bool | Unset = UNSET
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

        aggregate_identical_files = self.aggregate_identical_files

        aggregate_ignore: list[str] | Unset = UNSET
        if not isinstance(self.aggregate_ignore, Unset):
            aggregate_ignore = self.aggregate_ignore

        aggregate_only_on_same_storage = self.aggregate_only_on_same_storage

        allow_access_outside_scan_directories = (
            self.allow_access_outside_scan_directories
        )

        asset_versions_suffix = self.asset_versions_suffix

        auto_version_ignore: list[str] | Unset = UNSET
        if not isinstance(self.auto_version_ignore, Unset):
            auto_version_ignore = self.auto_version_ignore

        auto_version_ingest_throttle_value = self.auto_version_ingest_throttle_value

        delete = self.delete

        directory_assets_original_patterns: list[str] | Unset = UNSET
        if not isinstance(self.directory_assets_original_patterns, Unset):
            directory_assets_original_patterns = self.directory_assets_original_patterns

        directory_assets_transcode_patterns: list[str] | Unset = UNSET
        if not isinstance(self.directory_assets_transcode_patterns, Unset):
            directory_assets_transcode_patterns = (
                self.directory_assets_transcode_patterns
            )

        enable_auto_versioning = self.enable_auto_versioning

        enable_collection_directory_mapping = self.enable_collection_directory_mapping

        enable_directory_assets = self.enable_directory_assets

        filename_is_external_id = self.filename_is_external_id

        folder_name_tags_metadata_field_name = self.folder_name_tags_metadata_field_name

        folder_name_tags_metadata_view_id: None | str | Unset
        if isinstance(self.folder_name_tags_metadata_view_id, Unset):
            folder_name_tags_metadata_view_id = UNSET
        elif isinstance(self.folder_name_tags_metadata_view_id, UUID):
            folder_name_tags_metadata_view_id = str(
                self.folder_name_tags_metadata_view_id
            )
        else:
            folder_name_tags_metadata_view_id = self.folder_name_tags_metadata_view_id

        gateway_user_id: str | Unset = UNSET
        if not isinstance(self.gateway_user_id, Unset):
            gateway_user_id = str(self.gateway_user_id)

        growing_files_threshold = self.growing_files_threshold

        is_system = self.is_system

        local_keyframe_creation = self.local_keyframe_creation

        local_proxy_creation = self.local_proxy_creation

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

        public_identity = self.public_identity

        read = self.read

        remote_path = self.remote_path

        remote_storage_id: str | Unset = UNSET
        if not isinstance(self.remote_storage_id, Unset):
            remote_storage_id = str(self.remote_storage_id)

        scan = self.scan

        scan_directories: list[str] | Unset = UNSET
        if not isinstance(self.scan_directories, Unset):
            scan_directories = self.scan_directories

        scan_ignore: list[str] | Unset = UNSET
        if not isinstance(self.scan_ignore, Unset):
            scan_ignore = self.scan_ignore

        scan_include: list[str] | Unset = UNSET
        if not isinstance(self.scan_include, Unset):
            scan_include = self.scan_include

        scan_interval_seconds = self.scan_interval_seconds

        sidecar_metadata_required = self.sidecar_metadata_required

        skip_upload_on_any_remote_copy_found = self.skip_upload_on_any_remote_copy_found

        storage_addr = self.storage_addr

        title_includes_extension = self.title_includes_extension

        transcode_ignore: list[str] | Unset = UNSET
        if not isinstance(self.transcode_ignore, Unset):
            transcode_ignore = self.transcode_ignore

        transcode_include: list[str] | Unset = UNSET
        if not isinstance(self.transcode_include, Unset):
            transcode_include = self.transcode_include

        upload_files = self.upload_files

        upload_ignore: list[str] | Unset = UNSET
        if not isinstance(self.upload_ignore, Unset):
            upload_ignore = self.upload_ignore

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

        aggregate_identical_files = d.pop("aggregate_identical_files", UNSET)

        aggregate_ignore = cast(list[str], d.pop("aggregate_ignore", UNSET))

        aggregate_only_on_same_storage = d.pop("aggregate_only_on_same_storage", UNSET)

        allow_access_outside_scan_directories = d.pop(
            "allow_access_outside_scan_directories", UNSET
        )

        asset_versions_suffix = d.pop("asset_versions_suffix", UNSET)

        auto_version_ignore = cast(list[str], d.pop("auto_version_ignore", UNSET))

        auto_version_ingest_throttle_value = d.pop(
            "auto_version_ingest_throttle_value", UNSET
        )

        delete = d.pop("delete", UNSET)

        directory_assets_original_patterns = cast(
            list[str], d.pop("directory_assets_original_patterns", UNSET)
        )

        directory_assets_transcode_patterns = cast(
            list[str], d.pop("directory_assets_transcode_patterns", UNSET)
        )

        enable_auto_versioning = d.pop("enable_auto_versioning", UNSET)

        enable_collection_directory_mapping = d.pop(
            "enable_collection_directory_mapping", UNSET
        )

        enable_directory_assets = d.pop("enable_directory_assets", UNSET)

        filename_is_external_id = d.pop("filename_is_external_id", UNSET)

        folder_name_tags_metadata_field_name = d.pop(
            "folder_name_tags_metadata_field_name", UNSET
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

        _gateway_user_id = d.pop("gateway_user_id", UNSET)
        gateway_user_id: UUID | Unset
        if isinstance(_gateway_user_id, Unset):
            gateway_user_id = UNSET
        else:
            gateway_user_id = UUID(_gateway_user_id)

        growing_files_threshold = d.pop("growing_files_threshold", UNSET)

        is_system = d.pop("is_system", UNSET)

        local_keyframe_creation = d.pop("local_keyframe_creation", UNSET)

        local_proxy_creation = d.pop("local_proxy_creation", UNSET)

        metadata_conversion_url = d.pop("metadata_conversion_url", UNSET)

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

        public_identity = d.pop("public_identity", UNSET)

        read = d.pop("read", UNSET)

        remote_path = d.pop("remote_path", UNSET)

        _remote_storage_id = d.pop("remote_storage_id", UNSET)
        remote_storage_id: UUID | Unset
        if isinstance(_remote_storage_id, Unset):
            remote_storage_id = UNSET
        else:
            remote_storage_id = UUID(_remote_storage_id)

        scan = d.pop("scan", UNSET)

        scan_directories = cast(list[str], d.pop("scan_directories", UNSET))

        scan_ignore = cast(list[str], d.pop("scan_ignore", UNSET))

        scan_include = cast(list[str], d.pop("scan_include", UNSET))

        scan_interval_seconds = d.pop("scan_interval_seconds", UNSET)

        sidecar_metadata_required = d.pop("sidecar_metadata_required", UNSET)

        skip_upload_on_any_remote_copy_found = d.pop(
            "skip_upload_on_any_remote_copy_found", UNSET
        )

        storage_addr = d.pop("storage_addr", UNSET)

        title_includes_extension = d.pop("title_includes_extension", UNSET)

        transcode_ignore = cast(list[str], d.pop("transcode_ignore", UNSET))

        transcode_include = cast(list[str], d.pop("transcode_include", UNSET))

        upload_files = d.pop("upload_files", UNSET)

        upload_ignore = cast(list[str], d.pop("upload_ignore", UNSET))

        write = d.pop("write", UNSET)

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
