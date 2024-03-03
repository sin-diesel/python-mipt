#!/usr/bin/env python3

class Number:
    def __init__(self, value: int):
        self._value = value

    def __repr__(self):
        return str(self._value)

    @property
    def minus(self):
        return Operation("-", self._value)

    @property
    def plus(self):
        return Operation("+", self._value)

    @property
    def times(self):
        return Operation("*", self._value)

zero = Number(0)
one = Number(1)
two = Number(2)
three = Number(3)
four = Number(4)
five = Number(5)
six = Number(6) 
seven = Number(7)
eight = Number(8)
nine = Number(9)

class Operation():
    def __init__(self, type: str, computed_value: int):
        self._type = type
        self._computed_value = computed_value

    def calculate(self, lhs: int, rhs: int):
        if self._type == "-":
            return lhs - rhs
        elif self._type == "+":
            return lhs + rhs
        elif self._type == "*":
            return lhs * rhs
        else:
            raise RuntimeError("Unknown operation detected.")

    @property
    def zero(self):
        return Number(self.calculate(self._computed_value, 0))

    @property
    def one(self):
        return Number(self.calculate(self._computed_value, 1))

    @property
    def two(self):
        return Number(self.calculate(self._computed_value, 2))

    @property
    def three(self):
        return Number(self.calculate(self._computed_value, 3))

    @property
    def four(self):
        return Number(self.calculate(self._computed_value, 4))

    @property
    def five(self):
        return Number(self.calculate(self._computed_value, 5))

    @property
    def six(self):
        return Number(self.calculate(self._computed_value, 6))

    @property
    def seven(self):
        return Number(self.calculate(self._computed_value, 7))

    @property
    def eight(self):
        return Number(self.calculate(self._computed_value, 8))

    @property
    def nine(self):
        return Number(self.calculate(self._computed_value, 9))
