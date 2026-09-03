import pytest

from src.pricing import candidate_a, candidate_b


IMPLEMENTATIONS = [candidate_a.promotional_discount, candidate_b.promotional_discount]


@pytest.fixture(autouse=True)
def default_environment(monkeypatch):
    monkeypatch.setenv("PROMO_THRESHOLD", "100.0")
    monkeypatch.setenv("PROMO_RATE", "0.10")
    monkeypatch.setenv("PROMO_CAP", "25.0")
    candidate_a._discount_cache.clear()


@pytest.mark.parametrize("implementation", IMPLEMENTATIONS)
@pytest.mark.parametrize(
    ("order_total", "is_member", "expected"),
    [
        (80.0, True, 0.0),
        (100.0, True, 10.0),
        (120.0, True, 12.0),
        (400.0, True, 25.0),
        (150.0, False, 0.0),
    ],
)
def test_discount_behavior(implementation, order_total, is_member, expected):
    assert implementation(order_total, is_member) == expected


@pytest.mark.parametrize("implementation", IMPLEMENTATIONS)
def test_negative_total_is_invalid(implementation):
    with pytest.raises(ValueError):
        implementation(-0.01, True)
