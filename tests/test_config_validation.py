import pytest

from src.config_validation import require_config_value


def test_returns_config_value():
    assert require_config_value({"host": "localhost"}, "host") == "localhost"


def test_raises_for_missing_key():
    with pytest.raises(ValueError):
        require_config_value({}, "host")


def test_raises_for_blank_string():
    with pytest.raises(ValueError):
        require_config_value({"token": "   "}, "token")
