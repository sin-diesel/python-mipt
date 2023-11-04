#!/usr/bin/env python3

class Player:
    def __init__(self, id: int, name: str) -> None:
        self.id: int = id
        self.name: str = name
        self.scores: int = 0
        self.games: list = []

    def add_result(self, game_id: int, scores: int) -> None:
        self.games.append(game_id)
        self.scores += scores

    def get_mean(self) -> float:
        ngames = len(self.games)
        return self.scores / ngames if ngames != 0 else 0
