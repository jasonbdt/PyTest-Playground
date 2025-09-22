import pytest
from main import sumnums


def test_valid_input():
    assert sumnums(1, 3) == 6


def test_edge_case():
    assert sumnums(1, 1) == 1


pytest.main()
