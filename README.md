# Pythonik

Pythonik is a comprehensive Python SDK designed for seamless interaction with
the Iconik API. It offers a user-friendly interface to access various
functionalities of Iconik, making it easier for developers to integrate and
manage Iconik assets and metadata within their applications.

## Features

- Easy-to-use methods for accessing Iconik assets and metadata.
- Robust handling of API authentication and requests.
- Configurable timeout settings for API interactions.

## Installation

Install the Pythonik SDK using pip:

```bash
pip install pythonik
```

## Usage

### Get an Asset from Iconik

To retrieve an asset from Iconik, use the following code:

```python
from pythonik.client import PythonikClient

client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=5)
asset = client.assets().get(asset_id)
print(asset)
```

### Get Metadata from a View

To get metadata for an asset from a specific view, use the following code:

```python
from pythonik.client import PythonikClient

asset_id = '123'
view_id = '456'

client = PythonikClient(app_id=app_id, auth_token=auth_token, timeout=5)
metadata = client.metadata().get_asset_metadata(asset_id, view_id)
print(metadata)
```

Checkout the [API reference](./docs/API_REFERENCE.md) and [advanced usage guide](./docs/ADVANCED_USAGE.md) to see all you can do with Pythonik.

## Publishing to NSA Internal PyPI GitLab Package Registry

The CI/CD pipeline will automatically build and add a new version as a PyPI package to the package registry for this project.

To manually build and publish a new PyPI package:

1. Create and push a tag on the default branch (main):

   ```bash
   git tag {tag}
   git push
   ```

## Installing from NSA Internal PyPI GitLab Package Registry

To install the package in another project using Poetry:

1. Add the GitLab source with a priority of supplemental:

   ```bash
   poetry source add --priority=supplemental gitlab https://gitlab.com/api/v4/projects/51363622/packages/pypi/simple
   ```

2. Configure authentication:

   ```bash
   # your GitLab username and access token
   poetry config http-basic.gitlab <username> <password>
   ```

3. Install the package:

   ```bash
   poetry add --source gitlab pythonik
   ```

Note: If using a personal access token for authentication, it needs the `api` scope. If using a deploy token, set the scope to `read_package_registry`.

## Using Poetry

This project uses Poetry for dependency management and packaging. Below are instructions on how to work with Poetry, create a Poetry shell, and run tests using pytest.

### Setting Up Poetry

First, install Poetry if you haven't already:

### Creating a Poetry Shell

To create and activate a Poetry shell, which sets up an isolated virtual environment for your project:

1. Navigate to your project directory.
2. Run the following command:

   ```sh
   poetry shell
   ```

This command will activate a virtual environment managed by Poetry. You can now run Python commands and scripts within this environment.

### Install all dependencies including pytest

```sh
    poetry install
```

### Running Tests with pytest

To run tests using pytest, follow these steps:

1. Inside the Poetry shell, run the tests with the following command:

   ```sh
   pytest
   ```

This will discover and execute all the tests in your project.

---

By following these steps, you can efficiently manage dependencies, create a virtual environment, and run tests in your Python project using Poetry.

## Support

For support, please contact NSA.

## Roadmap

Details about upcoming features and enhancements will be added here.

## Contributing

Please see the [contribution guide](./CONTRIBUTING.md) for information on how to contribute.

## Authors and Acknowledgment

This SDK is developed and maintained by North Shore Automation developers,
including Brant Goddard, Prince Duepa, Giovann Wah, and Brandon Dedolph.

## Contributors

## License

License information will be available soon.

## Project Status

Current project status and updates will be posted here.
