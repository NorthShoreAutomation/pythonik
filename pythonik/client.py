from urllib3.util import Retry
from requests import Session
from requests.adapters import HTTPAdapter

from pythonik.specs.acls import AclsSpec
from pythonik.specs.assets import AssetSpec
from pythonik.specs.files import FilesSpec
from pythonik.specs.jobs import JobSpec
from pythonik.specs.metadata import MetadataSpec
from pythonik.specs.search import SearchSpec
from pythonik.specs.collection import CollectionSpec


# Iconik APIs
class PythonikClient:
    """
    Iconik Client
    """

    def __init__(self, app_id: str, auth_token: str, timeout: int, base_url: str  = "https://app.iconik.io" ):
        self.session = Session()
        self.base_url = base_url
        retry_strategy = Retry(
            total=4,  # Maximum number of retries
            backoff_factor=3,
        )
        http_adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", http_adapter)
        self.session.mount("https://", http_adapter)
        self.session.headers = {
            "App-ID": app_id,
            "Auth-Token": auth_token,
            "Accept": "application/json",
        }
        self.timeout = timeout

    def collections(self):
        return CollectionSpec(self.session, self.timeout, self.base_url)

    def assets(self):
        return AssetSpec(self.session, self.timeout, self.base_url)

    def files(self):
        return FilesSpec(self.session, self.timeout, self.base_url)

    def metadata(self):
        return MetadataSpec(self.session, self.timeout, self.base_url)

    def search(self):
        return SearchSpec(self.session, self.timeout, self.base_url)

    def jobs(self):
        return JobSpec(self.session, self.timeout, self.base_url)

    def acls(self) -> AclsSpec:
        return AclsSpec(self.session, self.timeout, self.base_url)
