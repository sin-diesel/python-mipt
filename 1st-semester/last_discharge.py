#!/usr/bin/python3

def last_discharge(string: str) -> int:
    dot_idx = string.find('.')
    if dot_idx == -1:
        return int(string) - 1
    after_decimal_len = len(string[dot_idx:])
    return float(string) - 10 ** (-1 * (after_decimal_len - 1))

def _main() -> None:
    print(last_discharge(input()))

if __name__ == "__main__":
    _main()
