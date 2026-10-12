from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.semantic_transcription_entity import SemanticTranscriptionEntity
    from ..models.understanding_tag import UnderstandingTag


T = TypeVar("T", bound="SemanticTranscription")


@_attrs_define
class SemanticTranscription:
    """
    Attributes:
        cut_reasons (list[str] | None | Unset):
        embedding (None | str | Unset):
        embedding_dim (int | None | Unset):
        embedding_encoding (None | str | Unset):
        embedding_model (None | str | Unset):
        embedding_model_version (None | str | Unset):
        entities (list[SemanticTranscriptionEntity] | None | Unset):
        language (None | str | Unset):
        speaker_count (None | str | Unset):
        tone (None | str | Unset):
        topics (list[UnderstandingTag] | None | Unset):
        track_id (None | str | Unset):
        valence (None | str | Unset):
    """

    cut_reasons: list[str] | None | Unset = UNSET
    embedding: None | str | Unset = UNSET
    embedding_dim: int | None | Unset = UNSET
    embedding_encoding: None | str | Unset = UNSET
    embedding_model: None | str | Unset = UNSET
    embedding_model_version: None | str | Unset = UNSET
    entities: list[SemanticTranscriptionEntity] | None | Unset = UNSET
    language: None | str | Unset = UNSET
    speaker_count: None | str | Unset = UNSET
    tone: None | str | Unset = UNSET
    topics: list[UnderstandingTag] | None | Unset = UNSET
    track_id: None | str | Unset = UNSET
    valence: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cut_reasons: list[str] | None | Unset
        if isinstance(self.cut_reasons, Unset):
            cut_reasons = UNSET
        elif isinstance(self.cut_reasons, list):
            cut_reasons = self.cut_reasons

        else:
            cut_reasons = self.cut_reasons

        embedding: None | str | Unset
        if isinstance(self.embedding, Unset):
            embedding = UNSET
        else:
            embedding = self.embedding

        embedding_dim: int | None | Unset
        if isinstance(self.embedding_dim, Unset):
            embedding_dim = UNSET
        else:
            embedding_dim = self.embedding_dim

        embedding_encoding: None | str | Unset
        if isinstance(self.embedding_encoding, Unset):
            embedding_encoding = UNSET
        else:
            embedding_encoding = self.embedding_encoding

        embedding_model: None | str | Unset
        if isinstance(self.embedding_model, Unset):
            embedding_model = UNSET
        else:
            embedding_model = self.embedding_model

        embedding_model_version: None | str | Unset
        if isinstance(self.embedding_model_version, Unset):
            embedding_model_version = UNSET
        else:
            embedding_model_version = self.embedding_model_version

        entities: list[dict[str, Any]] | None | Unset
        if isinstance(self.entities, Unset):
            entities = UNSET
        elif isinstance(self.entities, list):
            entities = []
            for entities_type_0_item_data in self.entities:
                entities_type_0_item = entities_type_0_item_data.to_dict()
                entities.append(entities_type_0_item)

        else:
            entities = self.entities

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        speaker_count: None | str | Unset
        if isinstance(self.speaker_count, Unset):
            speaker_count = UNSET
        else:
            speaker_count = self.speaker_count

        tone: None | str | Unset
        if isinstance(self.tone, Unset):
            tone = UNSET
        else:
            tone = self.tone

        topics: list[dict[str, Any]] | None | Unset
        if isinstance(self.topics, Unset):
            topics = UNSET
        elif isinstance(self.topics, list):
            topics = []
            for topics_type_0_item_data in self.topics:
                topics_type_0_item = topics_type_0_item_data.to_dict()
                topics.append(topics_type_0_item)

        else:
            topics = self.topics

        track_id: None | str | Unset
        if isinstance(self.track_id, Unset):
            track_id = UNSET
        else:
            track_id = self.track_id

        valence: None | str | Unset
        if isinstance(self.valence, Unset):
            valence = UNSET
        else:
            valence = self.valence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cut_reasons is not UNSET:
            field_dict["cut_reasons"] = cut_reasons
        if embedding is not UNSET:
            field_dict["embedding"] = embedding
        if embedding_dim is not UNSET:
            field_dict["embedding_dim"] = embedding_dim
        if embedding_encoding is not UNSET:
            field_dict["embedding_encoding"] = embedding_encoding
        if embedding_model is not UNSET:
            field_dict["embedding_model"] = embedding_model
        if embedding_model_version is not UNSET:
            field_dict["embedding_model_version"] = embedding_model_version
        if entities is not UNSET:
            field_dict["entities"] = entities
        if language is not UNSET:
            field_dict["language"] = language
        if speaker_count is not UNSET:
            field_dict["speaker_count"] = speaker_count
        if tone is not UNSET:
            field_dict["tone"] = tone
        if topics is not UNSET:
            field_dict["topics"] = topics
        if track_id is not UNSET:
            field_dict["track_id"] = track_id
        if valence is not UNSET:
            field_dict["valence"] = valence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.semantic_transcription_entity import SemanticTranscriptionEntity
        from ..models.understanding_tag import UnderstandingTag

        d = dict(src_dict)

        def _parse_cut_reasons(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cut_reasons_type_0 = cast(list[str], data)

                return cut_reasons_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cut_reasons = _parse_cut_reasons(d.pop("cut_reasons", UNSET))

        def _parse_embedding(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        embedding = _parse_embedding(d.pop("embedding", UNSET))

        def _parse_embedding_dim(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        embedding_dim = _parse_embedding_dim(d.pop("embedding_dim", UNSET))

        def _parse_embedding_encoding(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        embedding_encoding = _parse_embedding_encoding(
            d.pop("embedding_encoding", UNSET)
        )

        def _parse_embedding_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        embedding_model = _parse_embedding_model(d.pop("embedding_model", UNSET))

        def _parse_embedding_model_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        embedding_model_version = _parse_embedding_model_version(
            d.pop("embedding_model_version", UNSET)
        )

        def _parse_entities(
            data: object,
        ) -> list[SemanticTranscriptionEntity] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                entities_type_0 = []
                _entities_type_0 = data
                for entities_type_0_item_data in _entities_type_0:
                    entities_type_0_item = SemanticTranscriptionEntity.from_dict(
                        entities_type_0_item_data
                    )

                    entities_type_0.append(entities_type_0_item)

                return entities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SemanticTranscriptionEntity] | None | Unset, data)

        entities = _parse_entities(d.pop("entities", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_speaker_count(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        speaker_count = _parse_speaker_count(d.pop("speaker_count", UNSET))

        def _parse_tone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tone = _parse_tone(d.pop("tone", UNSET))

        def _parse_topics(data: object) -> list[UnderstandingTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                topics_type_0 = []
                _topics_type_0 = data
                for topics_type_0_item_data in _topics_type_0:
                    topics_type_0_item = UnderstandingTag.from_dict(
                        topics_type_0_item_data
                    )

                    topics_type_0.append(topics_type_0_item)

                return topics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UnderstandingTag] | None | Unset, data)

        topics = _parse_topics(d.pop("topics", UNSET))

        def _parse_track_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        track_id = _parse_track_id(d.pop("track_id", UNSET))

        def _parse_valence(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        valence = _parse_valence(d.pop("valence", UNSET))

        semantic_transcription = cls(
            cut_reasons=cut_reasons,
            embedding=embedding,
            embedding_dim=embedding_dim,
            embedding_encoding=embedding_encoding,
            embedding_model=embedding_model,
            embedding_model_version=embedding_model_version,
            entities=entities,
            language=language,
            speaker_count=speaker_count,
            tone=tone,
            topics=topics,
            track_id=track_id,
            valence=valence,
        )

        semantic_transcription.additional_properties = d
        return semantic_transcription

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
