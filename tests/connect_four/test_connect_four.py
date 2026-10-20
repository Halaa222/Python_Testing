import pytest
from testing_course.connect_four.connect_four_game import ConnectFourGame
from testing_course.connect_four.player import Player

@pytest.fixture
def game() -> ConnectFourGame:
    return ConnectFourGame(Player.RED)

def test_initial_state(game:ConnectFourGame) -> None:
    for row in range(6):
        for col in range(7):
            assert game.get_player_at(col, row) == Player.NONE
    assert game._player_on_turn == Player.RED
    assert not game._is_game_over
    assert game._winner == Player.NONE
    assert game._rows == 6
    assert game._cols == 7

def test_drop_places_disc_at_bottom():
    game = ConnectFourGame(Player.RED)
    game.drop(0)
    assert game.get_player_at(5, 0) == Player.RED
    assert game._player_on_turn == Player.YELLOW

def test_drop_full_column_raises_error():
    game = ConnectFourGame(Player.RED)
    for _ in range(6):
        game.drop(0)
    with pytest.raises(ValueError, match="Column is full"):
        game.drop(0)

def test_drop_invalid_column_raises_error():
    game = ConnectFourGame(Player.RED)
    with pytest.raises(ValueError, match="Invalid column"):
        game.drop(-1)
    with pytest.raises(ValueError, match="Invalid column"):
        game.drop(7)

def test_turn_switching():
    game = ConnectFourGame(Player.RED)
    game.drop(0)
    assert game._player_on_turn == Player.YELLOW
    game.drop(1)
    assert game._player_on_turn == Player.RED

def test_get_player_at_returns_correct_player():
    game = ConnectFourGame(Player.RED)
    game.drop(0)
    assert game.get_player_at(5,0) == Player.RED
    game.drop(1)
    assert game.get_player_at(5,1) == Player.YELLOW

def test_get_winner_vertical():
    game = ConnectFourGame(Player.RED)
    assert game.winner == Player.NONE
    game.drop(0)
    game.drop(1)
    game.drop(0)
    game.drop(1)
    game.drop(0)
    game.drop(1)
    game.drop(0)
    assert game.is_game_over == True
    assert game.winner == Player.RED
    assert game.winner != Player.YELLOW
    assert game.winner != Player.NONE
    
def test_get_winner_horizontal():
    game = ConnectFourGame(Player.RED)
    assert game.winner == Player.NONE
    game.drop(0)
    game.drop(0)
    game.drop(1)
    game.drop(1)
    game.drop(2)
    game.drop(2)
    game.drop(3)
    assert game.is_game_over == True
    assert game.winner == Player.RED
    assert game.winner != Player.YELLOW
    assert game.winner != Player.NONE
    
def test_get_winner_diagonal():
    game = ConnectFourGame(Player.RED)
    assert game.winner == Player.NONE
    game.drop(0)  
    game.drop(1) 
    game.drop(1) 
    game.drop(2) 
    game.drop(2) 
    game.drop(3) 
    game.drop(2) 
    game.drop(3) 
    game.drop(3) 
    game.drop(5)  
    game.drop(3) 
    assert game.is_game_over == True
    assert game.winner == Player.RED
    assert game.winner != Player.YELLOW
    assert game.winner != Player.NONE

def test_reset_game():
    pass

def test_board_full():
    pass

# main auch testen?
