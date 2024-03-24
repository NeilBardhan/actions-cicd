import pytest
import importlib
from demo_py_pkg import stats

def test_stats_exists():
    exists = importlib.util.find_spec("demo_py_pkg.stats") is not None
    assert exists