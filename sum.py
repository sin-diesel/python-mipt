#!env/bin/python3

import sys as _sys


def _main() -> None:
    N = int(input())
    result = sum([num ** 2 for num in range(1, N + 1)])
    print(result)

if __name__ == "__main__":
    _main()
