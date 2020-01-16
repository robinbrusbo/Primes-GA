import math


def smartBrute(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for x in range(3, math.sqrt(n), 2):
        if n % x == 0:
            return False
    return True
