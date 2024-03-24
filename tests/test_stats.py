import pytest
import importlib
from demo_py_pkg import stats

def test_stats_exists():
    exists = importlib.util.find_spec("demo_py_pkg.stats") is not None
    assert exists

def test_mean():
    input_list = [4, 5, 6]
    mean=stats.mean(input_list)
    assert mean == 5

def test_median():
    input_list = [4, 5, 6]
    median=stats.median(input_list)
    assert median == 5