from src.discount import promotional_discount


def test_non_member_gets_no_discount():
    assert promotional_discount(150.0, False) == 0.0


def test_member_above_threshold_gets_discount():
    assert promotional_discount(120.0, True) == 12.0


def test_member_below_threshold_gets_no_discount():
    assert promotional_discount(80.0, True) == 0.0


def test_discount_is_capped():
    assert promotional_discount(400.0, True) == 25.0
