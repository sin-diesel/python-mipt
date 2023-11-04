#!/usr/bin/env python3

class Player:
    id: int
    name: str
    scores: int = 0
    games: list = []

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def add_result(self, game_id: int, scores: int) -> None:
        self.games.append(game_id)
        self.scores += scores

    def get_mean(self) -> float:
        ngames: int = len(self.games)
        return self.scores / ngames if ngames != 0 else 0
