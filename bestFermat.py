import random

def Fermat(n, k):
  for i in range(k):
    a = random.randint(2, n - 2)
    if pow(a, n - 1) % n != 1:
      return("composite")
    return("probably prime")
