#FIX: Added tests for `logic_utils.py` during agent-assisted pairing; user reviewed assertions.
from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_parse_guess_valid_and_decimal():
    ok, val, err = parse_guess("42")
    assert ok and val == 42 and err is None

    ok, val, err = parse_guess("42.0")
    assert ok and val == 42 and err is None


def test_parse_guess_invalid():
    ok, val, err = parse_guess("")
    assert not ok and val is None and isinstance(err, str)

    ok, val, err = parse_guess("abc")
    assert not ok and val is None and isinstance(err, str)


def test_check_guess_outcomes():
    assert check_guess(50, 50) == "Win"
    assert check_guess(60, 50) == "Too High"
    assert check_guess(40, 50) == "Too Low"


def test_update_score_win_and_limits():
    # First attempt win: 100 points
    assert update_score(0, "Win", 1) == 100
    # Later attempt: points decrease but not below 10
    assert update_score(0, "Win", 10) == 10


def test_update_score_wrong_guess():
    assert update_score(20, "Too High", 2) == 15
    assert update_score(20, "Too Low", 3) == 15
