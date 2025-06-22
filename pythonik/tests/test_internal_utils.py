# pythonik/tests/test_internal_utils.py
import uuid

from pydantic import BaseModel

from pythonik.exceptions import PythonikException
from pythonik.specs._internal_utils import is_pydantic_model


class PydanticV1StyleModel:
    """Mock class that mimics a Pydantic v1 model."""

    __fields__ = {"test": "field"}

    def dict(self):
        return {"test": "value"}


class PydanticV2StyleModel:
    """Mock class that mimics a Pydantic v2 model."""

    model_fields = {"test": "field"}

    def model_dump(self):
        return {"test": "value"}


class RealPydanticModel(BaseModel):
    """A real Pydantic model for testing."""

    id: str
    name: str


class NonPydanticClass:
    """A regular class that is not a Pydantic model."""

    def __init__(self):
        self.value = "test"


def test_is_pydantic_model_with_real_model():
    """Test is_pydantic_model with a real Pydantic model."""
    model = RealPydanticModel(id=str(uuid.uuid4()), name="Test Model")
    assert is_pydantic_model(model) is True


def test_is_pydantic_model_with_none():
    """Test is_pydantic_model with None."""
    assert is_pydantic_model(None) is False


def test_is_pydantic_model_with_non_model():
    """Test is_pydantic_model with a non-model class instance."""
    non_model = NonPydanticClass()
    assert is_pydantic_model(non_model) is False


def test_is_pydantic_model_with_v1_style_mock():
    """Test is_pydantic_model with a class that looks like a Pydantic v1 model."""
    v1_model = PydanticV1StyleModel()
    assert is_pydantic_model(v1_model) is True


def test_is_pydantic_model_with_v2_style_mock():
    """Test is_pydantic_model with a class that looks like a Pydantic v2 model."""
    v2_model = PydanticV2StyleModel()
    assert is_pydantic_model(v2_model) is True


def test_is_pydantic_model_with_dict():
    """Test is_pydantic_model with a dictionary."""
    dict_data = {"id": str(uuid.uuid4()), "name": "Test Dict"}
    assert is_pydantic_model(dict_data) is False


def test_is_pydantic_model_with_exception():
    """Test is_pydantic_model when an exception is raised."""

    class ExceptionRaisingModel:
        """A model that raises an exception when properties are accessed."""

        @property
        def dict(self):
            raise PythonikException("Test exception")

        @property
        def model_dump(self):
            raise PythonikException("Test exception")

        @property
        def __fields__(self):
            raise PythonikException("Test exception")

    model = ExceptionRaisingModel()
    assert is_pydantic_model(model) is False
