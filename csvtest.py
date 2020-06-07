#!/usr/bin/env python3

import csv
from collections.abc import Iterator

with open('test.csv') as f:
    data = csv.reader(f)

with open('test.csv') as f:
    data = list(csv.reader(f))

for i in data:
    print(i)
