from .config import DEFAULT_POLICY, PricingPolicy
from .validation import require_valid_order_total


def promotional_discount(
    order_total: float,
    is_member: bool,
    policy: PricingPolicy = DEFAULT_POLICY,
) -> float:
    require_valid_order_total(order_total)
    if not is_member or order_total < policy.threshold:
        return 0.0
    return min(round(order_total * policy.rate, 2), policy.cap)
