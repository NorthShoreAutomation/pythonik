from typing import Union, Dict, Any, Optional

from pythonik.models.base import Response
from pythonik.models.search.search_body import SearchBody
from pythonik.models.search.search_response import SearchResponse
from pythonik.specs.base import Spec


SEARCH_PATH = "search/"


class SearchSpec(Spec):
    server = "API/search/"

    def search(
        self,
        search_body: Union[SearchBody, Dict[str, Any]],
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        scroll: Optional[bool] = None,  # Deprecated
        scroll_id: Optional[str] = None,  # Deprecated
        generate_signed_url: Optional[bool] = None,
        generate_signed_download_url: Optional[bool] = None,
        generate_signed_proxy_url: Optional[bool] = None,
        save_search_history: Optional[bool] = None,
        exclude_defaults: bool = True,
        **kwargs,
    ) -> Response:  # Response.data will be SearchResponse
        """
        Search iconik.
        Corresponds to POST /v1/search/

        Args:
            search_body: Search parameters, either as SearchBody model or dict.
            per_page: The number of documents for each page.
            page: Which page number to fetch.
            scroll: If true, uses scroll pagination. (Deprecated, use search_after in body).
            scroll_id: Scroll ID for scroll pagination. (Deprecated).
            generate_signed_url: Set to false if you don't need a URL, will speed things up.
            generate_signed_download_url: Set to true if you also want the file download URLs generated.
            generate_signed_proxy_url: Set to true if you want to generate signed download urls for proxies.
            save_search_history: Set to false if you don't want to save the search to the history.
            exclude_defaults: Whether to exclude default values when dumping Pydantic models for the request body.
            **kwargs: Additional kwargs to pass to the request (e.g., headers).

        Returns:
            Response with SearchResponse data model.
        """
        json_data = self._prepare_model_data(
            search_body, exclude_defaults=exclude_defaults
        )

        params = {}
        if per_page is not None:
            params["per_page"] = per_page
        if page is not None:
            params["page"] = page
        if scroll is not None:
            params["scroll"] = scroll
        if scroll_id is not None:
            params["scroll_id"] = scroll_id
        if generate_signed_url is not None:
            params["generate_signed_url"] = generate_signed_url
        if generate_signed_download_url is not None:
            params["generate_signed_download_url"] = generate_signed_download_url
        if generate_signed_proxy_url is not None:
            params["generate_signed_proxy_url"] = generate_signed_proxy_url
        if save_search_history is not None:
            params["save_search_history"] = save_search_history

        resp = self._post(
            SEARCH_PATH,  # Use the new path constant, which is ""
            json=json_data,
            params=params if params else None,
            **kwargs,
        )
        return self.parse_response(resp, SearchResponse)
