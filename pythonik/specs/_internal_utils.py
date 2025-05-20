from typing import Any

from pythonik.exceptions import PythonikException


def is_pydantic_model(obj: Any) -> bool:
    """
    Checks if an object is a Pydantic model instance.

    Args:
        obj: The object to check.

    Returns:
        True if the object is a Pydantic model instance, False otherwise.
    """
    # Check for common Pydantic model attributes/methods
    if obj is None:
        return False
    try:
        # Pydantic v1
        has_dict_method = hasattr(obj, "dict") and callable(
            getattr(obj, "dict", None))
        # Pydantic v2
        has_model_dump = hasattr(obj, "model_dump") and callable(
            getattr(obj, "model_dump", None))
        # Check for schema-related attributes that are common in Pydantic models
        has_schema_attrs = hasattr(obj, "__fields__") or hasattr(
            obj, "model_fields")
        return (has_dict_method or has_model_dump) and has_schema_attrs
    except PythonikException:
        return False
