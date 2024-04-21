#!/usr/bin/env python3

from bs4 import BeautifulSoup

def _main() -> None:
    filename = "armenia.html"
    with open(filename, "r") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    images = soup.find_all("img")
    nimages = len(images)
    import code; code.interact(local={**locals(), **globals()})

if __name__ == "__main__":
    _main()