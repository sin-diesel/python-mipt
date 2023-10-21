#!/usr/bin/python3

def fibonacci(index: int) -> int:
    if index == 1:
        return 0
    if index == 2:
        return 1
    prev = 0
    curr = 1
    for _ in range(3, index + 1):
        next = prev + curr
        prev, curr = curr, next
    return curr

def _main() -> None:
    print(fibonacci(int(input())))

if __name__ == "__main__":
    _main()
