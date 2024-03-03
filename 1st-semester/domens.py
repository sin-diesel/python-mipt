#!env/bin/python3

import code


def _main() -> None:
    domens = {
        ".uk": "Великобритания",
        ".de": "Германия",
        ".il": "Израиль",
        ".in": "Индия",
        ".kz": "Казахстан",
        ".mm": "Мьянма",
        ".om": "Оман",
        ".ru": "Россия",
        ".uz": "Узбекистан",
        ".et": "Эфиопия",
        ".com": "Международный",
        ".org": "Международный",
        ".net": "Международный"
    }

    url = input()
    last_dot = url.rfind('.')
    url_domen = url[last_dot:]
    print(domens[url_domen])

if __name__ == "__main__":
    _main()

