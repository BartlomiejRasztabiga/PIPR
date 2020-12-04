import pytest

from lotto import LottoGame, NumbersNotUniqueError, NumbersNotInRangeError, WrongCountOfNumbersError


def test_set_player_numbers_none():
    game = LottoGame()
    game.set_player_numbers()

    assert len(game.player_numbers()) == 6


def test_set_player_numbers_own():
    game = LottoGame()

    numbers = {1, 2, 3, 4, 5, 6}
    game.set_player_numbers(numbers)

    assert game.player_numbers() == numbers


def test_check_player_numbers_correct():
    numbers = [1, 3, 2, 5, 4, 7]

    game = LottoGame()
    assert game.check_player_numbers(numbers)


def test_check_player_numbers_not_unique():
    numbers = [1, 1, 2, 5, 4, 7]

    game = LottoGame()
    with pytest.raises(NumbersNotUniqueError):
        game.check_player_numbers(numbers)


def test_check_player_numbers_not_enough():
    numbers = [1, 2, 5, 4, 7]

    game = LottoGame()
    with pytest.raises(WrongCountOfNumbersError):
        game.check_player_numbers(numbers)


def test_check_player_numbers_not_in_range():
    numbers = [0, 1, 2, 5, 4, 7]

    game = LottoGame()
    with pytest.raises(NumbersNotInRangeError):
        game.check_player_numbers(numbers)


def test_win(monkeypatch):
    def returnList(f, t):
        return [1, 2, 3, 4, 5, 6]
    monkeypatch.setattr('lotto.sample', returnList)

    game = LottoGame()
    results = game.play([1, 2, 3, 4, 5, 6])

    assert "Trafiłeś poprawnie liczby: 1, 2, 3, 4, 5, 6" in results


def test_loose(monkeypatch):
    def returnList(f, t):
        return [1, 2, 3, 4, 5, 6]
    monkeypatch.setattr('lotto.sample', returnList)

    game = LottoGame()
    results = game.play([7, 8, 9, 10, 11, 12])

    assert "Brak trafionych cyfr" in results
