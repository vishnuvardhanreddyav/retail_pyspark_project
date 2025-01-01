import pytest
from lib.Utils import get_spark_session
from lib.DataReader import read_customers, read_orders
from lib.DataManipulation import filter_closed_orders,count_orders_state
from lib.ConfigReader import get_app_config

# @pytest.fixture
# def spark():
#     return get_spark_session("LOCAL")


def test_read_customers_df(spark):
    customers_count = read_customers(spark,"LOCAL").count()
    assert customers_count == 12435

def test_read_orders_df(spark):
    orders_count = read_orders(spark,"LOCAL").count()
    assert orders_count == 68883

@pytest.mark.transformation()
def test_filter_closed_orders(spark):
     oredrs_df = read_orders(spark,"LOCAL")
     closed_orders_count = filter_closed_orders(oredrs_df).count()
     assert closed_orders_count == 7556

def test_read_app_config():
    config = get_app_config("LOCAL")
    assert config["orders.file.path"] == "data/orders.csv"

@pytest.mark.transformation()
def test_count_orders_state(spark,expected_results):
    customers_df = read_customers(spark,"LOCAL")
    customers_agg_df = count_orders_state(customers_df)
    assert customers_agg_df.collect() == expected_results.collect()
