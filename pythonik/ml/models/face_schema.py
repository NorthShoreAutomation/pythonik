from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.face_schema_status import FaceSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.face_landmark_schema import FaceLandmarkSchema


T = TypeVar("T", bound="FaceSchema")


@_attrs_define
class FaceSchema:
    """
    Attributes:
        asset_id (UUID | Unset):
        augmented_embedding_ids (list[UUID] | Unset):
        bounding_box (list[float] | Unset):
        created_by_user (UUID | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        detection_probability (float | Unset):
        directory_path (str | Unset):
        embedding_id (UUID | Unset):
        filename (str | Unset):
        id (UUID | Unset):
        image_url (str | Unset):
        landmarks (list[FaceLandmarkSchema] | Unset):
        person_id (UUID | Unset):
        status (FaceSchemaStatus | Unset):
        storage_id (UUID | Unset):
        system_domain_id (UUID | Unset):
        timestamp_ms (int | Unset):
        version_id (UUID | Unset):
    """

    asset_id: UUID | Unset = UNSET
    augmented_embedding_ids: list[UUID] | Unset = UNSET
    bounding_box: list[float] | Unset = UNSET
    created_by_user: UUID | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    detection_probability: float | Unset = UNSET
    directory_path: str | Unset = UNSET
    embedding_id: UUID | Unset = UNSET
    filename: str | Unset = UNSET
    id: UUID | Unset = UNSET
    image_url: str | Unset = UNSET
    landmarks: list[FaceLandmarkSchema] | Unset = UNSET
    person_id: UUID | Unset = UNSET
    status: FaceSchemaStatus | Unset = UNSET
    storage_id: UUID | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    timestamp_ms: int | Unset = UNSET
    version_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id: str | Unset = UNSET
        if not isinstance(self.asset_id, Unset):
            asset_id = str(self.asset_id)

        augmented_embedding_ids: list[str] | Unset = UNSET
        if not isinstance(self.augmented_embedding_ids, Unset):
            augmented_embedding_ids = []
            for augmented_embedding_ids_item_data in self.augmented_embedding_ids:
                augmented_embedding_ids_item = str(augmented_embedding_ids_item_data)
                augmented_embedding_ids.append(augmented_embedding_ids_item)

        bounding_box: list[float] | Unset = UNSET
        if not isinstance(self.bounding_box, Unset):
            bounding_box = self.bounding_box

        created_by_user: str | Unset = UNSET
        if not isinstance(self.created_by_user, Unset):
            created_by_user = str(self.created_by_user)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        detection_probability = self.detection_probability

        directory_path = self.directory_path

        embedding_id: str | Unset = UNSET
        if not isinstance(self.embedding_id, Unset):
            embedding_id = str(self.embedding_id)

        filename = self.filename

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        image_url = self.image_url

        landmarks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.landmarks, Unset):
            landmarks = []
            for landmarks_item_data in self.landmarks:
                landmarks_item = landmarks_item_data.to_dict()
                landmarks.append(landmarks_item)

        person_id: str | Unset = UNSET
        if not isinstance(self.person_id, Unset):
            person_id = str(self.person_id)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        storage_id: str | Unset = UNSET
        if not isinstance(self.storage_id, Unset):
            storage_id = str(self.storage_id)

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        timestamp_ms = self.timestamp_ms

        version_id: str | Unset = UNSET
        if not isinstance(self.version_id, Unset):
            version_id = str(self.version_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if augmented_embedding_ids is not UNSET:
            field_dict["augmented_embedding_ids"] = augmented_embedding_ids
        if bounding_box is not UNSET:
            field_dict["bounding_box"] = bounding_box
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if detection_probability is not UNSET:
            field_dict["detection_probability"] = detection_probability
        if directory_path is not UNSET:
            field_dict["directory_path"] = directory_path
        if embedding_id is not UNSET:
            field_dict["embedding_id"] = embedding_id
        if filename is not UNSET:
            field_dict["filename"] = filename
        if id is not UNSET:
            field_dict["id"] = id
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if landmarks is not UNSET:
            field_dict["landmarks"] = landmarks
        if person_id is not UNSET:
            field_dict["person_id"] = person_id
        if status is not UNSET:
            field_dict["status"] = status
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if timestamp_ms is not UNSET:
            field_dict["timestamp_ms"] = timestamp_ms
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.face_landmark_schema import FaceLandmarkSchema

        d = dict(src_dict)
        _asset_id = d.pop("asset_id", UNSET)
        asset_id: UUID | Unset
        if isinstance(_asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = UUID(_asset_id)

        _augmented_embedding_ids = d.pop("augmented_embedding_ids", UNSET)
        augmented_embedding_ids: list[UUID] | Unset = UNSET
        if _augmented_embedding_ids is not UNSET:
            augmented_embedding_ids = []
            for augmented_embedding_ids_item_data in _augmented_embedding_ids:
                augmented_embedding_ids_item = UUID(augmented_embedding_ids_item_data)

                augmented_embedding_ids.append(augmented_embedding_ids_item)

        bounding_box = cast(list[float], d.pop("bounding_box", UNSET))

        _created_by_user = d.pop("created_by_user", UNSET)
        created_by_user: UUID | Unset
        if isinstance(_created_by_user, Unset):
            created_by_user = UNSET
        else:
            created_by_user = UUID(_created_by_user)

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = datetime.datetime.fromisoformat(_date_modified)

        detection_probability = d.pop("detection_probability", UNSET)

        directory_path = d.pop("directory_path", UNSET)

        _embedding_id = d.pop("embedding_id", UNSET)
        embedding_id: UUID | Unset
        if isinstance(_embedding_id, Unset):
            embedding_id = UNSET
        else:
            embedding_id = UUID(_embedding_id)

        filename = d.pop("filename", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        image_url = d.pop("image_url", UNSET)

        _landmarks = d.pop("landmarks", UNSET)
        landmarks: list[FaceLandmarkSchema] | Unset = UNSET
        if _landmarks is not UNSET:
            landmarks = []
            for landmarks_item_data in _landmarks:
                landmarks_item = FaceLandmarkSchema.from_dict(landmarks_item_data)

                landmarks.append(landmarks_item)

        _person_id = d.pop("person_id", UNSET)
        person_id: UUID | Unset
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _status = d.pop("status", UNSET)
        status: FaceSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FaceSchemaStatus(_status)

        _storage_id = d.pop("storage_id", UNSET)
        storage_id: UUID | Unset
        if isinstance(_storage_id, Unset):
            storage_id = UNSET
        else:
            storage_id = UUID(_storage_id)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        timestamp_ms = d.pop("timestamp_ms", UNSET)

        _version_id = d.pop("version_id", UNSET)
        version_id: UUID | Unset
        if isinstance(_version_id, Unset):
            version_id = UNSET
        else:
            version_id = UUID(_version_id)

        face_schema = cls(
            asset_id=asset_id,
            augmented_embedding_ids=augmented_embedding_ids,
            bounding_box=bounding_box,
            created_by_user=created_by_user,
            date_created=date_created,
            date_modified=date_modified,
            detection_probability=detection_probability,
            directory_path=directory_path,
            embedding_id=embedding_id,
            filename=filename,
            id=id,
            image_url=image_url,
            landmarks=landmarks,
            person_id=person_id,
            status=status,
            storage_id=storage_id,
            system_domain_id=system_domain_id,
            timestamp_ms=timestamp_ms,
            version_id=version_id,
        )

        face_schema.additional_properties = d
        return face_schema

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
