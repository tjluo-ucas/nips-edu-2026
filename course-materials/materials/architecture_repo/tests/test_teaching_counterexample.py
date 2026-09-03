"""Executable architecture evidence; this is intentionally not a style test."""

from src.pricing import candidate_a, candidate_b
from src.pricing.config import PricingPolicy


def test_global_cache_can_hide_runtime_policy_change(monkeypatch):
    monkeypatch.setenv("PROMO_THRESHOLD", "100.0")
    monkeypatch.setenv("PROMO_RATE", "0.10")
    monkeypatch.setenv("PROMO_CAP", "25.0")
    candidate_a._discount_cache.clear()

    assert candidate_a.promotional_discount(120.0, True) == 12.0
    monkeypatch.setenv("PROMO_RATE", "0.20")

    # Candidate A silently serves a value cached under a different policy.
    assert candidate_a.promotional_discount(120.0, True) == 12.0
    # Candidate B makes the policy dependency explicit and deterministic.
    policy = PricingPolicy(threshold=100.0, rate=0.20, cap=25.0)
    assert candidate_b.promotional_discount(120.0, True, policy) == 24.0
