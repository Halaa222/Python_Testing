from testing_course.bowling.game import Game


def test_create_game() -> None:
    sut = Game()   #subject under test

def test_roll_ball():
    sut = Game()
    sut.roll(0)

def test_gutter_game():
    sut = Game()
    for _ in range(20):
        sut.roll(0)
    assert sut.score() == 0