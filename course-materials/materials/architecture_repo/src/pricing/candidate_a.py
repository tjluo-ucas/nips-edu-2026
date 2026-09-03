import os


_discount_cache: dict[tuple[float, bool], float] = {}


def promotional_discount(order_total: float, is_member: bool) -> float:
    key = (order_total, is_member)
    if key in _discount_cache:
        return _discount_cache[key]

    if order_total < 0:
        raise ValueError("order_total must be non-negative")

    threshold = float(os.environ.get("PROMO_THRESHOLD", "100.0"))
    rate = float(os.environ.get("PROMO_RATE", "0.10"))
    cap = float(os.environ.get("PROMO_CAP", "25.0"))
    discount = min(round(order_total * rate, 2), cap) if is_member and order_total >= threshold else 0.0
    _discount_cache[key] = discount
    return discount
