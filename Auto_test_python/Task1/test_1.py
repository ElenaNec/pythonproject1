from task1 import chek_word


def test_word(good_word, bad_word):
    assert good_word in chek_word(bad_word) 