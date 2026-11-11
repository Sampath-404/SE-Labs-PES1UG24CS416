from hypothesis import given, settings, strategies as st
from self_storage import parse_rental, duration_average, payable_rent


@settings(report_multiple_bugs=False)
@given(st.text() | st.none())
def test_parse_rental_no_crash(s):
    try:
        parse_rental(s)
    except Exception as e:
        assert False, f"parse_rental crashed with {type(e).__name__}: {e}"


@settings(report_multiple_bugs=False)
@given(st.text() | st.none())
def test_duration_average_no_crash(s):
    try:
        duration_average(s)
    except Exception as e:
        assert False, f"duration_average crashed with {type(e).__name__}: {e}"


@settings(report_multiple_bugs=False)
@given(st.text() | st.none())
def test_payable_rent_no_crash(s):
    try:
        payable_rent(s)
    except Exception as e:
        assert False, f"payable_rent crashed with {type(e).__name__}: {e}"