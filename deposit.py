#!/env/bin/python3

def _main() -> None:
    initial_value = float(input())
    required_value = float(input())
    percents = float(input()) / 100
    current_value = initial_value

    month_counter = 0
    while current_value < required_value:
        current_value += current_value * percents
        month_counter += 1

    print(month_counter)


if __name__ == "__main__":
    _main()
