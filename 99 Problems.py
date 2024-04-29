def closest_99(n):
    if n < 100:
        return 99
    if n%100 > 48:
        return (n + (99 - n%100))
    else:
        return (n - (n%100 +1))

n = int(input())
print(closest_99(n))
