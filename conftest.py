import pytest
from lib.Utils import get_spark_session

@pytest.fixture
def spark():
    return get_spark_session("LOCAL")

@pytest.fixture
def expected_results(spark):
    agg_schema = "state string, count int"
    expected_results = spark.read.format("csv").option("header",True).schema(agg_schema).load("data/expected_results")
    return expected_results