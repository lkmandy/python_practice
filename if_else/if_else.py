#!/bin/python3

def check(n):
    weird = "Weird"
    not_weird = "Not Weird"

    if n % 2 != 0:
        return weird

    elif (n % 2 == 0) and (2 <= n <= 5):
        return not_weird

    elif (n % 2 == 0) and (6 <= n <= 20):
        return weird

    else:
        return not_weird
