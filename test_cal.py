import pytest
from calc import add
def test_add():
    assert add(4, 5) == 9
    