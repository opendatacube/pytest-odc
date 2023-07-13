# Infrastructure Testing with ODC

Anyone writing applications using an ODC Database will need to be able to repeatedly test their code. This requires an ODC Database to contain a known set of data, every time the test is done.

There's two challenges here:
  - Having an ODC Database requires a private database in a PostgreSQL server somewhere, which is a challenge to set up.
  - The database needs to be wiped and reset every time a test is run, to make it repeatable.

## The Solution

Included with ODC Core (soon!) are some [pytest](https://docs.pytest.org/) [fixtures](https://docs.pytest.org/en/stable/explanation/fixtures.html), which make it easy to write test code against an ODC Database.

### Steps to Create New Tests

1. Copy the [ODC Test Plugin](https://github.com/opendatacube/datacube-explorer/blob/develop/cubedash/testutils/database.py) into your application code.

2. Create at least one each of a Metadata Type, Product and Dataset YAML file. These will be loaded into an ODC Database before your test code runs.

3. Create a [pytest](https://docs.pytest.org/) Python file using this template:

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

4. Install extra test dependencies.

   ```console
   $ pip install docker
   ```

5. Create and activate a local environment.

   ```console
   $ mamba create -p ./testenv python=3.10 datacube pytest docker-py
   $ mamba activate /home/omad/dev/tmp-odc-testing/testenv
   ```

   Note: the conda-forge package is called `docker-py`, the PyPI package is simply `docker`.

6. Run the example tests

    pytest tests/


## How it Works
pytest-odc
==========

[![PyPI version](https://img.shields.io/pypi/v/pytest-odc.svg)](https://pypi.org/project/pytest-odc)

[![Python versions](https://img.shields.io/pypi/pyversions/pytest-odc.svg)](https://pypi.org/project/pytest-odc)

[![See Build Status on AppVeyor](https://ci.appveyor.com/api/projects/status/github/omad/pytest-odc?branch=master)](https://ci.appveyor.com/project/omad/pytest-odc/branch/master)

A pytest plugin for simplifying ODC database tests

------------------------------------------------------------------------

This [pytest](https://github.com/pytest-dev/pytest) plugin was generated
with [Cookiecutter](https://github.com/audreyr/cookiecutter) along with
[\@hackebrot](https://github.com/hackebrot)\'s
[cookiecutter](https://github.com/pytest-dev/cookiecutter)
template.

Features
--------

-   TODO

Requirements
------------

-   TODO

Installation
------------

You can install \"pytest-odc\" via
[pip](https://pypi.org/project/pip/) from
[PyPI](https://pypi.org/project):

    $ pip install pytest-odc

Usage
-----

-   TODO

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
