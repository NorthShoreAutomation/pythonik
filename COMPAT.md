# pythonik 1.x compatibility

pythonik 2.0 ships the complete pythonik 1.x hand-written API surface alongside the
generated SDK, so existing 1.x code runs unchanged:

- `from pythonik.client import PythonikClient` — same constructor
  (`PythonikClient(app_id=..., auth_token=..., timeout=..., base_url=...)`), same
  spec accessors (`.assets()`, `.collections()`, `.files()`, `.jobs()`,
  `.metadata()`, `.search()`), same methods on every spec class.
- `pythonik.specs.*` and `pythonik.models.*` import paths are unchanged, including
  the URL-template constants the specs export.
- Methods return the same `pythonik.models.base.Response` wrapper
  (`.response` is a `requests.Response`, `.data` is the parsed pydantic model), with
  the same `exclude_defaults=` kwargs and the same retry behavior
  (urllib3 `Retry(total=4, backoff_factor=3)`).

The compat layer is the 1.x implementation itself (as of 1.15.0), vendored verbatim
into this generated package and verified by running the full 1.x test suite against
it on every regeneration. It runs on `requests`, independent of the generated
httpx-based 2.0 surface — the two coexist and share nothing but the package.

## Deviations from 1.x

- **`pythonik.__version__` is `"2.0.0"`**, not `"1.15.0"`.
- **Debug prints removed.** 1.x printed every request URL and every successful
  response body to stdout (`Spec.send_request` / `Spec.parse_response`). The compat
  layer makes the same requests and returns the same values but no longer prints.
- **loguru replaced with stdlib `logging`.** The single 1.x loguru call site
  (`MetadataSpec.get_object_metadata` with `intercept_404`, warning when a disabled
  `raise_for_status` is called) now logs via `logging.getLogger("pythonik.specs.metadata")`.
  The package no longer depends on loguru.
- **`pythonik.tests` is not shipped.** The 1.x test suite (and its `requests-mock`
  dependency) is not part of the installed package; it runs in the generator instead.

Everything else — method names, parameters, defaults, URLs, request bodies, response
parsing, exceptions (`pythonik.exceptions`), constants (`pythonik.constants`) — matches
1.x exactly.

## Status

The compat layer is frozen at the 1.x surface for backwards compatibility. New code
should use the generated per-service subpackages (`pythonik.assets`,
`pythonik.files`, ...), which cover the full 953-endpoint iconik API — see README.md.
