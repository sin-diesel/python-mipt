#!/usr/bin/env python3

import re
from collections import Counter

def _main() -> None:
    email_regex = re.compile(r"[\w\.\-]+@[\w\-]+\.\w+")

    filename = "enron_3000.csv"
    with open(filename, "r") as f:
        text = f.read()

    matches = re.findall(email_regex, text)
    most_common = Counter(matches).most_common(20)
    for email in most_common:
        print(f"{email[0]} {email[1]}")


if __name__ == "__main__":
    _main()