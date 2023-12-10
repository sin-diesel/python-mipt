#!/usr/bin/env python3

import math
import re

input_string = input()

a, b = re.findall(r"\d+", input_string)

print(math.gcd(int(a), int(b)))
