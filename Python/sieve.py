import math


def sieve(N):
    length = N + 1
    nums = [True] * length

    for i in range(2, math.isqrt(length)):
        if not nums[i]:
            continue
        for j in range(i + 1, length):
            if j % i == 0:
                nums[j] = False

    # Print all primes
    for x in range(2, length):
        if nums[x]:
            print(x)


if __name__ == "__main__":
    N = int(input())
    sieve(N)
