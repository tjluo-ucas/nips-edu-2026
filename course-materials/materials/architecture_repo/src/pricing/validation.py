def require_valid_order_total(order_total: float) -> None:
    if order_total < 0:
        raise ValueError("order_total must be non-negative")
