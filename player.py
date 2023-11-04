#!/usr/bin/env python3

import abc

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

class Power(abc.ABC):
    name: str
    cost: int

    def __init__(self, name: str, cost: int) -> None:
        self.name = name
        self.cost = cost

    @abc.abstractmethod
    def use(self, player: Player) -> None:
        pass

class PhysicalPower(Power):
    def __init__(self, name: str, cost: int, count: int) -> None:
        super().__init__(name, cost)
        self.count = count

    def use(self, player: Player) -> None:
        if self.count > 0:
            print(f"{player.name} used {self.name}")
        else:
            print(f"{player.name} cannot use {self.name}")
        self.count -= 1

class MagicPower(Power):
    def __init__(self, name: str, cost: int) -> None:
        super().__init__(name, cost)

    def use(self, player: Player) -> None:
        print(f"{player.name} used {self.name}")
        player.scores += 1
