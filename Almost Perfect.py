def perfectCheck(n):
    divisors = []
    for i in range(1, n):
        if n%i == 0:
            divisors.append(i)
    if sum(divisors) == n:
        return "perfect"
    elif abs(sum(divisors)-n) <= 2:
        return "almost perfect"
    else:
        return "not perfect"


inp = []
while True:
    try:
        inp.append(int(input()))
    except:
        break
check = {}
for n in inp:
    check[n] = perfectCheck(n)
    
for k, v in check.items():
    print(f"{k} {v}")