import uuid
from pythonik.client import PythonikClient
from pythonik.models.files.format import Format
from pythonik.models.files.proxy import Proxy
import requests_mock

from pythonik.specs.files import (
    GET_ASSET_PROXY_PATH,
    GET_ASSETS_FORMATS_PATH,
    FilesSpec,
)


def test_get_proxy():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())
        proxy_id = str(uuid.uuid4())

        model = Proxy()
        data = model.model_dump()
        mock_address = FilesSpec.gen_url(
            GET_ASSET_PROXY_PATH.format(asset_id, proxy_id)
        )

        m.get(mock_address, json=data)
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        client.files().get_asset_proxy(asset_id, proxy_id)


def test_get_asset_formats():
    with requests_mock.Mocker() as m:
        app_id = str(uuid.uuid4())
        auth_token = str(uuid.uuid4())
        asset_id = str(uuid.uuid4())

        model = Format()
        data = model.model_dump()
        mock_address = FilesSpec.gen_url(GET_ASSETS_FORMATS_PATH.format(asset_id))
        m.get(mock_address, json=data)
        client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=3)
        params = {"per_page": 20}
        client.files().get_asset_formats(asset_id, params=params)