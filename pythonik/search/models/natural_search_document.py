from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.evidence import Evidence
    from ..models.match_assessment import MatchAssessment
    from ..models.natural_search_document_metadata_type_0 import (
        NaturalSearchDocumentMetadataType0,
    )
    from ..models.natural_search_segment import NaturalSearchSegment


T = TypeVar("T", bound="NaturalSearchDocument")


@_attrs_define
class NaturalSearchDocument:
    """A natural-search hit: the regular search document plus its ranking story.

    Identical to what ``/v2/search/`` returns for the same object — same
    post-processing, same signed URLs — so a client renders both result sets
    with one code path.

        Attributes:
            object_type (str):
            title (str):
            date_created (datetime.datetime | None | Unset):
            date_modified (datetime.datetime | None | Unset):
            description (None | str | Unset):
            evidence (list[Evidence] | None | Unset): Why this hit matched: every account, from every source that found it,
                each naming its own `source`. Empty when nothing matched textually and the filters alone selected the hit — see
                `match`.
            id (None | Unset | UUID):
            match (MatchAssessment | None | Unset): How this hit was retrieved, not how relevant it is: `quality` is `exact`
                when the query as typed matched, `related` when the query asked for what a result shows and it was matched by
                stand-in words, `approximate` when only a recovery round matched (fuzzed terms, a broadened phrase), and
                `filters_only` when no text matched and the filters alone selected it. `basis` names the evidence behind that
                verdict — `retrieval` today.
            metadata (NaturalSearchDocumentMetadataType0 | None | Unset):
            score (float | None | Unset):  Default: 0.0.
            segments (list[NaturalSearchSegment] | None | Unset): Matched moments within this hit, best first. Empty for a
                hit with no sub-structure, and always empty when `nested_results` is false.
    """

    object_type: str
    title: str
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    evidence: list[Evidence] | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    match: MatchAssessment | None | Unset = UNSET
    metadata: NaturalSearchDocumentMetadataType0 | None | Unset = UNSET
    score: float | None | Unset = 0.0
    segments: list[NaturalSearchSegment] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.match_assessment import MatchAssessment
        from ..models.natural_search_document_metadata_type_0 import (
            NaturalSearchDocumentMetadataType0,
        )

        object_type = self.object_type

        title = self.title

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

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        evidence: list[dict[str, Any]] | None | Unset
        if isinstance(self.evidence, Unset):
            evidence = UNSET
        elif isinstance(self.evidence, list):
            evidence = []
            for evidence_type_0_item_data in self.evidence:
                evidence_type_0_item = evidence_type_0_item_data.to_dict()
                evidence.append(evidence_type_0_item)

        else:
            evidence = self.evidence

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        match: dict[str, Any] | None | Unset
        if isinstance(self.match, Unset):
            match = UNSET
        elif isinstance(self.match, MatchAssessment):
            match = self.match.to_dict()
        else:
            match = self.match

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, NaturalSearchDocumentMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        score: float | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        segments: list[dict[str, Any]] | None | Unset
        if isinstance(self.segments, Unset):
            segments = UNSET
        elif isinstance(self.segments, list):
            segments = []
            for segments_type_0_item_data in self.segments:
                segments_type_0_item = segments_type_0_item_data.to_dict()
                segments.append(segments_type_0_item)

        else:
            segments = self.segments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_type": object_type,
                "title": title,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if description is not UNSET:
            field_dict["description"] = description
        if evidence is not UNSET:
            field_dict["evidence"] = evidence
        if id is not UNSET:
            field_dict["id"] = id
        if match is not UNSET:
            field_dict["match"] = match
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if score is not UNSET:
            field_dict["score"] = score
        if segments is not UNSET:
            field_dict["segments"] = segments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evidence import Evidence
        from ..models.match_assessment import MatchAssessment
        from ..models.natural_search_document_metadata_type_0 import (
            NaturalSearchDocumentMetadataType0,
        )
        from ..models.natural_search_segment import NaturalSearchSegment

        d = dict(src_dict)
        object_type = d.pop("object_type")

        title = d.pop("title")

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_evidence(data: object) -> list[Evidence] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                evidence_type_0 = []
                _evidence_type_0 = data
                for evidence_type_0_item_data in _evidence_type_0:
                    evidence_type_0_item = Evidence.from_dict(evidence_type_0_item_data)

                    evidence_type_0.append(evidence_type_0_item)

                return evidence_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Evidence] | None | Unset, data)

        evidence = _parse_evidence(d.pop("evidence", UNSET))

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

        def _parse_match(data: object) -> MatchAssessment | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                match_type_1 = MatchAssessment.from_dict(data)

                return match_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MatchAssessment | None | Unset, data)

        match = _parse_match(d.pop("match", UNSET))

        def _parse_metadata(
            data: object,
        ) -> NaturalSearchDocumentMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = NaturalSearchDocumentMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NaturalSearchDocumentMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))

        def _parse_segments(data: object) -> list[NaturalSearchSegment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                segments_type_0 = []
                _segments_type_0 = data
                for segments_type_0_item_data in _segments_type_0:
                    segments_type_0_item = NaturalSearchSegment.from_dict(
                        segments_type_0_item_data
                    )

                    segments_type_0.append(segments_type_0_item)

                return segments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NaturalSearchSegment] | None | Unset, data)

        segments = _parse_segments(d.pop("segments", UNSET))

        natural_search_document = cls(
            object_type=object_type,
            title=title,
            date_created=date_created,
            date_modified=date_modified,
            description=description,
            evidence=evidence,
            id=id,
            match=match,
            metadata=metadata,
            score=score,
            segments=segments,
        )

        natural_search_document.additional_properties = d
        return natural_search_document

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
