"""
Template pytest module for testing ODC Code
"""
import pytest

# UPDATE: these lists with the data you want loaded into your database
# Each string is for a file, relative to this python module.
METADATA_TYPES = ["metadata/eo3_landsat_ard.odc-type.yaml",]
PRODUCTS = ["products/ga_ls8c_ard_3.odc-product.yaml",]
DATASETS = ["datasets/ga_ls8c_ard_3-sample.yaml",]

# Use the 'auto_odc_db' fixture to populate the database with sample data.
pytestmark = pytest.mark.usefixtures("auto_odc_db")

def test_my_odc_code(odc_test_db: "datacube.Datacube"):
    ### REPLACE: with your own test code
    my_datasets = odc_test_db.find_datasets(product='ga_ls8c_ard_3')
    assert len(my_datasets) == 3
