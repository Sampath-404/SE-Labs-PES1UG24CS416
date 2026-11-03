
import pytest

from self_storage import rent_due, access_allowed, payment_status


# ==========================================
# RENT DUE - BRANCH COVERAGE TESTS
# ==========================================

def test_unknown_unit():
    with pytest.raises(ValueError):
        rent_due("invalid", 2, False, False)


def test_negative_months():
    with pytest.raises(ValueError):
        rent_due("small", -1, False, False)


def test_member_true():
    assert rent_due("small", 3, False, True) == 80


def test_member_false():
    assert rent_due("small", 3, False, False) == 160


def test_large_member():
    assert rent_due("large", 5, False, True) == 160


def test_extra_zero():
    assert rent_due("small", 1, False, False) == 0


def test_extra_positive():
    assert rent_due("small", 3, False, False) == 160


def test_climate_true():
    assert rent_due("small", 3, True, False) == 240


def test_climate_false():
    assert rent_due("small", 3, False, False) == 160


def test_extra_greater_than_six():
    assert rent_due("small", 8, False, False) == 490


def test_extra_not_greater_than_six():
    assert rent_due("small", 7, False, False) == 480


def test_long_term_climate():
    assert rent_due("small", 8, True, False) == 735


# ==========================================
# ACCESS - BRANCH COVERAGE TESTS
# ==========================================

def test_owner_access_allowed():
    assert access_allowed(23, 2, True) is True


def test_owner_access_denied():
    assert access_allowed(12, 5, True) is False


def test_non_owner_access():
    assert access_allowed(12, 2, False) is True


def test_before_opening():
    assert access_allowed(5, 1, False) is False


def test_after_closing():
    assert access_allowed(23, 1, False) is False


def test_visitor_limit_exceeded():
    assert access_allowed(12, 3, False) is False


# ==========================================
# PAYMENT STATUS - BRANCH COVERAGE TESTS
# ==========================================

def test_autopay_true():
    assert payment_status(0, True, False) == "current"


def test_autopay_false():
    assert payment_status(5, False, False) == "current"


def test_prior_late_true():
    assert payment_status(10, True, True) == "current"


def test_current_status():
    assert payment_status(5, False, False) == "current"


def test_grace_status():
    assert payment_status(-5, False, False) == "grace"


def test_lien_status():
    assert payment_status(-11, False, False) == "lien"
