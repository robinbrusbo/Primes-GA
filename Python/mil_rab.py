def MilRab(n, k):
    if n == 2:
        return True
    if n % 2:
        return False


write n as 2r·d + 1 with d odd(by factoring out powers of 2 from n − 1)
WitnessLoop: repeat k times:
    pick a random integer a in the range[2, n − 2]
    x ← ad mod n
    if x = 1 or x = n − 1 then
    continue WitnessLoop
    repeat r − 1 times:
        x ← x2 mod n
        if x = n − 1 then
        continue WitnessLoop
    return “composite”
return “probably prime”
