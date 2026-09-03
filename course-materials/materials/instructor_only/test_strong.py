import pytest
from src.discount import promotional_discount


def test_exact_threshold_qualifies():
    assert promotional_discount(100.0, True) == 10.0


def test_just_below_threshold_does_not_qualify():
    assert promotional_discount(99.99, True) == 0.0


def test_negative_total_is_rejected():
    with pytest.raises(ValueError):
        promotional_discount(-0.01, True)


def test_cap_boundary():
    assert promotional_discount(250.0, True) == 25.0
