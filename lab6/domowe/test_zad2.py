import pytest
from zad2 import (encrypt_vigenere2,
                  decrypt_vigenere2,
                  to_ascii,
                  validate_key_length,
                  validate_character_range,
                  calculate_offset,
                  get_nth_ascii_char)


def test_encrypt_regular():
    assert encrypt_vigenere2('NT OJES TBARDZ OTAJN YTEKS',
                             'TO JEST BARDZO TAJNY TEKST') == 'GH XNWL UBRUCN HTJWL RXOCL'


def test_encrypt_invalid_plaintext():
    with pytest.raises(ValueError):
        encrypt_vigenere2('KEY', 'TO %$ BARDZO TAJNY TEKSZ')


def test_encrypt_invalid_key():
    with pytest.raises(ValueError):
        encrypt_vigenere2('KEY%#', 'TO JEST BARDZO TAJNY TEKSZ')


def test_to_ascii_regular():
    assert to_ascii('ABC') == [65, 66, 67]


def test_to_ascii_non_char():
    assert to_ascii('#') == [35]


def test_to_ascii_empty_str():
    assert to_ascii('') == []


def test_validate_key_length_regular():
    validate_key_length('key')


def test_validate_key_length_empty():
    with pytest.raises(ValueError):
        validate_key_length('')


def test_validate_character_range_regular1():
    validate_character_range(ord('A'))


def test_validate_character_range_regular2():
    validate_character_range(ord('Z'))


def test_validate_character_range_invalid_char():
    with pytest.raises(ValueError):
        validate_character_range(ord('a'))


def test_calculate_offset_regular():
    assert calculate_offset(ord('A'), ord('B')) == 1


def test_calculate_offset_same_letter():
    assert calculate_offset(ord('A'), ord('A')) == 0


def test_calculate_offset_a_z():
    assert calculate_offset(ord('A'), ord('Z')) == 25


def test_get_nth_ascii_char_regular():
    assert get_nth_ascii_char(0) == 'A'


def test_get_nth_ascii_char_last():
    assert get_nth_ascii_char(25) == 'Z'


def test_get_nth_ascii_char_no_rollover():
    assert get_nth_ascii_char(26) != 'A'


def test_decrypt_regular():
    assert decrypt_vigenere2('NT OJES TBARDZ OTAJN YTEKS',
                             'GH XNWL UBRUCN HTJWL RXOCL') == 'TO JEST BARDZO TAJNY TEKST'


def test_decrypt_wrong_key():
    with pytest.raises(ValueError):
        decrypt_vigenere2('ZLY KLUCZ', 'GH XNWL UBRUCN HTJWL RXOCL')
