import time
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
    brute(n)


if __name__ == "__main__":
    driver()

# def primeTest(n):
# Insert the algorithm here
