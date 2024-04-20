#!/usr/bin/env python3

import re
from collections import Counter

def _main() -> None:
    email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    filename = "enron_3000.csv"
    with open(filename, "r") as f:
        lines = f.readlines()

    matches: list[str] = []
    for line in lines:
        cells = line.split(",")
        for cell in cells:
            matches.extend(re.findall(email_regex, cell))
    most_common = Counter(matches).most_common(20)
    for email_freq in most_common:
        email = email_freq[0]
        freq = email_freq[1]
        email = email.strip(".")
        print(f"{email} {freq}")


if __name__ == "__main__":
    _main()