#!/usr/bin/env python3

from bs4 import BeautifulSoup
import sys
import re


def process(filename):
    with open(filename) as f:
        soup = BeautifulSoup(f, "lxml")

    divs = soup.find_all("div", class_="admonition")

    for d in divs:
        if len(d.contents) != 1:
            continue
        m = re.match(r"\n*(Exercise \d+ \([\w ]+\))", d.contents[0].string)
        if m:
            exercise = m[1]
            a = soup.new_tag("a", id=exercise.replace(" ", "-"))
            a.string = exercise
            d.string=""
            d.append(a)
            #d.string = '<a name="%s">%s</a>' % (exercise.replace(" ", "-"), exercise)
            #print("\n", d)

    with open(filename, "w") as f:        
        f.write(str(soup))

for filename in sys.argv[1:]:
    process(filename)

