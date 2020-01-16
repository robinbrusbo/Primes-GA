import time
from smart_brute import smartBrute
# from FILE import FUNCTION


def driver():
    numbers = [12384589340257]
    times = []
    for n in numbers:
        start = time.time()
        primeTest(n)
        runTime = time.time() - start
        times.append(runTime)
    print(sum(times) / len(times))


def primeTest(n):
    smartBrute(n)


if __name__ == "__main__":
    driver()
