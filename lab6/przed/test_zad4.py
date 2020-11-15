import pytest
from zad4 import encrypt_vingere, decrypt_vingere


def test_encrypt_regular():
    assert encrypt_vingere('NT OJES TBARDZ OTAJN YTEKS',
                           'TO JEST BARDZO TAJNY TEKST') == 'GH XNWL UBRUCN HTJWL RXOCL'


def test_encrypt_wrong_key():
    with pytest.raises(ValueError):
        encrypt_vingere('ZLY KLUCZ', 'TO JEST BARDZO TAJNY TEKST')


def test_decrypt_regular():
    assert decrypt_vingere('NT OJES TBARDZ OTAJN YTEKS',
                           'GH XNWL UBRUCN HTJWL RXOCL') == 'TO JEST BARDZO TAJNY TEKST'


def test_decrypt_wrong_key():
    with pytest.raises(ValueError):
        decrypt_vingere('ZLY KLUCZ', 'GH XNWL UBRUCN HTJWL RXOCL')
