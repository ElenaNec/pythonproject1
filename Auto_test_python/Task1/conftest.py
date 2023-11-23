import pytest


@pytest.fixture
def good_word():
    return "кошка"


@pytest.fixture
def bad_word():
    return "кошкв"