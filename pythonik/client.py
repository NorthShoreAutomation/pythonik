from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from pythonik.specs.assets import AssetSpec
from pythonik.specs.collection import CollectionSpec
from pythonik.specs.files import FilesSpec
from pythonik.specs.jobs import JobSpec
from pythonik.specs.metadata import MetadataSpec
from pythonik.specs.search import SearchSpec


class PythonikClient:
    """
    Iconik Client providing access to all API endpoints.

    This client provides both implemented and placeholder methods for
    various Iconik API endpoints. Placeholder methods will raise
    NotImplementedError until the corresponding specs are implemented.
    """

    def __init__(
        self,
        app_id: str,
        auth_token: str,
        timeout: int,
        base_url: str = "https://app.iconik.io",
    ):
        """
        Initialize the Pythonik client.

        Args:
            app_id: Application ID for Iconik API
            auth_token: Authentication token
            timeout: Request timeout in seconds
            base_url: Base URL for Iconik instance
        """
        self.session = Session()
        self.base_url = base_url
        retry_strategy = Retry(
            total=4,
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

    # Implemented endpoints
    def collections(self):
        """Access collections API endpoints."""
        return CollectionSpec(self.session, self.timeout, self.base_url)

    def assets(self):
        """Access assets API endpoints."""
        return AssetSpec(self.session, self.timeout, self.base_url)

    def files(self):
        """Access files API endpoints."""
        return FilesSpec(self.session, self.timeout, self.base_url)

    def metadata(self):
        """Access metadata API endpoints."""
        return MetadataSpec(self.session, self.timeout, self.base_url)

    def search(self):
        """Access search API endpoints."""
        return SearchSpec(self.session, self.timeout, self.base_url)

    def jobs(self):
        """Access jobs API endpoints."""
        return JobSpec(self.session, self.timeout, self.base_url)

    def acls(self):
        """
        Access ACLs (Access Control Lists) API endpoints.

        Raises:
            NotImplementedError: ACLs endpoint not yet implemented
        """
        raise NotImplementedError(
            "ACLs endpoint is not yet implemented. "
            "Please check the documentation for updates or contribute "
            "to the pythonik project.")

    def auth(self):
        """
        Access authentication API endpoints.

        Raises:
            NotImplementedError: Auth endpoint not yet implemented
        """
        raise NotImplementedError(
            "Authentication endpoint is not yet implemented. "
            "Please check the documentation for updates or contribute "
            "to the pythonik project.")

    def automations(self):
        """
        Access automations API endpoints.

        Raises:
            NotImplementedError: Automations endpoint not yet implemented
        """
        raise NotImplementedError(
            "Automations endpoint is not yet implemented. "
            "Please check the documentation for updates or contribute "
            "to the pythonik project.")

    def notifications(self):
        """
        Access notifications API endpoints.

        Raises:
            NotImplementedError: Notifications endpoint not yet implemented
        """
        raise NotImplementedError(
            "Notifications endpoint is not yet implemented. "
            "Please check the documentation for updates or contribute "
            "to the pythonik project.")

    def settings(self):
        """
        Access settings API endpoints.

        Raises:
            NotImplementedError: Settings endpoint not yet implemented
        """
        raise NotImplementedError(
            "Settings endpoint is not yet implemented. "
            "Please check the documentation for updates or contribute "
            "to the pythonik project.")

    def stats(self):
        """
        Access statistics API endpoints.

        Raises:
            NotImplementedError: Stats endpoint not yet implemented
        """
        raise NotImplementedError(
            "Statistics endpoint is not yet implemented. "
            "Please check the documentation for updates or contribute "
            "to the pythonik project.")

    def transcode(self):
        """
        Access transcoding API endpoints.

        Raises:
            NotImplementedError: Transcode endpoint not yet implemented
        """
        raise NotImplementedError(
            "Transcoding endpoint is not yet implemented. "
            "Please check the documentation for updates or contribute "
            "to the pythonik project.")

    def users(self):
        """
        Access users API endpoints.

        Raises:
            NotImplementedError: Users endpoint not yet implemented
        """
        raise NotImplementedError(
            "Users endpoint is not yet implemented. "
            "Please check the documentation for updates or contribute "
            "to the pythonik project.")

    def users_notifications(self):
        """
        Access user notifications API endpoints.

        Raises:
            NotImplementedError: User notifications endpoint not yet
                implemented
        """
        raise NotImplementedError(
            "User notifications endpoint is not yet implemented. "
            "Please check the documentation for updates or contribute "
            "to the pythonik project.")
