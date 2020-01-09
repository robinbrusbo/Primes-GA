import math

N = int(input())

length = N + 1
nums = [True] * length

for i in range(2, math.isqrt(length)):
    if not nums[i]:
        continue
    for j in range(i + 1, length):
        if j % i == 0:
            nums[j] = False
