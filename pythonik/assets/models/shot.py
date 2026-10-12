from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.understanding_tag import UnderstandingTag


T = TypeVar("T", bound="Shot")


@_attrs_define
class Shot:
    """
    Attributes:
        actions (list[UnderstandingTag] | None | Unset):
        animal_species (list[UnderstandingTag] | None | Unset):
        brand_logo (list[UnderstandingTag] | None | Unset):
        camera_angle (None | UnderstandingTag | Unset):
        caption (None | str | Unset):
        color_palette (list[UnderstandingTag] | None | Unset):
        composition (None | str | Unset):
        dog_breeds (list[UnderstandingTag] | None | Unset):
        dominant_hue (None | str | Unset):
        embedding (None | str | Unset):
        embedding_dim (int | None | Unset):
        embedding_encoding (None | str | Unset):
        embedding_model (None | str | Unset):
        embedding_model_version (None | str | Unset):
        facial_expression (list[UnderstandingTag] | None | Unset):
        keyframe_ts (int | None | Unset):
        light_key (None | str | Unset):
        light_side (None | str | Unset):
        light_style (list[str] | None | Unset):
        light_time (None | str | Unset):
        mood (list[UnderstandingTag] | None | Unset):
        mood_valence (None | str | Unset):
        movement (list[str] | None | Unset):
        objects (list[UnderstandingTag] | None | Unset):
        ocr_text (None | str | Unset):
        orientation (None | str | Unset):
        people_age_range (list[str] | None | Unset):
        people_bucket (None | str | Unset):
        people_count (int | None | Unset):
        people_features (list[UnderstandingTag] | None | Unset):
        people_gender (list[str] | None | Unset):
        place (None | UnderstandingTag | Unset):
        resolution (None | str | Unset):
        scale_rank (int | None | Unset):
        season (None | UnderstandingTag | Unset):
        sensitive_content (list[UnderstandingTag] | None | Unset):
        setting (None | UnderstandingTag | Unset):
        shot_scale (None | UnderstandingTag | Unset):
        sport_type (None | UnderstandingTag | Unset):
        subject_type (list[UnderstandingTag] | None | Unset):
        time_of_day (None | str | Unset):
        track_id (None | str | Unset):
        weather (None | UnderstandingTag | Unset):
    """

    actions: list[UnderstandingTag] | None | Unset = UNSET
    animal_species: list[UnderstandingTag] | None | Unset = UNSET
    brand_logo: list[UnderstandingTag] | None | Unset = UNSET
    camera_angle: None | UnderstandingTag | Unset = UNSET
    caption: None | str | Unset = UNSET
    color_palette: list[UnderstandingTag] | None | Unset = UNSET
    composition: None | str | Unset = UNSET
    dog_breeds: list[UnderstandingTag] | None | Unset = UNSET
    dominant_hue: None | str | Unset = UNSET
    embedding: None | str | Unset = UNSET
    embedding_dim: int | None | Unset = UNSET
    embedding_encoding: None | str | Unset = UNSET
    embedding_model: None | str | Unset = UNSET
    embedding_model_version: None | str | Unset = UNSET
    facial_expression: list[UnderstandingTag] | None | Unset = UNSET
    keyframe_ts: int | None | Unset = UNSET
    light_key: None | str | Unset = UNSET
    light_side: None | str | Unset = UNSET
    light_style: list[str] | None | Unset = UNSET
    light_time: None | str | Unset = UNSET
    mood: list[UnderstandingTag] | None | Unset = UNSET
    mood_valence: None | str | Unset = UNSET
    movement: list[str] | None | Unset = UNSET
    objects: list[UnderstandingTag] | None | Unset = UNSET
    ocr_text: None | str | Unset = UNSET
    orientation: None | str | Unset = UNSET
    people_age_range: list[str] | None | Unset = UNSET
    people_bucket: None | str | Unset = UNSET
    people_count: int | None | Unset = UNSET
    people_features: list[UnderstandingTag] | None | Unset = UNSET
    people_gender: list[str] | None | Unset = UNSET
    place: None | UnderstandingTag | Unset = UNSET
    resolution: None | str | Unset = UNSET
    scale_rank: int | None | Unset = UNSET
    season: None | UnderstandingTag | Unset = UNSET
    sensitive_content: list[UnderstandingTag] | None | Unset = UNSET
    setting: None | UnderstandingTag | Unset = UNSET
    shot_scale: None | UnderstandingTag | Unset = UNSET
    sport_type: None | UnderstandingTag | Unset = UNSET
    subject_type: list[UnderstandingTag] | None | Unset = UNSET
    time_of_day: None | str | Unset = UNSET
    track_id: None | str | Unset = UNSET
    weather: None | UnderstandingTag | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.understanding_tag import UnderstandingTag

        actions: list[dict[str, Any]] | None | Unset
        if isinstance(self.actions, Unset):
            actions = UNSET
        elif isinstance(self.actions, list):
            actions = []
            for actions_type_0_item_data in self.actions:
                actions_type_0_item = actions_type_0_item_data.to_dict()
                actions.append(actions_type_0_item)

        else:
            actions = self.actions

        animal_species: list[dict[str, Any]] | None | Unset
        if isinstance(self.animal_species, Unset):
            animal_species = UNSET
        elif isinstance(self.animal_species, list):
            animal_species = []
            for animal_species_type_0_item_data in self.animal_species:
                animal_species_type_0_item = animal_species_type_0_item_data.to_dict()
                animal_species.append(animal_species_type_0_item)

        else:
            animal_species = self.animal_species

        brand_logo: list[dict[str, Any]] | None | Unset
        if isinstance(self.brand_logo, Unset):
            brand_logo = UNSET
        elif isinstance(self.brand_logo, list):
            brand_logo = []
            for brand_logo_type_0_item_data in self.brand_logo:
                brand_logo_type_0_item = brand_logo_type_0_item_data.to_dict()
                brand_logo.append(brand_logo_type_0_item)

        else:
            brand_logo = self.brand_logo

        camera_angle: dict[str, Any] | None | Unset
        if isinstance(self.camera_angle, Unset):
            camera_angle = UNSET
        elif isinstance(self.camera_angle, UnderstandingTag):
            camera_angle = self.camera_angle.to_dict()
        else:
            camera_angle = self.camera_angle

        caption: None | str | Unset
        if isinstance(self.caption, Unset):
            caption = UNSET
        else:
            caption = self.caption

        color_palette: list[dict[str, Any]] | None | Unset
        if isinstance(self.color_palette, Unset):
            color_palette = UNSET
        elif isinstance(self.color_palette, list):
            color_palette = []
            for color_palette_type_0_item_data in self.color_palette:
                color_palette_type_0_item = color_palette_type_0_item_data.to_dict()
                color_palette.append(color_palette_type_0_item)

        else:
            color_palette = self.color_palette

        composition: None | str | Unset
        if isinstance(self.composition, Unset):
            composition = UNSET
        else:
            composition = self.composition

        dog_breeds: list[dict[str, Any]] | None | Unset
        if isinstance(self.dog_breeds, Unset):
            dog_breeds = UNSET
        elif isinstance(self.dog_breeds, list):
            dog_breeds = []
            for dog_breeds_type_0_item_data in self.dog_breeds:
                dog_breeds_type_0_item = dog_breeds_type_0_item_data.to_dict()
                dog_breeds.append(dog_breeds_type_0_item)

        else:
            dog_breeds = self.dog_breeds

        dominant_hue: None | str | Unset
        if isinstance(self.dominant_hue, Unset):
            dominant_hue = UNSET
        else:
            dominant_hue = self.dominant_hue

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

        facial_expression: list[dict[str, Any]] | None | Unset
        if isinstance(self.facial_expression, Unset):
            facial_expression = UNSET
        elif isinstance(self.facial_expression, list):
            facial_expression = []
            for facial_expression_type_0_item_data in self.facial_expression:
                facial_expression_type_0_item = (
                    facial_expression_type_0_item_data.to_dict()
                )
                facial_expression.append(facial_expression_type_0_item)

        else:
            facial_expression = self.facial_expression

        keyframe_ts: int | None | Unset
        if isinstance(self.keyframe_ts, Unset):
            keyframe_ts = UNSET
        else:
            keyframe_ts = self.keyframe_ts

        light_key: None | str | Unset
        if isinstance(self.light_key, Unset):
            light_key = UNSET
        else:
            light_key = self.light_key

        light_side: None | str | Unset
        if isinstance(self.light_side, Unset):
            light_side = UNSET
        else:
            light_side = self.light_side

        light_style: list[str] | None | Unset
        if isinstance(self.light_style, Unset):
            light_style = UNSET
        elif isinstance(self.light_style, list):
            light_style = self.light_style

        else:
            light_style = self.light_style

        light_time: None | str | Unset
        if isinstance(self.light_time, Unset):
            light_time = UNSET
        else:
            light_time = self.light_time

        mood: list[dict[str, Any]] | None | Unset
        if isinstance(self.mood, Unset):
            mood = UNSET
        elif isinstance(self.mood, list):
            mood = []
            for mood_type_0_item_data in self.mood:
                mood_type_0_item = mood_type_0_item_data.to_dict()
                mood.append(mood_type_0_item)

        else:
            mood = self.mood

        mood_valence: None | str | Unset
        if isinstance(self.mood_valence, Unset):
            mood_valence = UNSET
        else:
            mood_valence = self.mood_valence

        movement: list[str] | None | Unset
        if isinstance(self.movement, Unset):
            movement = UNSET
        elif isinstance(self.movement, list):
            movement = self.movement

        else:
            movement = self.movement

        objects: list[dict[str, Any]] | None | Unset
        if isinstance(self.objects, Unset):
            objects = UNSET
        elif isinstance(self.objects, list):
            objects = []
            for objects_type_0_item_data in self.objects:
                objects_type_0_item = objects_type_0_item_data.to_dict()
                objects.append(objects_type_0_item)

        else:
            objects = self.objects

        ocr_text: None | str | Unset
        if isinstance(self.ocr_text, Unset):
            ocr_text = UNSET
        else:
            ocr_text = self.ocr_text

        orientation: None | str | Unset
        if isinstance(self.orientation, Unset):
            orientation = UNSET
        else:
            orientation = self.orientation

        people_age_range: list[str] | None | Unset
        if isinstance(self.people_age_range, Unset):
            people_age_range = UNSET
        elif isinstance(self.people_age_range, list):
            people_age_range = self.people_age_range

        else:
            people_age_range = self.people_age_range

        people_bucket: None | str | Unset
        if isinstance(self.people_bucket, Unset):
            people_bucket = UNSET
        else:
            people_bucket = self.people_bucket

        people_count: int | None | Unset
        if isinstance(self.people_count, Unset):
            people_count = UNSET
        else:
            people_count = self.people_count

        people_features: list[dict[str, Any]] | None | Unset
        if isinstance(self.people_features, Unset):
            people_features = UNSET
        elif isinstance(self.people_features, list):
            people_features = []
            for people_features_type_0_item_data in self.people_features:
                people_features_type_0_item = people_features_type_0_item_data.to_dict()
                people_features.append(people_features_type_0_item)

        else:
            people_features = self.people_features

        people_gender: list[str] | None | Unset
        if isinstance(self.people_gender, Unset):
            people_gender = UNSET
        elif isinstance(self.people_gender, list):
            people_gender = self.people_gender

        else:
            people_gender = self.people_gender

        place: dict[str, Any] | None | Unset
        if isinstance(self.place, Unset):
            place = UNSET
        elif isinstance(self.place, UnderstandingTag):
            place = self.place.to_dict()
        else:
            place = self.place

        resolution: None | str | Unset
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        else:
            resolution = self.resolution

        scale_rank: int | None | Unset
        if isinstance(self.scale_rank, Unset):
            scale_rank = UNSET
        else:
            scale_rank = self.scale_rank

        season: dict[str, Any] | None | Unset
        if isinstance(self.season, Unset):
            season = UNSET
        elif isinstance(self.season, UnderstandingTag):
            season = self.season.to_dict()
        else:
            season = self.season

        sensitive_content: list[dict[str, Any]] | None | Unset
        if isinstance(self.sensitive_content, Unset):
            sensitive_content = UNSET
        elif isinstance(self.sensitive_content, list):
            sensitive_content = []
            for sensitive_content_type_0_item_data in self.sensitive_content:
                sensitive_content_type_0_item = (
                    sensitive_content_type_0_item_data.to_dict()
                )
                sensitive_content.append(sensitive_content_type_0_item)

        else:
            sensitive_content = self.sensitive_content

        setting: dict[str, Any] | None | Unset
        if isinstance(self.setting, Unset):
            setting = UNSET
        elif isinstance(self.setting, UnderstandingTag):
            setting = self.setting.to_dict()
        else:
            setting = self.setting

        shot_scale: dict[str, Any] | None | Unset
        if isinstance(self.shot_scale, Unset):
            shot_scale = UNSET
        elif isinstance(self.shot_scale, UnderstandingTag):
            shot_scale = self.shot_scale.to_dict()
        else:
            shot_scale = self.shot_scale

        sport_type: dict[str, Any] | None | Unset
        if isinstance(self.sport_type, Unset):
            sport_type = UNSET
        elif isinstance(self.sport_type, UnderstandingTag):
            sport_type = self.sport_type.to_dict()
        else:
            sport_type = self.sport_type

        subject_type: list[dict[str, Any]] | None | Unset
        if isinstance(self.subject_type, Unset):
            subject_type = UNSET
        elif isinstance(self.subject_type, list):
            subject_type = []
            for subject_type_type_0_item_data in self.subject_type:
                subject_type_type_0_item = subject_type_type_0_item_data.to_dict()
                subject_type.append(subject_type_type_0_item)

        else:
            subject_type = self.subject_type

        time_of_day: None | str | Unset
        if isinstance(self.time_of_day, Unset):
            time_of_day = UNSET
        else:
            time_of_day = self.time_of_day

        track_id: None | str | Unset
        if isinstance(self.track_id, Unset):
            track_id = UNSET
        else:
            track_id = self.track_id

        weather: dict[str, Any] | None | Unset
        if isinstance(self.weather, Unset):
            weather = UNSET
        elif isinstance(self.weather, UnderstandingTag):
            weather = self.weather.to_dict()
        else:
            weather = self.weather

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actions is not UNSET:
            field_dict["actions"] = actions
        if animal_species is not UNSET:
            field_dict["animal_species"] = animal_species
        if brand_logo is not UNSET:
            field_dict["brand_logo"] = brand_logo
        if camera_angle is not UNSET:
            field_dict["camera_angle"] = camera_angle
        if caption is not UNSET:
            field_dict["caption"] = caption
        if color_palette is not UNSET:
            field_dict["color_palette"] = color_palette
        if composition is not UNSET:
            field_dict["composition"] = composition
        if dog_breeds is not UNSET:
            field_dict["dog_breeds"] = dog_breeds
        if dominant_hue is not UNSET:
            field_dict["dominant_hue"] = dominant_hue
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
        if facial_expression is not UNSET:
            field_dict["facial_expression"] = facial_expression
        if keyframe_ts is not UNSET:
            field_dict["keyframe_ts"] = keyframe_ts
        if light_key is not UNSET:
            field_dict["light_key"] = light_key
        if light_side is not UNSET:
            field_dict["light_side"] = light_side
        if light_style is not UNSET:
            field_dict["light_style"] = light_style
        if light_time is not UNSET:
            field_dict["light_time"] = light_time
        if mood is not UNSET:
            field_dict["mood"] = mood
        if mood_valence is not UNSET:
            field_dict["mood_valence"] = mood_valence
        if movement is not UNSET:
            field_dict["movement"] = movement
        if objects is not UNSET:
            field_dict["objects"] = objects
        if ocr_text is not UNSET:
            field_dict["ocr_text"] = ocr_text
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if people_age_range is not UNSET:
            field_dict["people_age_range"] = people_age_range
        if people_bucket is not UNSET:
            field_dict["people_bucket"] = people_bucket
        if people_count is not UNSET:
            field_dict["people_count"] = people_count
        if people_features is not UNSET:
            field_dict["people_features"] = people_features
        if people_gender is not UNSET:
            field_dict["people_gender"] = people_gender
        if place is not UNSET:
            field_dict["place"] = place
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if scale_rank is not UNSET:
            field_dict["scale_rank"] = scale_rank
        if season is not UNSET:
            field_dict["season"] = season
        if sensitive_content is not UNSET:
            field_dict["sensitive_content"] = sensitive_content
        if setting is not UNSET:
            field_dict["setting"] = setting
        if shot_scale is not UNSET:
            field_dict["shot_scale"] = shot_scale
        if sport_type is not UNSET:
            field_dict["sport_type"] = sport_type
        if subject_type is not UNSET:
            field_dict["subject_type"] = subject_type
        if time_of_day is not UNSET:
            field_dict["time_of_day"] = time_of_day
        if track_id is not UNSET:
            field_dict["track_id"] = track_id
        if weather is not UNSET:
            field_dict["weather"] = weather

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.understanding_tag import UnderstandingTag

        d = dict(src_dict)

        def _parse_actions(data: object) -> list[UnderstandingTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                actions_type_0 = []
                _actions_type_0 = data
                for actions_type_0_item_data in _actions_type_0:
                    actions_type_0_item = UnderstandingTag.from_dict(
                        actions_type_0_item_data
                    )

                    actions_type_0.append(actions_type_0_item)

                return actions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UnderstandingTag] | None | Unset, data)

        actions = _parse_actions(d.pop("actions", UNSET))

        def _parse_animal_species(
            data: object,
        ) -> list[UnderstandingTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                animal_species_type_0 = []
                _animal_species_type_0 = data
                for animal_species_type_0_item_data in _animal_species_type_0:
                    animal_species_type_0_item = UnderstandingTag.from_dict(
                        animal_species_type_0_item_data
                    )

                    animal_species_type_0.append(animal_species_type_0_item)

                return animal_species_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UnderstandingTag] | None | Unset, data)

        animal_species = _parse_animal_species(d.pop("animal_species", UNSET))

        def _parse_brand_logo(data: object) -> list[UnderstandingTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                brand_logo_type_0 = []
                _brand_logo_type_0 = data
                for brand_logo_type_0_item_data in _brand_logo_type_0:
                    brand_logo_type_0_item = UnderstandingTag.from_dict(
                        brand_logo_type_0_item_data
                    )

                    brand_logo_type_0.append(brand_logo_type_0_item)

                return brand_logo_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UnderstandingTag] | None | Unset, data)

        brand_logo = _parse_brand_logo(d.pop("brand_logo", UNSET))

        def _parse_camera_angle(data: object) -> None | UnderstandingTag | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                camera_angle_type_1 = UnderstandingTag.from_dict(data)

                return camera_angle_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UnderstandingTag | Unset, data)

        camera_angle = _parse_camera_angle(d.pop("camera_angle", UNSET))

        def _parse_caption(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caption = _parse_caption(d.pop("caption", UNSET))

        def _parse_color_palette(data: object) -> list[UnderstandingTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                color_palette_type_0 = []
                _color_palette_type_0 = data
                for color_palette_type_0_item_data in _color_palette_type_0:
                    color_palette_type_0_item = UnderstandingTag.from_dict(
                        color_palette_type_0_item_data
                    )

                    color_palette_type_0.append(color_palette_type_0_item)

                return color_palette_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UnderstandingTag] | None | Unset, data)

        color_palette = _parse_color_palette(d.pop("color_palette", UNSET))

        def _parse_composition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        composition = _parse_composition(d.pop("composition", UNSET))

        def _parse_dog_breeds(data: object) -> list[UnderstandingTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dog_breeds_type_0 = []
                _dog_breeds_type_0 = data
                for dog_breeds_type_0_item_data in _dog_breeds_type_0:
                    dog_breeds_type_0_item = UnderstandingTag.from_dict(
                        dog_breeds_type_0_item_data
                    )

                    dog_breeds_type_0.append(dog_breeds_type_0_item)

                return dog_breeds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UnderstandingTag] | None | Unset, data)

        dog_breeds = _parse_dog_breeds(d.pop("dog_breeds", UNSET))

        def _parse_dominant_hue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dominant_hue = _parse_dominant_hue(d.pop("dominant_hue", UNSET))

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

        def _parse_facial_expression(
            data: object,
        ) -> list[UnderstandingTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                facial_expression_type_0 = []
                _facial_expression_type_0 = data
                for facial_expression_type_0_item_data in _facial_expression_type_0:
                    facial_expression_type_0_item = UnderstandingTag.from_dict(
                        facial_expression_type_0_item_data
                    )

                    facial_expression_type_0.append(facial_expression_type_0_item)

                return facial_expression_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UnderstandingTag] | None | Unset, data)

        facial_expression = _parse_facial_expression(d.pop("facial_expression", UNSET))

        def _parse_keyframe_ts(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        keyframe_ts = _parse_keyframe_ts(d.pop("keyframe_ts", UNSET))

        def _parse_light_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        light_key = _parse_light_key(d.pop("light_key", UNSET))

        def _parse_light_side(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        light_side = _parse_light_side(d.pop("light_side", UNSET))

        def _parse_light_style(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                light_style_type_0 = cast(list[str], data)

                return light_style_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        light_style = _parse_light_style(d.pop("light_style", UNSET))

        def _parse_light_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        light_time = _parse_light_time(d.pop("light_time", UNSET))

        def _parse_mood(data: object) -> list[UnderstandingTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mood_type_0 = []
                _mood_type_0 = data
                for mood_type_0_item_data in _mood_type_0:
                    mood_type_0_item = UnderstandingTag.from_dict(mood_type_0_item_data)

                    mood_type_0.append(mood_type_0_item)

                return mood_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UnderstandingTag] | None | Unset, data)

        mood = _parse_mood(d.pop("mood", UNSET))

        def _parse_mood_valence(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mood_valence = _parse_mood_valence(d.pop("mood_valence", UNSET))

        def _parse_movement(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                movement_type_0 = cast(list[str], data)

                return movement_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        movement = _parse_movement(d.pop("movement", UNSET))

        def _parse_objects(data: object) -> list[UnderstandingTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                objects_type_0 = []
                _objects_type_0 = data
                for objects_type_0_item_data in _objects_type_0:
                    objects_type_0_item = UnderstandingTag.from_dict(
                        objects_type_0_item_data
                    )

                    objects_type_0.append(objects_type_0_item)

                return objects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UnderstandingTag] | None | Unset, data)

        objects = _parse_objects(d.pop("objects", UNSET))

        def _parse_ocr_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ocr_text = _parse_ocr_text(d.pop("ocr_text", UNSET))

        def _parse_orientation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        orientation = _parse_orientation(d.pop("orientation", UNSET))

        def _parse_people_age_range(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                people_age_range_type_0 = cast(list[str], data)

                return people_age_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        people_age_range = _parse_people_age_range(d.pop("people_age_range", UNSET))

        def _parse_people_bucket(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        people_bucket = _parse_people_bucket(d.pop("people_bucket", UNSET))

        def _parse_people_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        people_count = _parse_people_count(d.pop("people_count", UNSET))

        def _parse_people_features(
            data: object,
        ) -> list[UnderstandingTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                people_features_type_0 = []
                _people_features_type_0 = data
                for people_features_type_0_item_data in _people_features_type_0:
                    people_features_type_0_item = UnderstandingTag.from_dict(
                        people_features_type_0_item_data
                    )

                    people_features_type_0.append(people_features_type_0_item)

                return people_features_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UnderstandingTag] | None | Unset, data)

        people_features = _parse_people_features(d.pop("people_features", UNSET))

        def _parse_people_gender(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                people_gender_type_0 = cast(list[str], data)

                return people_gender_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        people_gender = _parse_people_gender(d.pop("people_gender", UNSET))

        def _parse_place(data: object) -> None | UnderstandingTag | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                place_type_1 = UnderstandingTag.from_dict(data)

                return place_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UnderstandingTag | Unset, data)

        place = _parse_place(d.pop("place", UNSET))

        def _parse_resolution(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        def _parse_scale_rank(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        scale_rank = _parse_scale_rank(d.pop("scale_rank", UNSET))

        def _parse_season(data: object) -> None | UnderstandingTag | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                season_type_1 = UnderstandingTag.from_dict(data)

                return season_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UnderstandingTag | Unset, data)

        season = _parse_season(d.pop("season", UNSET))

        def _parse_sensitive_content(
            data: object,
        ) -> list[UnderstandingTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sensitive_content_type_0 = []
                _sensitive_content_type_0 = data
                for sensitive_content_type_0_item_data in _sensitive_content_type_0:
                    sensitive_content_type_0_item = UnderstandingTag.from_dict(
                        sensitive_content_type_0_item_data
                    )

                    sensitive_content_type_0.append(sensitive_content_type_0_item)

                return sensitive_content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UnderstandingTag] | None | Unset, data)

        sensitive_content = _parse_sensitive_content(d.pop("sensitive_content", UNSET))

        def _parse_setting(data: object) -> None | UnderstandingTag | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                setting_type_1 = UnderstandingTag.from_dict(data)

                return setting_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UnderstandingTag | Unset, data)

        setting = _parse_setting(d.pop("setting", UNSET))

        def _parse_shot_scale(data: object) -> None | UnderstandingTag | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shot_scale_type_1 = UnderstandingTag.from_dict(data)

                return shot_scale_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UnderstandingTag | Unset, data)

        shot_scale = _parse_shot_scale(d.pop("shot_scale", UNSET))

        def _parse_sport_type(data: object) -> None | UnderstandingTag | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sport_type_type_1 = UnderstandingTag.from_dict(data)

                return sport_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UnderstandingTag | Unset, data)

        sport_type = _parse_sport_type(d.pop("sport_type", UNSET))

        def _parse_subject_type(data: object) -> list[UnderstandingTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subject_type_type_0 = []
                _subject_type_type_0 = data
                for subject_type_type_0_item_data in _subject_type_type_0:
                    subject_type_type_0_item = UnderstandingTag.from_dict(
                        subject_type_type_0_item_data
                    )

                    subject_type_type_0.append(subject_type_type_0_item)

                return subject_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UnderstandingTag] | None | Unset, data)

        subject_type = _parse_subject_type(d.pop("subject_type", UNSET))

        def _parse_time_of_day(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_of_day = _parse_time_of_day(d.pop("time_of_day", UNSET))

        def _parse_track_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        track_id = _parse_track_id(d.pop("track_id", UNSET))

        def _parse_weather(data: object) -> None | UnderstandingTag | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                weather_type_1 = UnderstandingTag.from_dict(data)

                return weather_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UnderstandingTag | Unset, data)

        weather = _parse_weather(d.pop("weather", UNSET))

        shot = cls(
            actions=actions,
            animal_species=animal_species,
            brand_logo=brand_logo,
            camera_angle=camera_angle,
            caption=caption,
            color_palette=color_palette,
            composition=composition,
            dog_breeds=dog_breeds,
            dominant_hue=dominant_hue,
            embedding=embedding,
            embedding_dim=embedding_dim,
            embedding_encoding=embedding_encoding,
            embedding_model=embedding_model,
            embedding_model_version=embedding_model_version,
            facial_expression=facial_expression,
            keyframe_ts=keyframe_ts,
            light_key=light_key,
            light_side=light_side,
            light_style=light_style,
            light_time=light_time,
            mood=mood,
            mood_valence=mood_valence,
            movement=movement,
            objects=objects,
            ocr_text=ocr_text,
            orientation=orientation,
            people_age_range=people_age_range,
            people_bucket=people_bucket,
            people_count=people_count,
            people_features=people_features,
            people_gender=people_gender,
            place=place,
            resolution=resolution,
            scale_rank=scale_rank,
            season=season,
            sensitive_content=sensitive_content,
            setting=setting,
            shot_scale=shot_scale,
            sport_type=sport_type,
            subject_type=subject_type,
            time_of_day=time_of_day,
            track_id=track_id,
            weather=weather,
        )

        shot.additional_properties = d
        return shot

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
