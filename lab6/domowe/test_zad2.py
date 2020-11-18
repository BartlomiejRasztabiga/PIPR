import pytest
from zad2 import encrypt_vigenere2, decrypt_vigenere2, to_ascii


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


def test_decrypt_regular():
    assert decrypt_vigenere2('NT OJES TBARDZ OTAJN YTEKS',
                             'GH XNWL UBRUCN HTJWL RXOCL') == 'TO JEST BARDZO TAJNY TEKST'


def test_decrypt_wrong_key():
    with pytest.raises(ValueError):
        decrypt_vigenere2('ZLY KLUCZ', 'GH XNWL UBRUCN HTJWL RXOCL')
