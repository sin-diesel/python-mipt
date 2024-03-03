#!/usr/bin/python3

def _main() -> None:
    file_name = input()
    with open(file_name, "r") as file:
        strings = file.read().split()
    strings_unique = set(strings)
    strings_frequency = [(string, strings.count(string)) for string in strings_unique]
    strings_frequency.sort(key=lambda sf: (- sf[1], sf[0]))
    for value in strings_frequency:
        print(value[1], value[0])

if __name__ == "__main__":
    _main()
