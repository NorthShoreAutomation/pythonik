# pythonik

A complete, generated Python SDK for the [iconik](https://app.iconik.io) media management API.

- **15 services**, one subpackage each: `pythonik.acls`, `pythonik.assets`, `pythonik.auth`, `pythonik.automations`, `pythonik.files`, `pythonik.jobs`, `pythonik.metadata`, `pythonik.ml`, `pythonik.notifications`, `pythonik.search`, `pythonik.settings`, `pythonik.stats`, `pythonik.transcode`, `pythonik.users`, `pythonik.usersnotifications`
- **Every operation in every service** — generated from iconik's published OpenAPI specs with [openapi-python-client](https://github.com/openapi-generators/openapi-python-client). Fully typed (attrs models, `py.typed`), sync and async for every endpoint (httpx).
- **2.0 is a rewrite with a 1.x compatibility layer**: 1.x was hand-written and covered a subset of the API; 2.0 is generated and covers the complete API surface (953 endpoints). The full 1.x interface (`pythonik.client.PythonikClient`, `pythonik.specs.*`, `pythonik.models.*`) still ships and works unchanged — see [COMPAT.md](COMPAT.md) for the short list of deviations.

## Install

```sh
pip install pythonik
```

Requires Python >= 3.10.

## Usage

Set your `App-ID` / `Auth-Token` credentials **once, on the client**; every call through that client is authenticated. Each service has its own base URL, `https://app.iconik.io/API/<service>`:

```python
import os

from pythonik.assets import Client
from pythonik.assets.api.assets import get_assets_by_asset_id

client = Client(
    base_url="https://app.iconik.io/API/assets",
    headers={
        "App-ID": os.environ["ICONIK_APP_ID"],
        "Auth-Token": os.environ["ICONIK_AUTH_TOKEN"],
    },
)

asset = get_assets_by_asset_id.sync(asset_id="some-asset-uuid", client=client)
print(asset)
```

Every endpoint module offers `sync`, `sync_detailed`, `asyncio`, and `asyncio_detailed`. The `*_detailed` variants return a `Response` with status code, headers, and the parsed body.

API function paths mirror the REST API: `GET /v1/assets/{asset_id}/versions/` on the assets service is `pythonik.assets.api.assets.get_assets_by_asset_id_versions`. If you know the endpoint, you know the function.

All subpackages share one client implementation (`pythonik._base`) — a `Client` built for one service works for another by swapping `base_url`, and cross-service `isinstance` checks on errors/types behave as expected.

## Upgrading from 1.x

Nothing to change: 2.0 vendors the 1.x implementation, so existing code keeps working —

```python
from pythonik.client import PythonikClient

client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=10)
asset = client.assets().get(asset_id)   # pythonik.models.base.Response(.response, .data)
```

The 1.x test suite runs against this package on every regeneration. The compat layer is frozen at the 1.x surface (~100 methods across 6 spec classes); use the generated subpackages for everything 1.x didn't cover. Deviations from 1.x (debug prints removed, loguru dropped): [COMPAT.md](COMPAT.md).

## How it's built

**This package is generated — don't edit it by hand.** It is emitted by [NorthShoreAutomation/iconik-sdk-generator](https://github.com/NorthShoreAutomation/iconik-sdk-generator), which fetches iconik's live OpenAPI specs, applies lossless overlay fixes (deterministic operationIds, client-level auth via injected security schemes, enum/oneOf/content-type repairs — all bigint-safe), runs openapi-python-client per service, and merges the 15 clients into this one package. The full pipeline and the iconik spec quirks knowledge base live in that repo.
