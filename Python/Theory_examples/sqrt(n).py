import math


def sqrtTime(N):
    sum = 0
    for number in range(math.isqrt(N)):
        sum += number
    print(sum)


if __name__ == "__main__":
    N = int(input())
    sqrtTime(N)
