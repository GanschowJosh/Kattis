def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def fareySum(n):
    s = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if gcd(i, j) == 1:
                s += i/j
    return s

print(fareySum(6))
"""
amt = int(input())
store = {}
for i in range(amt):
    inp = input()
    num, n = list(map(int, inp.split()))
    store[num] = fareySum(n)
for k, v in enumerate(store):
    print(f"{k} {v}")
"""