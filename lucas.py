#!/usr/bin/env python3

import code

class Lucas:
    def __init__(self, u0: int, u1: int, p: int, q: int, n: int) -> None:
        self._second = u0
        self._first = u1
        self._index = 0
        self._p = p
        self._q = q
        self._n = n

    def __iter__(self):
        return self

    def __next__(self):
        next_value: int = 0
        if self._index == 0:
            next_value = self._second
        elif self._index == 1:
            next_value = self._first
        elif self._index == self._n:
            raise StopIteration
        else:
            self._second, self._first = self._first, self._p * self._first - \
            self._q * self._second
            next_value = self._first
        self._index = self._index + 1
        return next_value

code.interact(local={**locals(), **globals()})