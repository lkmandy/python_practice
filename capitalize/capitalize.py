#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    name = s.split(" ")
    capitalize_name = [w.capitalize() for w in name]
    return " ".join(capitalize_name)


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
