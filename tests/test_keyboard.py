from src.keyboard import Keyboard
import pytest


@pytest.fixture()
def keyboard_setup():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb


def test_keyboard_str(keyboard_setup):
    kb = keyboard_setup
    assert str(kb) == "Dark Project KD87A"


def test_change_lang(keyboard_setup):
    kb = keyboard_setup

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"

    with pytest.raises(AttributeError):  # Error test syntax - NOTES REMEMBER
        kb.language = 'CH'

