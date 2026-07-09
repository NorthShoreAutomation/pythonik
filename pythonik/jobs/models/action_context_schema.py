from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_context_value import ActionContextValue


T = TypeVar("T", bound="ActionContextSchema")


@_attrs_define
class ActionContextSchema:
    """
    Attributes:
        abort (ActionContextValue | None | Unset):
        change_priority (ActionContextValue | None | Unset):
        pause (ActionContextValue | None | Unset):
        restart (ActionContextValue | None | Unset):
        resume (ActionContextValue | None | Unset):
    """

    abort: ActionContextValue | None | Unset = UNSET
    change_priority: ActionContextValue | None | Unset = UNSET
    pause: ActionContextValue | None | Unset = UNSET
    restart: ActionContextValue | None | Unset = UNSET
    resume: ActionContextValue | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_context_value import ActionContextValue

        abort: dict[str, Any] | None | Unset
        if isinstance(self.abort, Unset):
            abort = UNSET
        elif isinstance(self.abort, ActionContextValue):
            abort = self.abort.to_dict()
        else:
            abort = self.abort

        change_priority: dict[str, Any] | None | Unset
        if isinstance(self.change_priority, Unset):
            change_priority = UNSET
        elif isinstance(self.change_priority, ActionContextValue):
            change_priority = self.change_priority.to_dict()
        else:
            change_priority = self.change_priority

        pause: dict[str, Any] | None | Unset
        if isinstance(self.pause, Unset):
            pause = UNSET
        elif isinstance(self.pause, ActionContextValue):
            pause = self.pause.to_dict()
        else:
            pause = self.pause

        restart: dict[str, Any] | None | Unset
        if isinstance(self.restart, Unset):
            restart = UNSET
        elif isinstance(self.restart, ActionContextValue):
            restart = self.restart.to_dict()
        else:
            restart = self.restart

        resume: dict[str, Any] | None | Unset
        if isinstance(self.resume, Unset):
            resume = UNSET
        elif isinstance(self.resume, ActionContextValue):
            resume = self.resume.to_dict()
        else:
            resume = self.resume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abort is not UNSET:
            field_dict["ABORT"] = abort
        if change_priority is not UNSET:
            field_dict["CHANGE_PRIORITY"] = change_priority
        if pause is not UNSET:
            field_dict["PAUSE"] = pause
        if restart is not UNSET:
            field_dict["RESTART"] = restart
        if resume is not UNSET:
            field_dict["RESUME"] = resume

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_context_value import ActionContextValue

        d = dict(src_dict)

        def _parse_abort(data: object) -> ActionContextValue | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                abort_type_1 = ActionContextValue.from_dict(data)

                return abort_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionContextValue | None | Unset, data)

        abort = _parse_abort(d.pop("ABORT", UNSET))

        def _parse_change_priority(data: object) -> ActionContextValue | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                change_priority_type_1 = ActionContextValue.from_dict(data)

                return change_priority_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionContextValue | None | Unset, data)

        change_priority = _parse_change_priority(d.pop("CHANGE_PRIORITY", UNSET))

        def _parse_pause(data: object) -> ActionContextValue | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pause_type_1 = ActionContextValue.from_dict(data)

                return pause_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionContextValue | None | Unset, data)

        pause = _parse_pause(d.pop("PAUSE", UNSET))

        def _parse_restart(data: object) -> ActionContextValue | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                restart_type_1 = ActionContextValue.from_dict(data)

                return restart_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionContextValue | None | Unset, data)

        restart = _parse_restart(d.pop("RESTART", UNSET))

        def _parse_resume(data: object) -> ActionContextValue | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resume_type_1 = ActionContextValue.from_dict(data)

                return resume_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionContextValue | None | Unset, data)

        resume = _parse_resume(d.pop("RESUME", UNSET))

        action_context_schema = cls(
            abort=abort,
            change_priority=change_priority,
            pause=pause,
            restart=restart,
            resume=resume,
        )

        action_context_schema.additional_properties = d
        return action_context_schema

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
