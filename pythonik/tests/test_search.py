import uuid
import pytest
import requests_mock
# from urllib.parse import parse_qs # Unused import removed

from pythonik.client import PythonikClient
from pythonik.models.search.search_body import Filter, SearchBody, SortItem, Term
from pythonik.specs.search import SEARCH_PATH, SearchSpec

# Unused imports removed by Cascade:
# from pythonik.models.metadata.views import ViewMetadata
# from pythonik.models.mutation.metadata.mutate import (
#     UpdateMetadata,
#     UpdateMetadataResponse,
# )
# from pythonik.specs.metadata import (
#     ASSET_METADATA_FROM_VIEW_PATH,
#     UPDATE_ASSET_METADATA,
#     MetadataSpec,
# )

def test_search_assets_basic():
    """Test basic search functionality, similar to original test but using named params."""
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        # view_id = str(uuid.uuid4()) # Unused variable removed

        search_criteria = SearchBody(
            doc_types=["assets"],
            query=f"id:{asset_id}",
            filter=Filter(operator="AND", terms=[Term(name="status", value="active")]),
            sort=[SortItem(name="date_created", order="desc")]
        )

        mock_address = SearchSpec.gen_url(SEARCH_PATH)
        # Mock will match the base address; query params will be checked on m.last_request.qs
        matcher = m.post(mock_address, json=search_criteria.model_dump())

        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        client.search().search(
            search_body=search_criteria,
            generate_signed_url=True,
            generate_signed_download_url=True
        )
        assert matcher.called_once
        expected_qs = {
            'generate_signed_url': ['true'],
            'generate_signed_download_url': ['true']
        }
        assert m.last_request.qs == expected_qs


# Test cases for various query parameter combinations
# Each tuple: (test_id, query_params_for_search_method, expected_query_string_dict)
search_param_test_cases = [
    (
        "pagination",
        {"per_page": 20, "page": 3},
        {"per_page": ["20"], "page": ["3"]}
    ),
    (
        "signed_urls_off_and_proxy_on",
        {"generate_signed_url": False, "generate_signed_download_url": False, "generate_signed_proxy_url": True},
        {"generate_signed_url": ["false"], "generate_signed_download_url": ["false"], "generate_signed_proxy_url": ["true"]}
    ),
    (
        "save_history_off",
        {"save_search_history": False},
        {"save_search_history": ["false"]}
    ),
    (
        "scroll_params_active",
        {"scroll": True, "scroll_id": "test_scroll_123"},
        {"scroll": ["true"], "scroll_id": ["test_scroll_123"]}
    ),
    (
        "all_bools_mixed_values",
        {
            "generate_signed_url": True,
            "generate_signed_download_url": False,
            "generate_signed_proxy_url": True,
            "save_search_history": False,
        },
        {
            "generate_signed_url": ["true"],
            "generate_signed_download_url": ["false"],
            "generate_signed_proxy_url": ["true"],
            "save_search_history": ["false"],
        }
    ),
    (
        "no_extra_query_params",
        {},
        {}
    ),
]

@pytest.mark.parametrize("test_id, query_params, expected_qs_dict", search_param_test_cases)
def test_search_with_various_query_params(test_id, query_params, expected_qs_dict):
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())

        search_body_data = SearchBody(
            doc_types=["collections"],
            query=f"title:Test Collection AND id:{asset_id}"
        )

        base_mock_address = SearchSpec.gen_url(SEARCH_PATH)
        # Mock the base address, query parameters will be checked via m.last_request.qs
        matcher = m.post(base_mock_address, json=search_body_data.model_dump())

        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        client.search().search(
            search_body=search_body_data,
            **query_params  # Pass the dictionary of query params as keyword arguments
        )

        assert matcher.called_once
        assert m.last_request.qs == expected_qs_dict
