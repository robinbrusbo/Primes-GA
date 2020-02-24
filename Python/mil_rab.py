import random


def findIntegers(n):
    counter = 0
    number = n - 1
    while number % 2 == 0:
        counter += 1
        number //= 2
    return(counter, number)


def MillerRabin(n, k):
    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d) % n
        if x == 1 or x == n - 1:
            return "owo"
        for j in range(r - 1):
            x = (x ** x) % n
            if x == 1:
                return "comp"
            elif x == n - 1:
                return "owo"


if __name__ == "__main__":
    k = 5
    for n in range(5, 20):
        r, d = findIntegers(n)
        print(2**r * d + 1)
        print(MillerRabin(n, k))
