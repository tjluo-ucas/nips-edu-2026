"""Tiny teaching example for an executable verifier feedback loop."""


def promotional_discount(order_total: float, is_member: bool) -> float:
    """Return the promotional discount for an order."""
    if order_total < 0:
        raise ValueError("order_total must be non-negative")
    if not is_member:
        return 0.0
    return min(round(order_total * 0.10, 2), 25.0)
