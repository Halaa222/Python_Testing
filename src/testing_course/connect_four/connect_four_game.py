from testing_course.connect_four.player import Player


class ConnectFourGame:
    def __init__(self, player_on_turn: Player) -> None:
        self._player_on_turn = player_on_turn
        self._is_game_over = False
        self._winner = Player.NONE
        self._rows = 6
        self._cols = 7
       # Initialize an empty 6x7 board
        self._board = [[Player.NONE for _ in range(self._cols)] for _ in range(self._rows)]
        

    def get_player_at(self, row: int, col: int) -> Player:
        return self._board[col][row]

    @property
    def player_on_turn(self) -> Player:
        return self._player_on_turn

    @property
    def is_game_over(self) -> bool:
        # Player Red
        countRed = 0

        # Horizontal
        for row in range(self._rows):
            for col in range(self._cols - 1):
                if self._board[col][row] == Player.RED and self._board[col + 1][row ] == Player.RED:
                    countRed += 1
                if countRed == 4:
                    self._winner = Player.RED
                    self._is_game_over = True
                    return
        countRed = 0

        # Vertical
        for col in range(self._cols):
            for row in range(self._rows -1):
                if self._board[col][row] == Player.RED and self._board[col][row + 1] == Player.RED:
                    countRed += 1
                if countRed == 4:
                    self._winner = Player.RED
                    self._is_game_over = True
                    return
                
        # Diagnonal left bottom to top right
        #TODO
        
        # Digaonal left top to bottom right
        #TODO          

    @property
    def winner(self) -> Player:
        return self._winner

    def reset(self, player_on_turn: Player) -> None:
        raise NotImplementedError

    def drop(self, col: int) -> None:
        # Check if the column is valid
        if col < 0 or col >= self._cols:
            raise ValueError("Invalid column")

        # Find the lowest empty row in the specified column
        for row in reversed(range(self._rows)):
            if self._board[row][col] == Player.NONE:
                self._board[row][col] = self._player_on_turn
                # Switch turns
                self._player_on_turn = Player.YELLOW if self._player_on_turn == Player.RED else Player.RED
                return

        # If the column is full, raise an error
        raise ValueError("Column is full")
