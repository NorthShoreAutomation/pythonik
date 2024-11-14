# Changelog

## 2024-11-14 "You want some, you lose some" - version 0.9.0

### Added
- Add collections API endpoints to asset spec
- Add bulk & permanent delete operations
- Add collection endpoints and models

### Fixed
- Fix incorrect path name for object view mutations (missing 'v1/' prefix)
- Fix metadata field type to support multiple formats (changed to Any type)

### Changed
- Update metadata field types to be more flexible, supporting boolean, integer, and list values

## 2024-11-11 "Accidents Happen" - version 0.8.0

### Changed
- No substantial changes, just a version bump

## 2024-11-08 "Croissant" - version 0.7.0

### Added
- Add asset version creation endpoints:
  - Create new versions of existing assets (/v1/assets/{asset_id}/versions/)
  - Create versions from other assets (/v1/assets/{asset_id}/versions/from/assets/{source_asset_id}/)
- Add comprehensive version models:
  - `AssetVersionCreate` for basic version creation
  - `AssetVersionFromAssetCreate` for cross-asset version creation
  - `AssetVersionResponse` for version creation responses
- Add support for version creation with:
  - Metadata copying
  - Segment copying with type filtering
  - Source version specification
- Add proper handling of 200+ status codes for async version operations

### Changed
- Update AssetSpec to include version-related endpoints and models
- Improve type hints and documentation for version creation methods

## 2024-11-07 "rm -rf" - version 0.6.3

### Added
- Add DELETE endpoint for asset file sets (/v1/assets/{asset_id}/file_sets/{file_set_id}/)
- Add delete_asset_file_set method with dual response handling:
  - 200: Returns FileSet model when file set is marked as deleted
  - 204: Returns empty response when immediate deletion occurs
  - Includes status code conditional logic and optional keep_source parameter support

### Changed
- Fix file path variable names and add tests

## 2024-11-06 "No Time Like the Prune-sent" - version 0.6.2

### Added
- Add DELETE endpoint for asset file entries (/v1/assets/{asset_id}/files/{file_id}/)

### Changed
- Improved code examples in README.md

## 2024-11-05 "PyPi Public Release" - version 0.6.1

### Changed
- Updated package distribution name to `nsa-pythonik` for PyPI publishing
- Updated installation instructions in README.md
- Note: Internal imports remain unchanged, still using `from pythonik import ...`

## 2024-11-05 "Public Metamorphosis" - version 0.6.0

### Added

- Add ability to update sub-object metadata for segments (Brant Goddard)

## 2024-09-09

- Merge branch 'feature/proxy-placeholder-workflow' into 'main' (Brant Goddard)

## 2024-09-08

- Add additional proxy endpoints (Prince Duepa)

## 2024-09-02

- Add ability to create asset proxy (Prince Duepa)

## 2024-08-19

- Merge branch 'feature/asset-spec-updates' into 'main' (Brant Goddard)

## 2024-08-19

- Fix date serializer (Giovann Wah)

## 2024-08-19

- Update assets create model to allow a placeholder to be created with only a title (Giovann Wah)

## 2024-07-26

- Merge branch 'bugfix/correct-fileset-url' into 'main' (Brandon Dedolph)

## 2024-07-26

- Fix file set url (Prince Duepa)

## 2024-07-16

- Merge branch 'feature/placeholder-asset-workflow' into 'main' (Brandon Dedolph)

## 2024-07-16

- Add endpoints to facilitate placeholder asset workflow (Prince Duepa)

## 2024-06-18

- Merge branch 'AKMV3-2301-pythonik-update-marker' into 'main' (Brant Goddard)

## 2024-06-18

- bugfix: missing segment id, pushing (brant)

## 2024-06-18

- add create, update, partial update to segments (brant)

## 2023-11-29

- add storages (brant)

## 2023-11-28

- fix bug, add get proxies instead (brant)

## 2023-11-28

- attempt to add get proxy by asset id only (brant)

## 2023-11-23

- fix typo (brant)

## 2023-11-23

- add getting files add test for getting files (brant)

## 2023-10-27

- bugfix, updating jobs to use patch instead of put (brant)

## 2023-10-27

- modify intercept 404 to use ViewMetadataModel (brant)

## 2023-10-26

- add intercept 404 (brant)

## 2023-10-26

- fix minor typo (brant)

## 2023-10-26

- fix search models (brant)

## 2023-10-25

- add optional metadata response (brant)

## 2023-10-25

- fix search spec server add exclude defaults add json body (brant)

## 2023-10-25

- change to response.ok instead of 200 check (brant)

## 2023-10-25

- add exclude defaults to jobs (brant)

## 2023-10-25

- removed id from job body (brant)

## 2023-10-25

- fix jobs missing job id fix jobs needing to be a put (brant)

## 2023-10-25

- add jobs create and update (brant)

## 2023-10-25

- update search response model to be more accurrate (brant)

## 2023-10-25

- fix broken metadata values (brant)

## 2023-10-25

- updating view models to be more accurate (brant)

## 2023-10-25

- removed metadata model and removed metadatum model (brant)

## 2023-10-25

- fix format defaults (brant)

## 2023-10-25

- add format model change old format model to formats (brant)

## 2023-10-25

- add get asset format fix bug wrong asset format path (brant)

## 2023-10-24

- readme changes (brant)

## 2023-10-24

- readme changes (brant)

## 2023-10-24

- pipeline changes (brant)

## 2023-10-24

- adding release (brant)

## 2023-10-24

- for now changing version to 0.0.0 (brant)

## 2023-10-24

- more gitlab changes (brant)

## 2023-10-24

- move build command to build stage (brant)

## 2023-10-24

- attempt to get package into this projects packages (brant)

## 2023-10-24

- pipeline changes (brant)

## 2023-10-24

- ci/cd change (brant)

## 2023-10-24

- testing ci/cd builds (brant)

## 2023-10-24

- add cleanup add search add readme changes (brant)

## 2023-10-23

- add metadata spec add put method add update metadata add get asset metadata view add more tests (brant)

## 2023-10-23

- add getting asset formats (brant)

## 2023-10-20

- clean up tests (brant)

## 2023-10-20

- add refactor add tests add files spec (brant)

## 2023-10-19

- add project scaffold example usage asset spec get asset (brant)

## 2023-10-18

- add initial dependencies (brant)

## 2023-10-18

- update readme (brant)

## 2023-10-18

- Initial commit (Brant Goddard)
