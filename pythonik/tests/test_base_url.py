import uuid
import pytest
from pythonik.client import PythonikClient
from pythonik.specs.assets import AssetSpec
from pythonik.specs.collection import CollectionSpec
from pythonik.specs.files import FilesSpec
from pythonik.specs.jobs import JobSpec
from pythonik.specs.metadata import MetadataSpec
from pythonik.specs.search import SearchSpec
from pythonik.specs.base import Spec

SPECS = [
    AssetSpec,
    CollectionSpec,
    FilesSpec,
    JobSpec,
    MetadataSpec,
    SearchSpec
]

def test_default_base_url():
    """Test that all specs have the default base URL by default"""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

    for spec_class in SPECS:
        spec = spec_class(client.session, timeout=3)
        assert spec.base_url == "https://app.iconik.io"
        # Test that gen_url includes the base_url
        test_path = "test/path"
        url = spec.gen_url(test_path)
        assert url.startswith("https://app.iconik.io/")
        assert test_path in url

def test_alternative_base_url():
    """Test that all specs accept and use an alternative base URL"""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    alt_base_url = "https://alt.iconik.io"
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

    for spec_class in SPECS:
        spec = spec_class(client.session, timeout=3, base_url=alt_base_url)
        assert spec.base_url == alt_base_url
        # Test that gen_url includes the alternative base_url
        test_path = "test/path"
        url = spec.gen_url(test_path)
        assert url.startswith(f"{alt_base_url}/")
        assert test_path in url

def test_multiple_instances_share_base_url():
    """Test that multiple instances of the same spec share the base URL"""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    alt_base_url = "https://alt.iconik.io"
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

    for name, spec in vars(client).items():
        if isinstance(spec, Spec):
            try:
                # Create first instance with alternative base URL
                spec1 = type(spec)(client.session, timeout=3, base_url=alt_base_url)
                assert spec1.base_url == alt_base_url

                # Create second instance without specifying base URL
                spec2 = type(spec)(client.session, timeout=3)
                assert spec2.base_url == alt_base_url  # Should inherit the changed base URL
            except Exception as e:
                print(f"Failed for spec {name}: {e}")
                raise
            finally:
                # Reset base URL for next spec test
                spec_class = type(spec)
                spec_class.set_class_attribute("base_url", "https://app.iconik.io")

def test_base_url_inheritance():
    """Test that subclasses inherit the base URL from parent class"""
    app_id = str(uuid.uuid4())
    auth_token = str(uuid.uuid4())
    alt_base_url = "https://alt.iconik.io"
    client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)

    try:
        # Set base_url on each spec class
        for spec_class in SPECS:
            spec_class.set_class_attribute("base_url", alt_base_url)
            # Debug: check the base_url right after setting it
            print(f"{spec_class.__name__} base_url: {spec_class.base_url}")

        # Test each spec class
        for spec_class in SPECS:
            # Create new instance without specifying base URL
            spec = spec_class(client.session, 3, alt_base_url)
            assert spec.base_url == alt_base_url
    finally:
        # Reset base URL for each spec class
        for spec_class in SPECS:
            spec_class.set_class_attribute("base_url", "https://app.iconik.io")
