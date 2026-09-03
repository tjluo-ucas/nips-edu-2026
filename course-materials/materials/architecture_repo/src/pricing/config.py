from dataclasses import dataclass


@dataclass(frozen=True)
class PricingPolicy:
    threshold: float = 100.0
    rate: float = 0.10
    cap: float = 25.0


DEFAULT_POLICY = PricingPolicy()
