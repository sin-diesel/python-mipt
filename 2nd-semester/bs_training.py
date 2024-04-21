#!/usr/bin/env python3

from bs4 import BeautifulSoup, SoupStrainer
import re

def _main() -> None:
    filename = "armenia.html"
    with open(filename, "r") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    images = soup.find_all("img")
    nimages = len(images)

    table = soup.find("table")
    tags = table.find_all("tr")
    ntags = len(tags)

    text = soup.get_text()
    words = text.split(" ")
    nwords = len(words)

    date_regex = re.compile(r"\d{1,2} [а-я]+ \d{4}")
    dates = re.findall(date_regex, text)
    ndates = len(dates)

    all_refs = soup.find_all("a", href=True)
    nall = len(all_refs)
    non_wiki_refs = [ref for ref in all_refs if "/wiki/" not in ref["href"]]
    nnonwiki = len(non_wiki_refs)
    self_links = soup.find_all("a", attrs={"class": "mw-selflink selflink"})
    nself_links = len(self_links)
    nother = nall - nnonwiki - nself_links

    print("")


if __name__ == "__main__":
    _main()