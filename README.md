[![PyPI version](https://img.shields.io/pypi/v/pytest-odc.svg)](https://pypi.org/project/pytest-odc)

[![Python versions](https://img.shields.io/pypi/pyversions/pytest-odc.svg)](https://pypi.org/project/pytest-odc)

# pytest-odc

A [pytest](https://docs.pytest.org/) [plugin](https://docs.pytest.org/en/7.1.x/how-to/plugins.html) for simplifying [Open Datacube](https://www.opendatacube.org/) database tests.

# Testing Open Datacube Applications

Anyone writing applications using an ODC Database needs to be able to test their code. This requires an ODC Database containing a known set of data.

There's two challenges here:

- ODC requires a PostgreSQL server accessible anywhere test are run, which can be challenging to set up.
- The database should be reset every time a test is run, to make it possible to repeatedly run tests.

## The Solution

This package provides reusable [pytest](https://docs.pytest.org/) [fixtures](https://docs.pytest.org/en/stable/explanation/fixtures.html), to make it easy to write test code against an ODC Database. It handles starting and stopping a temporary PostgreSQL server using Docker, initialising it for ODC use, and loading/wiping sets of test data on a per test module basis.

### Steps to Create New Tests

1. Install the [ODC Test Plugin](https://github.com/opendatacube/datacube-explorer/blob/develop/cubedash/testutils/database.py) into your Python environment.
   
   `pip install pytest-odc`

2. Create at least one each of an ODC [Metadata Type](https://datacube-core.readthedocs.io/en/latest/installation/metadata-types.html), [Product](https://datacube-core.readthedocs.io/en/latest/installation/product-definitions.html) and [Dataset](https://datacube-core.readthedocs.io/en/latest/installation/dataset-documents.html) YAML files. These will be loaded into an ODC Database before your test code runs.

3. Create a [pytest](https://docs.pytest.org/) file using this template:

    ```python
    """
    Template pytest module for testing ODC Code
    """
    import pytest

    # UPDATE: these lists with the data you want loaded into your database
    # Each string is for a file, relative to this python module.
    METADATA_TYPES = ["metadata/eo3_metadata.yaml",]
    PRODUCTS = ["products/ga_ls8c_ard_3.odc-product.yaml",]
    DATASETS = ["datasets/ga_ls8c_ard_3-sample.yaml",]

    # Use the 'auto_odc_db' fixture to populate the database with sample data.
    pytestmark = pytest.mark.usefixtures("auto_odc_db")

    def test_my_odc_code(odc_db: "datacube.Datacube"):
        ### REPLACE: with your own test code
        my_datasets = odc_db.find_datasets(product='ga_ls8c_ard_3')
        assert len(my_datasets) == 3
    ```

4. Run your new tests.

       pytest tests/

# More Details / How it Works

The four provided pytest fixtures compose together to ensure an ODC Database is available and preloaded with test data for each test module.


## Fixtures

### `postgresql_server`

This fixture either:

- Runs a temporary PostgreSQL server using Docker
- Or checks that a test PostgreSQL server is already available via the `ODC_TEST_DB_URL` environment variable.

### `odc_db`

This fixture provides a `datacube.Datacube()` object configured to connect to the temporary test database. 

It can be added to the parameters for a test for getting access to the temporary database.

### `odc_test_db`

This fixture creates all the ODC Database tables.

### `auto_odc_db`

This fixture should be used as a `pytestmark autoload`, marking the test module as having variables named `METADATA_TYPES`, `PRODUCTS` and `DATASETS` being lists of files to load into the test database.


Contributing
------------

Contributions are very welcome. Tests can be run with
[tox](https://tox.readthedocs.io/en/latest/), please ensure the coverage
at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the [Apache Software License
2.0](http://www.apache.org/licenses/LICENSE-2.0) license,
\"pytest-odc\" is free and open source software

Issues
------

If you encounter any problems, please [file an
issue](https://github.com/omad/pytest-odc/issues) along
with a detailed description.

Release Process
---------------

```
rm -rf dist/
python -m build
twine upload --repository testpypi dist/*
twine upload dist/*
```
