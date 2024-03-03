#!/env/bin/python3


def _main() -> None:
    number = input()
    number_list = list(number)
    number_list.sort()
    first_nonzero = next((idx for idx, x in enumerate(number_list) if x != "0"), None)
    if number_list[0] == "0":
        number_list[0], number_list[first_nonzero] = number_list[first_nonzero], number_list[0]
    print(''.join(number_list))


if __name__ == "__main__":
    _main()

