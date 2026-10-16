class Game:
    def __init__(self) -> None:
        self._score = 0

    def score(self) -> int:
        return self._score

    def roll(self, pins:int):
        self._score += pins