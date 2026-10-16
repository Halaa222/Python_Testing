import pytest
from testing_course.bowling.game import Game
import pytest

@pytest.fixture
def sut():
    return Game()

def roll_many(game: Game, n: int, pins: int):
    for _ in range(n):
        game.roll(pins)

def test_gutter_game(sut: Game):
    roll_many(sut, 20, 0)
    assert sut.score() == 0

def test_all_ones(sut: Game):
    roll_many(sut, 20, 1)
    assert sut.score() == 20