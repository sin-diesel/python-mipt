#!env/bin/python3


def _main() -> None:
    numbers_months = {
        "1": "январь",
        "2": "февраль",
        "3": "март",
        "4": "апрель",
        "5": "май",
        "6": "июнь",
        "7": "июль",
        "8": "август",
        "9": "сентябрь",
        "10": "октябрь",
        "11": "ноябрь",
        "12": "декабрь"
    }
    seasons = [
        "зима",
        "весна",
        "лето",
        "осень"
    ]

    try:
        month_num = int(input())
    except ValueError:
        print("ошибка")
        return
    if month_num not in range(1, 13):
        print("ошибка")
        return
    print(numbers_months[str(month_num)])
    print(seasons[month_num % 12 // 3])


if __name__ == "__main__":
    _main()
