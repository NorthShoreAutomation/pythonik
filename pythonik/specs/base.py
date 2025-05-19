from pythonik._logger import logger
from urllib.parse import urljoin
from typing import Union, Type, Dict, Any, Optional

from pydantic import BaseModel
from requests import Request, Response, Session

from pythonik.models.base import Response as PythonikResponse

class Spec:
    server: str = ""
    api_version: str = "v1"
    base_url: str = "https://app.iconik.io"

    @classmethod
    def set_class_attribute(cls, name, value):
        setattr(cls, name, value)

    def __init__(self, session: Session, timeout: int = 3, base_url: str = "https://app.iconik.io"):
        self.session = session
        self.timeout = timeout
        self.set_class_attribute("base_url", base_url)
    
        
    @staticmethod
    def _prepare_model_data(data: Union[BaseModel, Dict[str, Any]], exclude_defaults: bool = True) -> Dict[str, Any]:
        """
        Prepare data for request, handling both Pydantic models and dicts.
        
        Args:
            data: Either a Pydantic model instance or a dict
            exclude_defaults: Whether to exclude default values when dumping Pydantic models
            
        Returns:
            Dict ready to be sent in request
        """
        if isinstance(data, BaseModel):
            return data.model_dump(exclude_defaults=exclude_defaults)
        return data

    @staticmethod
    def parse_response(response: Response, model: Optional[Type[BaseModel]] = None) -> PythonikResponse:
        """
        Return an ErrorResponse object if the response error code is >=400, an instance of "model", or the status code

        Args:
            response: The HTTP response
            model: The Pydantic model class to parse the response into
        """
        # try to populate the model
        if response.ok:
            logger.debug(response.text)
            if model:
                data = response.json()
                model_instance = model.model_validate(data)
                return PythonikResponse(response=response, data=model_instance)

        return PythonikResponse(response=response, data=None)

    @classmethod
    def gen_url(cls, path):
        url = urljoin(cls.server, f"{cls.api_version}/")
        url = urljoin(cls.base_url, url)
        return urljoin(url, path)

    def send_request(self, method, path, **kwargs) -> Response:
        """
        Send an http request to a particular URL with a particular method and arguments
        """

        url = self.gen_url(path)
        logger.debug("Sending {} request to {}", method, url)
        request = Request(
            method=method, url=url, headers=self.session.headers, **kwargs
        )
        prepped_request = self.session.prepare_request(request)
        response = self.session.send(prepped_request, timeout=self.timeout)

        return response

    def _delete(self, path, **kwargs):
        """DELETE http request"""
        return self.send_request("DELETE", path, **kwargs)

    def _get(self, path, **kwargs):
        """GET http request"""
        return self.send_request("GET", path, **kwargs)

    def _patch(self, path, **kwargs):
        """PATCH http request"""
        return self.send_request("PATCH", path, **kwargs)

    def _post(self, path, **kwargs):
        """POST http request"""
        return self.send_request("POST", path, **kwargs)

    def _put(self, path, **kwargs):
        """PUT http request"""
        return self.send_request("PUT", path, **kwargs)
