
import pytest
from self_storage import rent_due, access_allowed, payment_status


# RENT DUE TESTS

def test_small_unit_deposit():
    assert rent_due("small", 1, False, False) == 0


def test_unknown_unit():
    with pytest.raises(ValueError):
        rent_due("extra_large", 2, False, False)


def test_negative_months():
    with pytest.raises(ValueError):
        rent_due("small", -1, False, False)


def test_member_discount():
    assert rent_due("small", 3, False, True) == 80


def test_large_member():
    assert rent_due("large", 5, False, True) == 160


def test_climate_control():
    assert rent_due("small", 3, True, False) == 240


def test_long_term_non_climate():
    assert rent_due("small", 8, False, False) == 490


def test_long_term_climate():
    assert rent_due("small", 8, True, False) == 735


# ACCESS TESTS

def test_owner_access():
    assert access_allowed(12, 4, True) is True


def test_non_owner_access():
    assert access_allowed(12, 2, False) is True


def test_access_denied():
    assert access_allowed(12, 3, False) is False


# PAYMENT STATUS TESTS

def test_payment_current():
    assert payment_status(5, False, False) == "current"


def test_payment_grace():
    assert payment_status(-5, False, False) == "grace"


def test_payment_lien():
    assert payment_status(-11, False, False) == "lien"


def test_autopay_with_prior_late():
    assert payment_status(10, True, True) == "current"
def test_access_outside_allowed_hours():
    assert access_allowed(5, 1, False) is False