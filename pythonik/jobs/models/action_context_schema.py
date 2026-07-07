from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
        abort (ActionContextValue | Unset):
        change_priority (ActionContextValue | Unset):
        pause (ActionContextValue | Unset):
        restart (ActionContextValue | Unset):
        resume (ActionContextValue | Unset):
    """

    abort: ActionContextValue | Unset = UNSET
    change_priority: ActionContextValue | Unset = UNSET
    pause: ActionContextValue | Unset = UNSET
    restart: ActionContextValue | Unset = UNSET
    resume: ActionContextValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abort: dict[str, Any] | Unset = UNSET
        if not isinstance(self.abort, Unset):
            abort = self.abort.to_dict()

        change_priority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.change_priority, Unset):
            change_priority = self.change_priority.to_dict()

        pause: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pause, Unset):
            pause = self.pause.to_dict()

        restart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restart, Unset):
            restart = self.restart.to_dict()

        resume: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resume, Unset):
            resume = self.resume.to_dict()

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
        _abort = d.pop("ABORT", UNSET)
        abort: ActionContextValue | Unset
        if isinstance(_abort, Unset):
            abort = UNSET
        else:
            abort = ActionContextValue.from_dict(_abort)

        _change_priority = d.pop("CHANGE_PRIORITY", UNSET)
        change_priority: ActionContextValue | Unset
        if isinstance(_change_priority, Unset):
            change_priority = UNSET
        else:
            change_priority = ActionContextValue.from_dict(_change_priority)

        _pause = d.pop("PAUSE", UNSET)
        pause: ActionContextValue | Unset
        if isinstance(_pause, Unset):
            pause = UNSET
        else:
            pause = ActionContextValue.from_dict(_pause)

        _restart = d.pop("RESTART", UNSET)
        restart: ActionContextValue | Unset
        if isinstance(_restart, Unset):
            restart = UNSET
        else:
            restart = ActionContextValue.from_dict(_restart)

        _resume = d.pop("RESUME", UNSET)
        resume: ActionContextValue | Unset
        if isinstance(_resume, Unset):
            resume = UNSET
        else:
            resume = ActionContextValue.from_dict(_resume)

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
