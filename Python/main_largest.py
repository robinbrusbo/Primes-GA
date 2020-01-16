import time
from brute import brute
# from FILE import FUNCTION


def driver():
    n = 2
    primes = []
    timelimit = time.time() + 30  # Plus thirty seconds
    while (time.time() < timelimit):
        if primeTest(n):
            primes.append(n)
        n += 1
    print(max(primes))


def primeTest(n):
    if brute(n):
        return True
    return False


if __name__ == "__main__":
    driver()
